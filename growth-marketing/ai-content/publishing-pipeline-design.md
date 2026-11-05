# Publishing pipeline: design

How the daily publishing pipeline works, in plain English. This is the design,
not deployment code. The real scripts are tied to one company's website and
content management system (the CMS, the back-office tool where articles are
stored and published), so they aren't included here.

---

## The big picture

```
  WRITING (AI agents + human)                 PUBLISHING (automatic)
  ---------------------------                 ----------------------

  Topic chosen & checked          +-------------------------------+
  against existing articles       |  QUEUE (a simple list file)   |
            |                     |  article 1   published        |
            v                     |  article 2   published        |
  Draft EN + native Chinese       |  article 3   ready   <-- next |
            |                     |  article 4   ready            |
            v                     |  article 5   paused           |
  Gates 1-3 (score, links,        +---------------+---------------+
  fact-check agent)                               |
            |                                     |  every hour
            v                                     v
  Gate 4: human sign-off  ------>      PUBLISHER (runs on a scheduler)
  (article added to queue)             - is it 3pm or later, and nothing
                                         published today?  if not, stop
                                       - run its own checks again
                                       - upload image, publish English
                                       - add Chinese to the same article
                                       - mark "published", log it
                                                  |
                                                  |  5 minutes later
                                                  v
                                       HEALTH CHECK (every hour)
                                       - published in the last 2 days?
                                       - any "failed" articles?
                                       - is the queue empty?
                                       - running out of banner images?
                                                  |
                                    all fine -----+----- problem
                                       |                    |
                                  log "ALIVE"        log "STALLED" +
                                                     desktop alert +
                                                     warning file a
                                                     person will see
```

---

## The parts

### 1. The queue

A single list of articles in publishing order. Each entry has a title, the web
address it will live at, the article files (English and Chinese), a banner image
and a **status**:

| Status | Meaning |
|---|---|
| `ready` | Passed every gate. Waiting its turn. |
| `published` | Live. The web address and time are recorded. |
| `paused` | Held on purpose by a person. |
| `blocked` | Known problem, waiting for a decision. |
| `failed` | Failed three times in a row. Set automatically and skipped. |

**Design choice:** the publisher always takes the **first `ready` entry in the
list**. It does not sort by date. The target date on each entry is only a label
for people. This keeps the rule simple: to change the order, move the entry. (We
learned this the hard way. A paused article was revived and jumped ahead of one
that was meant to go first, because it sat higher in the list.)

### 2. The publisher

Runs on a scheduler (a tool that runs a script automatically at set times).

- **It runs every hour, not once at 3pm.** The machine running it could be asleep
  at 3pm. Each hourly run asks: "Is it 3pm or later, and has nothing gone out
  today?" If yes, it publishes. If the machine wakes at 6pm, the article goes out
  at 6pm. Nothing is lost.
- **One article a day, maximum.** If something already went out today, it exits.
- **It repeats its own checks** before uploading: no leftover page title or hidden
  comment in the article body, no links to the wrong site, correct call-to-action
  link. A **dry-run mode** runs every check without publishing. That dry run is the
  real final gate before an article joins the queue.
- **English first, then Chinese on the same article**, so the two languages stay
  linked in the CMS.
- **Three strikes.** Each failure is counted. After three in a row the article is
  marked `failed` and skipped, so one broken article can't stop the whole queue.

### 3. The health check

A second small script that runs five minutes after each publisher run. It writes
one line to a log, for example:

```
[date time] ALIVE | published N/M | K ready | next: <article> tomorrow 15:00
[date time] STALLED | NOTHING PUBLISHED FOR 3 DAYS - PIPELINE STUCK
```

It reports **STALLED** when:
- nothing has been published for two or more days,
- any article is marked `failed`, or
- the queue is empty.

When stalled, it shows a desktop notification and drops a warning file on the
desktop, where a person will notice it. When things recover, it deletes the file.
It also warns when the banner images are running low, so the team knows to make more.

**Why it checks outcomes:** the first version only logged "ALIVE" to show the
script had run, so a stuck article could block publishing while the log still
said "ALIVE" every hour. Now it checks the thing that matters: did an article
actually go out?

---

## Verifying an article is really live

**Trap: the website answered "OK" for pages that didn't exist.** Instead of a
proper "not found" error, it served the general article listing (a "soft 404").
So a status-code check passed for every address, even made-up ones.

**The check that works:** fetch the page and read its title. If it shows the
article's own title, it's live. If it shows the generic listing title, it isn't.
Check every language version.

**Second trap: drafts reserve web addresses too.** In the CMS, an unpublished
draft holds its web address as firmly as a published article. A search for
"published" articles can't see it. A forgotten draft blocked a new article's
address and stalled the queue. Now any check for "is this address free?"
includes drafts.

---

## Rules for when things go wrong

| Situation | What to do |
|---|---|
| Web address already taken | Find the entry that owns it (draft or published). Update that entry, or choose a new address. Never create a duplicate. |
| Days missing from the log | The machine was asleep. The hourly catch-up publishes at the next waking hour. |
| Health check says STALLED | Read the alert. Fix the failed or blocked article, or refill the queue. |
| A run crashed halfway | **Do not re-run.** Ask the CMS what already exists, then add only what's missing. Re-running creates duplicates. |
| Several days missed | **Don't catch up.** One article a day, always. Missed days are written off and the schedule shifts forward. A burst of articles looks like a content farm. |

---

## Security rules

- Logins and access keys live in a local settings file that is never copied,
  shared or printed into chat logs. A template with blank values sits beside it.
- The AI agents never see the keys. The publisher script reads them when it runs.

---

## What I'd change before reusing this

- **Move it off a laptop.** The hourly catch-up works around a sleeping machine.
  A small cloud scheduler would remove the problem.
- **Send alerts to where the team works** (chat or email), not only the desktop.
- **Track the banner-image count automatically** instead of updating it by hand.
- **Add the drafts-included address check** to the publisher itself, so it
  catches a blocked address before the first attempt.
