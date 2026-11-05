# Perceived value and NPS: putting a number on what to build

## The rule

Every feature that goes into development has to pass two tests:

| Test | Question | What goes wrong without it |
|---|---|---|
| **Perceived value (PV)** | Would users pay because of this feature? | The experience is nice but nobody pays for it |
| **NPS (Net Promoter Score)** | Is the experience good enough that users would recommend it? | The feature is valuable but a slow or confusing flow stops people using it |

If we couldn't show that a feature would raise one of these two scores, we didn't build it. Opinions, including mine, didn't count on their own.

## Scoring perceived value

PV is not "the product manager thinks it's important". It comes from two questions.

**1. The disappearance test.** If this feature vanished tomorrow, what would the user do?
- Find a replacement → low value
- Put up with it → medium value
- Refuse to accept it → high value

**2. The free-alternative test.** Is there a free product that does 80% of this?
- Yes → low value: we'd only be "also having it"
- No → high value: users can only get it from us

Then each feature gets a score against fixed anchors, so different people score the same way:

| Score | What the user would say | What they'd do |
|---|---|---|
| 9–10 | "If this disappeared I'd pay for another product to replace it" | Search for alternatives, accept a higher price |
| 7–8 | "I'd be annoyed, and I'd pay to keep it" | Hesitate at the paywall, then pay |
| 5–6 | "I'd miss it but wouldn't pay; I'd make do with free tools" | Close the paywall, come back occasionally |
| 3–4 | "Don't care, free tools are enough" | Never open the feature |
| 1–2 | "I didn't notice it existed" | — |

## Three levels of evidence

The score gets more reliable as the product moves towards launch:

| Stage | Method |
|---|---|
| Writing the spec | Price-sensitivity questions, the disappearance test, the free-alternative test |
| Beta and after launch | How many users use the feature, how often they come back to it, and how deep they go without being pushed |
| After launch | Real money: how many convert when they hit the paywall, and which feature people mention most when they downgrade |

## A real result: what the scores changed

We scored eight core features with 100 simulated users across six user types. Two findings changed the product:

- **News scored 1.7 out of 10, the lowest of all.** News is free everywhere, so nobody pays for it. We moved from news to in-depth articles, which also bring in search traffic.
- **The two highest-value features complemented each other.** One (daily stock ideas) was valued most by beginners and less by experts; the other (stock ratings) was the opposite. Together they covered every type of user, so those two became the core of the paid plan.

A third finding: AI search had real value for experienced users, but it was too slow, so its NPS was negative. The fix wasn't a new feature; it was making the existing one faster.

## Value is not the same as conversion

A high value score doesn't mean that share of users will pay. Three things cut it down:
1. **Real-world friction**, such as loading times, distractions and reluctance to pay: assume 50–70% of the theoretical number
2. **Drop-off at each step**: download → active → reaches the paywall
3. **Price**: a small one-off payment and an annual plan can convert 3–5 times differently

## Scoring NPS: five dimensions

To estimate how each change would move NPS, each release was scored on five weighted dimensions:

| Dimension | Weight |
|---|---|
| First impression | 0.15 |
| Content quality | 0.25 |
| Personalisation | 0.20 |
| Willingness to pay | 0.25 |
| Reasons to come back | 0.15 |

Each planned feature got an expected change on each dimension, which adds up to an expected change in NPS. Over four weekly releases, the simulated NPS moved from **−50 to +28**, then to +40 before a final correction for over-optimism (see [AI user simulation](../ai-user-simulation/)).

## How it was used every release

Every important feature carried three lines in the decision log:
- **Value:** one sentence on why someone would pay
- **NPS assumption:** the expected range and how we'd check it
- **Kill rule:** what we'd measure 4 weeks after launch, and the level below which we'd remove it

The kill rule is there because teams find it hard to delete something they've built. Deciding the threshold before launch takes the emotion out of it.

---

*The method, the five-dimension framework and the decision rules are mine; the release-by-release estimates were produced by AI agents. A teammate reviewed and corrected those estimates.*
