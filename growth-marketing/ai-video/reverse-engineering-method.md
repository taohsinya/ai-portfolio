# Reverse-Engineering Short Videos into a Production Spec

How to study short videos that perform well in a genre and turn what you learn into a spec an AI video pipeline can follow. The result is a set of rules for **your own original character and content**, not a copy of anyone.

---

## Ground rule: study the genre, not one person

- **Study several creators** in the same niche, not one. You want what the genre has in common, not one person's personal style.
- **Never copy** a real person's face, look, voice, catchphrases, or scripts. Don't save full transcripts in your project. Keep only patterns: structure, timing, hook types.
- **Your on-screen character is invented.** Design it from your brand, not from a real creator's appearance.
- **Respect platform terms** when collecting videos for analysis. Keep them private and delete them when the analysis is done.

---

## Step 1. Build a sample

- Pick 3–5 creators in your niche whose videos clearly perform well.
- Pull 20–60 videos across them. Include their best and their average posts.
- Log each one in a spreadsheet: length, topic type, views (if public), date.

## Step 2. Extract frames

Short videos move too fast to study by eye. Turn each one into still images:

- Grab **one frame every 3 seconds**. A 60-second video gives about 20 frames.
- Have an AI model with vision read every frame. It records: on-screen caption text, shot size, background, props, what's on screen besides the person (charts, article screenshots).
- For big samples, split the videos across several AI agents running in parallel, then merge the results.

At this step you are collecting **observations**, not opinions.

## Step 3. Write the style bible

Turn the observations into rules, and add a number to each one wherever you can. "Plain background in 45% of videos" is useful. "Usually a plain background" isn't.

| Section | What to capture |
|---|---|
| **Format** | Aspect ratio, typical length, length by topic type |
| **Structure** | What happens in seconds 0–3, 3–10, 10–25, 25+, and the last 5–10 |
| **Captions** | How long caption lines are, how fast they change, where numbers go |
| **Visuals** | Scene types and how often each appears; color palette; props |
| **Proof** | When on-screen evidence appears (article screenshots, data cards), and for how long |
| **Audio** | Voice pacing, music, sound effects |
| **Anti-patterns** | What these creators **never** do. Often the most useful section. |

## Step 4. Sort the hooks into types

Label the first 3 seconds of every video. Count how often each type appears. Typical types in news and finance short video:

| Hook type | Pattern | Template |
|---|---|---|
| **Shock number** | Number first, context second | `[$ amount] + [what kind of deal]` |
| **Inside information** | Viewer feels let in on something | `"So we have [a leak / an internal doc]..."` |
| **Biggest / newest** | Ranking plus recency | `[superlative] + [category] + [time frame]` |
| **Surprising action** | Someone does something unexpected | `[company] + [surprising verb] + [unexpected object]` |
| **Contradiction** | Two things that shouldn't both be true | `"I make [good income] and still [bad outcome]."` |
| **Confession** | An admission people relate to | `"I finally checked [scary thing]. It wasn't what I feared."` |

Then match hook types to topic types. Which hook works best for news, explainers, or results?

## Step 5. Learn the caption rhythm

A pattern that shows up again and again in short video: **captions as fragments, not sentences.**

- First 5 lines: 3–6 words each
- Next lines: 4–8 words
- Explanations later on: up to 12 words
- **Every key number gets its own line**
- No greeting, no "in this video", no hedging ("I think", "maybe")

Each fragment is a small hook that pulls the eye to the next one.

## Step 6. Turn it into a production spec, in three layers

The most common mistake is mixing these layers in one prompt. Keep them separate:

| Layer | Tool type | What it contains |
|---|---|---|
| **1. Script** | Writing (LLM) | The spoken words, in caption fragments. Feeds both lip-sync and captions. |
| **2. Video generation** | AI video model | **Two prompts per clip:** a CHARACTER prompt (look, outfit, action, expression) and a separate SCENE prompt (background, light, mood, no person). |
| **3. Post-production** | Code-based editor (e.g. Remotion) | Timed captions, data cards, article screenshots, bottom labels and disclaimers, audio mix. |

Why separate: video models are bad at rendering text and charts. Put every word and number in layer 3, where you control it exactly.

## Step 7. Keep your character consistent across clips

Most AI video tools make clips of about 15 seconds or less. A 60-second video is 4 clips joined together. To keep the character looking the same:

```
Clip 1: generate → save the last frame as image 1
Clip 2: use image 1 as the first frame → save the last frame as image 2
Clip 3: use image 2 as the first frame → save the last frame as image 3
Clip 4: use image 3 as the first frame → fade out at the end
```

Also write a **character sheet** and repeat its key details in every prompt. Example: hair, a signature prop, the outfit palette, and "natural, not perfect" skin and styling. Leave a detail out and the model fills in its own default. The fix: list the details the model keeps getting wrong, and put them in every prompt.

Always state the aspect ratio as **the first words** of every prompt. Many models default to landscape.

## Step 8. Write the output template

Every finished spec for one video should contain:

1. **Script.** Caption fragments with timestamps.
2. **Video prompts.** CHARACTER plus SCENE for each clip, and how the clips join.
3. **Post-production sheet.** When each caption, data card, and label appears.
4. **Post copy.** The caption text for the social post.
5. **Quality checklist.** Aspect ratio stated, character details present, numbers on their own lines, disclaimer present, no anti-patterns.

---

## What makes this method work

- **Numbers over vibes.** "40% of hooks open with a dollar amount" is a rule a model can follow. "Punchy openings" isn't.
- **Anti-patterns matter as much as patterns.** Knowing what top creators avoid stops the most common AI-content mistakes.
- **Version the spec.** Each test video exposes a new failure (wrong orientation, wrong hair, a missing prop). Write each fix into the spec and keep a changelog, so the next video doesn't repeat it.
- **The spec is a starting point, not a script to copy.** Your own content, brand voice, and compliance rules sit on top. For regulated categories like finance, the red lines in [scoring-rubric.md](scoring-rubric.md) override anything the benchmark creators do.
