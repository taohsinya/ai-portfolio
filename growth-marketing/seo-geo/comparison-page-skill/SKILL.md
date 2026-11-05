---
name: comparison-page
description: >-
  Write opinionated, EEAT-grade REVIEW and COMPARISON pages for {Product} —
  "best X tools" roundups, "X vs Y" head-to-heads, single-product reviews, and
  "alternatives" pages. Built for guest posts on other sites (backlinks and
  reach) and for pages that AI assistants can quote. NOT for generic how-to
  guides. Use when the user wants a guest post, comparison page, roundup,
  alternatives page, review, or a batch of them in English or Traditional
  Chinese (Hong Kong). Enforces an honest scorecard, answer-first structure,
  exactly 3 links, no FAQ block, and a compliance pass for a regulated
  (financial) product.
---

# Comparison Page / Guest Post

## What this page is for (read first)

A guest post lives on someone else's site. Its job is not to rank our own
site. Its job is to:

1. earn a link back to us (a "backlink", which helps our own pages rank),
2. reach that site's readers who are already shopping for a tool, and
3. get {Product} onto the shortlist of someone choosing a money tool.

Review and comparison pages with a real point of view do that job. Another
"how to set financial goals" guide does not — every finance blog already has
one.

> Generic how-to guides belong on **our own site**, where they can build topic
> authority and get picked up by Google's AI Overviews. If you catch yourself
> writing a how-to as a *guest* post, stop and switch to one of the page types
> in `references/page-types.md`.

## Workflow

1. **Pick the page type** from `references/page-types.md`: roundup,
   head-to-head, single review, or alternatives. If the user gives a topic or a
   news hook, choose the type that best matches what a buyer would search.
2. **Ground every claim in what ships today.** Keep a capability sheet with
   three lists: *shipping* (you may claim it), *ambiguous* (hedge it), *not
   built* (never claim it). If the sheet and the live website disagree, **the
   live website wins** — internal docs go stale. A spec or PRD is not a shipped
   feature. Check the live pricing page before you mention price.
3. **Research the competitors you name.** Real ones, with real strengths, from
   their public pages. No invented pros and cons.
4. **Write** using the page-type outline and the structural rules below.
5. **Compliance pass** against `references/compliance-checklist.md`. This is
   not optional. One slip (a buy/sell call, a made-up number, a feature that
   doesn't exist) can kill the placement and create legal risk.
6. **Deliver** one document per article, titled
   `[{week} · {locale} · {page type}] {headline}`, in a dated folder.

## Structural rules (every page type)

Thin pages get dropped from search. Clear, answer-first pages get quoted by
Google's AI Overviews and by chat assistants. So:

- **Answer first.** The first one or two sentences answer the title's question
  or give the verdict, in a form an AI could quote word for word. No warm-up.
- **Opinionated reviewer voice.** Pick a winner. Say who each tool is *wrong*
  for. A review with no point of view is useless.
- **Real pros AND cons for every tool, including {Product}.** Our honest cons
  (for example: it is a check-up, not a robo-advisor; it doesn't invest for you
  or file taxes) are what make the recommendation believable.
- **EEAT (Experience, Expertise, Authority, Trust).** Cite real, checkable
  sources: rules, public pricing, official docs. Attribute every figure. Use a
  real byline with relevant experience — never an invented author.
- **Put "People Also Ask" questions into the H2 headings.** Do **not** add a
  separate FAQ block at the end. FAQ rich results now show for very few sites,
  and the same 5-question block on every page looks like a template.
- **Depth over breadth.** About 1,000–1,400 words of real comparison, not a
  padded list.
- **Soft placement.** {Product} is one honest entry, not a wall-to-wall ad.
  Let the analysis do the selling.

## Scoring (roundups, comparisons, alternatives)

A score makes a review easy to scan and easy to quote — but only if it is
*earned*. Use a **transparent, criteria-based scorecard**, never a star rating
from nowhere.

- Define **4–6 criteria up front**. Score every tool on every criterion with
  one scale (for example /10). The overall score is the average of the
  criteria — a number the reader can rebuild.
- **Show the scorecard as a table** (tools × criteria + overall). The visible
  reasoning is the value you add over a promo listicle.
- **{Product} must NOT win every criterion.** If it does, the rubric is not
  honest and the page reads as an ad. Let it win where it really wins and lose
  clearly where it doesn't (for example: automation, hands-off investing,
  personal advice, tax filing). An honest score that we don't sweep persuades
  more than a perfect one.
- Scores are **editorial judgment, stated as such**. Invented precision ("4.7★
  from 2,300 users") is banned. Never invent user counts or ratings.
- **Price:** if the product is "free to start" with a paid plan, never call it
  "free". Don't give it a top cost score just because there is a free tier.

**Default criteria for a money tool** (adapt per piece):
Whole-picture visibility (cash, tax, concentration across accounts) ·
Decision support · Automation (does it act for you) · Cost and value ·
Transparency and trust.

For a **single-product review**, score each criterion with one sentence of
justification, then give one overall verdict.

## Link scheme (exactly 3 links)

1. **Brand link:** anchor `{Product}` → `{homepage}`
2. **Contextual link:** a descriptive anchor → one relevant article on our own
   site (`{site}/article/{slug}`). This is hub-and-spoke: the guest post passes
   authority to the on-site article that best fits the topic.
3. **Call to action** at the end → `{homepage}`, with an action anchor such as
   `Get your free check-up from {Product}`.

Never more than 3 links. Pick one CTA destination and keep it consistent across
all placements so results are comparable.

## Locales: English and Traditional Chinese (Hong Kong)

- **EN** = US reader.
- **繁中** = Hong Kong reader, in standard written Chinese (書面語), localized:
  HKD, HK property and MPF, HK-available tools. **Rewrite natively — do not
  translate the EN piece.** No Cantonese slang unless asked. Keep product and
  feature names in English. Disclaimer in Chinese.
- If you don't have real keyword data for a market, say so. Don't invent
  search volumes or difficulty scores.

## Reference files

- `references/page-types.md` — the four page-type outlines and when to use each.
  Read before writing.
- `references/compliance-checklist.md` — red lines, hedge templates, disclaimer,
  pre-publish checklist. Read during the compliance pass.
