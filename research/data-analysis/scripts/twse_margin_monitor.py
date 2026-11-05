#!/usr/bin/env python3
"""
TWSE margin-balance tracker: the Taiwan retail leverage channel.
"Margin" = money investors borrow from brokers to buy shares (融資). A rising balance
means more borrowed money in the market; a sharp fall usually means forced selling.

Endpoint (public, no key): MI_MARGN?date=YYYYMMDD&selectType=MS&response=json  (updates ~21:30 Taipei)
The summary-table row '融資金額(仟元)' (margin amount, NT$ thousands) has columns:
    [label, bought, sold, cash repaid, prior balance, today's balance]   <- LAST column = today's balance
(verified with the unit rows: prior + bought - sold - repaid = today)

Usage:
  python3 twse_margin_monitor.py backfill 20260101 20260731   # fill the history CSV
  python3 twse_margin_monitor.py daily                        # fetch latest, append, print change
Files are written to $MONITOR_DATA_DIR (default: the current directory).
"""
import sys, os, json, csv, time, datetime, urllib.request

DATA_DIR = os.environ.get("MONITOR_DATA_DIR", ".")
CSV = os.path.join(DATA_DIR, "twse_margin_history.csv")
STATE = os.path.join(DATA_DIR, "twse_margin_state.json")
URL = "https://www.twse.com.tw/rwd/zh/marginTrading/MI_MARGN?date={d}&selectType=MS&response=json"


def num(s):
    return int(s.replace(",", "").strip())


def fetch(d):
    """Return a dict for date d (YYYYMMDD), or None if the exchange has no data (holiday)."""
    req = urllib.request.Request(URL.format(d=d), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.load(r)
    if j.get("stat") != "OK":
        return None
    rows = []
    for t in j.get("tables", []):
        rows.extend(t.get("data", []))
    out = {"date": d}
    for row in rows:
        if not row:
            continue
        label = row[0]
        if label.startswith("融資金額"):          # margin amount (NT$ thousands)
            out["margin_bal_k"] = num(row[-1])
            out["margin_prev_k"] = num(row[-2])
            out["margin_buy_k"] = num(row[1])
            out["margin_sell_k"] = num(row[2])
        if label.startswith("融券(交易單位)"):    # short-sale balance (lots); no NT$ row exists
            out["short_bal_units"] = num(row[-1])
            out["short_prev_units"] = num(row[-2])
        if label.startswith("融資(交易單位)"):    # margin balance (lots)
            out["margin_bal_units"] = num(row[-1])
    if "margin_bal_k" not in out:
        return None
    out["margin_chg_k"] = out["margin_bal_k"] - out["margin_prev_k"]
    return out


FIELDS = ["date", "margin_bal_k", "margin_prev_k", "margin_chg_k",
          "margin_buy_k", "margin_sell_k", "margin_bal_units",
          "short_bal_units", "short_prev_units"]


def load_csv():
    if not os.path.exists(CSV):
        return []
    with open(CSV) as f:
        return list(csv.DictReader(f))


def write_csv(rows):
    rows = sorted(rows, key=lambda r: str(r["date"]))
    with open(CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def daterange(start, end):
    s = datetime.datetime.strptime(start, "%Y%m%d").date()
    e = datetime.datetime.strptime(end, "%Y%m%d").date()
    d = s
    while d <= e:
        if d.weekday() < 5:  # skip weekends
            yield d.strftime("%Y%m%d")
        d += datetime.timedelta(days=1)


def backfill(start, end):
    existing = {r["date"]: r for r in load_csv()}
    got, skipped = 0, 0
    for d in daterange(start, end):
        if d in existing and existing[d].get("margin_bal_k"):
            continue
        try:
            row = fetch(d)
        except Exception as e:
            print(f"  {d} ERR {e}", file=sys.stderr)
            time.sleep(0.5)
            continue
        if row:
            existing[d] = row
            got += 1
            print(f"  {d}  bal={row['margin_bal_k']/1e6:8.2f}B  chg={row['margin_chg_k']/1e6:+7.2f}B")
        else:
            skipped += 1  # holiday
        time.sleep(0.3)  # be polite to the exchange server
    write_csv(list(existing.values()))
    print(f"backfill done: +{got} days, {skipped} no-data (holidays), total {len(existing)} rows")


def daily():
    # Try today, then walk back up to 5 days to find the latest published day
    today = datetime.date.today()
    for back in range(0, 6):
        d = (today - datetime.timedelta(days=back)).strftime("%Y%m%d")
        try:
            row = fetch(d)
        except Exception as e:
            print(f"ERR {d}: {e}")
            return
        if row:
            existing = {r["date"]: r for r in load_csv()}
            new = d not in existing or not existing[d].get("margin_bal_k")
            existing[d] = row
            write_csv(list(existing.values()))
            with open(STATE, "w") as f:
                json.dump({"date": d, "margin_bal_k": row["margin_bal_k"], "margin_chg_k": row["margin_chg_k"]}, f)
            tag = "NEW" if new else "ALREADY"
            print(f"[{tag}] {d}  margin_bal={row['margin_bal_k']/1e6:.2f}B  chg={row['margin_chg_k']/1e6:+.2f}B (NT$)")
            return
    print("no data in last 6 days")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "daily"
    if cmd == "backfill":
        backfill(sys.argv[2], sys.argv[3])
    else:
        daily()
