# UI Prototype Design System

> **Apple aesthetic, Bloomberg data.**
> Generous whitespace. Let numbers speak — never explain in words what a chart or table can show.
> Every pixel earns its place. If text can be replaced by a visual, replace it.

## 0. Apple Design Principles (Non-Negotiable)

1. **Show, don't tell.** Numbers in tables/charts, not in paragraphs. "Revenue grew 65%" → a bar or a single bold number with a green arrow.
2. **One idea per view.** Each card has ONE focal point. Don't cram.
3. **Whitespace is content.** 32px minimum between sections. Cards breathe.
4. **Typography does the hierarchy.** Size and weight replace labels. A 28px bold number needs no "Revenue:" prefix.
5. **Progressive disclosure.** Feed = glanceable. Tap = details. Scroll = depth. Never show depth-3 content at depth-1.
6. **Motion > text.** Sparklines, progress rings, color gradients convey state faster than sentences.
7. **Zero decoration.** No borders unless separating data. No shadows unless lifting a card. No icons unless they replace a word.

---

## 1. Color Palette

> **Example palette** — neutral placeholder values. Swap in your own brand tokens;
> keep the token names and roles.

### Core
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-primary` | `#111827` | Dark slate — headers, primary text |
| `--color-accent` | `#16A34A` | Green — positive values, CTAs, selected states |
| `--color-negative` | `#DC2626` | Red — negative values only |
| `--color-surface` | `#FFFFFF` | Card backgrounds |
| `--color-bg` | `#F5F6FA` | Screen backgrounds |
| `--color-muted` | `#8E8E93` | Secondary text, timestamps |

### Data Colors
| Token | Hex | Usage |
|-------|-----|-------|
| `--data-bullish` | `#16A34A` | Positive price change, bullish signals |
| `--data-bearish` | `#DC2626` | Negative price change, bearish signals |
| `--data-neutral` | `#6C757D` | Unchanged, neutral data |
| `--data-highlight` | `#FFD700` | Featured/hero elements, ★ picks |

### Dark Mode (optional)
| Token | Hex | Usage |
|-------|-----|-------|
| `--dark-bg` | `#0D1117` | Screen background |
| `--dark-surface` | `#161B22` | Card background |
| `--dark-text` | `#E6EDF3` | Primary text |
| `--dark-border` | `#30363D` | Card borders |

---

## 2. Typography

### Font Stack
```
--font-primary: 'Inter', -apple-system, system-ui, sans-serif;
--font-mono: 'JetBrains Mono', 'SF Mono', monospace;  /* for data/numbers */
```

### Scale
| Token | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `--text-hero` | 28px | 700 | 1.2 | Greeting, hero headlines |
| `--text-h1` | 22px | 700 | 1.3 | Screen titles |
| `--text-h2` | 18px | 600 | 1.3 | Section headers |
| `--text-h3` | 16px | 600 | 1.4 | Card titles, ticker names |
| `--text-body` | 15px | 400 | 1.5 | Body text, descriptions |
| `--text-body-sm` | 13px | 400 | 1.4 | Secondary info, timestamps |
| `--text-data` | 14px | 500 | 1.3 | Numbers, metrics (mono font) |
| `--text-data-lg` | 18px | 600 | 1.2 | Price display (mono font) |
| `--text-caption` | 11px | 500 | 1.3 | Labels, tags |

### Chinese Typography
```
--font-zh: 'PingFang SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
```
- Body text 1px larger than EN (16px vs 15px)
- Line height 1.6 for Chinese text (vs 1.5 for EN)
- No italic — use color or weight for emphasis

---

## 3. Spacing & Grid

### Spacing Scale
```
--space-xs: 4px
--space-sm: 8px
--space-md: 12px
--space-lg: 16px
--space-xl: 24px
--space-2xl: 32px
--space-3xl: 48px
```

### Screen Layout
```
Screen padding: 16px horizontal
Card gap: 12px
Section gap: 24px
Tab bar height: 83px (includes safe area)
Status bar: 47px (iOS) / 24px (Android)
```

### Card Grid
- Feed cards: Full width, stacked vertically
- Hero card: Full width, min-height 180px
- Secondary cards: Can be 2-column on wider screens (≥390px)
- Card border-radius: 12px
- Card shadow: `0 1px 3px rgba(0,0,0,0.08)`
- Card padding: 16px

---

## 4. Component Variants — Apple Style Cards

**Core rule**: Cards are VISUAL, not paragraphs. Numbers are big and bold. Text is minimal. Tables replace sentences.

### Compact Row (~56px) — A_Casual
```
┌─────────────────────────────────────────┐
│                                         │
│  NVDA          ▁▂▃▄▅▆▇    $184.77      │
│  Nvidia        ────────    +4.2% ↑      │
│                                         │
└─────────────────────────────────────────┘
```
- Ticker + name left, sparkline center, price + change right
- Zero text description. The sparkline IS the story.
- Tap to reveal one-liner

### Standard Card (~96px) — B_Curious
```
┌─────────────────────────────────────────┐
│                                         │
│  NVDA  Nvidia                   +4.2%   │
│  $184.77                               │
│                                         │
│  Revenue +65%        AI chip demand     │
│  ███████████░░  ↑    is accelerating    │
│                                         │
│  ○ AI Capex  ○ Growth                   │
│                                         │
└─────────────────────────────────────────┘
```
- Price prominent (--text-data-lg)
- ONE key metric as a progress/bar visual, ONE sentence max
- Tags as subtle dots + text, not pill buttons

### Data Card (~120px) — D_Engaged
```
┌─────────────────────────────────────────┐
│                                         │
│  NVDA  Nvidia                   +4.2%   │
│  $184.77          Mkt Cap  $4.5T        │
│                                         │
│  ┌──────────┬──────────┬──────────┐     │
│  │ Rev       │ GM       │ PEG      │     │
│  │ +65% ↑   │ 75.0%    │ 0.8      │     │
│  │ $215.9B   │ -50bps   │ < 1 = ✓  │     │
│  └──────────┴──────────┴──────────┘     │
│                                         │
│  Next: May earnings                     │
│  ○ AI Capex  ○ Growth                   │
│                                         │
└─────────────────────────────────────────┘
```
- **3-column metric grid** replaces text paragraphs
- Each cell: label (small, muted) → value (large, bold) → delta (small, colored)
- ONE catalyst line. Not a list.
- Jargon tooltip on tap (ⓘ), not inline explanation

### Full Card (~148px) — F_Expert
```
┌─────────────────────────────────────────┐
│                                         │
│  NVDA  $184.77  +4.2%      $4.5T       │
│                                         │
│  ┌────────┬────────┬────────┬────────┐  │
│  │ Rev    │ GM     │ FCF    │ PEG    │  │
│  │ +65%   │ 75.0%  │ 51%   │ 0.8    │  │
│  ├────────┼────────┼────────┼────────┤  │
│  │ P/E    │ P/S    │ EV/Rev │ Short  │  │
│  │ 55.2x  │ 20.8x │ 28.5x │ 1.2%   │  │
│  └────────┴────────┴────────┴────────┘  │
│                                         │
│  May earnings · GTC · China policy      │
│  $155 Jun call unusual  ○ IV30 48%      │
│                                         │
└─────────────────────────────────────────┘
```
- **4×2 metric grid** — pure numbers, zero prose
- Catalysts as a single dot-separated line
- Options flow as data, not a sentence
- No description text at all — the grid IS the description

---

## 5. Data Display Patterns

### Metric Grid (Primary — replaces paragraphs)
```
┌────────┬────────┬────────┐
│ Label  │ Label  │ Label  │   ← --text-caption, --color-muted
│ Value  │ Value  │ Value  │   ← --text-data-lg, --color-primary, bold
│ Delta  │ Delta  │ Delta  │   ← --text-body-sm, colored (green/red/gray)
└────────┴────────┴────────┘
```
- 3 or 4 columns depending on archetype density
- Equal width columns, 8px gap
- No borders — whitespace separates
- Background: --color-surface (white)
- This is the **default** data display. Use this instead of inline text for metrics.

### Comparison Table (Detail page only — E_Sophisticated / F_Expert)
```
              Q4 FY25    QoQ      YoY     vs Est
Revenue       $35.1B    +12%     +93%     +8%
Gross Margin   75.0%   -50bp   +200bp    Inline
FCF Margin      51%   +200bp   +800bp      —
```
- No visible borders — alignment creates the grid
- Header row: --text-caption, --color-muted
- Data rows: --text-data, alternating bg (transparent / #F8F9FA)
- Numbers right-aligned, mono font
- Apple-style: feels like a spreadsheet that has been art-directed

### Scenario Visual (Detail page only — F_Expert)
```
        Bull ──────────────── $185  (30%)
        Base ─────────────── $155  (50%)  ← highlighted
        Bear ────────── $95  (20%)

        Weighted: $150
```
- Horizontal bars, length proportional to value
- Color: green/gray/red
- Base case highlighted with heavier weight
- NO table borders. Just bars + numbers.

### Sparkline
```
▁▂▃▂▃▄▅▆▅▆▇█
```
- 64px wide, 24px tall
- Stroke weight: 1.5px
- Color follows direction (green up, red down)
- No axis labels — this is a glanceable trend, not a chart

### Progress Ring (single metric spotlight)
```
    ╭───╮
    │75%│    Gross Margin
    ╰───╯
```
- 48px diameter
- Ring color: --data-bullish if above benchmark
- Center: the number in --text-data-lg
- Label below in --text-caption
- Use for 1-2 hero metrics on a card, not for grids

---

## 6. Interactive Elements

### Tag Pills
```
[AI Capex]  [Growth]  [Mod Cyclical]
```
- Border-radius: 16px
- Padding: 4px 12px
- Font: `--text-caption`, 500 weight
- Background: `#E8F5E9` (theme-colored, subtle)
- Text: `--color-primary`

### CTA Buttons
```
Primary:   [Show me my feed]     ← filled, --color-accent bg, white text
Secondary: [I'll explore first]  ← outlined, --color-accent border
```
- Border-radius: 8px
- Height: 48px
- Full width on mobile

### Chat Input
```
┌────────────────────────────── ▶ ┐
│  Ask me anything about NVDA...  │
└─────────────────────────────────┘
```
- Border-radius: 24px
- Background: `#F5F6FA`
- Placeholder text varies by archetype

### Feedback Widget
```
Was this helpful?  👍  👎
```
- On 👎, slide up: [Too simple] [Just right] [Too complex]
- Subtle, bottom of detail pages

### Follow-up Chips (Chat)
```
"Compare with AMD?"  "What's the bear case?"  "Buy or wait?"
```
- Outlined pills, tappable
- Max 3 per response
- Scroll horizontally if needed

---

## 7. Onboarding-Specific Components

### Welcome Screen
- Full-screen, centered
- Logo at top (40% from top)
- Tagline: `--text-hero`
- Subtitle: `--text-body`, `--color-muted`
- Single primary CTA
- Secondary CTA below (text link style)

### Language Selector
- Two large cards, 50% width each
- Flag emoji or language icon
- Selected state: `--color-accent` border, checkmark

### Topic Chips
- Wrap layout, 3 columns
- Unselected: outlined
- Selected: filled `--color-accent`, white text, checkmark
- Min 3 required, counter shown: "3/15 selected"

### Reading Style Cards (Step 3)
- 3 full-width cards, stacked
- **Must be visually VERY different in height** (3x ratio minimum)
- Card A: ~60px (2 lines)
- Card B: ~120px (4-5 lines, some data)
- Card C: ~200px (8+ lines, table, data-dense)
- Selected: green border + checkmark
- Title above: "When you read about a stock, what feels right?"

### Tone Selector
- 3 cards with example sentences
- Each shows the SAME information in different tone
- Reassuring: warm colors, softer
- Just the facts: neutral colors
- Direct: bold, action-oriented

---

## 8. Layout Patterns

### Tab Bar
```
┌──────┬──────┬──────┬──────┐
│ 🏠   │ 📊   │ 📰   │ 💬   │
│ Home │Picks │ News │ Chat │
└──────┴──────┴──────┴──────┘
```
- Active tab: `--color-accent` icon + text
- Inactive: `--color-muted`
- 83px total height (includes safe area)

### Screen Header
```
Good morning, Casey.
3 new picks for you today.
```
- Greeting: `--text-hero`
- Subtitle: `--text-body`, `--color-muted`
- Personalized with user's first name

### Section Dividers
```
── Earlier picks ──
```
- Centered text, `--text-caption`, `--color-muted`
- Thin lines on both sides
