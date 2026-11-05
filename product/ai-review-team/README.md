# Product review by a team of AI agents

Before a plan reaches designers or engineers, it has to survive a series of challenges. Several of those challengers are AI agents, each playing a different role. This is the release process I set for the team.

## The process: 8 stages, each one a test

| Stage | What happens | What it must produce |
|---|---|---|
| 1. Define the problem | The core problem, how we'll measure success, and a one-sentence value statement for every important feature | One-page release goal |
| 2. Cut it down | An AI agent applies first-principles thinking: what must stay, what can be simpler, what can wait, what should go | A shorter plan and a roadmap of what comes later |
| 3. Draft the spec | User stories, how it works, the user experience, a decision log | First draft |
| 4. Simulated NPS | Simulated users score the plan. **If the expected NPS is negative, it goes back to stage 3** | NPS report |
| 5. Four-role challenge | Four AI agents playing **product manager, designer, operations and brand** each attack the same plan independently | List of problems to fix |
| 6. Quality check before design | An AI checker reviews the logic: is every user path covered, does every screen have every state (empty, loading, error), are the branches complete? | Corrected spec |
| 7. Scope lock | Split by risk, lock the scope, and give every feature a **kill rule**: what we measure 4 weeks after launch and the level below which we remove it | Locked scope |
| 8. Go / no-go | Final review against a checklist | Decision to build |

## Rules that make the AI reviewers useful

**Each reviewer gets one clear role.** "Review this" gets polite, general feedback. "You are the operations lead who has to run this every day; list what will break" gets specific problems.

**Reviewers work independently.** The four role agents don't see each other's comments, so they don't just agree with each other.

**Numbers must come from a real source.** The quality checker fails any spec whose baseline numbers can't be found in the weekly data snapshot. AI writing tools are good at producing numbers that look right, so this rule stops made-up data getting into decisions.

**A negative result is a hard stop; a positive one isn't a pass.** See [AI user simulation](../ai-user-simulation/) for why AI reviewers are too optimistic.

**Founder perspectives give advice, not vetoes.** Agents that reflect how the founders think can raise their top three concerns, but they can't block a plan on their own.

## Example from practice

In one design review, six agents challenged a plan for push notifications. The plan had two options: fixed message templates, or letting the AI write every message. The agents' conclusion was that **both were wrong**: templates feel robotic, and fully AI-written messages are hard to control. The point is that the right answer wasn't on the table until the agents attacked both options.

## What I'd tell any team trying this

- AI reviewers are cheap, so use them early, before a designer has spent a week on the wrong thing.
- The value comes from **conflict between roles**, not from one smart reviewer.
- Keep a human decision at the end. The agents find problems; people decide.

---

*I designed the process and its rules. Teammates built most of the review tools (the spec writer and quality checker), and the four role agents were set up by the product team.*
