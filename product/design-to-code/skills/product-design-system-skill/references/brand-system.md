# {Product} Brand System & Design Tokens

Brand identity rules and design-system structure, derived from the product's Figma designs, production website, and brand guidelines.

> **Note:** All hex values below are a neutral **example palette**. Swap in your own brand
> tokens — the token names, roles, and usage rules are the reusable part.

## Brand Identity

### Core Brand Rules (Never Compromise)
- **Brand Name**: always written exactly as styled in the logo (e.g., `{product}` in lowercase)
- **Never Use**: re-cased variants of the brand name, the in-app AI persona name ({Assistant}), or internal codenames in external content
- **Voice**: Bloomberg meets smart trading friend
- **Tone**: Confident, democratizing, slightly rebellious

### Brand Voice
- **English**: Confident, democratizing, slightly rebellious
- **Chinese**: Bold, colloquial, dopamine-driven
- **Universal**: Data-driven, never hyperbolic, actionable over educational

### Content Rules
- **3-Line Max**: Any text over 3 lines = noise, rewrite shorter
- **8-Second Rule**: User must understand value within 8 seconds
- **Proof Over Promises**: Show real numbers, not vague claims
- **No Hype Words**: See forbidden vocabulary list below

## Design Tokens

### Color System (Example Palette)
```css
/* Background Colors */
--bg-primary: #0B0D10;        /* Main app background */
--bg-card: #15181D;           /* Card backgrounds */
--bg-elevated: #1F232A;       /* Modals, elevated cards */

/* Accent Colors */
--accent-primary: #4F8CFF;    /* Primary brand accent — section headers, active tabs */
--accent-green: #22C55E;      /* Gains, buy signals, positive numbers */
--accent-red: #EF4444;        /* Losses, sell signals, negative numbers */
--accent-warning: #F59E0B;    /* Warning states */
--accent-highlight: #FACC15;  /* Marketing CTAs only (external, never in-app) */

/* Text Colors */
--text-primary: #ffffff;      /* Primary text */
--text-secondary: #ffffffcc;  /* Secondary text (80% opacity) */
--text-muted: #ffffff66;      /* Muted text (40% opacity) */

/* Interactive Colors */
--interactive-hover: #ffffff1a;    /* Hover states */
--interactive-border: #3A3F47;     /* Card borders */
--interactive-backdrop: rgba(255, 255, 255, 0.1);
```

### Typography System
```css
/* Primary Font: {Brand Sans} (example: any geometric sans with 300–900 weights) */
--font-primary: '{Brand Sans}', -apple-system, BlinkMacSystemFont, sans-serif;

/* Font Weights */
--weight-light: 300;
--weight-regular: 400;
--weight-medium: 500;
--weight-bold: 700;
--weight-black: 900;

/* Usage Patterns */
/* Headlines: Bold or Black */
/* Body Text: Regular */
/* UI Labels: Medium */
/* Emphasis: Medium Italic */
```

### Spacing System (4px Baseline Grid)
```css
/* Spacing Scale - Based on 4px baseline grid */
--space-0: 0px;       /* spacing-0 */
--space-1: 4px;       /* spacing-1 */
--space-2: 8px;       /* spacing-2 */
--space-3: 12px;      /* spacing-3 */
--space-4: 16px;      /* spacing-4 */
--space-5: 20px;      /* spacing-5 */
--space-6: 24px;      /* spacing-6 */
--space-7: 28px;      /* spacing-7 */
--space-8: 32px;      /* spacing-8 */
--space-9: 36px;      /* spacing-9 */
--space-10: 40px;     /* spacing-10 */
--space-11: 44px;     /* spacing-11 */
--space-12: 48px;     /* spacing-12 */
--space-14: 56px;     /* spacing-14 */
--space-16: 64px;     /* spacing-16 */
--space-20: 80px;     /* spacing-20 */
--space-24: 96px;     /* spacing-24 */
--space-28: 112px;    /* spacing-28 */
--space-32: 128px;    /* spacing-32 */

/* Common Usage Patterns */
--card-padding: var(--space-6);        /* 24px - Standard card padding */
--card-gap: var(--space-3);           /* 12px - Gap between cards */
--section-gap: var(--space-8);        /* 32px - Gap between sections */
--screen-padding: var(--space-4);     /* 16px - Screen horizontal padding */
--button-padding-x: var(--space-4);   /* 16px - Button horizontal padding */
--button-padding-y: var(--space-2);   /* 8px - Button vertical padding */
--element-gap: var(--space-3);        /* 12px - Gap between related elements */

/* Tailwind CSS Classes (Use these in components) */
/* gap-2 (8px), gap-3 (12px), gap-4 (16px), gap-6 (24px), gap-8 (32px) */
/* px-4 (16px), py-2 (8px), py-6 (24px), p-6 (24px) */
/* space-y-6 (24px), space-y-8 (32px) for vertical stacking */
```

### Border Radius
```css
--radius-sm: 4px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-card: 12px;      /* Standard card radius */
--radius-full: 9999px;    /* Pills, badges */
```

## Component Patterns

### Card Hierarchy
1. **Stock Pick Cards** - Primary trading recommendations
2. **Earnings Cards** - Earnings plays with probability
3. **IPO Cards** - IPO strategies with countdown
4. **Mission Cards** - Gamification system
5. **Metric Cards** - Portfolio summaries

### Card Interaction Rules
- **Cards with buttons**: No hover effects on card container - let buttons handle interactions
- **Cards without buttons**: Can have hover effects (hover:bg-white/10)
- **Simple containers**: Use bg-white/5 background, avoid colored borders unless specified
- **No gradients on cards**: Card and component backgrounds use solid colors only

### Background Color Rules
- **Regular cards**: Use bg-white/5 or bg-[#15181D] background only — solid colors
- **Tinted background components**: Use matching colored background at 5% opacity WITH matching borders (e.g., bg-[#4F8CFF]/5 with border-[#4F8CFF]/20)
- **Gradient exceptions (only these two cases)**:
  - ✅ **Signal Banner**: `bg-gradient-to-r from-[#4F8CFF]/20 to-[#22C55E]/20` — intentional live-data indicator
  - ✅ **Marketing/website backgrounds**: Accent-to-dark section gradients allowed in website-design.md contexts
  - ❌ Everything else: solid colors only

### Background Usage Guidelines
- **White/5 backgrounds**: Regular cards, containers — no borders needed
- **Tinted backgrounds**: Information sections, alerts, highlights — always include matching border

### Badge & Label Styling
- **All tags/labels/badges**: Always use `font-bold` for text
- **Risk labels**: Medium Risk, High Risk, Low Risk - always bold
- **Rating badges**: Strong Buy, Buy, etc. - always bold
- **Category tags**: Always bold with proper color coding

### Icon System Rules
- **ONLY use the product's own icon set**: Never use other open source icons or libraries
- **Icon library location**: the core-components file in the team's design tool (link kept internal)
- **When generating UI**: Always reference the product icon library for any icon needs
- **Consistency**: All icons across the product must come from the official icon set

### Message Icon Color Rules
- **Icon colors match message tint**: If message background is red-tinted (`bg-[#EF4444]/5`), icon should be red (`#EF4444`)
- **Accent messages**: Use accent icons (`#4F8CFF`)
- **Green messages**: Use green icons (`#22C55E`)
- **Red/Warning messages**: Use red icons (`#EF4444`)
- **Orange messages**: Use orange icons (`#F97316`)
- **Color consistency**: Icon, background tint, and border should all use the same color family

### Layout Patterns
1. **Horizontal Scroll** - Card collections (picks, earnings, IPOs)
2. **Vertical Stack** - Main content sections
3. **Grid Layout** - Price data, stats display
4. **Bottom Sheet** - AI chat interface
5. **Fixed Elements** - Signal banner, floating chat button

### Navigation Architecture
```
Bottom Navigation (5 tabs):
├── Home — Core features hub
├── Discover — Content exploration (13+ modules)
├── Portfolio — Asset management + AI companion
├── News — AI-curated feeds
└── Missions — Gamification system

Floating Elements:
└── AI Chat Bubble — Accessible from every screen
```

## Forbidden Vocabulary (Anti-Scammy)

### Never Use These Words
| Forbidden | Use Instead |
|-----------|-------------|
| "exploding" / "explosion" | "accelerating", "inflection point" |
| "massive" | "significant", "substantial" |
| "insane" / "crazy" | "remarkable", "notable" |
| "moonshot" | "high-growth", "emerging" |
| "game-changer" | "structural shift" |
| "nobody is talking about" | "overlooked", "under-discussed" |
| "no cap" / "yo" / "lowkey" | REMOVE — too crypto-bro |
| "to the moon" / "rocket" | NEVER — crypto scam signal |
| "secret" / "hidden gem" | "under-the-radar" (sparingly) |

### Credibility Check Questions
1. Could this sentence appear in a crypto pump video? If yes → rewrite
2. Numbers as facts or hype? Facts = credible. Hype = scammy
3. Does the CTA create curiosity or desperation? Curiosity = good
4. Would The Economist use this sentence? If no → rewrite

## UX Writing Patterns

### Rationale Text (Thesis/Setup/Strategy)
**Rules:**
- Max 2 sentences
- Lead with insight, not stock name
- Use contrast structure: "[Catalyst]. [Implication]."
- Be opinionated, don't hedge

**Examples:**
- ✅ "NVDA overvalued. Capital rotating to AMD. MI350 orders beating expectations."
- ✅ "Ads sold out. Playing for a violent gap up. All-in ATM Calls right before the event."
- ❌ "AMD is a semiconductor company that makes processors and graphics cards."

### Bilingual Feature Names
| English (App) | Chinese (App) | Context |
|---------------|---------------|---------|
| {Product} Picks | {Product} 精選 | Core stock picks |
| Track Record | 過往戰績 | Performance history |
| Next Earnings Plays | 未來一周財報博奕 | Earnings predictions |
| HK IPO Strategies | 港股打新策略 | IPO recommendations |
| Ask {Assistant} | 詢問 {Assistant} | AI chat interface |
| Win Rate | 勝率 | Success percentage |
| The Thesis | 投資論點 | Pick rationale |
| Strong Buy / Strong Sell | 強烈買入 / 強烈賣出 | Signal strength |

### Notification Copy Patterns
Keep under 60 characters. Lead with ticker or event:
- "[TICKER] hit your entry price. Time to act."
- "[TICKER] earnings in 2h. Our call: BEAT."
- "New {Product} Pick dropped. Check it before market opens."

## Data Display Standards

### Financial Formatting
- **Currency**: Always $ with 2 decimals ($150.00)
- **Percentages**: 2 decimals with sign (+19.42%, -3.21%)
- **Large Numbers**: Use comma separators (1,247 signals)
- **Dates**: "Jan 12 (EST)" for earnings, "Today 18:00" for news
- **Account Numbers**: Always mask (Broker ****1234)

### Color Coding Rules
- **Green (#22C55E)**: Positive numbers, gains, buy signals
- **Red (#EF4444)**: Negative numbers, losses, sell signals
- **Accent (#4F8CFF)**: Brand accent, active tabs, section headers, neutral positive
- **White (#ffffff)**: Neutral/zero values, primary text
- **Gray (#ffffffcc / #ffffff66)**: Secondary and muted information

### Win Rate Display
- Circular badge with accent border
- Percentage inside (e.g., 85%)
- Used alongside section headers for credibility
- Always real historical data, never estimated

## Responsive Design Rules

### Mobile-First (PWA)
- Touch targets: minimum 44x44px
- Horizontal scroll with peek cards
- Bottom navigation always visible (main tabs)
- Full-screen detail pages (hide bottom nav)

### Accessibility Standards
- Semantic HTML structure
- ARIA labels for financial data
- Color never sole indicator (use +/- symbols)
- Screen reader friendly component names
- Keyboard navigation support

### Performance Requirements
- Lazy loading for card collections
- Optimized images and assets
- Smooth scrolling animations
- Fast touch response (<100ms)

This brand system ensures consistent, credible, and production-ready UI components that maintain the product's professional trading platform identity.
