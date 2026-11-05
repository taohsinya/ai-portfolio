# Obsidian vault structure

> **Not investment advice.** All note names below are fictional examples.

Obsidian stores every note as a plain Markdown text file in a folder (a "vault") and draws links between notes written as `[[Note Name]]`. Claude writes and updates the files; I read them in Obsidian, follow the links and use the graph view to see what depends on what.

---

## Folder layout

```
research-vault/
│
├── Home.md                      ← start page: thesis table, signals due soon, current backdrop
├── How This Works.md            ← the rules (note types, red lines, daily routine)
├── Thesis Map.canvas            ← hand-arranged visual map of theses and their links
│
├── tracker/
│   ├── thesis/
│   │   ├── Thesis Index.md
│   │   ├── T1 Demand Outruns Supply.md
│   │   ├── T2 Long Contracts Set A Floor.md
│   │   ├── T3 Shortage Moves Downstream.md
│   │   └── ... (about 10)
│   │
│   ├── signals/
│   │   ├── Signal Index.md      ← open signals sorted by deadline + closed signals table
│   │   ├── S11 Server Order Growth.md
│   │   ├── S14 Board Supplier Price Increase Sticks.md
│   │   └── ...
│   │
│   ├── evidence/
│   │   ├── Evidence Index.md
│   │   ├── E07 Cloud Provider Raises Spending Plan.md
│   │   └── ...
│   │
│   ├── findings/                ← lessons from closed signals (the calibration record)
│   │   ├── Findings Index.md
│   │   └── F04 Announced Price Rises Land at Half.md
│   │
│   ├── audit/                   ← the adversarial layer
│   │   ├── Audit Layer.md       ← the six questions and the hard rule
│   │   ├── Audit Discipline.md  ← "don't flatter me" rules + 7-item self-check
│   │   └── Audit — Shortage Chain.md
│   │
│   ├── Factor Board.md          ← shared drivers, each with a next_signal
│   ├── World State 2026-Q3.md   ← dated snapshot of the market backdrop
│   └── Change Log.md            ← what changed each day, and why
│
└── stocks/                      ← one note per company, linking back to theses
    ├── Company A.md
    └── Company B.md
```

**Not in the vault, ever:** personal positions, prices paid, buy or sell decisions, and Obsidian's own settings folder when sharing.

---

## How the note types link

```
                       ┌──────────────────┐
                       │   World State    │  (backdrop; read by everything)
                       └────────┬─────────┘
                                │
   ┌──────────────┐     ┌───────▼────────┐      ┌──────────────┐
   │   Evidence   │────▶│     Thesis     │◀─────│ Factor Board │
   │ (one fact,   │     │ claim + chain  │      │ shared       │
   │  many links) │     │ + kill cond.   │      │ drivers      │
   └──────┬───────┘     └───┬────────▲───┘      └──────┬───────┘
          │                 │        │                 │ next_signal
          │      tested by  │        │ confidence      │
          │                 ▼        │ up / down       ▼
          │         ┌───────────────────────────────────────┐
          └────────▶│                Signal                 │
                    │ claim · 3 outcomes · deadline · source│
                    └───────┬───────────────────────▲───────┘
                            │ scored on deadline    │ proposes new
                            ▼                       │ signals (candidate only)
                    ┌───────────────┐       ┌───────┴───────┐
                    │    Finding    │       │     Audit     │
                    │ lesson learned│       │ six questions │
                    └───────────────┘       └───────────────┘
                            │
                            ▼
                      Change Log
```

The audit can **propose** but cannot **change** a thesis or a piece of evidence. Changes only happen when a signal is scored.

---

## Example: one fact rippling through the vault

A (fictional) large cloud provider raises its annual spending plan.

1. **One evidence note** is created: `E07 Cloud Provider Raises Spending Plan`. Its header records the source, how reliable and direct it is, whether it was independently confirmed, how fresh it is, and which direction it points.
2. That note is **linked from four places**: `T1 Demand Outruns Supply` (supports), `T2 Long Contracts Set A Floor` (supports), a funding-risk thesis (it also means more borrowing, which argues *against*), and the signal `S06 Big Spenders Cut Plans` (an early reading against it).
3. On the **Factor Board**, the "data-centre spending" factor updates its state, and its `next_signal` points to the next earnings season.
4. The **Change Log** gets one line: date, files touched, and the fact that one piece of evidence now supports three theses and argues against a fourth.

Opening `E07` in the graph view shows at a glance how much of the research rests on this one fact. That is the "hidden concentration" check.

---

## Evidence note header (fields)

```yaml
type: Evidence
date: 2026-03-20
source: "Company earnings call (public)"
source_reliability: high      # how trustworthy the source is in general
directness: high              # is this the fact itself, or someone's summary of it?
independence: true            # confirmed by sources that don't share the same bias?
freshness: current            # current / recent / stale (stale lowers strength one step)
evidence_strength: high
direction: bullish            # which way it points for the theses it touches
referenced_by: ["[[T1 ...]]", "[[T2 ...]]", "[[S06 ...]]"]
```

**Grading rule of thumb:** confirmed by three or more independent sources → high; two → medium; one → low. If credible sources actively disagree, mark `contradiction: true`, which forces the related signal's confidence to low and moves the thesis to "contested" until it is settled.

---

## Factor Board row (fields)

| Field | Meaning |
|:---|:---|
| current_state | What the driver reads now |
| direction | rising / falling / flat |
| strength | how big the effect is |
| confidence | how sure we are of the reading |
| market_awareness | ignored / noticed / crowded |
| priced_in | not / partly / fully, in the current share prices |
| affected companies | who it moves |
| supporting / opposing | links to theses and signals |
| **next_signal** | the next dated test that will tell us something about this driver |
