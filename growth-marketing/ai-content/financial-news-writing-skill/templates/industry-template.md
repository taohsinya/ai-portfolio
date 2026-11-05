# Industry Trend Template (Model C)

Use for: Tech & AI (all), Energy>EV & Clean, Healthcare>Biotech

---

## Output Format

```markdown
# [Title: ≤11 words, sentence case, name the competitive shift not the product]

[LEDE: One sentence, ≤35 words. Lead with the INDUSTRY IMPACT, not the product feature.
Bad: "Amazon announced its Trainium3 chip at re:Invent 2025."
Good: "Amazon's Trainium3 chip offers 2x the memory bandwidth of Nvidia's H100 at an estimated 40% lower cost, threatening Nvidia's $62B data center business."]

**Key Takeaways:**
- [What's new: product/technology + key spec with number]
- [Who wins and who loses: competitive shift with data]
- [Investment implication: ticker + directional view]

## [H2 #1: Product/Technology name — headline includes a number]

[200-300 words. Explain the technology/product in plain language.
Jargon rule: if a term requires domain expertise, add a parenthetical.
Key specs with comparison to predecessor AND competitor.
Timeline: availability date, production ramp, GA date.
Named company source (press release, exec quote, filing).]

## [H2 #2: Competitive impact — headline names winner and loser]

[200-350 words. Market share data or revenue comparison.
Who gains share, who loses — quantified.
Customer reaction or adoption signals (design wins, pre-orders, pipeline).
Named analyst view on competitive dynamics (firm + analyst name + key quote/view).]

## [H2 #3: Investment angle — headline connects to a ticker or sector]

[150-250 words. Which tickers are affected and directional view.
Valuation context: is the market pricing this in? (P/E, EV/Revenue vs history).
Key risk to the investment thesis.
What to watch next: specific date, event, or data point.]

---
*Disclaimer: This article is for informational purposes only and does not constitute investment advice. Past performance is not indicative of future results. Always conduct your own research before making investment decisions.*
```

## AI Slop Enforcement (Model C gets strictest check)

Before output, run EVERY sentence through these filters:
1. Does the sentence contain ANY Tier 1 banned word? → Rewrite
2. Does the sentence contain ANY Tier 4 (Model C specific) banned word? → Rewrite
3. Can you remove the sentence and lose zero information? → Delete it
4. Does the sentence have at least one number or named entity? → If not, it's probably filler

## Checklist Before Output

- [ ] Lede ≤ 35 words, leads with industry impact
- [ ] Title ≤ 11 words, sentence case, names the competitive shift
- [ ] At least 1 competitor named with quantified comparison
- [ ] Investment angle present with ticker
- [ ] Plain language rule applied (parentheticals for jargon)
- [ ] ZERO Tier 4 banned words (disruptive, ecosystem, game-changer, revolutionary, groundbreaking, next-generation, state-of-the-art)
- [ ] Every technology claim has a number attached
- [ ] Total word count: 600-1,000
- [ ] Zero banned words from all tiers
