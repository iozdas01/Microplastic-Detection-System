# Furniture Manufacturing — Assumption Lab

Testing one idea: **custom cabinetry costs three times stock cabinetry, and most of that
premium is a designer's afternoon rather than a manufacturing cost.** If that is right, the
same machines sell a custom kitchen at a semi-custom price.

The repo is two halves that feed each other.

| Half | What it is |
|---|---|
| **The lab** (root) | The assumption pipeline — a founder-owned belief, one falsifiable hunch, an assumption graph of what must be true, an evidence ledger, and the outreach and interview machinery that moves them. Operated by Claude sessions. |
| **`research/`** | The market-evidence pipeline that produced the idea. Collectors against Census, BLS, Google Trends and UN Comtrade; a factory model derived from station cycle times; and the HTML reports built from both. |

`research/` came first and is what moved the thesis: it started on configurable furniture sold
direct to consumers and measured its way to fitted kitchen cabinets, which was the only one of
24 categories where search carried commercial intent. Its findings enter the lab as ledger
entries in `reports/custom-kitchen-cabinets/03-validation/evidence.md`, graded as what they
are — desk measurement, not buyer evidence. See `research/README.md` for how to run it.

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
- The plan the outreach is testing: `research/reports/cabinet-plan-final.html`
- What to do in what order, with costs: `research/reports/build-board.html`
