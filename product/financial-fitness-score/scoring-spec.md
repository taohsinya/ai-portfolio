# Financial Fitness Score · Scoring Spec (v2, after red-team fixes)

> Sanitised from an internal product spec. Brand names, internal metrics and team details removed. Sub-metric formulas and targets follow standard personal-financial-planning ratios (CFP textbook, Ch. 4) unless marked otherwise.

---

## 1. Categorising the balance sheet

| Side | Category | Definition |
|---|---|---|
| Assets | Cash and cash equivalents | Convertible to cash within 1 year |
| | Investment assets | Held for growth or income (brokerage, retirement and education accounts) |
| | Personal-use assets | Home, car, household goods; not meant to be sold |
| Liabilities | Current | Due within 1 year (credit cards, current portion of mortgage, short loans) |
| | Long-term | Due after 1 year |

- **Net worth** = total assets − total liabilities
- **Liquid net worth** = cash + investments − total debt: what is left if you had to sell up tomorrow. Shown next to the score, never buried.

## 2. Pillars and sub-metrics

### Control (cash flow), 30% of score

| Sub-metric | Formula | Target | Weight |
|---|---|---|---|
| Cash runway | cash only / monthly essential spending | 1–3 months × dependant multiplier | 0.30 |
| Current ratio | current assets / current liabilities | 1.0–2.0 | 0.25 |
| Savings ratio | (annual savings + employer match) / annual gross income | ≥ 10% | 0.20 |
| Housing cost ratio | (principal + interest + tax + insurance) / monthly gross | ≤ 28% | 0.15 |
| Total debt service | (housing + other debt payments) / monthly gross | ≤ 36% | 0.10 |

### Safety (balance sheet), 35% of score

| Sub-metric | Formula | Target | Weight (v1 → v2) |
|---|---|---|---|
| Emergency fund ratio | current assets / monthly essential spending | 3–6 months × dependant multiplier | 0.30 → **0.25** |
| Net worth growth (YoY) | (NW now − NW last year) / NW last year | positive | 0.25 → **0.20** |
| Debt to net worth | total debt / net worth | declining | 0.20 → **0.15** |
| Concentration risk | largest holding / total investments | < 15% | 0.15 → **0.30** |
| Consumer debt to income | (credit card + auto payments) / monthly gross | ≤ 20% | 0.10 |

Cash runway (cash only) and emergency fund ratio (all current assets) are deliberately different, otherwise the cash cushion is counted twice and makes up about 20% of the total score.

### Growth (earning power), 35% of score

| Sub-metric | Formula | Target | Weight |
|---|---|---|---|
| Investment to income | invested assets / annual gross income | age-based: 1× at 30, 3× at 40, 6× at 50, 10× at 67 (Fidelity benchmark) | 0.30 |
| Return on investments | (end value − start value − contributions) / average invested | 9–12% | 0.30 |
| Income growth (YoY) | (income now − last year) / last year | inflation + 3% | 0.25 |
| Diversification | inverse Herfindahl index across asset classes | broad spread | 0.15 |

## 3. Overall score and tiers

```
Score = 0.30 × Control + 0.35 × Safety + 0.35 × Growth
```

| Tier | Range |
|---|---|
| Legacy | 98+ |
| Steward | 94–97 |
| Sovereign | 88–93 |
| Free | 80–87 |
| Building | 70–79 |
| Buffered / Cushioned | 40–69 |
| Surviving | 25–39 |
| Exposed | 0–24 |

## 4. Guardrails added after the red-team review (v2)

1. **Concentration hard cap:** if the largest holding is ≥ 50% of investments, `Safety = min(Safety, 60)`.
2. **Dependant multiplier:** runway and emergency-fund targets × `(1 + 0.5 × dependants)`.
3. **Liquid net worth ceiling:** if liquid net worth < 0, `Score = min(Score, 69)` and tier = *Cushioned*, with an explanation shown next to the score.
4. **Open decision:** for very high concentration (≥ 70%) with strong growth, show a separate risk flag rather than lowering the score further.

## 5. Partial data

When only some sub-metrics are available (for example, from a 6-question onboarding quiz):
1. Drop the unavailable sub-metrics from each pillar.
2. Re-normalise the remaining weights in that pillar to sum to 1.0.
3. Label the result *"Directional · N of 16 metrics"* until full account data is connected.

When the full data arrives and the score changes, it is framed as *sharpening the picture*, never as failure.

## 6. When the score may and may not go down

| ✅ Allowed to lower the score (real position changed) | ❌ Never lowers the score (conversation or behaviour) |
|---|---|
| Cash falls | A goal expires or is abandoned |
| Concentration rises | Worried or guilty language in chat |
| Debt rises | Checking the app anxiously |
| Full data reveals a weaker position than the quiz suggested | Anything said in conversation |

## 7. Scope

The score covers cash flow, balance sheet and earning power. It does **not** cover insurance, estate planning or tax. It is designed as a second opinion that helps people know what to ask a professional, not a replacement for one.

## 8. Known gaps (future work)

- Pending assets (escrow, delayed inheritance, deferred compensation) are invisible
- Freelancer income uses annual averages and misses recent zero-income months
- Levered real estate is under-penalised
- The *Exposed* tier never triggered in testing; the lower floors may be too lenient
- Cross-border tax complexity and illiquid private-company equity are not modelled
