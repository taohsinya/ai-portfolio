# On-chain / Technical Data Template (Model D)

Use for: Crypto>Bitcoin, Crypto>Altcoins & DeFi, Markets>Market Moves, Energy>Mining & Commodities

---

## Output Format

```markdown
# [Title: ≤11 words, sentence case, lead with price/level + direction]

[LEDE: One sentence, ≤25 words. Price + move + timeframe. Nothing else.
Bad: "Bitcoin surged today as market sentiment improved amid institutional interest."
Good: "Bitcoin hit $97,400, up 4.2% in 24 hours, after $340M in short liquidations triggered a rally above $95,000."]

**Key Takeaways:**
- [Price action: exact price, % change, key level breached or tested]
- [Flow/on-chain signal: whale move, exchange flow, OI change, funding rate — with source]
- [What to watch: next level, upcoming event, risk scenario]

## [H2 #1: Price Action — headline includes exact price and direction]

[150-250 words. Price with full precision (see model-d-onchain.md rules).
Volume (24h, vs 7d average).
24h high/low range.
Key support/resistance levels tested, with date context for those levels.
Liquidation data if >$50M: "$X million in [long/short] liquidations across [exchanges] in [timeframe]".]

## [H2 #2: On-chain / Flow Signal — headline names the specific signal]

[150-250 words. Exchange inflow/outflow: net direction, magnitude, 7d trend.
Whale transactions: amount, source (Arkham, Whale Alert), wallet identification if known.
Open Interest: absolute + % change + direction.
Funding Rate: exact value + whether it's rising/falling + what it implies.
For commodities: inventory data, production data, rig count.]

## [H2 #3: What's Next — headline names the level or catalyst]

[100-200 words. Next technical level with historical context.
Upcoming catalyst with exact date.
One specific risk scenario: "If [price drops below $X], then [Y]."
No speculation — only data-backed scenarios.]

---
*Disclaimer: This article is for informational purposes only and does not constitute investment advice. Past performance is not indicative of future results. Always conduct your own research before making investment decisions.*
```

## Data Precision Rules (Non-negotiable)

| Asset | Precision | Example |
|-------|-----------|---------|
| BTC | Nearest $1 | $97,423 |
| ETH | Nearest $0.01 | $3,847.12 |
| Altcoins >$1 | Nearest $0.01 | $178.34 |
| Altcoins <$1 | Nearest $0.0001 | $0.6234 |
| Gold | Nearest $0.10 | $2,178.40/oz |
| Oil (WTI) | Nearest $0.01 | $78.43/bbl |
| Copper (LME) | Nearest $1 | $9,234/tonne |
| S&P 500 | Nearest 0.01 | 5,234.18 |
| VIX | Nearest 0.01 | 18.34 |

## Checklist Before Output

- [ ] Lede ≤ 25 words, price + move + timeframe only
- [ ] Title ≤ 11 words, includes number
- [ ] Every price follows precision rules above
- [ ] Every data point has a timestamp (at minimum "as of [date]")
- [ ] Every on-chain claim names the source (Glassnode, CryptoQuant, Arkham, etc.)
- [ ] No sentiment words in lede (surged, plummeted, soared, tanked)
- [ ] Liquidation data in standard format if included
- [ ] Total word count: 400-700
- [ ] Zero banned words
