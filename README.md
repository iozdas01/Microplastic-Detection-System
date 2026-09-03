# HMLV Manufacturing — Assumption Lab

Testing one belief: **software and machines don't talk, and you have to own both to fix it.**

Scoped (2026-08-31) to manufacturing where **the design-to-machine handoff is per-order and
still manual** — every job needs its own geometry, toolpath, cost and schedule, and a person
moves that between CAD, CAM, ERP and the floor by hand.

**Which industry is deliberately still open.** Picking the wedge is the question this repo
exists to answer, not an input to it. Cabinetry and millwork are one candidate lane among
several, not the frame — the repo was called Furniture Manufacturing while the belief was
still cabinet-specific, and the belief has since been raised a level. `belief.md` carries
that history in its version log; don't strip it.

## Layout

Code at the root, everything about the idea under `reports/{slug}/`.

```
CLAUDE.md  ARCHITECTURE.md  schemas/  methods/  founders/  .claude/skills/

scripts/              the assumption pipeline — generators, validators, loader
scripts/data/         shared query library (Reddit, HN, news, LinkedIn export)
scripts/research/     market-evidence collectors — Census, BLS, Trends, Comtrade

reports/high-mix-manufacturing/
  BRIEF.md            generated session entry point — read this first
  control-room.html   generated: hunch → assumptions → evidence → outreach, one page
  01-ideation/        the hunch lineage
  02-assumptions/     the assumption graph
  03-validation/      the evidence ledger, and interview notes as they land
  04-mutation/        offerings
  outreach/           contacts, and the copy archive as it fills
  pages/              every other readable report — plans, evidence, the call-notes sheet
  research/           what the collectors measured: REPORT.md, data/, archive/
```

There is one `reports/` tree, one `scripts/` tree and one `data/` directory, on purpose. The
market-research pipeline used to be a self-contained `research/` folder with its own copies of
all three; that meant "reports" named two different things depending on where you stood.

The collectors produced this idea rather than the other way round: they started on configurable
furniture sold direct to consumers and measured their way to fitted kitchen cabinets, the only
one of 24 categories where search carried commercial intent. That measurement is what the
belief was later generalised FROM — it is provenance, and it is furniture-shaped for good
reason. Their findings enter the pipeline
as ledger entries in `03-validation/evidence.md`, graded as what they are — desk measurement,
not buyer evidence. `scripts/research/README.md` says how to run them.

## Setup

Once per clone:

```bash
scripts/setup.sh
```

Creates `.venv`, installs dependencies, installs the git hooks, and verifies the repo. Nothing
runs without it — macOS refuses a system-wide `pip install` (PEP 668), so the validators and
generators fail with `No module named 'yaml'` until the venv exists. Afterwards, run repo
scripts with `.venv/bin/python`.

## Starting a session

Name the idea. The assistant reads `reports/{slug}/BRIEF.md` — a generated digest of that
idea's current state — and loads only the artifacts the task needs.

- **`CLAUDE.md`** — how to behave: what to load, what to write, which skill to use.
- **`ARCHITECTURE.md`** — how it is built: the loop, the modules, the folder layout, the schemas.
- **`reports/lifecycle.yaml`** — which ideas are active, dormant, or superseded.

## Where the idea stands

One idea is active: `high-mix-manufacturing`.

The belief and hunch are recorded, the assumption graph is built, and **every assumption is
untested**. The ledger holds six entries and all six are our own desk measurement at 2/5 — no
dealer, remodeler or cabinet shop has been asked anything. The root assumption `H1A2` (do
dealers actually lose out-of-catalogue jobs?) has zero evidence and is the cheapest thing in
the graph to settle: roughly seventy trade targets in one metro, ten phone calls, one question,
no product and no spend.

That is the next move, and it is what this repo was merged to do.

- **Open this:** `reports/high-mix-manufacturing/control-room.html` — the hunch, the ranked
  assumptions, the evidence, the outreach funnel, and a **Pages** tab linking every other
  report with its status.
- Session entry point for an assistant: `reports/high-mix-manufacturing/BRIEF.md`
- The plan the outreach is testing: `pages/cabinet-plan.html`
- What to do in what order, with costs: `pages/build-board.html`
- Notes template for the calls themselves: `pages/call-log.html`
