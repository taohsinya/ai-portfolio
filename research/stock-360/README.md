# Stock 360: an institutional-grade equity research method for LLMs

A single prompt (about 10,000 tokens) that turns a large language model into a disciplined sell-side-style analyst. Give it a company name and ticker, and it produces a full research report with the same structure, accounting rules and valuation logic every time.

I wrote this method for an AI investing product and used it to generate and validate around 90 reports across 14+ sectors. It is published here as an example of how I design analysis systems for LLMs.

> **Not investment advice.** This is a research method, not a recommendation to buy or sell anything.

---

## The problem it solves

Ask an LLM to "analyse NVIDIA" and you get a different report every time: different metrics, mixed GAAP and non-GAAP numbers, peers chosen at random, and valuation targets with no stated method. That is fine for a chat, but useless for a product where thousands of reports must be comparable.

This method fixes the analyst's behaviour before it starts writing.

## How it is designed

### 1. Global protocols, stated once
Rules that apply to every section, so the model never has to guess:
- **Valuation:** GAAP is the default; forward estimates are allowed but labelled; non-GAAP only when it differs by more than 10%, and the gap must be explained (stock-based comp, restructuring, impairment).
- **Comparison:** every metric is compared against its 5-year history, 3–5 named peers, and the industry median.
- **EPS, margins, revenue:** always diluted EPS; GAAP margins with a stock-based-comp flag above 5% of revenue; revenue growth split into reported, constant-currency and organic.
- **Free cash flow and multi-segment companies:** one definition of FCF, and sum-of-the-parts rules for conglomerates.

### 2. Sector frameworks, injected selectively
17 sector playbooks (banks, insurance, semiconductors, SaaS, biotech, REITs, energy, pre-revenue and more). Each defines what matters in that industry, which KPIs to use, and which valuation methods to use or **not** use. For example, pre-profit biotech is valued on risk-adjusted NPV of the pipeline, never on P/E.

At runtime only the 1–2 relevant frameworks are injected, cutting the prompt from about 10,000 to about 7,000 tokens and keeping the model's attention on the right lens.

### 3. A fixed six-part report
1. **Business overview and industry:** segments, competitive landscape, market size, management track record
2. **Financials and growth:** latest earnings, revenue quality, valuation, margins, cash flow, balance sheet, earnings quality, risks and catalysts
3. **Competitive moat:** sources of advantage and capital allocation
4. **Momentum and investor confidence:** relative strength, volume, risk-adjusted momentum
5. **Narratives and analyst sentiment**
6. **Valuation scenarios:** bull, base, bear and disaster cases, each with a stated method, key assumptions and a probability; the four probabilities must add up to 100%

Every subsection ends with a one- or two-sentence **Subsection Thesis**, so a reader (or another agent) can skim the conclusions.

### 4. Output built for retrieval
Reports are written as paragraphs and bullet points, never tables, because they feed a retrieval (RAG) knowledge base and tables lose their structure when converted to vectors. Risks, catalysts and valuation scenarios use fixed templates (`EVENT BLOCK`, `VALUATION SCENARIO BLOCK`) so they can be parsed.

## Design choices worth noting
- **Force the model to show its working on valuation.** A target price must state its method, e.g. "35x forward P/E × $25.8 FY26 EPS", not just a number.
- **Probabilities in 5% steps.** Coarse steps stop the model from implying false precision.
- **Allow, but constrain, autonomy.** The model may add a new subsection when the data reveals a material theme, but it must follow the same format and end with a thesis.
- **Resolve conflicting guidance explicitly.** When the sector lens and the company's stage disagree (P/E vs P/S for a high-growth company), the prompt tells the model how to reconcile them.

## Files
- [`prompt.md`](prompt.md): the full prompt, v2.1

## How to use it
Replace `{company_name}` and `{ticker}`, keep the global protocols, and remove all sector frameworks except the one or two that fit the company. It works best with a model that has web search or a financial-data tool attached, since the prompt asks for cited, current data.
