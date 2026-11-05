# How I test whether a signal predicts anything

A plain-English guide to the **Information Coefficient (IC)** test, the method behind [`scripts/twse_cross_sectional_ic.py`](scripts/twse_cross_sectional_ic.py), with a worked example on public Taiwan data, including the part where the signal stopped working.

> Not investment advice. This describes a research method.

---

## The question

Lots of market claims sound like "when X happens, stocks go up". The useful version of the question is narrower:

> On a given day, if I rank stocks by X, do the top-ranked stocks do better than the bottom-ranked ones over the next few days?

That is a **cross-sectional** question (comparing stocks with each other on the same day), and it is how professional quant investors test a **factor**: any measurable characteristic that might help pick stocks.

## What IC is

The **Information Coefficient** is the correlation between today's signal and the return that follows.

1. **Pick a signal.** In my example: how much foreign investors net-bought each stock, divided by that stock's trading volume that day. Dividing by volume makes big and small stocks comparable.
2. **Pick a horizon** (k days): the stock's return from today's close to the close k trading days later.
3. **Each day, rank all stocks twice:** once by signal, once by the return that followed. Measure how well the two rankings agree. This is the **Spearman rank correlation**: +1 means the rankings match perfectly, 0 means no relationship, −1 means they are reversed. Using ranks rather than raw values stops one extreme stock from dominating.
4. **That gives one IC per day.** Average them over the whole period. That average is the factor's IC.

A **liquidity filter** removes thinly traded stocks (I used NT$100 million of daily turnover), because their prices are noisy and you could not trade them at size anyway.

## How to read it

**The size will be small, and that is normal.** A real single factor usually has an average IC of about 0.02 to 0.06. A reported IC of 0.3 or higher for one simple signal usually means a mistake: too little data, overlapping samples, or information from the future leaking in.

**Look at the hit rate too.** The share of days with positive IC tells you how consistent the signal is. 70% of days positive with a small average is more useful than a large average driven by a few days.

**Check it is not luck: the t-statistic.** Average IC divided by its day-to-day variability, times the square root of the number of days. Roughly, **|t| of 2 or more** means the result is unlikely to be chance.

**Correct for overlap.** This is the most common mistake. With a 5-day horizon, Monday's window and Tuesday's window share four days of returns. The daily ICs are not independent, so counting every day as a fresh observation overstates confidence. My fix is conservative: treat the sample as `number of days ÷ k`. A t of 9 at 5 days becomes about 4.

**Watch how it decays.** Real signals usually fade as the horizon lengthens. A signal that gets *stronger* at long horizons deserves suspicion.

## Worked example (public data)

*All figures below are my own calculations from public Taiwan Stock Exchange data (per-stock institutional flow and daily closing prices). They describe a past period and are not a forecast.*

**Discovery period:** 376 trading days, January 2025 to July 2026, about 377 liquid stocks per day.

| Horizon | Mean IC | % of days positive | t (naive) | t (overlap-adjusted) | Verdict |
|---|---|---|---|---|---|
| +1 day | +0.044 | 72% | 9.65 | 9.65 | significant |
| +3 days | +0.045 | 71% | 9.48 | 5.47 | significant |
| +5 days | +0.045 | 70% | 9.62 | 4.30 | significant |
| +10 days | +0.036 | 69% | 8.48 | 2.66 | significant |
| +20 days | +0.040 | 70% | 8.88 | 1.94 | noise |

Reading: a modest but consistent short-horizon signal, strongest around 3 days and fading to noise by 20. Note how the overlap adjustment changes the verdict at 20 days.

The same flow data showed **no** signal when tested as "does total foreign buying predict the index?" or stock by stock. The signal only exists as a comparison across stocks.

**Out-of-sample check:** I then ran the same script, unchanged, on the period after the discovery window (August to mid-October 2026, about 50 trading days, about 390 stocks per day).

| | Discovery | Out-of-sample |
|---|---|---|
| +5-day mean IC | +0.045 | about −0.006 |
| t (overlap-adjusted) | 4.30 | about −0.2 |
| By month, +5-day IC | 19 months, worst −0.016 | Aug −0.041 (worst month on record), Sep 0.000, Oct +0.084 (few days) |

Reading: the signal stopped working right after it was validated. The period followed a sharp crash and rebound, and buying what foreign investors bought stopped paying. Two to three months is not enough to say the factor is dead, but it is enough to stop relying on it.

**What I did:** demoted it from "core signal" to "under review", re-run the test monthly, and set the bar for restoring it in advance: two positive months in a row.

## Pitfalls checklist

- **Overlapping windows.** Adjust the sample size or you will overstate significance.
- **One regime.** 18 months covering one rally and one crash is a single market regime. Test across more years if the data allows.
- **Look-ahead.** The signal must be known before the return starts. Flow data is published after the close, so the return must start from that close or later.
- **Revised data.** Some exchange numbers are corrected after first publication. Backtests use the corrected figure; live use gets the first one.
- **One way of measuring the signal.** I divided by volume. Dividing by company size, or using cumulative flow over several days, can give different answers. Trying many versions and keeping the best one is overfitting; decide the version before testing.
- **Costs.** An IC of 0.045 is real but small. After trading costs it may not be worth acting on. I did not model costs.
- **Survivorship.** The stock list comes from each day's actual trading, so delisted stocks are included on the days they traded. Check this whenever you reuse the method with another data source.
- **Decide the pass/fail rule first.** Write the threshold (|t| ≥ 2, two positive months to restore) before seeing the result, and do not move it afterwards.

## Reusing the method

The script needs only two things per day: a signal value per stock and a closing price per stock. Swap the data source and the same code tests any factor (analyst revisions, short interest, insider buying) in any market.
