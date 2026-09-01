# WARP.md — Warp agent entry point

Warp auto-detects this file at the repo root and loads it as a project rule. It deliberately
authors **no** behavior of its own: this repo's rule is *one fact, one author*, so duplicating
the contract here would create a second author that drifts. Instead:

**Before doing anything in this repo, read — in this order — and follow them as written:**

1. `CLAUDE.md` — how to behave: what to load each session, what to write, which skill to reach
   for, the single-authorship rules, the `main`-branch + pull-rebase push discipline, and the
   `gap:` capture protocol. This is the behavior contract; it applies to any agent, Warp included.
2. `ARCHITECTURE.md` — how it is built: the loop, the five modules, the folder layout, the schemas.
3. `reports/{slug}/BRIEF.md` for the idea named in the request — the generated, freshest digest.
   Load it first, then load only the one full artifact the task needs (pointers at the brief's end).

**Warp-specific setup notes**

- Skills live in `.claude/skills/` (14 of them). Warp does not import them as slash-commands, but
  its agent can read a skill's `SKILL.md` and follow it directly, or run the `scripts/*` CLIs.
- Warp does not inherit Claude Code's MCP config. Configure any MCP servers you need in Warp's
  settings; none are required to run the core pipeline.
- Generated files (`BRIEF.md`, `control-room.html`, `methods/index.md`, `results-*.md`) are never
  hand-edited — fix the source and rerun the generator named at the top of the file.
- Run `scripts/setup.sh` once per clone: it creates `.venv`, installs dependencies and the git
  hooks, and verifies. Repo scripts then run as `.venv/bin/python scripts/...`.
- `scripts/validate_repo.py` must pass before every commit; the pre-commit hook enforces it.
