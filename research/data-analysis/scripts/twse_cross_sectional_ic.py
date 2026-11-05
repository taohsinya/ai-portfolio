#!/usr/bin/env python3
"""
Cross-sectional Information Coefficient (IC) test:
does foreign net buying on day t predict which Taiwan stocks do better over the next k days?

Each day:
  signal_i = foreign net shares bought_i / shares traded_i   (scale-free: share of the day's volume)
  target_i = close_i(t+k) / close_i(t) - 1                   (k-day forward return)
  IC_t     = Spearman rank correlation of signal vs target across all liquid stocks that day
Then average IC_t over all days, and test whether the average is distinguishable from zero.
Because k-day forward windows overlap, the t-statistic uses an effective sample of n_days / k.

Data: public TWSE endpoints, no key. T86 (per-stock institutional flow) and MI_INDEX (daily closes).
Standard library only (no numpy/pandas) so it runs anywhere.

Usage (run the same script on two periods: one to discover, one to check out-of-sample):
  python3 twse_cross_sectional_ic.py 2025-01-01 2026-07-31 ic_in_sample.csv
  python3 twse_cross_sectional_ic.py 2026-08-01 2026-10-31 ic_out_of_sample.csv
A full run makes two requests per trading day; expect it to take a while. Keep the pause
between requests so you don't hammer the exchange's servers.
"""
import sys, json, urllib.request, datetime, time, math

if len(sys.argv) < 3:
    sys.exit(__doc__)
START = datetime.date.fromisoformat(sys.argv[1])
END = datetime.date.fromisoformat(sys.argv[2])
OUT_CSV = sys.argv[3] if len(sys.argv) > 3 else "cross_sectional_ic_daily.csv"
TURN_MIN = 100e6          # liquidity filter: NT$100 million daily turnover
MIN_NAMES = 20            # skip days with too few stocks to rank
HORIZONS = [1, 3, 5, 10, 20]
PAUSE = 1.0               # seconds between days
UA = "Mozilla/5.0"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.JSONDecoder().raw_decode(r.read().decode("utf-8").lstrip("﻿").lstrip())[0]


def num(s):
    try:
        return float(str(s).replace(",", "").replace("+", "").strip())
    except Exception:
        return None


# ---- 1. Download the panel ----------------------------------------------------
foreign, price = {}, {}     # date -> {code: net_shares} ; date -> {code: (close, volume, turnover)}
d = START
while d <= END:
    if d.weekday() < 5:
        ymd = d.strftime("%Y%m%d")
        try:
            j = get(f"https://www.twse.com.tw/rwd/zh/fund/T86?date={ymd}&selectType=ALL&response=json")
            if j.get("stat") == "OK":
                # column 4 = foreign (excluding foreign dealers) net shares
                fm = {r[0].strip(): num(r[4]) for r in j.get("data", []) if num(r[4]) is not None}
                if fm:
                    foreign[ymd] = fm
        except Exception:
            pass
        try:
            j = get(f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={ymd}&type=ALLBUT0999&response=json")
            for t in j.get("tables", []):
                if any("證券代號" in str(x) for x in t.get("fields", [])):   # the per-stock quote table
                    pm = {}
                    for r in t["data"]:
                        cl, vol, turn = num(r[8]), num(r[2]), num(r[4])
                        if cl and vol and turn:
                            pm[r[0].strip()] = (cl, vol, turn)
                    if pm:
                        price[ymd] = pm
                    break
        except Exception:
            pass
        time.sleep(PAUSE)
    d += datetime.timedelta(days=1)

dates = sorted(set(foreign) & set(price))
if not dates:
    sys.exit("no data downloaded")


# ---- 2. Rank correlation helpers ---------------------------------------------
def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    return sxy / ((sxx * syy) ** 0.5) if sxx > 0 and syy > 0 else None


def ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    r = [0] * len(v)
    for p, i in enumerate(order):
        r[i] = p + 1
    return r


def spearman(xs, ys):
    return pearson(ranks(xs), ranks(ys)) if len(xs) >= 3 else None


def daily_ic(i, k):
    """IC for signal date dates[i] against the k-day forward return."""
    t, fut = dates[i], price[dates[i + k]]
    xs, ys = [], []
    for code, (cl, vol, turn) in price[t].items():
        if turn < TURN_MIN or cl <= 0:
            continue
        fn = foreign[t].get(code)
        pf = fut.get(code)
        if fn is None or not pf:
            continue
        xs.append(fn / vol)
        ys.append(pf[0] / cl - 1)
    return spearman(xs, ys) if len(xs) >= MIN_NAMES else None


# ---- 3. Average and test -----------------------------------------------------
liquid = round(sum(1 for t in dates for (_, _, tn) in price[t].values() if tn >= TURN_MIN) / len(dates))
print(f"panel: {len(dates)} trading days, {dates[0]}..{dates[-1]}; avg liquid names/day: {liquid}")
print(f"\nCROSS-SECTIONAL IC  (signal = foreign net / volume; universe: turnover >= NT${TURN_MIN/1e6:.0f}M)")
print(f"  {'horizon':<8}{'meanIC':>8}{'stdIC':>8}{'%pos':>7}{'t_naive':>9}{'t_adj':>8}{'n_days':>8}  verdict")
for k in HORIZONS:
    ics = [ic for i in range(len(dates) - k) if (ic := daily_ic(i, k)) is not None]
    n = len(ics)
    if n < 3:
        print(f"  +{k}d: not enough days")
        continue
    m = sum(ics) / n
    sd = (sum((x - m) ** 2 for x in ics) / (n - 1)) ** 0.5
    pos = 100 * sum(1 for x in ics if x > 0) / n
    t_naive = m / sd * math.sqrt(n)
    t_adj = m / sd * math.sqrt(max(1, n // k))   # overlap-adjusted: effective N = n_days / k
    verdict = "significant" if abs(t_adj) >= 2 else "noise"
    print(f"  {f'+{k}d':<8}{m:>+8.4f}{sd:>8.3f}{pos:>6.0f}%{t_naive:>9.2f}{t_adj:>8.2f}{n:>8}  {verdict}")

# Save the daily +5d IC series so it can be charted or split by month later
with open(OUT_CSV, "w") as f:
    f.write("date,ic_fwd5\n")
    for i in range(len(dates) - 5):
        ic = daily_ic(i, 5)
        f.write(f"{dates[i]},{'' if ic is None else round(ic, 4)}\n")
print(f"\ndaily IC(+5d) series -> {OUT_CSV}")
print("t_adj uses effective N = n_days / k. |t_adj| >= 2 is the bar for 'probably not luck'.")
