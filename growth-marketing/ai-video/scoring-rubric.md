# Ad Scoring Rubric

A rubric for an AI scoring agent that judges short video ad scripts **before** anyone spends money making them. Written for a consumer finance product, but it works for most apps. Replace `{Product}` with your product.

---

## How to set up the scorer

Tell the agent it is a **strict performance creative director**, not a helpful assistant. Specifically:

1. **Forced ranking.** Score the whole batch together and rank it. Use the full 1–10 range on each dimension. The middle of the batch should land around 5–6, not 8.
2. **Low scores are normal.** Don't soften them.
3. **Quote the script.** Every score must point to the exact line that earned it.
4. **One fix per script.** Name the single change that would raise the score the most. It's usually the first 3 seconds.
5. **Then look at the batch.** After scoring each script, report patterns: which dimension is weakest across the batch, which scripts repeat each other, and what the failures have in common.

---

## Version A: General rubric (any format)

| Dimension | Weight | Question |
|---|---:|---|
| **Hook (0–3 seconds)** | 40 | Does the first line or frame stop the scroll? Does it work **on mute**, with captions only? Is it a real moment, a contradiction, a confession, a challenge, or a surprising number? |
| **Conversion pull** | 25 | Does the viewer want something before the call to action? Is there one clear, low-effort next step? |
| **Brand fit** | 20 | Does it sound like the brand? Does it stay inside the red lines below? |
| **Differentiation** | 10 | Does it pass the swap test? Does it feel like native content rather than "an ad"? |
| **Format fit** | 5 | Is the format used well? (Example: several people talking, not one AI face staring at the camera.) |
| **Total** | **100** | |

The hook gets 40% on purpose. If people scroll past second 3, nothing else in the ad gets seen.

## Version B: Podcast-clip rubric (when you need finer detail)

Each dimension scored 1–10, then weighted to a total out of 100.

| Dimension | Weight | Question |
|---|---:|---|
| **Hook** | 20 | Does the first sentence stop a muted scroll? Is there a number or a clear "this is you" in it? |
| **Watch-through** | 15 | Is the reveal a real surprise, or can you guess it? Does the tension build? |
| **Download reflex** | 20 | Does the viewer think "wait, what's *my* number?" |
| **Worth paying for** | 15 | Is the insight deep and ongoing, or a one-time trick a free tool gives you? |
| **Differentiation (swap test)** | 15 | Does the reveal need *this* product? |
| **Shareability** | 10 | Would someone screenshot it or tag a friend? |
| **Format authenticity** | 5 | Does the listener react naturally ("wait, *you*?") or turn into a comedy partner? Does it end on a realization or a punchline? |

## Version C: Stand-up rubric

Six sub-scores, each 1–10:

| Dimension | Question |
|---|---|
| **Hook on mute** | Does the opening work with captions only? |
| **Funny without the product** | Delete the product line. Is it still funny? If not, the joke is an ad pretending to be a joke. |
| **Differentiation** | Swap test (below). |
| **Feature clarity** | Can a viewer say what {Product} does after one watch? |
| **AI-performable** | Can current AI video tools act this out without looking fake? |
| **Compliance** | Inside the red lines? |

---

## Verdicts

| Score | Verdict | Action |
|---|---|---|
| **80–100** | Ship | Storyboard and produce |
| **60–79** | Revise | Fix the weakest dimension (usually the hook), then score again |
| **Below 60** | Kill | Cut. If it's funny but generic, move it to unpaid social instead of paid ads |
| **Any red-line breach** | Kill | Regardless of score |

---

## The swap test

> **Replace {Product} with a competitor. Does the ad still work?**

Try at least three swaps: the category leader, a cheaper single-feature app, and a human professional (an accountant, an advisor).

| If the ad still works with… | It means… | Fix |
|---|---|---|
| Any competitor | You're selling the category. A bigger brand will get the click. | Change the reveal, not the hook |
| A single-feature app | The reveal uses one account or one transaction | Make the reveal need the whole picture |
| A human professional | You're selling "advice" in general | Show something only {Product} does fast, cheaply, or always-on |

**The pattern we found:** every swap failure was a reveal from **one account** ("you spent $400 on delivery"). Every swap winner was a reveal you can **only get by connecting everything** ("your five funds hold mostly the same stocks"). Use this as a rule when writing, not only when scoring.

---

## Gate 2: Does the ad land?

A script can pass the rubric and still fail. Before production, also check:

- [ ] **It ends in a decision, not a discovery.** "Here's what you spent" is a discovery. "Rent was the problem, not coffee" is a decision.
- [ ] **It asks one specific question.** "Can you afford this house?" beats "Get your free check-up."
- [ ] **It gives a number the viewer can't work out alone.**
- [ ] **The landing page answers that same question.** The ad and the first screen use the same sentence.

---

## Red lines (any breach = Kill)

Written for a finance product. Adjust for your category.

- No "advice" or "financial advisor" claims about the product
- No "guaranteed", no return promises, no "get rich"
- No price predictions, no buy / sell / hold
- No fear-of-missing-out, guilt, fake urgency, or countdown timers
- No numbers you can't verify today
- Only advertise features that are live now
- No real people's faces or real apps' logos in AI footage
- Add a small disclaimer to the end card (example: "Illustrative. Not financial advice.")

---

## Optional: a five-voice review panel

For bigger campaigns, the single scorer becomes a panel. Each voice reviews on its own first, then they argue:

| Voice | Looks for |
|---|---|
| **Brand** | Tone, red lines, would it attract the wrong audience? |
| **Marketing** | Right hook for the audience and the channel? Does it sound like every other ad? |
| **Design** | Does the first frame work? Is text under 20% of the screen? End card correct? |
| **Video** | Hook (0–3s), value (3–10s), call to action (last 2–3s). At least 2 cuts in the first 5 seconds. Works on mute. Crops cleanly to all three sizes. |
| **Funnel** | Clear next step? Will it bring real users or junk installs? What should we A/B test? |

The useful part is the **planned disagreement**. Brand says "too aggressive." Marketing says "this is what performs." Funnel wants a bold claim. Brand says "that's a red line." The final call comes out as Ship, Revise, or Kill, with a short list of must-fix items.

---

## Output template

```
Script: [title]
Total: [score]/100   Verdict: Ship / Revise / Kill
Hook        [x] — "[quoted line]" — [why]
...
Swap test:  Pass / Fail — [which competitor it still works for]
Red lines:  OK / [which one]
One fix:    [the single highest-leverage change]
```

Batch summary: ranking table · weakest dimension across the batch · swap-test failures and their common cause · 2–3 rules for the next batch.
