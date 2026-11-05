# Signal template

> **Not investment advice.** The example below is entirely fictional: companies, numbers and dates are made up to show the format.

A **signal** is one specific bet that tests one part of a thesis. It has three things that make it useful:

1. **A deadline tied to a real event** that will produce the answer (an earnings report, a monthly data release, a pricing season).
2. **Three outcomes written in advance**: what counts as verified, falsified, or contested.
3. **A data source**, or an honest note that there isn't one.

A signal with no deadline never closes, so it never changes your confidence. A signal with no data source is pretending to be tracked.

---

## Blank template

```markdown
---
type: Signal
id: <stable-slug>
thesis_refs: ["[[T<n> <Slug>]]"]       # which thesis (and assumption) this tests
assumption: A<n>
trigger_condition: "<one-line summary of the test>"
deadline: YYYY-MM-DD                   # tied to a named event below
deadline_event: "<the event that will settle it>"
data_source: "<where the reading comes from>"   # or "KNOWN GAP: no source yet"
contradiction: false                   # true if credible sources already disagree
claim_confidence: low | med | high     # forced to low if contradiction: true
status: pending | verified | falsified | contested
created: YYYY-MM-DD
adjudicated:                           # date scored
---

# S<nn> · <Slug>

## Claim
> One sentence. Read this BEFORE the thresholds when scoring: some claims are
> deliberately counter-intuitive (e.g. "X will NOT happen").

## Three outcomes (written before the evidence arrives)
| Outcome | Threshold |
|:---|:---|
| 🟢 verified | ... |
| 🔴 falsified | ... |
| ⚪ contested | ... (and what we would write down about why) |

## What would prove me wrong
Plain words, written now: the observation I would least like to see.

## Reading rules for this signal
- Which number counts (a business fact, not the share price)
- If the test involves a "beat" or "miss": against WHICH expectation?
- Any known bias in the indicator (does it naturally move one way in a sell-off?)

## Result  (fill in only after the deadline)
- Date scored:
- Reading:
- Outcome: verified / falsified / contested
- Effect on thesis: confidence ↑ / ↓ / unchanged; status change?
- If contested: why it couldn't be decided, and the new deadline
- Was the threshold well designed? (Answer honestly, but score the original anyway.)
- Lesson → link to a Finding note if worth keeping
```

---

## Filled-in example (fictional)

```markdown
---
type: Signal
id: board-supplier-price-increase-sticks
thesis_refs: ["[[T3 Shortage Moves Downstream]]"]
assumption: A2
trigger_condition: "Company A's announced 15% board price rise shows up in its reported prices next quarter"
deadline: 2026-07-31
deadline_event: "Company A Q2 earnings report"
data_source: "Company A quarterly report: average selling price per board"
contradiction: true      # one research house says customers are already switching to Company B
claim_confidence: low    # forced low because of the contradiction
status: pending
created: 2026-04-15
adjudicated:
---

# S14 · Board Supplier Price Increase Sticks

## Claim
> Company A's 15% price rise will stick: its customers will pay it rather than switch.

## Three outcomes
| Outcome | Threshold |
|:---|:---|
| 🟢 verified | Q2 average selling price up ≥ 10% on Q1, and volumes not down more than 5% |
| 🔴 falsified | Average selling price up < 3%, OR volumes down > 15% (customers walked) |
| ⚪ contested | Price up 3–10%, or the company stops reporting price per board. Record which. |

## What would prove me wrong
Company A reports flat prices and says it "chose to share the benefit with key customers."
That would mean the shortage is not tight enough to give it pricing power, and A2 is in trouble.

## Reading rules for this signal
- Use reported average selling price, not the share price reaction on the day.
- Ignore management's "we expect" language; only reported numbers count.
- Known bias: the price rise was announced in a hot month, so early channel checks will
  overstate it. Wait for reported figures.

## Result
- Date scored: 2026-07-31
- Reading: average selling price +6% on Q1; volumes −2%
- Outcome: ⚪ contested (inside the 3–10% band)
- Effect on thesis: confidence unchanged. Status stays pending.
- Why it couldn't be decided: price rose, but by less than half the announced amount.
  We can't yet tell "partial pass-through" from "discounting to keep share".
- New deadline: 2026-10-31 (Q3 report). Threshold unchanged.
- Was the threshold well designed? The 3–10% band was too wide. Noted for the next
  signal of this type, but this one is scored as written.
- Lesson → [[F04 Announced Price Rises Land at Half]]
```

---

## Scoring checklist (run on the deadline)

- [ ] Did I score expiring signals before reading today's new research?
- [ ] Did I read the claim before the threshold?
- [ ] Am I using the reading named in `data_source`, not the share price?
- [ ] For any "beat" or "miss": did I say against which line?
- [ ] Did I change any threshold while the window was open? (If yes: undo, score the original, open a new signal.)
- [ ] If contested: did I write down why, and set a new event-based deadline?
- [ ] Did I update the thesis confidence only if the evidence actually moved?
