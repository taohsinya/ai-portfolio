# Thesis template

> **Not investment advice.** The example below is entirely fictional: "Company A", "Company B" and all numbers are made up to show the format.

A **thesis** is a belief about how part of the market works, written so it can be proven wrong. It is built from assumptions (each one testable) and evidence (facts stored in their own notes). Keep about ten live at once.

Two ratings are kept apart on purpose:
- `confidence` (low / med / high): how strong the evidence is.
- `status` (pending / verified / contested / falsified): what the tests have shown so far.

---

## Blank template

```markdown
---
type: Thesis
id: <stable-slug>             # never renamed after creation
title: <one-line claim>
themes: [<theme>, <theme>]
confidence: low | med | high  # strength of evidence
status: pending | verified | contested | falsified
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
signals: ["[[S<nn> <Slug>]]", ...]   # every signal testing this thesis
audit: "[[Audit — <Topic>]]"        # adversarial review note, if any
---

# T<n> · <Slug>

## Core claim
> One sentence. Must be something that could turn out false.

## Causal chain
Write the steps that must all be true. Give each assumption an ID and a light:
🟢 has a live signal and supporting evidence · 🟡 has evidence but no signal · 🔴 nothing is watching it

| ID | Assumption | Light | Watched by |
|:---|:---|:---:|:---|
| A1 | ... | | [[S..]] |
| A2 | ... | | — |

## Supporting evidence
- [[E.. ]] — why it supports, and which assumption it touches

## Opposing evidence
- [[E.. ]] — why it argues against. (If this section is empty, the audit should ask why.)

## Kill condition
> The specific thing that would make me drop this thesis. Without one, confidence cannot go above "med".

## Who is on the other side?
Who is betting against this, and what do they know or need that I don't?

## Ratings, split into layers
| Layer | Rating | Note |
|:---|:---|:---|
| Direction (is the claim right?) | | |
| Timing (is it right *now*?) | | Early ≠ wrong |
| Portfolio policy (what kind of exposure fits?) | | General rule only. No positions in this file. |

## Change history
- YYYY-MM-DD — what changed and which signal or evidence caused it
```

---

## Filled-in example (fictional)

```markdown
---
type: Thesis
id: shortage-moves-downstream
title: The supply shortage is moving down the chain, and each stage gains pricing power in turn
themes: [supply-chain, pricing-power]
confidence: med
status: pending
first_seen: 2026-03-02
last_updated: 2026-04-15
signals: ["[[S14 Board Supplier Price Increase Sticks]]", "[[S15 Test Equipment Lead Times]]"]
audit: "[[Audit — Shortage Chain]]"
---

# T3 · Shortage Moves Downstream

## Core claim
> The bottleneck in building AI servers is not fixed. It moves from chip packaging, to circuit
> boards, to testing. Each stage that becomes the bottleneck can raise prices for a while.

## Causal chain
| ID | Assumption | Light | Watched by |
|:---|:---|:---:|:---|
| A1 | Server orders keep growing faster than packaging capacity | 🟢 | [[S11 Server Order Growth]] |
| A2 | Once packaging catches up, circuit boards become the tightest input | 🟢 | [[S14 Board Supplier Price Increase Sticks]] |
| A3 | Board makers can pass on higher costs without losing customers | 🟡 | — (audit asked for a signal) |
| A4 | Testing capacity becomes the next bottleneck after boards | 🔴 | — |

## Supporting evidence
- [[E07 Cloud Provider Raises Spending Plan]] — more servers ordered, supports A1
- [[E09 Company A Announces 15% Board Price Rise]] — supports A2

## Opposing evidence
- [[E10 Company B Adds Two New Board Factories]] — new supply could end the shortage early, weakens A2/A3

## Kill condition
> If board prices fall for two quarters in a row while server orders are still growing,
> the shortage did not move downstream. Drop the thesis.

## Who is on the other side?
Buyers of servers (large cloud providers) have every reason to dual-source and push prices
down. Anyone selling board-maker shares today is betting that new factories arrive first.

## Ratings, split into layers
| Layer | Rating | Note |
|:---|:---|:---|
| Direction | med | Two of four assumptions have live tests |
| Timing | low | Stage-to-stage timing is unclear; early ≠ wrong |
| Portfolio policy | — | Treat as one bet, not four (see Factor Board: all four assumptions depend on server orders) |

## Change history
- 2026-04-15 — Audit flagged A3 and A4 as unwatched. Proposed new signal for A3 (candidate only).
- 2026-03-02 — Created from research on server orders.
```
