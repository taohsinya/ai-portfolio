# Mock Data — Sample Simulation Outputs

> Sample outputs from a personalization simulation run (snapshot dated 2026-03).
> Inputs: deep-dive research reports on public tickers, public news headlines, and
> **synthetic user personas** (names and portfolios are fictional test data).
> Figures are illustrative snapshots for prototyping only — not investment data.

---

## 1. Sample Stock Data

| Stock | Price | Change | Mkt Cap | Style | Theme |
|-------|-------|--------|---------|-------|-------|
| NVDA | $184.77 | +4.2% | $4.5T | Growth | AI Capex |
| JPM | $289.29 | +1.1% | $778.7B | Quality+Value | 利率敏感 |
| KO | $79.49 | +0.3% | $341.9B | Income+Quality | Defensive |

---

## 2. Synthetic User Profiles

| User | Name | Archetype | Depth | Jargon | Density | Tone | Framing | Lang | Positions |
|------|------|-----------|-------|--------|---------|------|---------|------|-----------|
| U017 | Casey | A_Casual | headline | explain | light | reassuring | impact_on_me | en | VTI, VXUS, QQQ |
| U001 | Blake | B_Curious | summary | explain | medium | direct | what_to_think | en | NVDA, AMZN, MSFT, AAPL, GOOGL, BRK.B, VOO |
| U003 | Robin | E_Sophisticated | analysis | native | heavy | direct | what_to_think | en | TLT, GOOGL, NVDA, BTC, SPY, AAPL, TSLA |
| U027 | Dana | B_Curious (中文) | summary | plain | medium | neutral | what_happened | zh-CN | QQQ, VTI, VOO |
| U005 | Frankie | F_Expert | deep_dive | native | heavy | direct | what_to_watch | en | OXY, GOOGL, AAPL, SPY, TSLA, GS, JPM, AMD |

---

## 3. Daily Picks — NVDA × 5 Users

### U017 Casey (A_Casual)

> Nvidia makes the chips that power AI — and right now, everyone wants them. The stock is up about 4% today. Your QQQ index fund already gives you some exposure.

**Card specs**: ~60px row, 0 data points, 1 tag [AI], zero jargon

---

### U001 Blake (B_Curious)

> **Why it's a pick:** Nvidia's revenue grew 65% last year to $215.9 billion — almost all of it from selling AI chips to big tech companies. Think of it like being the main supplier of pickaxes during a gold rush.
>
> **Key Numbers:**
> - Revenue growth: 65% (very fast for a company this size)
> - PEG ratio: 0.8 (under 1.0 means the stock might be underpriced relative to its growth — think of it as "growth-adjusted value")
> - Free cash flow: $25+ billion per year (this is the actual cash left after all expenses)
> - Next earnings: May — this will be the big test
>
> Your AMZN, MSFT, and GOOGL are all major Nvidia customers, so their spending plans directly affect this stock.

**Card specs**: ~100px standard, 4 data points inline, jargon explained in parentheses

---

### U003 Robin (E_Sophisticated)

> **NVDA** $184.77 (+4.2%) | Mkt Cap $4.5T
>
> **Setup:** FY26 $215.9B (+65% YoY), Q4 $68.1B (+73%). Data Center $35.1B/qtr (+93%). GM 75% (-50bps QoQ, stable). FCF margin 51.2%, best-in-class. PEG <1.0 — growth-adjusted valuation is cheaper than it looks at 55x P/E.
>
> Valuation framework: EV/Revenue fwd 28.5x (vs 5yr avg 22x), but revenue base has 3x'd. P/S 20.8x. At current growth trajectory, PEG normalizes to 0.6 by FY27E.
>
> **Risk overlay (Structure: Mod Cyclical):**
> - China export controls: ~15% historical revenue. H20 chip workaround now also restricted. Net impact: ~$5B revenue headwind.
> - Cyclicality: Moderate — design-win driven with 6-12 month lag.
> - Competition: AMD MI300X gaining share in inference. ASIC threat from GOOGL TPU / AMZN Trainium. But ecosystem lock-in (CUDA) is the moat.
>
> | Metric | Current | vs Prior Qtr | vs Estimate |
> |--------|---------|-------------|-------------|
> | Revenue | $35.1B DC | +12% QoQ | Beat by 8% |
> | Gross Margin | 75.0% | -50bps | In-line |
> | FCF Margin | 51% | +200bps | — |
> | P/E | 55.2x | — | — |
> | PEG | 0.8 | — | — |
> | EV/Revenue (fwd) | 28.5x | — | — |
>
> **Catalysts:**
> 1. NVDA earnings (May) — guide + B200 ramp commentary
> 2. MSFT/GOOGL earnings — capex acceleration or deceleration
> 3. GTC — next-gen architecture reveal
> 4. China policy — any additional export restrictions
> 5. AMD MI350 launch — competitive benchmark
>
> Cross-portfolio: Your TLT position is duration-sensitive. If BOJ hikes to 1.00% (see today's N2), global yields shift — both your TLT and NVDA (growth = duration proxy) face headwinds.

**Card specs**: ~130px data-dense, 8+ data points, 1 table, native jargon, cross-portfolio reference

---

### U027 Dana (B_Curious 中文)

> **英伟达 (NVDA) $184.77 (+4.2%)**
>
> 英伟达是做 AI 芯片的公司，现在所有大科技公司都在抢着买它的产品。去年收入涨了 65%，达到 2159 亿美元——相当于每天赚将近 6 亿美元。
>
> 你的 QQQ 基金里有一部分就是英伟达的股票。这个公司很赚钱（利润率 75%），但股价也不便宜（市盈率 55 倍，就是说你花 55 块钱才买到它 1 块钱的利润）。
>
> 下一次财报在 5 月，到时候会知道 AI 的需求是不是还在加速。

**Card specs**: ~100px standard, 3 data points, plain language with analogies, zh-CN

---

### U005 Frankie (F_Expert)

> **NVDA** $184.77 (+4.2%) | Mkt Cap $4.5T
>
> **Setup:** Revenue +65% YoY ($215.9B), Q4 $68.1B (+73%). DC $35.1B (+93%). GM 75.0% (-50bps QoQ, inline). FCF $18B/qtr, 51% margin. PEG 0.8 — cheapest growth-adjusted valuation since Q2 FY24. EV/Rev fwd 28.5x vs 5yr avg 22x, but revenue base has 3x'd.
>
> **Bull/Base/Bear:**
>
> | Scenario | FY26E Revenue | P/E | Fair Value | Prob |
> |----------|---------------|-----|-----------|------|
> | Bull: Capex accelerates, B200 ramp ahead | $160B | 50x | $185 | 30% |
> | Base: Guided trajectory, GM stable | $140B | 45x | $155 | 50% |
> | Bear: Capex pause, China full cut | $110B | 35x | $95 | 20% |
> | **Probability-weighted** | | | **$150** | |
>
> **Transmission chain:**
> Hyperscaler capex cycle H1→H2 transition. MSFT guided $80B FY25 capex (+59% YoY). GOOGL $75B. META $60-65B. AMZN est. $85B. Total ~$300B annualized. NVDA est. share: 70-80% training, 50-60% inference.
>
> **Counter-thesis:**
> 1. ASIC displacement: GOOGL TPU v6, AMZN Trainium 2 — est. 15-20% of internal workloads by FY26
> 2. China revenue cliff: H20 restricted → $5-7B annual loss
> 3. Inventory digestion: 2025 could see mini-cycle pause (comp: 2019 crypto hangover, 2 quarters)
>
> **Full metric grid:**
>
> | Metric | Q4 FY25 | QoQ | YoY | vs Est | Peer (AMD) |
> |--------|---------|-----|-----|--------|-----------|
> | Revenue (DC) | $35.1B | +12% | +93% | +8% | $7.5B (+32%) |
> | Gross Margin | 75.0% | -50bps | +200bps | Inline | 52.0% |
> | Op Margin | 62.0% | +100bps | +500bps | +200bps | 22.0% |
> | FCF Margin | 51% | +200bps | +800bps | — | 18% |
> | P/E (fwd) | 55.2x | — | — | — | 48.5x |
> | PEG | 0.8 | — | — | — | 1.5 |
> | EV/Rev (fwd) | 28.5x | — | — | — | 10.2x |
>
> **Catalyst calendar (probability-weighted):**
>
> | Date | Event | Impact | Direction |
> |------|-------|--------|-----------|
> | May earnings | FY26 guide + B200 ramp | ±15% | Depends on guide |
> | Apr MSFT earnings | Capex guide update | ±5% | Bull if >$85B |
> | Apr GOOGL earnings | TPU v6 + capex | ±3% | Watch ASIC mix |
> | Q3 GTC | Next-gen arch reveal | +5-8% | Historically bullish |
> | Ongoing | China export controls | -3-5% | Binary downside |
>
> **Options flow:** Unusual call activity $155 Jun, $170 Sep. Put/call ratio 0.6 (bullish skew). IV30 at 48% vs HV30 42%.

**Card specs**: ~160px full, 15+ data points, 3 tables, peer comp, options flow, native jargon

---

## 4. Cross-Stock Routing — Robin × 3 Stocks

### NVDA (Growth base)
Key metrics: Revenue growth +65%, PEG 0.8, P/S 20.8x, EV/Revenue 28.5x
Narrative: Growth acceleration + AI capex cycle
Catalysts: NVDA earnings, hyperscaler capex guides

### JPM (Financial Leverage — COMPLETE indicator replacement)
Key metrics: NIM, ROTCE 18%, CET1, NCO rate, Efficiency ratio, Fee Income 40%+
Narrative: Fortress balance sheet + capital return + rate sensitivity
Catalysts: FOMC meeting, stress test results, Basel III
**Zero overlap with NVDA indicators — FCF, P/S, PEG completely absent**

### KO (Income base)
Key metrics: Div yield 2.7%, 64-year consecutive increases, Payout ratio, FCF coverage $12.2B
Narrative: Income reliability + dividend aristocrat + pricing power
Catalysts: CEO transition (March 31), CPI/PPI data, dividend hike announcement

---

## 5. News — Tesla Cybercab × 3 Users

### Casey (A_Casual)
> Tesla wants to build a self-driving taxi — a small car with no steering wheel, priced under $30,000. It's still early and faces a lot of hurdles. None of your funds (VTI, VXUS, QQQ) have big Tesla exposure, so this is more interesting than urgent.

### Robin (E_Sophisticated)
> **TSLA Cybercab: Autonomous play with binary risk profile**
>
> Tesla revealed the Cybercab — fully autonomous, no steering wheel, sub-$30k target, April production start at Giga Texas. 35 kWh battery, ~200-mile range. "Unboxed" manufacturing = parallel module assembly, potentially halving factory footprint.
>
> **Your TSLA position:** This is the bull case catalyst that justifies TSLA's 394.9x P/E. The robotaxi TAM ($2T+ by 2030 per ARK) is the entire non-automotive valuation premium. But execution risk is extreme:
> - FMVSS requires driver controls — Tesla needs exemptions that don't exist yet
> - 60% public distrust (UCSD study) — adoption curve will lag tech readiness
> - Competitive: Waymo already operating driverless in SF/Phoenix
>
> Counter-read on UBER: if Tesla cracks L4, UBER's driver model is disrupted. But UBER pivoting to platform (autonomous partners). Watch partnership announcements as hedge signal.

### Dana (中文 B_Curious)
> **特斯拉要造无人驾驶出租车了**
>
> 特斯拉公布了一款叫 Cybercab 的小车，没有方向盘也没有踏板，完全自动驾驶，定价不到 3 万美元。计划 4 月在德州工厂开始生产。
>
> 不过这个计划有不少障碍：美国的安全标准要求车上必须有方向盘，而且有调查显示超过 60% 的美国人不信任自动驾驶技术。
>
> 你的 QQQ 和 VTI 基金里都包含一些特斯拉股票，但占比不大。

---

## 6. Chat Scenarios

### Scenario A: Casey × NVDA Daily Pick → "Should I buy?"

**User**: "Is this a good time to buy Nvidia?"

> That's a great question — let me walk you through the key things to think about instead of a yes or no.
>
> **What's working:** Nvidia's business is growing really fast. Think of it like a company that's selling the essential equipment during a gold rush — every big tech company needs their chips for AI.
>
> **What to consider:**
> - The stock is already priced for a lot of growth. If AI spending slows down even a little, the stock could dip.
> - You already own QQQ, which has about 8% Nvidia in it. So you're already getting some of the upside.
>
> **Bottom line:** It's not a "now or never" situation. Nvidia reports earnings in May — that'll give a clearer picture. No rush.
>
> 💬 Want to know more?
> - "How much Nvidia is already in my QQQ?"
> - "What happens to Nvidia if AI spending slows?"
> - "Is there a simpler way to invest in AI?"

### Scenario B: Robin × Tesla News → Portfolio Impact

**User**: "How does this affect my portfolio?"

> **Direct exposure: TSLA** — you hold it, this is a catalyst event.
>
> The Cybercab is the bull thesis crystallized: L4 autonomy at sub-$30k, "unboxed" manufacturing to cut production costs. If execution hits, the robotaxi TAM ($2T+ ARK estimate) justifies the 394.9x P/E.
>
> But the execution hurdles are real:
> - **Regulatory**: FMVSS requires steering controls
> - **Consumer**: 60% distrust autonomous vehicles
> - **Timeline**: Musk has missed every robotaxi timeline since 2019
>
> **Cross-portfolio read**: If Cybercab succeeds → bullish for GOOGL (Waymo), NVDA (inference chips). Your GOOGL and NVDA are both positively correlated to autonomous success.
>
> 💬 Dig deeper:
> - "What's Waymo's timeline vs Cybercab?"
> - "Size the robotaxi TAM for my TSLA position"
> - "How would I hedge the TSLA binary risk?"

### Scenario C: Frankie × JPM Daily Pick → Rate Deep Dive

**User**: "Walk me through the NII sensitivity to the June FOMC."

> JPM's NII guidance: ~$103B for FY26, assuming current rate environment holds.
>
> **Rate sensitivity model:**
>
> | Scenario | Fed Funds | NII Impact | ROTCE Impact |
> |----------|-----------|-----------|-------------|
> | Base (2 cuts) | 4.50-4.75% | -$2.5-3.0B | ~17.5% |
> | Dove (4 cuts) | 3.75-4.00% | -$5-6B | ~16.0% |
> | Hold (0 cuts) | 5.25-5.50% | +$1.5B | ~19.0% |
>
> **Counter-consensus read:**
> 2 cuts would re-steepen the curve (2s10s), which actually drives NIM expansion — absolute level matters less than shape.
>
> Your GS: similar NII sensitivity but higher trading mix (~45% vs JPM's ~25%). GS outperforms JPM in volatile rate environments.
>
> 💬 Next:
> - "Compare JPM vs GS NII sensitivity side by side"
> - "Model the NCO trajectory if rates hold through Q3"
> - "What's the CET1 impact of the Basel III endgame delay?"

---

## 7. Sample News Headlines (for News Feed mock data)

| # | Headline | Theme | Date |
|---|----------|-------|------|
| N1 | Arista Unveils 12.8 Tbps Optic, Boosting AI Data Center Density 4X | AI Infrastructure | 2026-03-12 |
| N2 | BOJ Poised for 1.00% Rate Hike as Inflation Pressures Mount | Macro/Rates | 2026-03-12 |
| N3 | Berkshire Resumes Buybacks After Two-Year Hiatus | Value/Defensive | 2026-03-12 |
| N4 | Tesla Reveals Sub-$30k Cybercab With No Steering Wheel | EV/Autonomous | 2026-03-12 |
| N5 | Pharmaron Stock Climbs 12.6% on $200M Eli Lilly GLP-1 Deal | Healthcare/GLP-1 | 2026-03-12 |
| N6 | Asian LNG Supply at Risk as Mideast Conflict Threatens Chokepoint | Geopolitics/Energy | 2026-03-12 |
| N7 | Defensive Stocks Fail as Investors Favor US Dollar | Macro/Defensive | 2026-03-12 |
