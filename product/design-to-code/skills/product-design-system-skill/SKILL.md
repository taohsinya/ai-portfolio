---
name: product-design-system-skill
description: Product design-system skill for a dark-themed, mobile-first investing app — UI component generation (Next.js / React + Tailwind PWA), design tokens and brand rules, marketing-site design, and bilingual UX writing (EN + Traditional Chinese, multi-locale). Use for frontend component work, in-app copy, labels, tooltips, notifications, onboarding flows, and landing pages that must stay consistent with the product's design system and voice.
---

# {Product} Design System

**{Product}** is a stock market app for retail investors to discover opportunities across US stocks, HK stocks, crypto, and IPOs. This skill equips you with the design system, brand voice rules, UI generation patterns, and UX-writing conventions needed to build on-brand screens and copy.

## Task Routing

| Task | Reference to Read |
|------|-------------------|
| Build UI / write code / implement app components | [ui-generator.md](references/ui-generator.md) |
| Design tokens, colors, spacing, brand system | [brand-system.md](references/brand-system.md) |
| Vibe-code website / landing page / marketing web page | [website-design.md](references/website-design.md) + [brand-system.md](references/brand-system.md) |
| Write in-app copy, labels, tooltips, notifications | [ux-writing.md](references/ux-writing.md) |

Load only what you need. For complex tasks spanning multiple areas, load the primary reference first, then supplement.

## Universal Rules (Always Apply)

### Brand Identity
- Brand name: always written exactly as styled in the logo (e.g., **{product}** in lowercase) — never re-cased in external-facing copy
- Never use the in-app AI persona name (**{Assistant}**) or internal codenames in external content (permitted inside app UI only)
- Logo always visible in marketing materials

### The 3-Line Rule
More than 3 lines of text = noise. This applies everywhere: UI cards, marketing copy, ad headlines, push notifications. If it takes more than 8 seconds to parse, rewrite it shorter.

### Proof Over Promises
Always show real numbers: tickers, percentages, win rates, price targets. Never use vague claims like "great returns" or "smart investing." The product speaks through data.

### Multilingual Defaults
- Global audience, English as primary language
- Traditional Chinese (HK) is the primary secondary language
- Supported locales (example set): EN, zh-TW, zh, ko, vi, es, tr, fr, ja
- English and Chinese are **independent voices**, not translations of each other
- Chinese (HK) uses Cantonese slang and HK internet vocabulary
- Tickers always in English, company names localized per language

### Tone
- **English**: Confident, democratizing, slightly rebellious. Example tagline: "{example tagline}".
- **Chinese**: Bold, colloquial, dopamine-driven. Uses 爆升, 當炒, 揀出. Street energy, not corporate.
- **Both**: Never lecture. Let users feel they're discovering. Actionable > educational.

### Brand Voice (Credible, Not Hyperbolic)

Think Bloomberg or The Economist, **not** crypto Twitter. Authority comes from DATA, not adjectives.

- Short punchy sentences. No filler. Contractions always.
- One idea per sentence. Numbers are facts, not hype: "30% CAGR" is a fact. "EXPLODING 30%" is hype.
- Easy for non-native English speakers — no idioms that don't translate.
- Smart analyst who explains clearly, like a smart friend who trades.

**Strictly forbidden:**
- Self-referential AI persona names (e.g., {Assistant}) in external content
- "X isn't Y, it's Z" patterns (AI slop)
- "let's dive in", "buckle up", "without further ado"
- Questions in headlines or hooks — be assertive, not rhetorical
- Assuming the viewer already has a portfolio or is an investor

**Forbidden hype words (anti-scammy):**

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

**Credibility check (apply to all content):**
1. Could this sentence appear in a crypto pump video? If yes → rewrite.
2. Numbers as facts or hype? Facts = credible. Hype = scammy.
3. Does the CTA create curiosity or desperation? Curiosity = good. Desperation = scammy.
4. Would The Economist use this sentence? If no → rewrite.

### Gating Philosophy (Content vs App)

Free content creates an itch only the app can scratch.

**REVEALED (free content — all formats):**
- The macro narrative / thesis / sector
- Catalysts and key stats
- Triggering tickers (companies that CAUSE or FLAG the opportunity, e.g., NVIDIA)
- The theme name
- The count of plays: "{N} stock plays identified"

**GATED (app only — NEVER in free content):**
- Play tickers (companies you'd actually buy)
- Specific ratings and entry points
- Portfolio positions and stop losses

**Why this matters:** If free content reveals the play tickers, the viewer looks up the company and skips the app. Every piece of free content should make the viewer know a sector is moving but NEVER which specific companies to buy.

**FOMO > Begging.** The CTA creates curiosity ("3 stock plays identified — see them in the app"), never desperation ("please download our app").

### Legal
Every piece of content showing stock data, picks, or performance numbers must include:
- **EN**: "This material is for information only and does not constitute an offer, invitation, commitment, advice or recommendation to acquire."
- **CN**: "本資料不構成任何投資意見，亦並非以銷售任何投資產品或服務為目的，亦不應被視為與其有關的要約、招攬、建議或保證。"

## UI Quality Checklist

Before deploying any generated component:
- [ ] Uses the exact design-token colors (example palette: #0B0D10 bg, #15181D cards, #4F8CFF accent)
- [ ] No gradient backgrounds on cards/components — solid colors only, EXCEPT Signal Banner (`bg-gradient-to-r from-[#4F8CFF]/20 to-[#22C55E]/20`) and marketing/website section backgrounds
- [ ] Only the product's own icon library used — no open-source icon libraries
- [ ] All badge/label/tag text uses font-bold
- [ ] Follows 3-line text rule for all content blocks
- [ ] Includes proper win rate badges and credibility indicators where applicable
- [ ] Implements the brand font family correctly
- [ ] Responsive design works on mobile and desktop (mobile-first)
- [ ] Touch targets minimum 44x44px for all interactive elements
- [ ] Brand voice maintained (no forbidden terms)
- [ ] Realistic data examples used (not placeholder lorem ipsum)
- [ ] Accessibility standards met (color never sole indicator, +/- with colors)
