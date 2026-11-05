# Testing with simulated users

AI can play hundreds of users in minutes. That makes it a powerful way to test a product before launch, and an easy way to fool yourself. This page is about how I used it and how I kept it honest.

## Three rounds of checks

```
Round 1 · On paper
  Score the spec with simulated users (expected NPS must be positive)
    ↓
Round 2 · Simulated behaviour
  Simulated users go through the beta product; we get where they click and where they drop off
    ↓
Round 3 · Real launch
  Compare with real user data
    ↓
Review the gap → adjust the simulation → repeat
```

The goal: by the time the spec is written, be able to predict roughly how a feature will perform.

## Why AI simulations are too optimistic

An AI simulation is **necessary but not enough**:

- **If the simulated score is negative → strong signal.** Real users will be even less happy. Send it back.
- **If the simulated score is positive → weak signal.** It only proves the idea makes sense on paper.

There are three built-in biases:
1. **Too agreeable.** AI tends to give reasonable answers. It doesn't simulate someone in a bad mood who just closes the app.
2. **Blind to friction.** Loading times, distractions and the pain of paying aren't in the simulation.
3. **Too rational.** AI doesn't simulate irrational decisions.

My rule of thumb: **discount positive simulated results to 50–70%** of what the simulation says.

## Correcting the simulation with real data

Two examples of where simulation and reality disagreed, and what we did:

- **The starting score was too negative.** A first simulation put the starting NPS at −100: every simulated user unhappy. But real trial data showed many users were at least satisfied enough to try the paid plan, so a teammate corrected the baseline to −50. Lesson: anchor the simulation to whatever real data you already have.
- **The simulation overrated entry points and underrated the core.** It gave a welcome screen more impact than the main analysis page. After review, the main analysis page became the biggest single contributor and the welcome screen dropped. Lesson: check whether the ranking makes sense, not just the totals.

The final simulated NPS was multiplied by 0.8 as a standing correction, and later compared with an NPS estimate built from real user behaviour, which the data team built from usage logs.

## Same data, different presentation

One design rule came out of these tests: **the data is the same for everyone; only the presentation changes.** A quick reader and an in-depth reader see the same scores, but one gets a short summary and the other gets every chart expanded. For the same stock, simulated NPS went from 0 to 60 just by matching the presentation to the type of user.

## Worked example

**[Financial Fitness Score](../financial-fitness-score/)**: the full loop on one model. 35 simulated users → an AI acting as a sceptical financial planner rated the first version 5.5/10 → three fixes → re-score.
