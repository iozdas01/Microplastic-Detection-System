# Furniture Manufacturing — Assumption Lab

Testing one idea: **custom cabinetry costs three times stock cabinetry, and most of that
premium is a designer's afternoon rather than a manufacturing cost.** If that is right, the
same machines sell a custom kitchen at a semi-custom price.

## Layout

Code at the root, everything about the idea under `reports/{slug}/`.

```
CLAUDE.md  ARCHITECTURE.md  schemas/  methods/  founders/  .claude/skills/

scripts/              the assumption pipeline — generators, validators, loader
scripts/data/         shared query library (Reddit, HN, news, LinkedIn export)
scripts/research/     market-evidence collectors — Census, BLS, Trends, Comtrade

reports/custom-kitchen-cabinets/
  BRIEF.md            generated session entry point — read this first
  control-room.html   generated: hunch → assumptions → evidence → outreach, one page
  01-ideation/        the hunch lineage
  02-assumptions/     the assumption graph
  03-validation/      the evidence ledger, and interview notes as they land
  04-mutation/        offerings
  outreach/           contacts, and call-log.html for taking notes during a call
  research/           what the collectors measured: REPORT.md, the HTML reports, data/
```

There is one `reports/` tree, one `scripts/` tree and one `data/` directory, on purpose. The
market-research pipeline used to be a self-contained `research/` folder with its own copies of
all three; that meant "reports" named two different things depending on where you stood.

The collectors produced this idea rather than the other way round: they started on configurable
furniture sold direct to consumers and measured their way to fitted kitchen cabinets, the only
one of 24 categories where search carried commercial intent. Their findings enter the pipeline
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

One idea is active: `custom-kitchen-cabinets`.

The belief and hunch are recorded, the assumption graph is built, and **every assumption is
untested**. The ledger holds six entries and all six are our own desk measurement at 2/5 — no
dealer, remodeler or cabinet shop has been asked anything. The root assumption `H1A2` (do
dealers actually lose out-of-catalogue jobs?) has zero evidence and is the cheapest thing in
the graph to settle: roughly seventy trade targets in one metro, ten phone calls, one question,
no product and no spend.

That is the next move, and it is what this repo was merged to do.

- Session entry point: `reports/custom-kitchen-cabinets/BRIEF.md`
- Everything in one page: `reports/custom-kitchen-cabinets/control-room.html`
- The plan the outreach is testing: `reports/custom-kitchen-cabinets/research/cabinet-plan-final.html`
- What to do in what order, with costs: `reports/custom-kitchen-cabinets/research/build-board.html`
- Notes template for the calls themselves: `reports/custom-kitchen-cabinets/outreach/call-log.html`
