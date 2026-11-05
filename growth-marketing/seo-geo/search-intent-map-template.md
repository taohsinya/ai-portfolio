# Search Intent Map — Template

**What this is:** a one-page map of what real people type into Google about
your topic, what kind of page currently wins, and whether you have a hook (an
ad line, a page, a tool) that answers it. It tells you where to write, where to
build a free tool, and where not to bother.

**Rule zero:** start from the search, not from your product. Ask "what is the
person trying to decide?" before "what do we want to say?"

---

## 0. Be honest about your data

Write this box first, every time.

| Item | Status |
|---|---|
| Search volume source | e.g. SEO tool export / none yet |
| Who currently ranks | checked by hand / from tool |
| Forums (Reddit etc.) checked? | yes / no |
| Unverified facts | list them |

If you don't have volumes, say so. **"No published figure" is not "small".**
Give the structure now and list the exact keywords to pull later (section 6).

---

## 1. The key split: "manual" vs "verdict" searches

| | Manual-type search | Verdict-type search |
|---|---|---|
| What the person wants | A general rule, a table | **A judgment on *my* situation** |
| Example | "average savings by age" | "am I behind for my age?" |
| Who wins today | Big publishers, banks, affiliate sites | Often nobody |
| Why nobody | — | You need the person's own data to answer |
| Can a newcomer win? | Rarely | **Yes, if your product can see their numbers** |

Most manual-type searches are verdict searches in disguise. Nobody searches
"average net worth by age" out of curiosity — they want to know if *they* are
behind. The big sites answer the literal question; the real question is open.

---

## 2. Cluster table (one per topic)

Repeat for each topic cluster (e.g. *Am I on track*, *Equity compensation*,
*Investing*, *Savings*, *Cash flow*).

**Cluster: {name}**

| Search phrase | Stage | Manual / Verdict | Who ranks today | SERP softness | Our existing hook | Verdict |
|---|---|---|---|---|---|---|
| how much should I have saved by 35 | Worry | Verdict in disguise | Big publishers, long articles | 🟡 | "{hook id}" | Write: answer with a percentile |
| net worth percentile calculator | Check | Verdict | Small personal sites, no big brand | 🟢 | none | **Gap → free tool** |
| do my funds overlap | Check | Verdict | Tiny tools that compare 2 tickers only | 🟢 | "{hook id}" | Own it |
| best high-yield savings account | Shop | Manual | Daily-updated affiliate publishers | 🔴 | — | **Don't fight** |
| how long could I survive without income | Worry | Verdict | Blog posts, no major brand | 🟢 | "{hook id}" | Own it: tool + page |
| cancel unused subscriptions | Act | Manual | A funded app that does it for you | 🔴 | 3 hooks | Keep hooks for social, not SEO |

**Columns explained**

- **Stage:** where the person is — *Worry* (something feels off) → *Check*
  (measure it) → *Shop* (compare options) → *Act* (do something).
- **SERP softness** (SERP = the Google results page):
  🟢 open (small sites, old pages, forum threads asking for help),
  🟡 contested, 🔴 locked (big brands that update daily, or funded
  competitors whose core business is this word).
- **Signs a results page is soft:** a top result that is years old; a
  discontinued product still ranking; forum threads titled "X no longer
  available — alternatives?"; one small site publishing four near-identical
  posts on the same phrase; results from the wrong country.

---

## 3. What the ideal answer looks like

For each verdict search worth owning, write the answer you'd want the reader
to get — with placeholders, not made-up numbers.

> **Search:** "how much company stock is too much"
> **Ideal answer:** "{Company} is **{x}%** of your investable money. {y}% is
> stock you were granted; another **{z}%** you didn't count — it's inside your
> index funds and retirement account."
> **Compliance check:** shows a fact about their holdings; no buy/sell call. ✅

If writing the ideal answer needs a personal tax or investment number, mark it
for compliance review before it becomes a hook (see
`compliant-ad-copy-guide.md`).

---

## 4. Three kinds of mismatch (the output)

**A. Search exists, no hook → write one.**

| Intent | Evidence | Existing hooks | Priority |
|---|---|---|---|
| {intent} | {why it's open} | 0 | 1 |

**B. Hook exists, no search → change its job, don't delete it.**

| Hook | Why no search | Use instead |
|---|---|---|
| {funny spending joke} | Definitional topic, no buyer | Social / short video |

**C. Hook and search both exist, but the product can't deliver (or the word is locked).**

| Hook | Search | Blocker |
|---|---|---|
| {hook} | {phrase} | Funded competitors own it — skip |

---

## 5. Intent → free tool ranking

Free tools (calculators, checkers) are often the highest-leverage SEO asset
for a data product. Rank them by evidence, not by what's easiest to build.

| Rank | Tool | Why (target user, verdict share, competition, time-sensitivity) |
|---|---|---|
| 1 | {tool} | {reason} |
| 2 | {tool} | {reason} |

---

## 6. Keywords to pull (paste into your SEO tool)

Columns to export: **Volume · Difficulty · Cost per click · Parent topic ·
SERP features · Current #1**.

```
# Cluster A
{phrase}
{phrase}

# Cluster B (highest priority)
{phrase}
```

---

## 7. What I could not verify

A short, honest list: missing volumes, sources you couldn't open, dates you
only have second-hand, assumptions you haven't tested. This list is part of the
deliverable.
