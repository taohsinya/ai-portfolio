---
name: ui-prototype-skill
description: >
  Generate Figma-ready or code-based UI prototypes for a personalized investing
  content app with 4 features (Onboarding, Daily Picks, News, Chat). Produces adaptive
  card layouts, data-dense financial screens, and constraint-vector-driven content
  differentiation across 6 user archetypes, using a fixed set of synthetic mock data.
  Trigger on: "design a screen", "Figma prototype", "UI mockup", "make a screen",
  "onboarding flow", "picks layout", "news feed design", "chat UI", "设计界面",
  "做原型", "画页面". Also trigger when the user wants to visualize how
  personalization looks across archetypes.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, AskUserQuestion
---

# UI Prototype Skill v1.0

You design screens for **{Product}**, a personalized investing content app. Every screen must demonstrate
**dual-axis differentiation**: the same stock/news changes indicator sets via
3D routing (Style × Structure × Theme), and the same content changes presentation
via the user's 5-dimension constraint vector (depth, jargon, density, tone, framing).

## What Makes This UI Different from Generic Finance Apps

{Product} is NOT a trading app (no buy/sell), NOT an aggregator (no raw feeds), and
NOT a chatbot wrapper. It's a personalization engine. The UI must make the user
feel "this was written for me" without ever showing the personalization machinery.

**The user never sees**: archetype labels, constraint vectors, routing tables,
"simple/advanced" toggles, or any hint of segmentation.

**The user feels**: "This app just gets me."

## Apple Design DNA (MUST follow)

Every screen follows Apple's design language:

1. **Numbers > Words.** Data lives in metric grids and tables, NOT in text paragraphs. Show "+65%" in a big bold number with a green arrow — never write "revenue grew 65%".
2. **Whitespace is sacred.** 32px+ between sections. Cards breathe. Nothing feels crammed.
3. **Progressive disclosure.** Feed = glanceable (metric grid). Tap = details (comparison table). Scroll = depth (scenario bars). Each layer adds, never repeats.
4. **One focal point per card.** The eye lands on ONE thing — a number, a sparkline, a delta.
5. **Zero decorative text.** No "Key Metrics:" labels when the grid IS the metrics. No "Here's what's happening:" when a sparkline shows it.
6. **Tables replace paragraphs.** F_Expert doesn't get more text — they get a 4×2 metric grid. A_Casual doesn't get fewer words — they get a sparkline and a price.

**Anti-patterns (NEVER do):**
- Paragraph that describes data → USE a metric grid cell instead
- Card with >2 sentences of body text → USE a metric grid + 1 catalyst line
- Inline data like "P/E: 55.2x, P/S: 20.8x" → USE table columns
- Labels that state the obvious ("Price:", "Change:") → position conveys it

---

## Step 1 — Determine What to Design

Ask the user which screen(s) to design. If unclear, use AskUserQuestion:

**Screen options:**
1. **Onboarding** — 5-step flow (Welcome → Language → Topics → Reading Style → Tone → Confirmation)
2. **Daily Picks Feed** — Personalized stock cards with adaptive density
3. **Daily Picks Detail** — Full stock analysis page (C2/C5/C7 sections)
4. **News Feed** — Personalized news cards with adaptive headlines
5. **News Detail** — Full article with portfolio-linked commentary
6. **Chat** — Context-aware conversation UI (from Daily Picks or News entry)
7. **Multi-archetype comparison** — Same screen × multiple archetypes side-by-side

Also determine:
- **Archetype(s)**: Which user archetype(s) to show (A_Casual through F_Expert)
- **Language**: EN, 中文, or both
- **Stock/News context**: Which specific stock or news to use as content

If the user doesn't specify, default to a **multi-archetype comparison** of the
Daily Picks Detail screen for NVDA, showing 3 archetypes (A_Casual, D_Engaged, F_Expert).

---

## Step 2 — Load Mock Data

Read `references/mock-data.md` for the sample simulation outputs. These are
outputs generated from deep-dive research reports (NVDA, JPM, KO) and public news
articles, across 5 synthetic user profiles. Use these EXACTLY as mock data — do not generate new content.

The mock data includes:
- **Daily Picks**: NVDA × 5 users (38 words to 650 words)
- **Cross-stock routing**: Same user × NVDA/JPM/KO (completely different indicator sets)
- **News**: Tesla Cybercab × 3 users
- **Chat**: 3 scenarios (buy question, portfolio impact, rate deep dive)

---

## Step 3 — Load Design System

Read `references/design-system.md` for:
- Color palette, typography scale, spacing grid
- Card component variants (compact/standard/expanded/full)
- Data display patterns (inline, table, chart placeholder)
- Adaptive density rules per archetype

---

## Step 4 — Generate the Screen

### For Figma MCP (if available)

If the user has Figma MCP tools connected and provides a Figma file URL:
1. Use `get_design_context` to read existing design tokens
2. Generate components that match the existing design system
3. Adapt the mock data into the component structure

### For Code-Based Prototypes

Generate React + Tailwind components that match the design system. Structure:

```
ui-prototype/
├── src/
│   ├── components/
│   │   ├── OnboardingFlow.tsx
│   │   ├── PicksFeed.tsx
│   │   ├── PicksDetail.tsx
│   │   ├── NewsFeed.tsx
│   │   ├── NewsDetail.tsx
│   │   └── ChatView.tsx
│   ├── data/
│   │   └── mock-data.ts    ← from references/mock-data.md
│   └── styles/
│       └── design-tokens.ts ← from references/design-system.md
```

### For ASCII Prototypes (quick iteration)

Use AskUserQuestion with `preview` to show layout options. Example:

```
┌─────────────────────────────┐
│  Good morning, Casey.        │
│  3 new picks for you today.  │
├─────────────────────────────┤
│  NVDA  $184.77  +4.2%       │  ← A_Casual: 60px compact row
│  "AI chips are in demand"    │     1 tag, no data table
│  [AI]                        │
├─────────────────────────────┤
│  AAPL  $195.20  +1.1%       │
│  "Solid quarter"             │
│  [Tech]                      │
└─────────────────────────────┘
```

vs

```
┌─────────────────────────────┐
│  Frankie, 3 picks.          │
├─────────────────────────────┤
│  ★ NVDA  $184.77  +4.2%     │  ← F_Expert: 160px full card
│  Rev $215.9B (+65%), Q4     │     Full data panel
│  $68.1B (+73%), GM 75%      │     Multiple metrics inline
│  PEG 0.8 | EV/Rev 28.5x    │
│  ┌─ Catalysts ────────────┐ │
│  │ May: Earnings (+guide)  │ │
│  │ Apr: MSFT capex signal  │ │
│  └─────────────────────────┘ │
│  [AI Capex] [Growth] [Mod C] │
└─────────────────────────────┘
```

---

## Step 5 — Onboarding (Special Flow)

For the Onboarding screen, use **AskUserQuestion** to simulate the actual user
experience. This lets the user feel what their end-users will feel.

### Onboarding Simulation Sequence

**Step 0 — Welcome**: Show the welcome screen preview via AskUserQuestion.

**Step 1 — Language**: AskUserQuestion with 2 options (English / 中文).

**Step 2 — Topics**: AskUserQuestion with multiSelect=true, 4 topic groups
(each representing 3-4 topics). User picks 1-4 groups.

**Step 3 — Reading Style**: AskUserQuestion with 3 options + preview.
Each preview shows the SAME stock with different depth/jargon/density.
This is the core differentiation step — the previews must make the difference
viscerally obvious (3x length difference minimum).

**Step 4 — Tone**: AskUserQuestion with 3 options (Reassuring / Just the facts / Direct).

**Step 5 — Confirmation**: Show "Your {Product} is ready" with the inferred
constraint vector (hidden from real users, shown here for demo purposes).

Read `references/onboarding-flow.md` for the exact AskUserQuestion configurations.

---

## Screen-Specific Rules

### Daily Picks Feed
- Card height adapts: A_Casual ~60px → F_Expert ~160px
- Hero card is always larger, regardless of archetype
- "Why these picks?" expandable at bottom
- Theme + Style tags shown as pills
- sparkline placeholder for price trend

### Daily Picks Detail
- Sections: TL;DR → Why it's a pick (C2) → Key Numbers (C5) → Coming Up (C7)
- C5 indicator set determined by 3D routing (Growth ≠ Financial Leverage ≠ Income)
- Chat entry point: "Want to dig deeper? Ask {Assistant} about [TICKER]"
- Feedback: 👍/👎 with "too simple / just right / too complex" on 👎

### News Feed
- Segment control: For You | Markets | Trending
- Hero news card with personalized headline
- Compact list below with source + timestamp
- Cross-link cards: "Your [TICKER] has news"

### News Detail
- Full personalized rewrite (not original article)
- Related stocks section → links back to Daily Picks
- "Ask {Assistant} about this" → Chat with news context

### Chat
- Entry shows conversation starters (personalized per archetype)
- User messages: right-aligned bubbles
- AI responses: full-width content blocks (NOT bubbles) — can contain tables, charts, ticker cards
- Follow-up suggestions: 2-3 clickable chips after each AI response
- Input placeholder changes per archetype:
  - A_Casual: "Ask me anything about your investments..."
  - F_Expert: "Query: stock, sector, macro..."

---

## Voice Rules (Non-Negotiable for All Content)

These apply to ALL text shown in the UI:

1. **Never say "I'm an AI"** — {Product} is a product, not a persona
2. **Never use "As a large language model"** or any meta-AI language
3. **Never show the personalization machinery** — no "Based on your profile..."
4. **Always end with disclaimer** on detail pages: "This is not financial advice."
5. **Ticker format**: Always `TICKER` (never "$TICKER" or "ticker")
6. **Number format**: AP Style ($1.2B not $1,200,000,000; 4.2% not 0.042)
7. **Chinese content**: Native expression, not translation. 市盈率 not "P/E ratio 的中文"

---

## Multi-Archetype Comparison Layout

When showing the same screen across archetypes, use a side-by-side or stacked
layout that makes the differentiation viscerally obvious:

```
┌── A_Casual ──┐  ┌── D_Engaged ──┐  ┌── F_Expert ───┐
│ 38 words      │  │ 250 words      │  │ 650 words      │
│ No data       │  │ 4 data points  │  │ 3 tables       │
│ "AI chips     │  │ Revenue grew   │  │ Rev $215.9B    │
│  are hot"     │  │ 65% YoY...     │  │ (+65%), Q4...  │
│               │  │ [explain PEG]  │  │ PEG 0.8, P/S   │
│               │  │                │  │ 20.8x, EV/Rev  │
│               │  │                │  │ 28.5x...       │
│               │  │                │  │ ┌─ Scenarios ─┐│
│               │  │                │  │ │Bull: $185   ││
│               │  │                │  │ │Base: $155   ││
│               │  │                │  │ │Bear: $95    ││
│               │  │                │  │ └─────────────┘│
└───────────────┘  └────────────────┘  └────────────────┘
```

This layout is the single most powerful demo of the product's value proposition.
