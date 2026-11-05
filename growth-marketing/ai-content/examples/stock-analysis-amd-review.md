# CFA Review: AMD — 2026-04-17

**Article:** `[article file] 上传/articles/AMD_20260417/en/amd-stock-analysis-ai-chip-tsmc-catalyst-2026.md`
**Sources reviewed:** Article text, published articles registry, TSMC Q1 2026 earnings data (as cited)
**Verdict:** ✅ PASS

## Summary
- Valuation stress test: Probability-weighted PT calculates to $303.50 vs stated ~$310 (2.1% gap — acceptable rounding)
- Peer comparison fairness: NVDA discussed honestly with CUDA moat acknowledged; INTC mentioned as share donor; AVGO/MRVL cited as TSMC peers. Fair and balanced.
- Risk coverage: 5/7 categories covered (cyclical, regulatory, execution, competitive, customer concentration). Missing: FX/geopolitical (partial — China export controls covered but no FX discussion) and capital structure (net cash position noted but no dilution/SBC risk discussion).
- Thesis consistency: PASS — all numbers consistent across Summary, Valuation, Conclusion, and FAQ sections.

## Detailed Findings

### ⚠️ Analytical Warnings (editor should review)

1. **Probability-weighted PT gap of 2.1%.** Bull $380 x 30% ($114) + Base $295 x 50% ($147.50) + Bear $210 x 20% ($42) = $303.50. Article states ~$310. The $6.50 gap is within acceptable tolerance for a rounded target but should be acknowledged. The article text says the distribution is "skewed to the upside" which implicitly justifies rounding up, but a precise investor would notice the math.

2. **Only 3 scenarios, no Disaster case.** The skill template calls for 4 scenarios (Bull/Base/Bear/Disaster). This article omits a Disaster scenario (e.g., AMD loses a major hyperscaler, TSMC capacity allocation cut, or severe China decoupling). For a $400B market cap semiconductor company with significant geopolitical exposure, a Disaster case at 5-10% probability (e.g., $140-160 implied price) would strengthen the analytical framework. The current 3-scenario structure is common in sell-side research and is not a blocking issue, but adding a Disaster tail would be best practice.

3. **Missing INTC stock page link.** Intel is mentioned multiple times as AMD's primary competitor in server CPUs but was never linked. **AUTO-FIXED**: Added `Intel ($INTC)` at first substantive mention (line 46).

4. **SBC dilution risk not explicitly called out.** The article notes the GAAP vs Non-GAAP earnings divergence (GAAP P/E ~92x vs forward Non-GAAP ~48x) and attributes it to SBC and Xilinx amortization, but does not quantify ongoing dilution from stock-based compensation as a specific risk. For an article using Non-GAAP as the primary valuation metric, a brief note on annual dilution rate (AMD's SBC is ~$3-4B/year) would add rigor.

5. **Forward P/E of ~48x described as "reasonable premium."** This is a subjective characterization that could be challenged. AMD's ~48x forward Non-GAAP P/E compares to NVDA at ~35-40x and the SOX index at ~25x. Describing 48x as a "discount to pure-play AI names" is accurate (some trade at 60x+), but the word "reasonable" in isolation could mislead. The article does contextualize this with the PEG ratio of ~1.6x, which partially mitigates the concern.

### ✅ Analytical Pass

- **Scenario probabilities sum to 100%.** 30% + 50% + 20% = 100%. Base case (50%) is modal. Bull + Base (80%) >> Bear (20%), consistent with a Buy rating.
- **Rating/catalyst alignment is sound.** Buy rating with $310 PT (26% upside) is supported by catalysts within the 12-month horizon: MI350 deployment late 2026, MI400 qualification, and continued EPYC share gains. No mismatched long-dated catalysts.
- **Valuation metrics consistent throughout.** Forward P/E ~48x, GAAP P/E ~92x, PEG ~1.6x, EV/EBITDA ~23x — all stated consistently in Summary (line 33), Valuation section (line 79), Conclusion (line 102), and FAQ (line 114). No stale or contradictory values found.
- **Peer comparison is fair and symmetric.** NVIDIA's CUDA moat is acknowledged as "the single largest structural barrier to AMD's AI accelerator ambitions." This is honest bear-case engagement, not dismissive. The article does not cherry-pick metrics that only flatter AMD.
- **Revenue segment table internally consistent.** Data Center $16.6B (48%) + Client & Gaming $14.6B (42%) + Embedded $3.3B (10%) = $34.5B, consistent with the stated ~$34.6B total (rounding).
- **Cross-links verified against published articles registry.** CRDO (entry #4), MU vs SNDK (entry #3), and IonQ (entry #5) all have valid seoPath values matching the registry.
- **Balance sheet claims consistent.** $10.35B cash, $7.33B net cash, current ratio >2.0x — cited in both the operating performance section and conclusion.
- **Institutional voice maintained throughout.** No hype language, no emojis, appropriate hedging ("appears poised," "credible but execution risk is real," "any delay... would slow"). Uncertainty is properly calibrated.
- **FAQ section consistent with body.** All FAQ answers reference the same data points as the body text. No contradictions found.
- **Risk section covers 3+ specific risks with clear mechanisms.** China export controls ($800M quantified), NVIDIA CUDA ecosystem (switching costs mechanism explained), semiconductor cyclicality + customer concentration (hyperscaler capex dependency specified).

## Senior Analyst Opinion

This is a defensible Buy thesis built on a sound analytical framework. The TSMC read-through as a demand validation signal is well-reasoned and avoids the common trap of treating supplier commentary as a direct revenue forecast. The article's greatest strength is its honest treatment of the NVIDIA competitive dynamic — calling CUDA "the single largest structural barrier" while maintaining the Buy case demonstrates analytical maturity. The 2.1% gap between calculated probability-weighted PT ($303.50) and stated PT ($310) is minor but reflects an implicit upside bias that should be transparent. The missing Disaster scenario is the most notable structural gap; a 5% probability tail at $150 would actually strengthen the Buy case by showing the thesis survives stress testing. The ~48x forward P/E is aggressive for a company still proving its AI accelerator credentials, but the PEG of 1.6x provides reasonable support given the 30%+ earnings growth trajectory. Overall, this article meets the standard for publication.

## Recommendations

1. **Consider adding a Disaster scenario** at 5% probability (e.g., major hyperscaler defection + China full export ban + MI400 delay = $150 implied). Redistribute: Bull 25%, Base 50%, Bear 20%, Disaster 5%. This would make the weighted PT ~$296, still supporting a Buy at $245.
2. **Add one sentence on SBC dilution** in the Risk section or Valuation section — e.g., "Annual stock-based compensation of approximately $3-4 billion represents ~1% dilution, partially offset by the company's share repurchase program."
3. **No blocking issues.** Article is ready to publish after editor reviews the two warnings above.

## Auto-fixes Applied

| # | Issue | Fix | Location |
|---|-------|-----|----------|
| 1 | Missing INTC stock page link | Added `Intel ($INTC)` | Line 46 (Lisa Su section, first substantive Intel mention) |
