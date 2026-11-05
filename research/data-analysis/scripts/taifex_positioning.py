#!/usr/bin/env python3
"""
TAIFEX futures/options POSITIONING monitor: the "under the surface" positioning data
(foreign index-futures net open interest, foreign call/put net open interest,
retail mini-TX net open interest).
Complements the cash-market institutional flow monitor (TWSE BFI82U) and the margin line.

Sources (public Taiwan Futures Exchange downloads; POST; Big5/cp950 CSV; accept a date RANGE in one call):
  futures:  /cht/3/futContractsDateDown   commodity_id=TXF -> TAIEX futures (臺股期貨) + mini-TAIEX futures (小型臺指期貨) rows
  options:  /cht/3/callsAndPutsDateDown    commodity_id=TXO -> TAIEX options (臺指選擇權) CALL/PUT rows
Investor-type rows: dealers (自營商) / investment trusts (投信) / foreign investors (外資及陸資).
Net open interest in contracts = field[13] (futures) / field[14] (options).
Retail mini-TX net OI = -(sum of the 3 institutions' mini-TX net OI), because the whole market nets to zero.

Output was cross-checked by hand against a broker's published daily summary for several dates.

Usage:
  python3 taifex_positioning.py backfill 20240101 20261031
  python3 taifex_positioning.py daily
Files are written to $MONITOR_DATA_DIR (default: the current directory).

Change vs the private version: the latest reading is now reported against BOTH the full history
and the last 60 trading days. A single long-window percentile turned out to be misleading
(see ../README.md, "Lessons").
"""
import os, sys, csv, json, datetime, urllib.request, urllib.parse

DATA_DIR = os.environ.get("MONITOR_DATA_DIR", ".")
CSV = os.path.join(DATA_DIR, "taifex_positioning_history.csv")
STATE = os.path.join(DATA_DIR, "taifex_positioning_state.json")
FUT = "https://www.taifex.com.tw/cht/3/futContractsDateDown"
OPT = "https://www.taifex.com.tw/cht/3/callsAndPutsDateDown"
SHORT_WINDOW = 60  # trading days


def post_csv(url, start, end, commodity):
    data = urllib.parse.urlencode({"down_type": "1", "queryStartDate": start,
                                   "queryEndDate": end, "commodity_id": commodity}).encode()
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=90).read()
    text = raw.decode("cp950", errors="ignore")  # the exchange serves Big5-family encoding
    rows = []
    for line in text.splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 15 and "/" in parts[0]:
            rows.append(parts)
    return rows


def to_i(s):
    try:
        return int(s.replace(",", ""))
    except Exception:
        return None


def pull(start, end):
    """Return {date: {...positioning fields...}} for the range."""
    d = {}
    for r in post_csv(FUT, start, end, "TXF"):
        date, prod, ident = r[0], r[1], r[2]
        netoi = to_i(r[13])  # net open interest (contracts)
        if netoi is None:
            continue
        e = d.setdefault(date, {})
        if prod == "臺股期貨" and "外資" in ident:          # TAIEX futures, foreign investors
            e["fx_tx_netoi"] = netoi
        if prod == "小型臺指期貨":                           # mini-TAIEX futures, any institution
            e["mtx_inst"] = e.get("mtx_inst", 0) + netoi
    for r in post_csv(OPT, start, end, "TXO"):
        date, prod, cp, ident = r[0], r[1], r[2], r[3]
        netoi = to_i(r[14])
        if netoi is None:
            continue
        if prod == "臺指選擇權" and "外資" in ident:        # TAIEX options, foreign investors
            e = d.setdefault(date, {})
            if cp == "CALL":
                e["fx_call_netoi"] = netoi
            elif cp == "PUT":
                e["fx_put_netoi"] = netoi
    for date, e in d.items():
        if "mtx_inst" in e:
            e["retail_mtx_netoi"] = -e["mtx_inst"]
        if "fx_put_netoi" in e and "fx_call_netoi" in e:
            e["fx_put_call_skew"] = e["fx_put_netoi"] - e["fx_call_netoi"]  # positive = net long puts = defensive
    # Guard: drop dates with no real foreign futures figure (unpublished rows come back as 0)
    return {dt: e for dt, e in d.items() if e.get("fx_tx_netoi")}


FIELDS = ["date", "fx_tx_netoi", "fx_call_netoi", "fx_put_netoi", "fx_put_call_skew", "retail_mtx_netoi"]


def load():
    if not os.path.exists(CSV):
        return {}
    return {r["date"]: r for r in csv.DictReader(open(CSV))}


def write(rows):
    rows = sorted(rows.values(), key=lambda r: str(r["date"]))
    with open(CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def slash(d):  # 20260804 -> 2026/08/04
    return f"{d[:4]}/{d[4:6]}/{d[6:]}"


def backfill(start, end):
    existing = load()
    sy, ey = int(start[:4]), int(end[:4])
    for yr in range(sy, ey + 1):  # one request per calendar year
        s = slash(start) if yr == sy else f"{yr}/01/01"
        e = slash(end) if yr == ey else f"{yr}/12/31"
        print(f"  pulling {s} .. {e} ...", file=sys.stderr)
        try:
            chunk = pull(s, e)
        except Exception as ex:
            print(f"  ERR {yr}: {ex}", file=sys.stderr)
            continue
        for date, vals in chunk.items():
            existing[date] = {**existing.get(date, {}), "date": date, **{k: vals.get(k, "") for k in FIELDS[1:]}}
    write(existing)
    print(f"backfill done: {len(existing)} trading days -> {CSV}")
    report_latest(existing)


def pct_rank(series, val):
    return sum(1 for x in series if x <= val) / len(series) * 100 if series else None


def report_latest(rows):
    dates = sorted(rows)
    if not dates:
        return
    last = rows[dates[-1]]
    prev = rows[dates[-2]] if len(dates) > 1 else {}

    def g(r, k):
        return to_i(str(r.get(k, ""))) if r.get(k, "") not in ("", None) else None

    fx = g(last, "fx_tx_netoi")
    fx_series = [g(rows[d], "fx_tx_netoi") for d in dates if g(rows[d], "fx_tx_netoi") is not None]
    print(f"\n=== TAIFEX positioning {dates[-1]} ===")
    if fx is not None:
        chg = fx - (g(prev, "fx_tx_netoi") or fx)
        p_full = pct_rank(fx_series, fx)
        p_short = pct_rank(fx_series[-SHORT_WINDOW:], fx)
        print(f"  Foreign TX futures net OI : {fx:+,} contracts (chg {chg:+,})")
        print(f"    percentile vs last {SHORT_WINDOW}d: {p_short:.0f}%   vs full history ({len(fx_series)}d): {p_full:.0f}%")
        print(f"    [low = more net short than usual; read the {SHORT_WINDOW}-day figure first]")
    for k, lab in [("fx_call_netoi", "Foreign CALL net OI"), ("fx_put_netoi", "Foreign PUT net OI"),
                   ("fx_put_call_skew", "PUT minus CALL (defensive +)"), ("retail_mtx_netoi", "Retail mini-TX net OI")]:
        v, pv = g(last, k), g(prev, k)
        if v is not None:
            chg = v - pv if pv is not None else 0
            print(f"  {lab:<28}: {v:+,} contracts (chg {chg:+,})")


def daily():
    today = datetime.date.today()
    start = (today - datetime.timedelta(days=12)).strftime("%Y/%m/%d")
    end = today.strftime("%Y/%m/%d")
    chunk = pull(start, end)
    if not chunk:
        print("no TAIFEX data (not published yet / holiday)")
        return
    existing = load()
    for date, vals in chunk.items():
        existing[date] = {**existing.get(date, {}), "date": date, **{k: vals.get(k, "") for k in FIELDS[1:]}}
    write(existing)
    report_latest(existing)
    last = sorted(existing)[-1]
    json.dump({"date": last, **existing[last]}, open(STATE, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "daily"
    if cmd == "backfill":
        backfill(sys.argv[2], sys.argv[3])
    else:
        daily()
