# Getting Found in Search and AI Answers — Inside Financial-Ad Rules

**Context:** growth for an AI money assistant (a consumer app that reads a
person's accounts and gives them a check-up on their finances). The product is
**not** a licensed adviser, so every page and ad had to stay on the right side
of financial-advertising rules.

Two terms used throughout:

- **SEO** (search engine optimisation) = getting found in Google.
- **GEO** (generative engine optimisation) = getting quoted or cited when
  someone asks an AI assistant (ChatGPT, Gemini, Google's AI Overviews) a
  question.

This folder shows the method, not results. **No traffic or ranking numbers are
claimed here.**

---


## My playbook

**1. Start from intent, not volume.** I look for searches where the person is close to a decision (comparing options, checking whether they're on track), not just the biggest keywords. A smaller search with clear intent beats a big one with none.

**2. Study what already works for competitors.** I look at which root keywords (the core words a whole group of searches is built around) bring competitors most of their traffic and which of their pages spread, then decide where we can win.

**3. Pick the fight that matches your size.**
- **Small or new site:** go after long-tail searches, the longer, more specific phrases that big sites don't bother with. They're easier to rank for and often have clearer intent.
- **Established site:** compete directly on the root keywords.

**4. For a product starting from zero, build presence outside your own site first:**
- **Guest posts** on relevant sites
- **Links from other sites.** "Do-follow" links pass ranking strength to your site. "No-follow" links don't pass it directly, but they still bring visitors and show search engines and AI tools that people talk about you.
- **Places AI assistants and searchers already trust:** recommendations on social media, YouTube, X (Twitter), Google Images and Reddit. AI answers often cite these sites, so being discussed there is a large part of GEO.

**5. Measure everything.**

| Tool | What I use it for |
|---|---|
| Ahrefs | Keywords, competitors' traffic and the links pointing to each site |
| Google Search Console | Which searches show our pages, and how often people click |
| Google Analytics | What visitors from search actually do on the site |
| AITDK | Tracking visibility in AI-driven search |

## What's in this folder

| File | What it is |
|---|---|
| `README.md` | This case write-up |
| `search-intent-map-template.md` | How to map what people search at each stage, and where you can actually win |
| `comparison-page-skill/` | A Claude Code skill that writes honest comparison and review pages (guest posts) |
| `compliant-ad-copy-guide.md` | Red lines and safe wording for money-product ads, with sample scripts |

---

## 1. Start from the search, not the product

Before writing anything, we mapped what people actually type into Google
across five topics (am I on track, equity pay, investing, savings, cash flow).
For each phrase we asked three questions:

1. **What stage is the person at?** Worried → checking → shopping → acting.
2. **Who wins the results page today?** Big publishers that update daily, or
   small sites, old pages and forum threads?
3. **Do we already have a hook that answers it?**

The most useful finding was a split between two kinds of search:

- **Manual-type:** "average savings by age". The person wants a table. Big
  publishers own these. A newcomer can't win.
- **Verdict-type:** "am I behind for my age?" The person wants a judgment on
  *their* situation. Almost nobody owns these, because you need the person's
  own numbers to answer — which is exactly what a product that reads your
  accounts has.

Most manual searches are verdict searches in disguise. That reframed the
roadmap: **the best SEO asset was not more articles, it was free tools that
return a personal verdict.**

The map also produced three kinds of mismatch, which is where the decisions
came from:

- **Search exists, no hook** → write one (the biggest gap was a whole topic
  where our ad library had zero lines).
- **Hook exists, no search** → keep it for social video, don't build a page.
  Several of our funniest ad lines had no search demand behind them.
- **Search exists but the word is locked** by funded competitors → skip it.

→ Template: [`search-intent-map-template.md`](search-intent-map-template.md)

---

## 2. Comparison pages with an honest scorecard

Guest posts (articles placed on other sites) have a different job from blog
posts. They earn a link back, reach readers who are already shopping, and get
you onto the shortlist. Generic "how to budget" guides don't do that. **Review
and comparison pages do** — "best X apps", "X vs Y", "X alternatives".

The rules that made them work:

- **Answer first.** The first sentence gives the verdict, so an AI can quote it.
- **Transparent scorecard.** 4–6 criteria, every tool scored on each, overall
  = the average. The reader can rebuild the number.
- **Our product must not win every criterion.** If it does, the rubric isn't
  honest and the page reads as an ad. We win where we really win and lose
  clearly where we don't (we don't invest for you, don't file taxes). This is
  the rule I'm proudest of: an honest loss on the scorecard sells better than
  a clean sweep.
- **Exactly 3 links:** brand, one relevant on-site article, one call to action.
- **No FAQ block.** Reader questions go into the H2 headings instead. A
  copy-pasted FAQ at the bottom of every page looks like a template.
- **Native localization.** The Hong Kong Chinese version is rewritten for
  Hong Kong readers, not translated.

→ Skill: [`comparison-page-skill/`](comparison-page-skill/)

---

## 3. Writing so AI assistants cite you (GEO)

More and more money questions start in a chat box, not a search box. What we
learned about getting quoted there:

- **Put the answer in the first two sentences**, in plain words, with the
  number and its date. AI summaries lift the opening.
- **Make the title and the H1 different on purpose.** The title targets the
  comparison search ("X vs Y vs Z"); the H1 is the natural question people ask
  an assistant ("Which AI gets money questions right?").
- **Show your reasoning in a table.** A visible scorecard or comparison table
  is easy to extract and hard to fake.
- **Date-stamp every figure** and cite a checkable source. Stale numbers get
  you dropped — and in finance they're also a compliance problem.
- **Be the source, not the summary.** Publishing your own method and data
  gives assistants something original to cite (see next section).
- **Before writing, name the one Google question this page answers** and check
  that it returns real results. If you can't, the page isn't ready.

---

## 4. Content idea: "We tested AI money answers"

The team ran a benchmark that asked several AI
assistants (ours, ChatGPT and Gemini) the same real-world money questions and
scored the answers. As content, it worked because it was the kind of thing
journalists, comparison sites and AI assistants like to cite: original,
dated, and with a published method.

**The method (the part that's safe to share):**

- **Three scored dimensions, weighted before scoring:** accuracy 45%,
  usefulness 35%, expression (readability) 20%, each on a 1–5 scale.
- **Usefulness is defined as decision help:** does the answer name the figures
  that matter, show how they combine, and say what they mean for the choice?
- **Accuracy veto:** an answer with a fact that verification proves false
  cannot win, however useful it reads.
- **Blind scoring.** Human panels saw answers stripped of branding, in random
  order. An automated judge saw anonymous labels in random positions.
- **Outside judge.** The model doing the judging came from a different model
  family than every system under test, including ours.
- **Live fact-check** of key figures (prices, dates, holdings) against sources
  from the same day the answers were generated.
- **Close calls flagged** (top two within a small margin get lower confidence).
- **A limitations section** is published with the results, so readers can see
  what the test does and doesn't prove.

**What's not here:** the questions came from real user queries, so the
question set and the results data are not published. Only the method and
rubric are.

**What I'd copy:** if you run any AI product in a regulated field, a
transparent benchmark that you're willing to lose is one of the strongest
trust and citation assets you can build.

---

## 5. Marketing compliance in a regulated industry

Telling a specific person what to do with their money can count as
personalised investment advice, which brings licensing duties. The product was
built to stay a *mirror*, not an adviser. In copy, that came down to verbs:

- ✅ **benchmark, map, scan, show** — the product measures your situation
  against a neutral reference.
- ❌ **recommend, should, move your money to** — the product tells you what to do.

Other red lines: no buy/sell/hold calls, no return predictions, no FOMO, no
invented stats or testimonials, no features that haven't shipped, and every
tax line hedged with "your accountant fills in the number."

The ad sat at the level of *diagnosis* ("here is your number"); deeper next
steps stayed inside the app, behind their own review. Borderline lines (for
example, strong language about big banks) went to legal as explicit questions
instead of being quietly shipped.

→ Guide: [`compliant-ad-copy-guide.md`](compliant-ad-copy-guide.md)

---

## Lessons

1. **Intent before content.** The biggest wins came from deciding what *not*
   to write. A large share of our ad library had no search demand behind it.
2. **Your data is your SEO moat.** Big publishers can answer the general
   question. Only a product that sees the user's numbers can answer "what about
   me?" Build free tools around that.
3. **Honesty is a ranking and conversion strategy.** Scorecards we don't sweep,
   published losses, real cons — these are what editors accept and what AI
   assistants trust.
4. **Compliance is a copy skill, not a blocker.** Pick the right verbs early
   and most copy passes legal on the first round.
5. **Say what you couldn't verify.** Every research doc ended with a "what I
   could not check" list. It caught at least one problem before launch: an ad
   line was using a market rate that had gone stale.
6. **Live site beats internal docs.** Specs and capability sheets go stale.
   Before claiming a feature or a price, check the live page.

---

## Credit

- **Comparison-page skill:** written by me; later handed over to a teammate to
  run. Debranded here.
- **Search intent map:** I set the direction ("start every brief from Google
  intent") and the questions; the research pass was done with an AI research
  agent and reviewed by me. Only the structure is published.
- **The AI-answers benchmark:** a company research project run by the team. My part shown
  here is the content and search packaging (title / H1 / description). Method
  only — no questions or data.
- **Compliance guide:** adapted from a brief our growth team sent to legal.
  Rewritten as a generic guide; recipient and brand removed.
