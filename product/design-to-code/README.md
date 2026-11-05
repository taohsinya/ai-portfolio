# Design to code: Claude Design → Figma → code

The product flow I set for the team. It does two things:

1. **Ideas reach working code fast.** An idea becomes a clickable prototype in hours, not weeks, so we could try more ideas and drop the weak ones early.
2. **Problems are caught at the design stage.** Engineering and operations could check the design before anyone wrote production code, instead of finding problems after it was built.

## The flow

```
Idea
  ↓  Claude Design: turn the idea into a clickable prototype using the product's design rules
Prototype
  ↓  Review: product, engineering and operations check it (and AI reviewers challenge it)
Figma
  ↓  The design team turns the approved prototype into final designs
Figma to code
  ↓  Engineers build from the final designs, reading them directly into code
Shipped feature
```

## Why it works

**The prototype uses the real design rules.** The AI that builds prototypes is given the product's design system: colours, spacing, components, every screen state (empty, loading, error) and how to write the words on screen. So a prototype already looks and behaves like the real product, and the step to Figma is small.

**Engineering checks early.** Because the prototype is concrete, the people who will build and run it can say "this won't work" before any production code exists. Fixing a design costs minutes; fixing shipped code costs days.

**Every step hands over something specific.** Idea → prototype, prototype → reviewed design, design → code. No step starts from a blank page.

## The tools

Two instruction sets ("skills") that teach an AI to build prototypes inside the product's design system. Brand names, colours and product details have been replaced with placeholders such as `{Product}`.

| Skill | What it does |
|---|---|
| [UI prototype skill](skills/ui-prototype-skill/) | Builds clickable prototypes from a description, with the design system, a sample onboarding flow and made-up example data |
| [Product design system skill](skills/product-design-system-skill/) | The full design system, screen-generation rules, website design and on-screen writing rules |

---

*I designed the flow and wrote these two skills. The Figma-reading tools used in the last step were built by a teammate and are not included.*
