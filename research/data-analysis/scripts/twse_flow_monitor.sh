#!/bin/bash
# Daily monitor of TWSE BFI82U: how much the three institutional investor groups
# (foreign investors, local investment trusts, dealers) bought minus sold on the Taiwan Stock Exchange.
# Data is published after ~3pm Taipei time and can be revised later the same evening,
# so treat a same-day reading as provisional.
#
# Prints one STATUS line for a scheduler to decide whether to send an alert:
#   TWSE_FOREIGN_FLIP -> foreign net changed sign vs last reading (seller<->buyer) and |net| >= NT$20bn
#   TWSE_FOREIGN_BIG  -> |foreign net| >= NT$100bn (unusually large day)
#   TWSE_OK           -> report only, no alert
#   TWSE_STALE        -> today's data not published yet (weekend / before ~3pm) -> no alert
#
# Files are written to $MONITOR_DATA_DIR (default: the current directory).
DATA_DIR="${MONITOR_DATA_DIR:-.}"
STATE="$DATA_DIR/twse_flow_state.json"
UA="Mozilla/5.0"
TODAY="$(date +%Y%m%d)"
TMP="$(mktemp)"
curl -sS --max-time 30 -L "https://www.twse.com.tw/rwd/zh/fund/BFI82U?dayDate=${TODAY}&type=day&response=json" \
  -H "User-Agent: $UA" -o "$TMP" || echo "{}" > "$TMP"
python3 - "$STATE" "$TMP" "$TODAY" <<'PY'
import json, sys, os
state_path, tmp, today = sys.argv[1], sys.argv[2], sys.argv[3]
try: d = json.load(open(tmp, encoding="utf-8"))
except Exception: d = {}
if d.get("stat") != "OK" or d.get("date") != today:
    print(f"STATUS=TWSE_STALE asof={d.get('date')} (today={today}, not published yet / weekend)")
    sys.exit(0)
def net(rows, key):
    for r in rows:
        if r[0].startswith(key):
            return int(r[3].replace(",", ""))
    return None
rows = d.get("data", [])
foreign = net(rows, "外資及陸資")   # foreign investors
trust   = net(rows, "投信")         # local investment trusts
total   = net(rows, "合計")         # all three groups
if foreign is None:
    print("STATUS=TWSE_PARSE_ERROR"); sys.exit(0)
prev = {}
if os.path.exists(state_path):
    try: prev = json.load(open(state_path))
    except Exception: prev = {}
pf = prev.get("foreign")
json.dump({"date": today, "foreign": foreign, "trust": trust, "total": total},
          open(state_path, "w"), ensure_ascii=False, indent=1)

# History: the state file keeps only the latest day, so append one row per date
# (idempotent) or past days are lost for good.
hist_path = os.path.join(os.path.dirname(state_path) or ".", "twse_flow_history.csv")
seen = set()
if os.path.exists(hist_path):
    with open(hist_path, encoding="utf-8") as fh:
        for ln in fh:
            p = ln.split(",")
            if p and p[0].isdigit(): seen.add(p[0])
else:
    with open(hist_path, "w", encoding="utf-8") as fh:
        fh.write("date,foreign_100m,trust_100m,total_100m\n")   # units: NT$100 million
if today not in seen:
    with open(hist_path, "a", encoding="utf-8") as fh:
        fh.write("%s,%.1f,%.1f,%.1f\n" % (today, foreign/1e8, trust/1e8, (total or 0)/1e8))
fy, ty, tt = foreign/1e9, (trust or 0)/1e9, (total or 0)/1e9   # NT$ billions
tag = "net buy" if foreign > 0 else "net sell"
line = f"date={today} foreign={fy:+.1f}bn ({tag}) trust={ty:+.1f}bn total={tt:+.1f}bn (NT$)"
flip = pf is not None and (pf < 0) != (foreign < 0) and abs(foreign) >= 2e10
if flip:
    frm = "sell->buy" if foreign > 0 else "buy->sell"
    print(f"STATUS=TWSE_FOREIGN_FLIP {frm} | {line} | prev foreign={pf/1e9:+.1f}bn")
elif abs(foreign) >= 1e11:
    print(f"STATUS=TWSE_FOREIGN_BIG | {line}")
else:
    print(f"STATUS=TWSE_OK | {line}")
PY
rm -f "$TMP"
