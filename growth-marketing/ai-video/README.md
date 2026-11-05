# AI Video Ads, Judged by a Harsh AI Critic

[!["The Vet": a finished brand video. Click to watch on YouTube](https://img.youtube.com/vi/LMzKBIJ2rzk/hqdefault.jpg)](https://www.youtube.com/watch?v=LMzKBIJ2rzk)

*▶️ "The Vet": a finished brand video. Click to watch on YouTube*

**The short version:** I built a production line for short video ads, made with AI, for an AI money assistant. The most important part isn't the video generator. It's a scoring agent that ranks every script against the others, kills weak ones, and asks one hard question: *"Would this ad still work if you put a competitor's logo on it?"* Only the scripts that pass get storyboarded and made into video.

- **Product:** a consumer AI money assistant (US market, English ads)
- **Formats:** stand-up comedy clips, two-person podcast clips, street interviews, short skits
- **Channels:** TikTok, Reels, Shorts, YouTube, Meta feed, Google App Campaigns
- **Tools:** Claude (writing and scoring agents), AI video generators (Higgsfield, Seedance), Remotion for captions and graphics

---

## Why I built it this way

AI made video cheap. That changed what's scarce. We could write dozens of hooks in an afternoon and generate a video from any of them. That makes **picking** the hard part.

Most teams score their own ideas politely. Everything gets a 7 out of 10. Nothing gets cut. So I set the scoring agent up to be a strict creative director:

- It must rank scripts against each other. It cannot give everyone a good score.
- Low scores are expected. In one batch, the middle score was about 5 out of 10 on each dimension.
- Every score needs a reason quoted from the script.
- Every script gets one "highest-leverage fix", usually the opening line.

---

## The pipeline

```
1. Hook ideas  →  2. Scoring agent  →  3. Storyboard  →  4. AI video  →  5. Variants
   (many)          (rank + swap test)     (shot by shot)    (one master)     (topics × sizes)
```

### 1. Hook ideas
Every ad starts from a **money moment** the viewer has lived, not from a product feature. "I make $180k and my card got declined for a coffee." Not "Introducing our new dashboard."

Ideas come from three places:
- **Swipe files.** Ads that competitors have run for 3+ months. If an ad stays live that long, it's probably making money. Short-lived ads tell you nothing.
- **Proven hook types** for money content: contradiction, confession, hard lesson, direct challenge, a surprising number.
- **The product itself.** What can it calculate that the viewer can't work out alone?

### 2. Scoring agent
Each script is scored out of 100 (full rubric in [scoring-rubric.md](scoring-rubric.md)). The opening 3 seconds carry the most weight. If people scroll past, nothing else matters.

**The swap test** is the key idea. Replace our product with a competitor: a budgeting app, a robo-advisor, an accountant. If the ad still works, it isn't selling *us*. It's selling the category, and a bigger brand will get the click.

In one podcast batch, the swap test explained the whole ranking:
- Every script that **failed** showed something from a single account. "You spent $400 on food delivery." Any budgeting app can tell you that.
- Every script that **passed** showed something you can only see by connecting all your accounts. "Your five funds hold mostly the same stocks." "Most of your net worth is tied to your employer."

That one pattern became a rule for the next batch: *the big reveal must need the whole picture.*

### 3. Storyboard
Shipped scripts become shot-by-shot storyboards. Each shot gets its length in seconds, the framing, the caption text, and a ready-to-paste prompt for the video generator. A script generates the storyboard pages, so a change to the script updates every page.

### 4. AI video
We generate one master in vertical 9:16 format. Rules that saved us the most retakes:
- **No single AI face staring at the camera.** People spot it and trust drops. Formats with two or more people (podcast, street interview, stand-up with an audience) keep attention on *what* is said, not *whether the face is real*.
- **One locked hero shot.** Don't ask the AI to move a mouth, change a shape, and move the camera all at once.
- **Built to work on mute.** Captions and sound effects carry the story. Most feed video is watched without sound.
- **A fixed cast.** Three recurring AI characters with locked looks and voices, so freelancers can reproduce them.
- **Same ending for every ad.** The hooks change. The final card (logo, line, download) stays the same.

### 5. Variants (one creative becomes 42 videos)
I organized production in three layers so it could scale without me in the room:

```
Creative (the format)   →   Topic (the content)   →   Format (the size)
Stand-up                    14 locked topics            9:16 / 1:1 / 16:9

1 creative × 14 topics × 3 sizes = 42 videos
```

- **9:16 is made first**, with the subject centered, then cropped to 1:1 and 16:9. One shoot covers all three.
- **Each size has its own safe zone**, so captions never sit under the platform's buttons. Bottom 20% and right 15% on TikTok-style feeds. 10% on all sides for square. Bottom-right 20% on YouTube (the Skip button).
- **One audio track** is shared across all three sizes.
- **A strict file name** tells anyone what a file is: `Creative_TopicID_slug_Size_version`, for example `Standup_T09_3amMath_9x16_v1`.
- **Split the work.** The plan was for the in-house team to make 3 topics × 3 sizes = 9 "golden masters" that set the look, captions, and ending. Freelancers then copy that pattern for the other 33. I picked the first 3 topics to cover both comedy styles, both lead characters, and three different product messages, so the masters would teach the whole pattern.

---

## Kill, revise, ship

| Score | Verdict | What happens |
|---|---|---|
| **80+** | Ship | Goes to storyboard and production |
| **60–79** | Revise | Rewrite the weakest part (usually the first 3 seconds), then score again |
| **Below 60** | Kill | Cut it, or move it to unpaid social if it's funny but generic |
| **Any red-line breach** | Kill | No matter the score |

Red lines for a money product: no "advice" claims, no guarantees, no price predictions, no buy/sell/hold, no fear-of-missing-out or guilt, no "get rich" angle, and only advertise features that are live today.

---

## Reviewing hooks before production

Halfway through, I saw a problem with our own process. We were judging hooks only on **"will people click?"** We never asked **"where does the click land?"** Early data suggested clicks were not turning into sign-ups. (That data was later suspected to be a tracking bug, so I treated it as a hypothesis, not a fact.) But the structural problem was real either way.

So every hook now has to pass two gates:

**Gate 1. Does it stop the scroll and pass the swap test?**
This is the scoring agent above.

**Gate 2. Does it end in a decision, and does that decision have somewhere to go?**
- **A decision, not a discovery.** "You spent too much on coffee" is a discovery. "Coffee wasn't the problem. Rent was." is a decision. Free chatbots give discoveries. A decision about *your* numbers is what people pay for.
- **A matching place to land.** Each hook must point to one specific question the product answers, with one number the viewer can't work out alone. For example: "Can you actually afford this house?", not "Get your free financial check-up." The product had 16 specific checks, but the ads sold all of them under one vague label.

I then regrouped all our hooks by the decision they help with. For each decision, I checked three things: the ad hook, the product feature, and a free tool someone could find through search. Every decision already had hooks and features. Not one had a free tool. That gap became the recommendation.

---

## Watch

▶️ **["The Vet": brand video](https://www.youtube.com/watch?v=LMzKBIJ2rzk)**: a finished brand video for the AI money assistant ("your money person").

## What I learned

1. **When making is cheap, judging is the job.** Most of the value was in the scoring rubric and the kill decisions, not the video model.
2. **The swap test beats taste.** It turns "I don't love this one" into a reason anyone can check. And when you look at all the failures together, they show you a pattern.
3. **Score the batch, not just the ad.** One stand-up batch scored fine one by one. Seen together, 8 of 13 scripts made the same joke ("you waste money on small things"). That's a budgeting app's home turf. The batch needed more "here's your whole picture" ideas.
4. **Front-load the number.** The weakest high-weight score across a whole batch was the hook. Most scripts opened on a feeling ("I always thought…") instead of a number or a clear "this is you." Fix: put the number in the first five words.
5. **End on a decision, not a punchline.** Comedy formats tend to end on the joke. The ad needs to end on the moment of relief.
6. **Pick AI-friendly formats.** Several people talking hides AI weaknesses. One face talking to camera shows all of them.
7. **Check where the click lands before you buy more clicks.** A great hook pointing at a vague landing page wastes the budget.

---

## My role and credits

- **Me:** designed the pipeline, the scoring rubric, the swap test, the hook review, and the 42-video production plan. Wrote most of the review-agent instructions. Scored, rewrote, and selected scripts.
- **Colleagues:** the stand-up scripts started from a colleague's original comedy drafts and writing guide. I scored and revised them; the jokes began as hers. Video production was shared with the wider team and freelancers.
- **AI:** Claude ran the scoring and review agents and helped draft scripts. AI video tools generated the footage.

## Files in this folder

| File | What it is |
|---|---|
| [scoring-rubric.md](scoring-rubric.md) | The scoring rubric: dimensions, weights, thresholds, swap test, review panel |
| [reverse-engineering-method.md](reverse-engineering-method.md) | How to break down successful short videos into a production spec |

*Brand names, people, internal links and numbers have been removed. The product is referred to as {Product} in templates.*
