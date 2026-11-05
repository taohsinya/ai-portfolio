# Falsifiable Portfolio Research: theses, signals with deadlines, and an adversarial audit

A personal method for running investment research so that it can be **proven wrong on a date**. Research gets turned into about ten written theses. Each thesis is tested by "signals": specific bets with a deadline and a pre-written answer to "what would prove me wrong". An AI audit layer is told to attack the theses, not agree with them. When a deadline arrives, the bet is scored honestly, including the misses.

I ran this for several months on a fast-moving sector, with Claude doing the daily upkeep and Obsidian (a note-taking app) as the visual layer. This page explains the method. The names, holdings and real research have been removed, and every example is made up.

> **Not investment advice.** This is a research method. Nothing here is a recommendation to buy or sell anything. All companies, numbers and dates in the examples are fictional.

**Files in this folder**

| File | What it is |
|:---|:---|
| [`README.md`](README.md) | The method as a story, and how it is organised in Obsidian |
| [`thesis-template.md`](thesis-template.md) | Fill-in template for a thesis, with a made-up example |
| [`signal-template.md`](signal-template.md) | Fill-in template for a signal (a dated, falsifiable bet), with a made-up example |
| [`market-thesis-skill.md`](market-thesis-skill.md) | The thinking rules I give Claude before any market analysis: the dialectical method, the evidence ranking, and a list of my own known mistakes |
| [`obsidian-structure.md`](obsidian-structure.md) | Text diagram of the vault: folders, note types, and how they link |

---

## The problem

Most investment research cannot be wrong. It says things like "demand remains strong" or "we see upside". Those sentences survive any outcome, so you never learn anything from them.

I had a second problem. I read a lot of research from big investment banks (the "sell side": banks that publish research to win trading business). Their research is useful for knowing what everyone else thinks. But it leans bullish by design, and when four banks agree, that is one crowded story, not four pieces of proof.

And a third problem, which appeared once I started working with an AI assistant: **AI models like to agree with you.** If you hold a strong view, the model will find ways to read every new data point as support. That feels good and is worthless.

So I wanted a system where:

1. Every belief is written down in a form that can fail.
2. Every test has a date.
3. Something in the loop is paid to disagree with me.
4. The score is kept honestly, including the times I was wrong.

---

## The method, step by step

### Step 1. Turn research into about ten falsifiable theses

A **thesis** is a belief about how part of the market works, written so that it could be shown false. "Chip stocks will do well" is not a thesis. "The shortage is moving down the supply chain, from chip packaging to circuit boards to testing, and each stage gains pricing power in turn" is a thesis, because you can check whether the next stage actually gains pricing power.

I keep it to about ten. More than that and they stop being watched.

Each thesis has:
- **A one-sentence core claim.**
- **A causal chain**: the steps that must be true for the claim to hold ("A causes B, which causes C"). Each step is an assumption, and each assumption is something that could break.
- **A kill condition**: what would make me drop the thesis. A story with no way to fail is not allowed to become a high-confidence thesis.
- **Two separate ratings.** *Confidence* (how strong is the evidence?) and *status* (pending, verified, contested, or falsified) are tracked separately. You can have strong evidence for a thesis that has not been tested yet.

See [`thesis-template.md`](thesis-template.md).

### Step 2. Attach signals that have a deadline and a pre-written "what would prove me wrong"

A **signal** is one specific, dated bet that tests one part of a thesis. Every signal must have:
- **A claim**, in one sentence.
- **A trigger condition** with three outcomes, written *before* the evidence arrives:
  - **verified**: the bet came true (and here is the exact threshold),
  - **falsified**: the bet failed (and here is the exact threshold),
  - **contested**: the evidence did not settle it (and here is what that would look like).
- **A deadline tied to a real event** that will produce the answer: an earnings report, a monthly trade data release, a price-setting season. "By year-end" is weak. "By the Q3 earnings call on 31 October" is strong.
- **A data source.** If I know what to watch but have no way to read it, the signal says so plainly ("known gap: no source"). A signal with a deadline but nothing to read is just taking up space and pretending to be tracked.

The deadline matters more than anything else. **A bet with no deadline never closes, so it never feeds back into how confident you should be.**

See [`signal-template.md`](signal-template.md).

### Step 3. Run an adversarial audit, with a "don't flatter me" rule

On top of the theses sits an **audit layer**. Its job is to find the weak points. I run it with Claude, and the first rule, in my own words, was *"don't tailor your conclusions to please me."*

The audit asks six questions of every thesis:

1. **Rebuild the causal model.** Is every step in the chain written down? Does each arrow have an assumption behind it?
2. **Audit the assumptions.** Which assumptions have no signal watching them? Which signals have expired?
3. **Test the evidence.** Is the supporting evidence independent, or is it the same source repeated? Is the opposing evidence getting a fair hearing?
4. **Find contradictions.** Is evidence against the thesis being quietly down-weighted? Is any data point being read the wrong way round?
5. **Trace the damage.** If one assumption fails, what else breaks? Who else wins or loses?
6. **Design the missing tests.** Which signals should exist but do not? Are the current deadlines sensible?

**Hard rule: the audit only proposes.** It can suggest new assumptions, new signals or new weightings, but it never changes a thesis's status or edits evidence directly. Changes go through the normal scoring process in Step 4. This stops a persuasive argument from rewriting the record without a test.

The audit also follows a short discipline, because without it the audit turns into "repeat the thesis back in different words":

- **Never say "this confirms your view".** Agreeing with a strong prior removes the only value a second opinion has. If you agree, explain why independently.
- **Bank consensus is not evidence.** Several banks with the same built-in bias agreeing is a crowded story. Discount it; do not count it twice.
- **If X and not-X both "support" the thesis, stop.** One example: money flowing *into* a sector was read as "strong demand, thesis holds", and money flowing *out* was read as "healthy clean-out, thesis holds". A conclusion that survives every possible observation is not being tested. Assign each data point to the scenario it can actually tell apart, or mark it "does not discriminate".
- **Don't flip to please, either.** When challenged ("are you just agreeing with me?"), fix the reasoning. Do not jump to the opposite conclusion to look independent.
- **No made-up probabilities.** A number is only allowed if you can say where it came from and how sure you are. If a real market price exists for the question (for example, futures pricing for an interest-rate decision), use the market's number instead of your gut. If something has already happened, state it as fact, not as a probability. If nothing prices it, give a direction, a wide range and "low confidence", never a precise-looking decimal.
- **Ask for the latest numbers.** Web searches lag on fast-moving data. They pick up dramatic headlines and miss quiet reversals. For the last day or two, ask the human for the live figure.

After each audit, the AI runs a seven-item self-check: Did I say "this confirms your view"? Did I treat bank agreement as proof? Did I read any data point as support whichever way it came out? Can the flow data I cited actually tell the scenarios apart? Can I source every probability? Did I flip sides just because I was challenged? Did I look up the last two days' numbers, or ask for them?

### Step 4. Score yourself honestly after the deadline

When a signal's deadline arrives, it is scored as **verified**, **falsified** or **contested**, and the result flows back into the thesis:

```
verified    -> thesis confidence goes up
falsified   -> thesis confidence goes down;
               if it hit a core assumption, the thesis status becomes "falsified"
contested   -> can't be decided; extend the deadline AND write down why it couldn't be decided
```

Rules that make the scoring honest:

- **Score expiring signals first**, before reading any new research. Otherwise new stories crowd out old bets.
- **Read the claim before the threshold.** Some signals are deliberately counter-intuitive. If the claim is "banks will refuse to admit X", then banks admitting X means the signal is *falsified*, even though it sounds like good news. Do not score by gut feel.
- **Never move the goalposts during the game.** A threshold can be changed before the window opens or after it closes, never inside it. If a threshold looks badly designed mid-window, say so, score the original anyway, and open a new signal with a better one.
- **"Beat" needs a reference line.** A company can beat the published analyst average and still miss what investors were privately expecting. The stock trades on the second number. Any "beat" or "miss" that doesn't say which line it means gets less weight.
- **Stock price moves are not readings.** The threshold is about the business fact (a contract price, a capacity number), not whether the stock went up.
- **A right answer is not proof of right reasoning.** Each closed signal is written up as a **finding** (what happened, what I learned). The findings are the calibration record.

The scoring also produces an **error book**: a list of times my own judgment was beaten. Each entry records what I got wrong and the rule I changed because of it. For example, wherever a market price exists for an outcome, I now use it instead of my own estimate.

### Step 5. Three ideas that run through everything

**Anti-confirmation is as valuable as confirmation.** The most informative data point is the one that argues against your current read. If a market sells off hard but the currency holds firm, that tells you it was probably not capital flight. I actively hunt for these.

**Early ≠ wrong.** Being right about the business but early on timing is a *timing cost*, not a failed thesis. A record quarter followed by a falling stock can mean "peak earnings, low valuation multiple" (the multiple being the price investors pay per dollar of earnings), not "the business broke". Always say which layer moved: the business, the multiple, or the timing. I rate these separately: direction, timing, and portfolio policy each get their own grade.

**Who is on the other side of the trade?** Every trade has a buyer and a seller. *How* a price moved often matters more than *how far*. A crash that forces borrowed-money buyers to sell clears out risk. A sharp rebound that rescues them leaves the risk in place. The two can look identical on a chart.

---

## How it is organised in Obsidian

Obsidian is a free note-taking app that stores notes as plain text files and draws links between them. I use it as the **visual layer**: Claude writes and updates the notes, and I read them, follow the links and look at the graph.

**Five kinds of note, never mixed:**

| Note type | What it holds | Example name (made up) |
|:---|:---|:---|
| **Evidence** | One fact that happened, with its source and quality ratings. Written once and linked from every thesis it touches. | `E07 Cloud Provider Raises Spending Plan` |
| **Signal** | One dated, falsifiable bet with three-outcome thresholds. | `S14 Board Supplier Price Increase Sticks` |
| **Thesis** | A belief built from assumptions and evidence, with a kill condition. | `T3 Shortage Moves Downstream` |
| **Factor** | A driver that can be compared across companies (for example, "memory chip tightness"). Has a state but is not true or false. | Row on the `Factor Board` |
| **World State** | A dated snapshot of the overall market backdrop. | `World State 2026-Q3` |

Plus three supporting types: **Audit** notes (output of the adversarial layer), **Finding** notes (lessons from closed signals), and a **Change Log** (what changed each day and why).

**Red lines the structure enforces:** opinion is not evidence; an assumption is not a claim; a factor is not a thesis; a simulation is not a fact; a decision is not a thesis; position size is not conviction; and a right outcome is not right reasoning.

**Why evidence lives in its own notes:** one fact (say, a large cloud provider raising its spending plan) can affect four theses at once. Writing it once and linking it four times means the fact is never copied out of sync, and you can see how much rests on it.

**Why factors get their own board:** pulling drivers out of the theses shows **hidden concentration**: "four of my ten theses are really one bet on the same variable." Each factor row ends with a `next_signal` field, which points to the signal that will next tell you something about it.

**Naming and links:** theses are `T<n> <Slug>`, signals are `S<nn> <Slug>`, and the slug never changes once created. Everything links with `[[double brackets]]`. A link to a note that doesn't exist yet is deliberate: it marks work still to do.

**What never goes into the vault:** personal positions, entry or exit prices, and buy or sell decisions. Those stay out of the files entirely. The vault holds research, not a trading book.

**The daily routine**, run by a scheduled Claude job, always in this order:

1. Score any signals that expire today.
2. Turn each new disagreement in the day's research into a new signal, with a deadline tied to the next event that can settle it.
3. Update the factor board.
4. Change a thesis's confidence only if the evidence actually moved.
5. Write the change log. If nothing material changed, write one line saying so. Don't invent activity.

See [`obsidian-structure.md`](obsidian-structure.md) for the folder diagram and an example of how one fact ripples through the links.

---

## What I learned running it

- **The deadline is the whole trick.** Most of the value came from being forced to write "by this date, this number, or I'm wrong".
- **"Contested" is a real answer.** Several signals could not be decided on their date. Writing down *why* (the data wasn't published, the threshold was ambiguous) improved the next signal.
- **The audit caught me most when I agreed with myself.** The worst mistake I recorded was softening my own threshold right after a scary data point, in the cautious direction. It felt like prudence. The original threshold, scored as written, turned out to be right. That is now a hard rule (see `market-thesis-skill.md`).
- **The AI is a good adversary only if you tell it to be one, in writing, and check it with a list.**
