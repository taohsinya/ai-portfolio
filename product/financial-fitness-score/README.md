# Financial Fitness Score: stress-testing a scoring model before launch

A personal financial health score (0–100) for a consumer AI money assistant, and how I tested it with made-up users and a critical AI reviewer to find where it gave the wrong answer, before any real user saw it.

The interesting part is not the formula. It is the testing loop: **write the formula → score 35 made-up users → have an AI acting as a sceptical financial planner rate every result → fix the 3 worst problems → score again.** The first version looked reasonable on paper and was wrong for exactly the users the product was built for.

> **Not financial advice.** This is a product design case study. The "CFP reviewer" below is an AI model told to act as a sceptical certified financial planner (CFP), not a human professional.

---

## The problem

Consumer finance apps love a single score. A single score also hides things. A tech worker with most of her net worth in one stock, or a young family whose wealth is all locked in a mortgaged house, can look "healthy" on a composite number and be one layoff away from insolvency.

I wanted a score that a professional planner would defend, so every sub-metric had to map to a published planning ratio, and the whole thing had to survive an adversarial review before it shipped.

## Version 1: the model

Three scored pillars, built on standard personal-financial-planning ratios (CFP textbook, Ch. 4):

| Pillar | Question it answers | Sub-metrics (weight) |
|---|---|---|
| **Control** (cash flow) | Can you cover your life month to month? | Cash runway 0.30 · current ratio 0.25 · savings ratio 0.20 · housing cost ratio 0.15 · total debt service 0.10 |
| **Safety** (balance sheet) | Are you protected if a shock hits? | Emergency fund ratio 0.30 · net worth growth 0.25 · debt to net worth 0.20 · concentration risk 0.15 · consumer debt to income 0.10 |
| **Growth** (earning power) | Is your money building? | Investment to income, age-adjusted 0.30 · return on investments 0.30 · income growth 0.25 · diversification 0.15 |

```
Score = 0.30 × Control + 0.35 × Safety + 0.35 × Growth
```

Scores map to eight tiers, from *Exposed* (0–24) to *Legacy* (98+). Two design rules shaped the rest of the product:
- **Partial data is allowed but labelled.** With only a short onboarding quiz, 6 of 16 measures can be calculated; the missing ones are left out, the rest are re-weighted to add up to 100%, and the score is shown as *"Directional · 6 of 16 metrics"*.
- **Conversations never subtract.** The score moves only when the user's real financial position moves. Missing a goal or venting in chat never lowers it.

Full spec: [scoring-spec.md](scoring-spec.md)

## Step 1: test it on 35 made-up users

7 types of target user × 5 situations = 35 made-up people, each with full details of what they own, owe, earn and spend.

- **Archetypes:** big-tech employee paid in stock, dual-income no kids, new parents, cross-border high net worth, pre-retiree, recent inheritance, freelancer
- **Conditions:** well-off, median, struggling, edge case (e.g. 73% of net worth in one stock, extreme early-retirement saver), and a recent shock (layoff, divorce, medical bill, fertility-treatment debt, a 4-month income gap)

What worked: it caught money sitting idle (someone who inherited $1.2M and left it all in cash scored only 68), and everyone who had just had a shock (layoff, divorce, medical bill) dropped to the bottom levels.

What broke: **8 of the 35 scored 70 or more even though their cash and investments were smaller than their debts**, meaning they would still owe money after selling their home.

## Step 2: a critical reviewer

An AI told to act as a sceptical financial planner with 20+ years of practice rated every one of the 35 results from 1 to 10 for "would I defend this to a client?"

**Verdict: 5.5 / 10.** Competent for a median salaried professional aged 28–45 with no dependents. Wrong, sometimes badly, for four of the seven archetypes the product was targeting:

| Made-up user | First score | Reviewer rating | Problem |
|---|---:|---:|---|
| 73% of net worth in one stock | 87 "Free" | **2** | "A CFP would refuse to sign this" |
| Single-income family, 2 kids, debts larger than cash and investments | 78 "Building" | **3** | No allowance for dependents |
| Big-tech employee whose debts exceed cash and investments by $285K | 84 "Free" | **4** | One layoff from insolvency, labelled as having arrived |
| Owes more than they own while waiting for an inheritance | 49 "Cushioned" | **4** | Label too generous for someone in the red |

Overall, the first version scored people **6–8 points too high** on average (70.4 vs the 62–65 the reviewer expected), mainly because the cash-flow part gave full marks to 16 of the 35.

## Step 3: three critical fixes

1. **Concentration counts double.** Its weight in Safety rose from 0.15 to 0.30, with a hard cap: if one holding is 50%+ of investments, Safety cannot exceed 60.
2. **Dependants raise the bar.** Cash runway and emergency-fund targets are multiplied by `1 + 0.5 × dependants`, so a family with two children needs 12 months of runway, not 6, to score full marks.
3. **Negative liquid net worth caps the score.** If cash + investments − debt < 0, the score is capped at 69 and the tier at *Cushioned*, with a plain-language explanation shown next to it.

## Step 4: score again

| | v1 | v2 |
|---|---:|---:|
| Overall mean | 70.4 | **~65.5** (reviewer's expected range: 62–65) |
| People wrongly labelled "Free" | 10 | **5** |
| Tier moved down / up / unchanged | | 11 / 0 / 24 |

The big-tech employee who would still owe $285K moved from 84 "Free" to 69 "Cushioned". The single-income family moved from 78 to 69.

**One case I did not fully fix,** on purpose: the person with 73% of her money in one stock still scores 80, because her income and returns are genuinely strong. Capping the score again would punish real wealth-building. The recommendation was a separate **risk flag** shown next to the score, not a lower number. Knowing when to stop tuning a formula is part of the design.

## What I'd take from this to any scoring model

- **A plausible formula is not a validated one.** Score the edge cases on purpose; the median user will always look fine.
- **Test against the users you are actually targeting,** not an average user. v1 failed on four of seven target archetypes.
- **Make the adversary specific.** "Review this" gets polite feedback. "You are a planner who has to sign this in front of a client; rate each case 1–10" gets a 2/10 and a reason.
- **LLM reviewers are a first pass, not a sign-off.** The next step for a model like this is calibration against real, consented user data and a human professional's review.

---

*Personas are synthetic; no real user data was used. Brand names, internal metrics and team details have been removed. The pillar framework, the top-level weights and the "conversations never subtract" rule came from the wider product team; the sub-metric quantification, the stress test, the adversarial review and the fixes are my work.*
