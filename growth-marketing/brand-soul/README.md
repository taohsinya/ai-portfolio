# Writing a "soul" for an AI product

[![The soul as a brand video. Click to watch on YouTube](https://img.youtube.com/vi/LMzKBIJ2rzk/hqdefault.jpg)](https://www.youtube.com/watch?v=LMzKBIJ2rzk)

*▶️ The soul as a brand video. Click to watch on YouTube*

**In one line:** I wrote a one-page document that says who our AI money assistant *is*: what it believes, how it talks, and what it will never do. Then I turned that page into rules that every ad, push notification and piece of copy had to pass.

Positioning line it all hangs from: **"Finally, a money person on your side."**

---

## The problem

An AI product talks to users all day, in thousands of messages nobody on the team will ever read. Copywriters, engineers writing prompts, designers and marketers each make small choices about how it sounds. Without a shared reference, you get five different personalities:

- The chat answers sound like a helpful robot.
- The push notifications sound like a sales team chasing a target.
- The ads sound like a trading tips channel.

Users notice. In money products, a mixed personality reads as "I can't trust this."

A normal brand book does not fix this. It tells you about fonts, colours and tone words. It does not tell an engineer what the assistant should say when it has no data, or tell a marketer whether "Don't miss out" is allowed.

## What a soul document is

A soul document defines **who the product is, not what it can do.** It sits above the brand book and the feature specs. The rule at the top of ours was simple:

> Every product decision, prompt, copy draft and notification must line up with this document. If anything conflicts, this document wins.

Ours had seven parts:

1. **Who it is** - one picture of the character in plain words.
2. **What it believes** - five short beliefs, each with a concrete example.
3. **How it shows up for different people** - one character, six kinds of relationship.
4. **How it shows care** - when to speak, and when to stay quiet.
5. **How it talks** - voice rules, with "say this, not that" pairs.
6. **How it gets smarter** - how the relationship deepens over time.
7. **What it never does** - eight hard rules, plus a rule about silence.

It ends with one question for each team (product, engineering, design, copy) to ask before they ship.

The reusable structure is in [`soul-template.md`](soul-template.md).

## How I wrote it

I rewrote the soul document myself. These are the choices that shaped it:

- **Started from a feeling, not a feature.** The first line is "Your money is going to be okay." Everything else explains how the product earns that sentence.
- **Wrote beliefs as trade-offs.** Each belief picks a side: honest over polished, quiet over impressive. A belief that costs nothing is not a belief.
- **Gave every rule an example.** "Don't make the call" is vague. "Don't say *you should buy this stock*. Say *it ranks in the top 15% on valuation in its sector, but the chart setup is the weakest in the group. Here's the data - your call.*" is something a writer can copy.
- **Described people by what they say, not by a label.** Each user type opens with a quote, like *"I used to feel dumb asking about investing."* That keeps the team thinking about real fears, not personas on a slide.
- **Wrote down what it never does.** The "never" list did more work than anything else in the document. It is the part people could check.

## Five excerpts that show the voice

Lightly edited and with the product name removed.

**1. Honest over polished**
> When it doesn't know something, it says "I don't have that data." It doesn't fabricate a plausible-sounding analysis. It doesn't use "market consensus suggests" to cover up "I'm guessing." It would rather say one true thing that disappoints you than ten false things that make you feel good.

**2. Data first. Judgment is yours.**
> It provides the parts of a judgment, not the judgment itself. Users are adults. It respects that.

**3. Care isn't interruption**
> The market drops 5%. It doesn't push "market down 5%" - any news app can tell you that. It pushes "your stock is down 8%, but you said you'd consider adding below a certain price. It's not there yet. No rush." Three things in that sentence only it knows. That's care.

**4. Silence is care too**
> When it has nothing to say, it says nothing. No "all clear" daily digest. No "daily tip" made up to hit an engagement number. If you go a week without hearing from it, that's because nothing worth interrupting you happened.

**5. The technology stays quiet**
> The more powerful the technology, the quieter it should be. What users feel isn't "this AI is so smart." It's "this product really gets me."

## How the soul flowed down into real work

A soul document only matters if it changes what ships. It reached three places.

### 1. Copy and brand voice

The brand guidelines (a team document) were rewritten to point back to the soul. The soul covers how the assistant talks *inside* the relationship. The brand guidelines cover how it sounds *before* the relationship exists: ads, app store pages, the first day. Brand personality traits like "Honest without apology" and "Calm under pressure" are the public face of the soul's beliefs.

A condensed, debranded version is in [`brand-guidelines-example.md`](brand-guidelines-example.md).

### 2. Push notifications

I wrote the prompts that generate push notifications. Their rules come straight from the soul:

- A result is "a fact, not a flex." No gloating, no guilt, no "we told you so."
- No emojis. The last sentence is a statement, never a question.
- Never promise a return.

### 3. Marketing review: the "kill" rule

I wrote a review checklist that an AI reviewer (or a person) runs on every ad, video script, banner and social post before launch. It checks seven things. Two of them are **red lines**: break one and the creative is killed, not edited.

**Red line 1 - the soul.** Kill the creative if it:
- tells people to buy, sell or hold, or implies the product does;
- makes a prediction or price target sound like the product's call;
- brags ("it spotted it first", "it was right");
- uses fear of missing out or guilt ("Don't miss out", "Before it's too late");
- invents urgency (countdown timers, "Act now");
- shows off internal systems instead of value to the user.

**Red line 2 - product truth.** Kill the creative if a number, feature or performance claim cannot be checked against what is live in the app today.

The other five checks (brand tone, "who would this attract?", channel format, visual style, call to action) lead to "revise", not "kill".

The "who would this attract?" check was the most useful for growth. We named the audiences we did *not* want, for example the **"loss-porn gambler"** who responds to tips and urgency. If a hook would pull in that crowd, it gets rewritten, even if it would get clicks.

Each review ends with a verdict (Pass / Revise / Kill), a "must fix" list and a suggested A/B test. A short table of common violations sits at the end, with the fix next to each one:

| Breaks the soul | Fix |
|---|---|
| "{Assistant} says buy this stock" | "{Assistant} found it ranks top 15% on valuation. Here's the data." |
| "{Assistant}'s prediction: +12%" | "{Assistant} flagged the margin trend." |
| "Don't miss the next one" | "See what {Assistant} found today." |
| Big performance claim nobody can verify | Verify it, or don't use it. |

## See it in action

▶️ **["The Vet": brand video](https://www.youtube.com/watch?v=LMzKBIJ2rzk)**: the soul turned into a brand video. Notice the voice: calm, on your side, no hype.

## What I'd tell other teams

1. **Write the "never" list first.** It is the easiest part to agree on and the only part you can enforce.
2. **One example per rule.** If a writer can't copy it, it's not a rule yet.
3. **Make the soul win.** Say so at the top. Otherwise it loses to the first conversion target.
4. **Turn it into a checklist.** A document people read once fades. A review step that can kill an ad does not.
5. **Name the users you don't want.** Your hooks decide who shows up. A growth team that only chases clicks will attract the wrong crowd for a trust product.
6. **Treat silence as a feature.** In an AI product, the message you don't send is part of the voice.

## Credits

- **Soul document:** rewritten by me.
- **Push notification prompts:** written by me.
- **Marketing review checklist:** written by me, with small edits from a product teammate.
- **Brand guidelines:** a team document. I used it as a source and linked it to the soul; the condensed version here is my summary.

Product names, colours, logos, numbers and internal details have been removed.
