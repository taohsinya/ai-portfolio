# Market data monitors and signal testing

A set of small scripts I built in 2026 to watch Asian equity markets (mainly Taiwan and Korea) through **public exchange data**, plus the method I use to check whether a signal actually predicts anything.

The point is not the scripts. It is the habit behind them: collect hard data every day, write down what each number should mean before looking, and test claims instead of trusting them. Several of the most useful results below are cases where the data proved my earlier reading wrong.

> **Not investment advice.** This is research tooling and a write-up of method. Nothing here is a recommendation to buy or sell anything, and none of it reflects personal positions.

---

## What each monitor watches

A few terms first:
- **Net buying / selling:** shares bought minus shares sold by a group of investors on a day.
- **Open interest (OI):** the number of futures or options contracts still open at the end of the day. "Net OI" for a group is its long contracts minus its short contracts.
- **Margin:** money investors borrow from their broker to buy shares. It is a direct measure of retail leverage.

| Monitor | What it watches | Why it matters (one sentence) | Data |
|---|---|---|---|
| **Institutional flow** | Daily net buying of Taiwan stocks by foreign investors, local funds and dealers | Foreign investors are the largest swing buyer in Taiwan, so a change from selling to buying (or back) often marks a turn in sentiment. | Taiwan Stock Exchange (TWSE), public |
| **Margin balance** | Total borrowed money used to buy Taiwan stocks, and its daily change | A fast rise means the market is running on borrowed money; a sharp fall usually means forced selling. | TWSE, public |
| **Margin destination** | Which stocks, size buckets and themes the new margin money went into that day | It shows whether leverage is spreading to small, speculative names, which tends to happen late in a run. | TWSE and Taipei Exchange (TPEx), public |
| **Futures positioning** | Foreign investors' net position in Taiwan index futures and index options, and retail traders' net position in mini futures | It shows how large players are hedged or positioned "under the surface", which cash-market flow does not reveal. | Taiwan Futures Exchange (TAIFEX), public |
| **Korea leverage thermometer** | A composite measure of Korean retail leverage from a public dashboard (the site is named after the "kimchi premium", the gap between Korean and global prices) | Korean retail investors use a lot of leverage, and when it unwinds it moves the whole market, especially memory stocks. | Third-party public dashboard |
| **Capex vs memory** | Units outstanding of memory and semiconductor ETFs, and whether a public dashboard of big-tech data-centre spending ("hyperscaler capex") has new figures | Memory chip prices (DRAM) depend on how much the largest cloud companies spend on data centres, and ETF units show whether money is entering or leaving the trade. | Public web pages |
| **SK Hynix buyback** | Daily progress of SK Hynix's announced share buyback against its plan (shares bought, pace, price paid) | A buyback that slows when the stock falls tells you more about the company's conviction than the headline size. | Korean exchange disclosures, via a third-party site |
| **Factor test (IC)** | Whether stocks that foreign investors buy today go on to beat other stocks over the next few days | It turns "foreign buying matters" from a belief into a number that can pass or fail. | TWSE, public |

Why ETF **units** and not ETF **assets**: total assets move every day with the price, so they cannot tell you whether investors added money. Units outstanding only change when money actually goes in or out.

## How the pieces fit

```
public data  →  check  →  alert / digest  →  notes
```

1. **Data.** Each monitor downloads one public dataset after the market closes and appends it to a history file (CSV). History is kept so every reading can be compared with the past.
2. **Check.** The script compares today with the last reading and with history, and prints a single `STATUS=` line, for example `TWSE_FOREIGN_FLIP` or `TWSE_OK`. The rules for what counts as unusual are written in the script, not decided after seeing the number.
3. **Alert / digest.** A scheduled AI agent (Claude Code) runs the monitors each day and only messages me when a status says something changed. Separately, an automated pipeline reads daily broker research and writes a digest. After each digest, the agent checks it against the hard data: does a claim rest on an analyst's forecast when an exchange number already exists?
4. **Notes.** Readings that matter go into an Obsidian vault (a linked note-taking app) organised as *evidence*, *signals* (each with a deadline) and *theses* (each with a written condition that would prove it wrong). The vault has a standing rule: no personal positions or buy/sell calls.

## Scripts in this folder

These four use only public exchange data, need no API key, and have had machine-specific paths replaced: they write to the folder in the `MONITOR_DATA_DIR` environment variable (default: the current folder). Python 3 standard library only.

**[`scripts/twse_flow_monitor.sh`](scripts/twse_flow_monitor.sh)** downloads the TWSE's daily summary of net buying by foreign investors, local funds and dealers. It keeps the previous reading and flags two cases: foreign investors switched from net selling to net buying (or back) on a day bigger than NT$20 billion, or any day bigger than NT$100 billion. It also appends each day to a history file. That was added after I found the first version only kept the latest day and had silently lost several days of data.

**[`scripts/twse_margin_monitor.py`](scripts/twse_margin_monitor.py)** tracks the total margin balance (borrowed money used to buy stocks) and the short-selling balance. It can backfill any date range and then run daily, picking up the latest published day even after a holiday. The tricky part was finding which column of the exchange's table is today's balance; the script checks it with simple arithmetic (yesterday + bought − sold − repaid = today).

**[`scripts/taifex_positioning.py`](scripts/taifex_positioning.py)** pulls foreign investors' net futures and options positions and derives the retail traders' net position in mini futures (because the market nets to zero, retail is minus the sum of the institutions). It handles the exchange's older Chinese text encoding (Big5) and can pull a whole year per request. The output was checked by hand against a broker's published daily summary. The public version reports today's reading against **both** the last 60 days and the full history, for the reason explained in Lessons.

**[`scripts/twse_cross_sectional_ic.py`](scripts/twse_cross_sectional_ic.py)** is the factor test. For each trading day it ranks liquid Taiwan stocks by how much foreign investors bought (as a share of that day's volume), ranks them again by their return over the next 1 to 20 days, and measures how well the two rankings line up. Run it once on a period to find a signal and again on a later period to check it still works. The method is explained in [factor-testing-method.md](factor-testing-method.md).

### Not published, and why

| Script | Reason |
|---|---|
| Margin destination | Clean, but it includes my own theme lists; I'd rather publish it after rewriting those as a config file. |
| Korea leverage thermometer | Reads a third-party site's data feed; I have not confirmed its terms allow redistribution. |
| Capex vs memory | Reads data out of web pages rather than an official feed, and part of the parsing has broken. |
| SK Hynix buyback | Depends on an unofficial third-party feed, covers one stock, and the buyback has finished. |
| Live "today's ranking" from the factor test | It outputs a list of stocks, which reads like a stock tip. The research version above is enough to show the method. |
| Research ingestion pipeline | Not shown. It processes licensed research. |

## Lessons

**1. Test the claim, at the right level.** "Foreign investors know something" was the belief. Tested on the whole-market total against the index, and on single stocks one at a time, it was noise. Tested *across* stocks (which ones foreigners bought, not whether they bought), it was clearly significant. The same information can look useless or useful depending on which question you ask of it.

**2. A signal that passes once has not passed.** The foreign-flow factor passed comfortably on 2025 to mid-2026 data. On the three months after, it stopped working, with the sign flipping in the first month. I demoted it to "under review" and set a rule: re-run monthly, and restore it only after two positive months in a row. The full numbers (all public data) are in the [method note](factor-testing-method.md).

**3. "Extreme" depends on what you compare against.** The futures monitor used to print a percentile against all available history. On one day in September 2026 the same foreign short position was at the **4.8th** percentile of the full 647-day history but the **51.7th** percentile of the last 60 days. "Unusually short" was true against 2024–25 and false against the current regime. The script now prints both and the 60-day figure first.

**4. Level is not change.** Days when foreign investors were *most* short were not followed by weak markets; days when they *added* a lot of shorts were (small sample: 33 days, so directional evidence only). These are two different questions and need separate tests.

**5. Take composite indicators apart.** When the Korea leverage composite hit its highest alert level, I split it into its parts. A large share of the move came from an ETF adjustment term that lags by design, not from new borrowing. The monitor now always prints the clean borrowing ratio next to the composite.

**6. Know whether a number is final.** The exchange revises some same-day figures that evening. A reading taken at 3pm and one taken at 9pm can differ. Each history row should record when it was taken.

**7. Read what a number can and cannot tell you.** For the buyback, the average price paid versus the closing price looked like a measure of discipline. It is not: a steady buyer will pay below the close on up days and above it on down days. The real test was whether the company kept buying the same quantity on down days.

**8. Monitors fail quietly.** Scheduled jobs can stop without anyone noticing. Every job now has a roll call after any restart, and every script keeps a history file instead of overwriting one state file.

---

*Data sources: Taiwan Stock Exchange, Taipei Exchange and Taiwan Futures Exchange public data. Exchange data is © the respective exchanges; check their terms before redistributing downloaded data.*
