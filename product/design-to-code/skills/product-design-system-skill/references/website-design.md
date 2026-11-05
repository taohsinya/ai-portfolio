# {Product} Website Design Guide

For vibe-coding the {Product} marketing website, landing pages, and web experiences. Combines the product's brand identity with production-grade frontend aesthetics.

---

## Design Thinking (Before You Code)

Understand the context and commit to a BOLD aesthetic direction:

- **Purpose**: What problem does this page solve? What does the user do next?
- **Tone**: For {Product} — dark, premium, data-driven. Think Bloomberg meets streetwear. Credible but not corporate.
- **Differentiation**: What makes this page UNFORGETTABLE? One striking visual or interaction the user will remember.

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. The website should feel like a premium trading terminal, not a generic fintech SaaS landing page.

---

## Brand Constraints (Always Apply)

These override any general design choices:

### Colors (Example Palette — swap for your brand tokens)
```css
--bg-primary: #0B0D10;        /* Main background */
--bg-card: #15181D;           /* Cards, panels */
--bg-elevated: #1F232A;       /* Modals, elevated */
--accent-primary: #4F8CFF;    /* Primary brand accent */
--accent-green: #22C55E;      /* Gains, positive */
--accent-red: #EF4444;        /* Losses, negative */
--accent-highlight: #FACC15;  /* Marketing CTAs only */
--text-primary: #ffffff;
--text-secondary: #ffffffcc;
--text-muted: #ffffff66;
--border: #3A3F47;
```

### Typography
```css
/* Primary: {Brand Sans} — the brand's geometric sans, weights 300–900 */

/* Secondary (marketing aspirational emphasis only): Italic serif */
/* Use sparingly — e.g., italic "Stock Picks" in hero headlines */
```

- Headlines: {Brand Sans} Bold or Black — large and commanding
- Body: {Brand Sans} Regular
- Labels/UI: {Brand Sans} Medium
- **Never**: generic defaults (Inter, Roboto, Arial, or system fonts)

### Layout Rules
- Dark theme throughout — no light mode
- No gradient backgrounds on components (solid colors only)
- Highlight color (`--accent-highlight`) for acquisition CTAs: "Free Trial", "Download Now"
- White for premium CTAs: "Get Started →", "Try for Free →" (conversion)
- Real tickers and real % data — proof over promises

---

## Frontend Aesthetics (adapted from the frontend-design Claude Code plugin)

### Typography
- Pair the brand sans (primary) with a distinctive italic serif for aspirational moments
- Large, commanding type scales — headlines should dominate the viewport
- Unexpected sizing hierarchies that create visual rhythm

### Motion & Animation
- Use animations for high-impact moments: staggered reveals on page load, scroll-triggered sections
- Micro-interactions on CTAs and data elements (ticker numbers, percentages animating in)
- CSS-only for simple effects, Motion library for React when available
- One well-orchestrated entrance is better than scattered micro-interactions

### Spatial Composition
- Generous negative space in hero sections
- Asymmetric layouts that break the grid intentionally
- Phone mockup as hero visual — always showing real app screen
- Data visualizations (sparklines, heatmaps, signal counts) as design elements, not afterthoughts

### Backgrounds & Visual Depth
- Subtle noise textures or grain overlays for depth
- Gradient meshes behind key sections (accent-to-dark) for atmosphere — allowed in marketing, not in-app
- Layered transparencies for glassmorphism effects on cards
- Dramatic shadows on phone mockups and key UI elements

### What to AVOID
- Generic purple gradient on white — the site is dark always
- Cookie-cutter fintech SaaS aesthetic (blue, white, rounded everything)
- Stock photo people — use real app screens and data
- Vague copy ("powerful", "seamless") — use numbers and tickers

---

## Website Section Architecture

### Standard Landing Page Flow
```
1. Hero        — Bold headline + phone mockup + CTA
2. Problem     — One-line problem/positioning statement
3. Product     — Interactive demo or feature showcase
4. Features    — 3 pillars: Discovery, Picks, Portfolio
5. Proof       — Win rates, track record, testimonials, press
6. Pricing     — Tier comparison (e.g., Free / Pro / Expert)
7. FAQ         — Common objections handled
8. CTA Footer  — Final conversion push
```

### Hero Section Pattern
```
Headline (max 6 words): "{example headline}"
Subheadline (1 sentence): "{what the product does}. {availability}. {price anchor}."
CTA: [Free Trial] [Get Started →]
Visual: Phone mockup (right-aligned), accent gradient background behind
Signal count: "{N} signals scanned today" as social proof strip
```

### Pricing Section
| Tier | Price | Badge |
|------|-------|-------|
| Free | {price} | — |
| Pro | {price}/yr (Save {N}%) | "best" |
| Expert | {price}/yr (Save {N}%) | "best" |

Value anchor: total cost of comparable premium tools vs the product's price.

---

## Website Copy Rules

Same as universal brand voice — credible, not hyperbolic:
- Max 6 words per headline
- One idea per sentence
- Lead with data: "{N}% win rate", "{N} signals/day", "{price} vs {incumbent price}"
- CTAs create curiosity, not desperation
- Legal disclaimer required on any page showing stock data

### Key Taglines
- Keep a short, fixed list of approved taglines and use them verbatim
- Italic serif may emphasize one word in a tagline (e.g., "*actually*")

---

## Tech Stack for Website
- **Framework**: Next.js (same as app — shared codebase)
- **Styling**: Tailwind CSS with custom design tokens
- **Animations**: CSS animations + Framer Motion for React
- **PWA**: Web-first, installable on mobile
- **Performance**: Lazy loading, optimized assets, <3s LCP target
