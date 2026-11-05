# An AI content engine that publishes daily and checks its own facts

**What it is:** a system I designed for an AI money assistant (a consumer
personal-finance app). AI agents write in-depth articles in English and Traditional
Chinese. Each article passes a series of checks before a human signs it off. A
scheduler then publishes one article a day, and a health check raises an alarm if
publishing stops.

**My role:** I set the content strategy, designed the gates and writing rules, and
built and ran the pipeline with AI coding tools (Claude Code). The AI agents
drafted and checked. Human editors did the final tone check. The company's
engineers owned the website and its content management system.

**What's in this folder**

| File | What it is |
|---|---|
| [`README.md`](README.md) | This case study |
| [`publishing-pipeline-design.md`](publishing-pipeline-design.md) | How the pipeline works, in plain English |
| [`financial-news-writing-skill/`](financial-news-writing-skill/) | The writing rules I gave the AI, as a reusable Claude skill: 6 writing models, 39 topic "voices", a banned-word list and a scoring script |

---


## See the output

- [A stock analysis article, in English and Chinese, with the review it had to pass](examples/)
- [A personal-finance explainer for Hong Kong readers](examples/4-percent-rule-zh-hk.md)

## 1. The problem: AI makes content cheap, and Google stopped rewarding cheap content

The obvious play for an AI product is to publish a lot: daily market news,
written by AI, in many languages. We tried a version of that first. It taught us
three things.

**News has a short life and low search value.** A news story is read for a day.
Big news outlets already own those searches. A small site's news story rarely
ranks and almost nobody clicks it a week later.

**In-depth articles keep bringing visitors.** A guide that fully answers a
question people keep asking ("How much cash is too much to keep in savings?")
gets found through search for months. In our competitor research, one large
personal-finance site lost most of its weaker, lower-ranked pages over two years,
while its top-3 rankings grew. The lesson: a long tail of thin posts gets wiped
out. Fewer, deeper articles that reach the top 3, or get quoted in Google's AI
answers, are what last.

**Machine translation counts as duplicate content.** We stopped publishing plain
machine translations. They read like Google Translate output, and Google treats
near-copies as low value. Each language had to be written natively instead (see
section 3).

So the goal changed from "publish more" to **"publish one article a day that
deserves to rank, and never publish one that is wrong."**

---

## 2. The process: five gates before anything goes live

Each article passes these gates in order. A failure sends it back. It never
skips ahead.

```
 Draft  ->  Quality score  ->  Link check  ->  Fact-check agent  ->  Human sign-off
                                                                          |
                         Health check  <-  Scheduled publish  <-----------+
                         (alarm if publishing stops)
```

| Gate | What happens | Why it exists |
|---|---|---|
| **0. Draft** | An AI agent writes to a fixed set of rules: answer the question in the first ~200 words, no generic filler, a table where it helps, one link to the matching topic hub page, one soft product mention at the end | Rules beat "write me an article". The writing skill in this folder is an example. |
| **1. Quality score** | An automated reviewer scores the draft out of 100 (content, SEO, credibility, technical setup, how quotable it is for AI search) and estimates how "AI-sounding" it is. Pass bar: **85+, no critical issues, low AI-likelihood.** | Catches thin articles, missing page setup and robotic phrasing before a human spends time on it. |
| **2. Link check** | Every link is opened and must load the real page. Links point to final addresses, so readers don't bounce through redirects. | A broken link in a finance article costs trust. See the "soft 404" lesson below. |
| **3. Fact-check agent** | A separate agent traces **every number, date and price** to a source it actually opened, and checks compliance red lines (more below). | Writers, human or AI, don't check their own work well. |
| **4. Human sign-off** | A native-speaking editor reads each language for tone. **Never skipped.** | The automated gates are filters. A human makes the final call. |

The scoring pass bar was set honestly. The scorer rewards articles with many
statistics. We **exempted** that check, because hitting a statistics quota is how
you end up inventing statistics. Fewer real numbers beat more fake ones.

**Compliance red lines** (it's a financial product, so these work like legal rules, not
style choices):
- Never describe the product as an adviser. It reads your accounts, shows and flags things. It does not advise.
- No buy, sell or hold instructions. No naming a specific fund or stock as what to buy.
- No real company used as an example of a bad investment.
- Every number has a source and a date.

---

## 3. Two languages, written natively, not translated

Each article ships in English and in formal written Traditional Chinese for Hong
Kong readers. The Chinese version is a **native rewrite**:

- The headline, sub-headings and opening are rebuilt around what a Hong Kong reader
  actually types into Google. They are not translated from English.
- Every statistic stays exactly the same. US data is labelled as US data. **We
  never invent a Hong Kong equivalent** for a US number.
- Brand names, tickers and terms readers already use in English stay in English.
- US-only topics (US tax rules, US-only products) skip Chinese entirely. A
  Chinese article about a product a Hong Kong reader can't use helps nobody.
- A Hong Kong native does the final read, because "correct" and "sounds local" are different tests.

---

## 4. The biggest lesson: AI agents make up statistics that read perfectly

This is the part I'd want any team putting AI into published content to hear.

In stress tests of our research-article pipeline, the review step caught
invented figures: plausible percentages, returns and counts that came from no
real source. None of them looked wrong.
They had the right number of decimal places, sat in sensible sentences, and
matched what you'd expect. That is the danger. **A made-up statistic doesn't look
made up.**

What we changed:

1. **Every number needs a source the agent actually opened, with a date.** A
   number "from memory" doesn't count. Neither does a search result snippet it
   didn't click. If it can't be checked, the section is written without the number.
2. **Assume your agent fabricated something** until a second agent has traced it.
3. **One wrong number is worse than no article.** A reader can disprove it with
   one search, and Google's quality systems notice inconsistencies too.
4. **A source-trust ladder** decides what counts as a source:

```
  MOST TRUSTED
    1. Primary sources: government and regulator pages (tax authority,
       labour statistics, securities regulator), company filings,
       a company's own pricing page
    2. Established financial press
    3. Review aggregators and content farms  ->  never used for any figure
  LEAST TRUSTED
```

When a primary source blocks automated access, the agent finds another route
to the same primary data, often an official data API. It does not fall back to a
second-hand site.

The writing skill in this folder builds this in as a **Zero Fabrication Rule**:
- Fixed facts (a chip's published specs, when a law passed) may be cited from
  known sources, with attribution.
- Anything that changes (prices, valuations, analyst quotes) **must** be verified
  in the current session.
- No verification means no number.

---

## 5. Keeping it running: the pipeline has to tell you when it breaks

A daily schedule is only useful if you know when it stops. Three real failures
shaped the design (details in [`publishing-pipeline-design.md`](publishing-pipeline-design.md)):

- **"Alive" isn't the same as "working".** The first health check only confirmed
  the script ran, so a stuck article could stop publishing while the health log
  still said "alive". The fix: the health check now asks "has anything
  actually been published in the last two days?" If not, it raises a desktop alert
  and leaves a warning file where a person will see it.
- **The site said "OK" for pages that didn't exist.** The website returned a
  success code even for missing articles (a "soft 404": it quietly showed the
  general listing page). Checking the status code proved nothing. Now we check that
  the page shows **the article's own title**.
- **One bad article could block the whole queue.** Now an article that fails
  three times in a row is marked "failed" and skipped. The queue moves on and a
  human gets an alert.

---

## 6. Lessons

1. **Design the gates before you scale the writing.** Generating text is the cheap part.
   Checking it is where the cost and the risk sit.
2. **Make AI output easy to verify, not just good-sounding.** Inline sources and a
   trust ladder turn "looks right" into "checked".
3. **Never let a quality score push the writer to invent things.** We turned off
   the "more statistics" reward on purpose.
4. **Fight the template fingerprint.** When we audited earlier AI news articles, almost
   all of them used the same skeleton. Readers and search engines can spot that. The
   writing skill now forces structural variety. Lay out five articles from one channel, and
   you shouldn't be able to predict the sixth.
5. **Rewrite for each market; don't translate.** Machine translation added pages
   but no value.
6. **Monitor the outcome, not the process.** Check that an article went live, not
   that a script ran.
7. **Keep a human at the last gate.** The agents are filters, not the editor.
8. **Steady beats bursty.** One article a day, every day. After an outage we don't
   catch up by publishing a backlog. Missed days are written off, so the site never
   looks like a content farm.

---

*Notes: brand names, colleague names, internal systems and internal metrics are
removed. This folder publishes the design and the writing skill, not the running
deployment code.*
