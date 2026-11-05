# Onboarding Flow — AskUserQuestion Configurations

> This file contains the exact AskUserQuestion parameters for simulating
> the {Product} onboarding experience. When the skill is triggered for onboarding,
> run these steps sequentially.

---

## Step 0 — Welcome Screen (Preview Only)

Show the welcome screen as context, then proceed to Step 1.

```
Welcome preview (not an AskUserQuestion — just display this):

┌─────────────────────────────┐
│                             │
│         ✦ {PRODUCT}            │
│                             │
│  "Investing info that       │
│   actually fits you."       │
│                             │
│  Not dumbed down.           │
│  Not jargon-heavy.          │
│  Just right.                │
│                             │
│  [Let's set it up — 30 sec] │
│                             │
│   I'll explore first →      │
│                             │
└─────────────────────────────┘
```

---

## Step 1 — Language Selection

```json
{
  "questions": [
    {
      "question": "Which language do you prefer for {Product}?",
      "header": "Language",
      "multiSelect": false,
      "options": [
        {
          "label": "English",
          "description": "All content in English"
        },
        {
          "label": "中文",
          "description": "所有内容使用中文"
        }
      ]
    }
  ]
}
```

---

## Step 2 — Topic Interests

```json
{
  "questions": [
    {
      "question": "What investing topics interest you? Pick at least 3.",
      "header": "Topics",
      "multiSelect": true,
      "options": [
        {
          "label": "AI & Tech + Semis",
          "description": "Artificial intelligence, cloud computing, semiconductor chips (NVDA, MSFT, AAPL)"
        },
        {
          "label": "EV + Clean Energy",
          "description": "Electric vehicles, solar, nuclear, battery tech (TSLA, NEE, OKLO)"
        },
        {
          "label": "Healthcare + Crypto",
          "description": "GLP-1 drugs, biotech, Bitcoin, DeFi (LLY, BTC, COIN)"
        },
        {
          "label": "Dividends + Value",
          "description": "Income investing, undervalued stocks, real estate (KO, JPM, BRK.B)"
        }
      ]
    }
  ]
}
```

**Mapping logic:**
- AI & Tech → Theme: AI Capex, 中国供应链; Style hint: Growth
- EV + Clean → Theme: EV, Nuclear; Style hint: Growth/Speculative
- Healthcare + Crypto → Theme: GLP-1, Crypto; Style hint: mixed
- Dividends + Value → Theme: Defensive, 利率敏感; Style hint: Income/Value

---

## Step 3 — Reading Style (Core Step)

This is the most important step. The previews must make the difference
viscerally obvious — 3x length difference minimum.

**For English users:**

```json
{
  "questions": [
    {
      "question": "When you read about a stock, what feels right? Pick the one that sounds like how you'd want to hear it.",
      "header": "Style",
      "multiSelect": false,
      "options": [
        {
          "label": "Keep it simple",
          "description": "Quick, jargon-free. Get the point in one sentence.",
          "preview": "NVDA  $184.77  +4.2%\n\nNvidia makes the chips that\npower AI — and right now,\neveryone wants them.\n\nYour QQQ gives you some\nexposure already."
        },
        {
          "label": "Full picture",
          "description": "Explain what's happening and why it matters. Use plain language.",
          "preview": "NVDA  Nvidia  $184.77  +4.2%\n\nRevenue grew 65% last year\nto $215.9B — almost all from\nAI chips.\n\nPEG ratio: 0.8\n(under 1.0 means the stock\nmight be underpriced relative\nto its growth)\n\nFree cash flow: $25B+/year\n\nNext earnings: May — the big\ntest for whether AI spending\nis still accelerating."
        },
        {
          "label": "Fluent finance",
          "description": "Data-dense, professional language. No hand-holding.",
          "preview": "NVDA  $184.77 (+4.2%) | $4.5T\n\nFY26 $215.9B (+65% YoY)\nQ4 $68.1B (+73%), DC $35.1B\nGM 75% (-50bps QoQ)\nFCF margin 51.2%\nPEG 0.8 | EV/Rev 28.5x\n\n| Metric    | Value  | QoQ  |\n|-----------|--------|------|\n| Revenue   | $35.1B | +12% |\n| Gross Mgn | 75.0%  |-50bp |\n| FCF Mgn   | 51%    |+200bp|\n\nCatalysts: May earnings,\nGTC arch reveal, China policy"
        }
      ]
    }
  ]
}
```

**For 中文 users:**

```json
{
  "questions": [
    {
      "question": "看股票分析时，哪种风格最舒服？选最顺眼的那个就行，没有对错。",
      "header": "风格",
      "multiSelect": false,
      "options": [
        {
          "label": "简单明了",
          "description": "一句话说清楚，不用专业术语。",
          "preview": "英伟达 (NVDA)  $184.77  +4.2%\n\n英伟达是做 AI 芯片的公司，\n现在所有大科技公司都在\n抢着买它的产品。\n\n你的 QQQ 基金里已经包含\n了一部分英伟达股票。"
        },
        {
          "label": "看全貌",
          "description": "解释来龙去脉，用通俗语言讲清关键数据。",
          "preview": "英伟达 (NVDA) $184.77 +4.2%\n\n去年收入涨了 65%，达到\n2159 亿美元。\n\n市盈率 55 倍（你花 55 块\n才买到 1 块利润），但考虑\n到增速，其实不算太贵。\n\n利润率 75%，每年赚 250 亿\n美元现金。\n\n下次财报在 5 月，到时候\n会知道 AI 的需求是不是还\n在加速。"
        },
        {
          "label": "专业数据",
          "description": "数据密集，专业术语直接用，不需要解释。",
          "preview": "NVDA $184.77 (+4.2%) | $4.5T\n\nFY26 $215.9B (+65% YoY)\nQ4 $68.1B (+73%)\n毛利率 75% (-50bps QoQ)\nFCF margin 51.2%\nPEG 0.8 | EV/Rev 28.5x\n\n| 指标     | 数值   | 环比  |\n|----------|--------|------|\n| 数据中心 | $35.1B | +12% |\n| 毛利率   | 75.0%  |-50bp |\n| FCF率    | 51%    |+200bp|\n\n催化剂：5月财报, GTC大会,\n中国出口管制"
        }
      ]
    }
  ]
}
```

**Constraint vector mapping:**

| Selection | depth | jargon | density | Archetype range |
|-----------|-------|--------|---------|-----------------|
| Keep it simple / 简单明了 | headline | plain/explain | light | A_Casual / B_Curious |
| Full picture / 看全貌 | summary/analysis | explain | medium | B_Curious / C_Informed / D_Engaged |
| Fluent finance / 专业数据 | analysis/deep_dive | native | heavy | E_Sophisticated / F_Expert |

---

## Step 4 — Tone Preference

```json
{
  "questions": [
    {
      "question": "How should we talk to you about your investments?",
      "header": "Tone",
      "multiSelect": false,
      "options": [
        {
          "label": "Reassuring",
          "description": "\"Your portfolio is doing well — no need to worry.\"",
          "preview": "Your portfolio is up 3.2%\nthis month.\n\nNo need to worry — you're\non track. The market dipped\na bit last week, but that's\nnormal.\n\nNothing you need to do\nright now. ✓"
        },
        {
          "label": "Just the facts",
          "description": "\"Your portfolio is up 3.2% this month.\"",
          "preview": "Portfolio: +3.2% MTD\n\nTop performer: NVDA (+8.1%)\nLaggard: KO (-1.2%)\n\nNext event: NVDA earnings\n(May 28)"
        },
        {
          "label": "Direct",
          "description": "\"Portfolio +3.2% MTD. Consider rebalancing into the dip.\"",
          "preview": "Portfolio +3.2% MTD.\n\nNVDA +8.1% — now 35% of\nyour portfolio. That's\nconcentration risk.\n\nConsider trimming 5% into\nthe tech dip for balance.\n\nAction item: rebalance\nbefore May earnings."
        }
      ]
    }
  ]
}
```

**For 中文 users, replace with:**
- Reassuring → "安心型": "你的组合表现不错，不用担心。"
- Just the facts → "客观型": "你的组合本月涨了 3.2%。"
- Direct → "直接型": "组合 +3.2%，可以考虑趁回调调仓。"

**Mapping:**
| Selection | tone | framing hint |
|-----------|------|-------------|
| Reassuring / 安心型 | reassuring | impact_on_me |
| Just the facts / 客观型 | neutral | what_happened |
| Direct / 直接型 | direct | what_to_think / what_to_watch |

---

## Step 5 — Confirmation

After collecting all responses, display the result.

**For the demo/prototype**, show the inferred constraint vector:

```
"Got it. Your {Product} is ready."

Inferred profile (for demo purposes):
┌──────────────────────────────┐
│ Depth:   summary             │
│ Jargon:  explain             │
│ Density: medium              │
│ Tone:    neutral             │
│ Framing: what_happened       │
│ Topics:  AI, EV, Dividends   │
│ Language: English             │
│ Archetype: B_Curious          │
└──────────────────────────────┘

→ [Show me my feed]
```

**In the real app**, the user would NEVER see the constraint vector.
They would just see: "Got it. Your {Product} is ready." → CTA → Daily Picks feed.

---

## Post-Onboarding: What Happens Next

After onboarding completes, the skill should generate the Daily Picks Feed
screen populated with mock data matching the user's inferred archetype.

For example, if the user selected:
- "Full picture" + "Just the facts" → B_Curious / neutral
- Show Daily Picks feed with Blake's (U001) mock data
- Standard cards (~100px), 4 data points, jargon explained

This creates a seamless "set up → see result" experience in the prototype.
