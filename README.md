# Microplastic Detection System — Assumption Lab

One company, one idea, tested as a bundle of assumptions. The repo holds the framework
(schemas, methods, generators, skills) and the idea's own state, and nothing else.

**Where it stands (2026-09-09):** reset to a blank slate. No belief is written, no hunch is
active, the assumption graph and evidence ledger do not exist yet. The next move is
`/startup-belief-intake`, which writes `input-context/belief.md` and nothing else; the first
hunch then comes from `/startup-ideate-shotgun` in explore mode, from a real corpus.

## Layout

Code at the root, everything about the idea under `reports/`, raw inputs under `input-context/`.

```
CLAUDE.md  ARCHITECTURE.md  schemas/  methods/  founders/  signals/  .claude/skills/

scripts/              the assumption pipeline — generators, validators, loader
scripts/data/         shared query library (Reddit, HN, news, procurement, LinkedIn export)
cad/                  parametric hardware models for the idea's own apparatus

input-context/        belief.md (the pipeline seed) + dated raw snapshots
reports/
  BRIEF.md            generated session entry point — read this first
  control-room.html   generated: belief → hunch → assumptions → evidence → outreach, one page
  01-ideation/        the hunch lineage
  02-assumptions/     the assumption graph
  03-validation/      the evidence ledger, and interview notes as they land
  04-mutation/        offerings
  outreach/           contacts, companies, and the copy archive as it fills
  pages/              every other readable report, listed in pages.yaml with its status
```

There is no idea folder inside `reports/`. The repo was multi-idea until 2026-09-09; with one
company that layer only added a path segment to every command, so it was removed. Idea
findings never go into a root file or into memory — `CLAUDE.md` says where each kind goes.

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

The assistant reads `reports/BRIEF.md` — a generated digest of the idea's current state — and
loads only the artifacts the task needs.

- **`CLAUDE.md`** — how to behave: what to load, what to write, which skill to use.
- **`ARCHITECTURE.md`** — how it is built: the loop, the modules, the folder layout, the schemas.
- **Open this:** `reports/control-room.html` — the belief, the hunch, the ranked assumptions,
  the evidence, the outreach funnel, and a **Pages** tab linking every other report.

Regenerate after any change to a living artifact:

```bash
.venv/bin/python scripts/build_brief.py
.venv/bin/python scripts/build_control_room.py
```

## Kanban board and Vercel

The **To do** tab is a four-stage Kanban board. Outreach cards are still derived from the
ledger and cannot be edited there. Manual cards live in `data/kanban.json`; every create,
edit, move, or delete made on the hosted board updates that file through `api/tasks.js`,
adds an activity entry, and creates a GitHub commit.

Import this repository into Vercel with `main` as the production branch. `vercel.json`
serves `reports/control-room.html` at `/`; Vercel's Git integration then publishes pushes to
`main` as production deployments and other branches as previews.

Configure these project environment variables in both Production and Preview:

- `GITHUB_TOKEN` — a fine-grained token limited to this repository with **Contents: Read and write**.
- `BOARD_WRITE_KEY` — a long random phrase used to authorize browser writes.
- `GITHUB_OWNER`, `GITHUB_REPO`, `GITHUB_BRANCH` — optional overrides; defaults are already
  set for `iozdas01/Microplastic-Detection-System` on `main`.

Do not put either secret in this repository. Opening the generated HTML directly remains a
read-only view; edits are available only through the hosted API.

## Carried over

`reports/pages/startup-map.html` is a static snapshot of the manufacturing startup scene
from the previous idea, kept as reference. Everything else from that idea lives in git
history before 2026-09-09.
