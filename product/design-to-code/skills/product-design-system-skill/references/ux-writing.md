# {Product} UX Writing Guide

## Core Principles

1. **8-second rule** — user must understand value within 8 seconds of seeing any screen
2. **3-line max** — any text block over 3 lines is noise, rewrite shorter
3. **Actionable > educational** — "give me tickers, not financial reports"
4. **Guided exploration** — don't spoon-feed, let users discover (under your guidance)
5. **Dopamine-first** — investing is for the thrill, not retirement
6. **Global-first, localize second** — English is the primary language; localize for key markets (HK Traditional Chinese is the most developed secondary locale)

## Bilingual Copy Conventions

### Language Pairing Rules
- Tickers: always English (AAPL, 09988.HK)
- Company names: localized (Apple / 蘋果, Broadcom / 博通)
- Feature names: bilingual with English brand prefix ({Product} Picks / {Product} 精選)
- Numbers, percentages, prices: universal format (+25.56%, $138, 97%)
- Section headers: can be English-only in app (most sections use English headers)

### Bilingual Feature Name Glossary

| English (App) | Chinese (App) | Context |
|---------------|---------------|---------|
| {Product} Picks | {Product} 精選 | Core stock picks |
| Track Record | 過往戰績 / 歷史回購 | Performance history |
| Next Earnings Plays | 未來一周財報博奕 | Earnings predictions |
| HK IPO Strategies | 港股打新策略 | IPO recommendations |
| TA Signals | 技術分析信號 | Technical Analysis signals |
| Whale Tracker | 大佬持倉 | Guru portfolio tracking |
| Thematic Investing | 投資主題 | Theme-based stock lists |
| Sector Heatmap | 板塊熱力圖 | Sector performance overview |
| Deep-Dive Report | 深度報告 | Deep stock analysis |
| Portfolio Health Check | 投資組合健康檢查 | AI portfolio analysis |
| Ask {Assistant} | 詢問 {Assistant} | AI chat |
| Trending Themes | 熱門主題 | Market trends |
| Top Gainers | 升幅榜 | Best performers |
| Top Losers | 跌幅榜 | Worst performers |
| Win Rate | 勝率 | Success percentage |
| The Thesis | 投資論點 | Pick rationale |
| The Setup | 策略部署 | Earnings play rationale |
| The Strategy | 策略 | IPO rationale |
| Strong Buy / Strong Sell | 強烈買入 / 強烈賣出 | TA signal strength |
| Free Trial | 免費試用 | CTA |
| Download Now | 立即下載 | CTA |
| Get Started | 立即開始 | CTA |
| YTD | 年初至今 | Year-to-date label |

## Screen-by-Screen Copy Patterns

### Home Screen
**Signal banner**: "[number] signals scanned today" — use real-time count, builds trust through volume.

**Section headers**: Feature name + ">" arrow. Keep to 2-3 words. Include win rate badge where applicable (e.g., "85%").

**Stock pick cards** must include:
- Ticker + company name
- Entry price, Stop Loss, Current price
- Potential % (accent/green for positive)
- "The Thesis" — 1-2 sentences max, explain WHY, not WHAT
  - Good: "NVDA overvalued. Capital rotating to AMD. MI350 orders beating expectations."
  - Bad: "AMD is a semiconductor company that makes processors and graphics cards."

**Earnings cards** must include:
- Date + "Earnings Release"
- T+5 Probability (e.g., "80% Up")
- EPS Est. + Rev. Est. (Beat/Miss)
- "The Setup" — 1-2 sentences on the trade logic

**IPO cards** must include:
- Stock name + code
- Strategy recommendation (e.g., "Strongly Subscribe")
- Key stats: Potential, Over-sub ratio, Sponsor Win Rate
- Countdown timer for urgency
- "The Strategy" — 1-2 sentences on why

### Discover Tab
Each of the 13+ modules needs:
- Short section header (2-3 words)
- ">" for drill-down
- Market Pulse / AI insight: 1 sentence, opinionated, uses "but" or contrast structure
  - Good: "AI is back. NVIDIA is leading the charge, but small caps are lagging. Selective buys only."
  - Bad: "The AI sector has seen some positive movements recently."

### Portfolio Tab
- AI companion cards use question format: "What happened today?" / "Portfolio Health Check"
- Proactive, warm tone — this is "The Companion"
- Account display: mask account numbers (Broker ****1234)

### News Tab
- "For You" greeting: "Hey, [name] — Your news summary is ready."
- Show AI agent names as sources (Agent Sentiment, Macro Agent)
- Every news card has "Ask" button — implies conversational, not passive reading

### {Assistant} Chat
- Greeting: "我是您的智慧助手。這一次您想和我談論什麼？"
- Suggested prompts must be specific and investment-focused:
  - Include real tickers (both US and HK)
  - Ask about concrete metrics (ROE, support/resistance, institutional holders)
  - Never use generic prompts like "How can I help?"
- Input placeholder: "今天想一起探索些什麼？"

### Missions Tab
- Mission descriptions: Start with a verb, keep under 8 words. e.g., "Read 1 Deep-Dive Report", "See what {Assistant} found for your positions"
- Credit rewards: Always show the badge (+10, +50, +200) next to the task
- Check-in CTA: Simple "Checkin" button (white, high contrast)
- Streak language: "[number]/[target] days" with fire icon for streak
- Category pill labels: one word each (Weekly, Social, Onboarding, Advanced)
- Currency labels: "{Reputation points}" (reputation multiplier) and "Credits" (spendable)
- Help links: "View Breakdown" (accent) and "How to earn?" for transparency

## Writing Rationale Text (Thesis / Setup / Strategy)

Every pick, play, and IPO recommendation needs a rationale block. Rules:

1. **Max 2 sentences**
2. **Lead with the insight**, not the stock name
3. **Use contrast or catalyst structure**: "[Catalyst]. [Implication]."
4. **Be opinionated** — take a stance, don't hedge
5. **Use market jargon** the audience knows (gap up, squeeze, rotation, breakout)

Examples:
- "NVDA overvalued. Capital rotating to AMD. MI350 orders beating expectations."
- "Ads sold out. Playing for a violent gap up. All-in ATM Calls right before the event."
- "Cold chain logistics leader with strong cash flow. Sponsor has a high success rate on recent listings."
- "High probability of earnings beat. Validated by confirmed semiconductor memory price hikes."

## Paywall / Subscription Copy

### Tier Taglines
- One sentence per tier describing **who it is for**, not what it contains
- Pattern: "[Audience] [doing what], [with what level of depth]."
- Free → casual/new users; mid tier → everyday traders; top tier → full-time traders and analysts

### Conversion Copy Patterns
- Headline: short, personal value statement (e.g., "Your Personalized AI for Markets")
- Subheadline: how far the product goes, from essential signals to a fully tailored assistant
- Value anchor: "{annual price}" vs "{combined cost of comparable tools}"
- Urgency: "Save {N}%" on annual billing
- Social proof: Win rates, track record, testimonials
- CTA: "Subscribe" / "Get Started" / "Try for Free"

### Feature Copy Style
- Lead with the benefit, not the feature name
- Use concrete numbers: "{N} credits/month", not "lots of credits"
- "Unlimited Auto-Sync" > "Portfolio sync available"
- "Real-time + Institutional Depth" > "Advanced data"

### Payment Options
- "Subscribe" (primary CTA, white button)
- Secondary payment option shown below as a text link

## Push Notification / Alert Copy (Template)

Keep under 60 characters. Lead with the ticker or event.

- "[TICKER] hit your entry price. Time to act."
- "[TICKER] earnings in 2h. Our call: BEAT."
- "New {Product} Pick dropped. Check it before the market opens."
- "Your portfolio is up 3.2% today. See what's driving it."
