# CLAUDE.md — Startup Assumption Lab

How to behave in this repo: what to load, what to write, which skill to reach for.
`ARCHITECTURE.md` holds the structure — the loop, the modules, the folder layout, the
schemas, the data layer.

---

## Before Every Session

**One company, one idea.** This repo holds exactly one idea: its state lives in `reports/`
and its raw inputs in `input-context/`, with no idea folder in between. There is no
hand-written "current state" file, on purpose: `reports/BRIEF.md` is generated and is the
only summary. If a `CURRENT.md` ever appears at the root, delete it without reading it.

1. Read `ARCHITECTURE.md`. Sections marked **cold by default** (Folder Structure, the
   firecrawl notes) are skipped at session start and read when their trigger applies.
2. Read `memory/MEMORY.md` — terse founder preferences and process decisions only.
   Machine-local session memory holds per-founder personal habits. Neither carries
   findings about the idea.
3. **Read `reports/BRIEF.md` first.** It is generated from the idea's own files, so it is
   both the cheapest and the freshest statement of the belief, the hunch, the ranked
   assumptions and the outreach position. Then load only the one full artifact the task
   needs — the brief's closing table says which.

   Stale brief? `python3 scripts/build_brief.py`. Never hand-edit a generated file.

   **Before creating ANY new artifact, read the brief's `What already exists for this idea`
   inventory.** It lists every file in the folder with the purpose that file declares about
   itself, so "does something already cover this?" is answerable without a search. If a file
   covers the fact, add to it. Writing a second author for an existing fact is the failure
   the inventory exists to prevent, and it has happened.
4. Read `input-context/` for the raw material staged for the idea.

---

## End of Every Session

1. **Idea state goes inside `reports/` only.** Living artifacts (`hunch-lineage.md`,
   `graph.md`, `evidence.md`, `contacts.md`, `companies.md`, `offerings.md`) update in place;
   dated artifacts are appended, never overwritten. The founder-owned belief is the one
   exception — it is an input at `input-context/belief.md`. Nothing about the idea goes
   into a root-level file or into memory.
2. **`memory/MEMORY.md`: one terse line per genuinely new founder preference or process
   decision** — never findings about the idea. Delete stale lines in the same edit; git
   preserves them. If in doubt, don't write it.
3. **Regenerate what is generated.** After writing to a living artifact:
   `python3 scripts/build_brief.py`, plus
   `python3 scripts/build_control_room.py` when outreach or thesis data changed.
   This is the one author for that instruction — skills do not each restate it.

---

## Single Authorship — NON-NEGOTIABLE

**One fact, one author. Everything you read first is generated from those authors.**

A fact written twice will drift, and the copy read first is usually the stale one.

- **State lives in frontmatter or a `status:` field. Prose is dated past-tense history.**
  Writing "— ACTIVE" in a heading is a bug even when it is momentarily true.
- **Enums are declared once** in `schemas/vocabularies.yaml`, referenced as `vocab:{name}`.
  An undeclared value is either a typo or new vocabulary — decide which, and say so there.
- **Evidence is graded once**, on the ledger entry (`confidence` 1–5). Assumption-level
  strength is derived by the generators; never hand-set it on a node.
- **Never hand-edit a generated file** (`BRIEF.md`, `control-room.html`, `methods/index.md`,
  `results-*.md`). Fix the source, rerun the generator. Generated files say so at the top.
- **Never hand-maintain a summary of data in the same file as that data.**
- **Every living artifact opens with `purpose:`** — one line naming the fact it owns. The
  brief's inventory is generated from those lines.
- **Never explain the method to the founder.** No page, report, generator or skill output
  defines belief, hunch, assumption, evidence grade, or why the process works that way — the
  founder built it. Write findings, data, and the legend a chart needs to be read; delete
  anything that would survive as a sentence about the framework rather than about this idea.
  This applies to writing the prose *and* to reviewing it: a generator paragraph that teaches
  vocabulary is a bug, same as a duplicated fact.

Enforced by `python3 scripts/validate_repo.py --fix-hint`. Set up a clone once with
`scripts/setup.sh` — it creates `.venv` (nothing runs without it), installs the pre-commit
gate, and verifies. Run repo scripts with `.venv/bin/python`.

---

## Shared Ledgers & Push Discipline

The rules below were paid for in the predecessor repo, not this one — they are carried
forward deliberately so they do not have to be relearned. **When two people push in
parallel** (PRs from one side, direct commits to `main` from the other), `main` moves
underneath open branches, and every append-only ledger (`contacts.md` C-ids, `graph.md`
A-ids, `evidence.md` E-ids) gets two sessions allocating the same next-free ID against the
same offset. That was the predecessor's most frequent failure and it cost: `C98-C135`
renumbered to `C101-C138`; three contacts lost inside a 2100-line conflict; two separate
A-id collisions (A5/A6/A7, then A11/A12); and `E48` reassigned to a different claim, so
citations to it still resolved and silently lied.

**Work on `main` by default — founders and Claude sessions alike (founder decision,
2026-08-08).** Do not open a branch per task. Every clean merge in the predecessor's history
had `main` move 0–2 commits underneath the branch; both painful ones had it move far more, so
divergence *time* is the variable, not review. Committing straight to `main` is the limiting
case of a short-lived branch and cannot diverge from itself.

While the team is one person these rules cost nothing to follow and prevent nothing from
happening; they become load-bearing again the moment a second founder starts pushing.

Open a PR only when the work needs something a merge cannot give: a founder decision the
session could not make, or a change big enough to want reverting in one click. Then land it
the same session — an agent branch left open overnight is what produced the A11/A12 collision.

Five rules, ordered by how much each saves:

1. **Pull immediately before you write, and again before you push.** `git pull --rebase`.
   Nearly every collision is an ID allocated against a stale next-free number. Working on
   `main` shortens that window; it does not close it, because you can still read at 9am,
   write for two hours, and push against a two-hour-old base.
2. **`main` wins every ID contest.** Whatever has not reached `main` renumbers itself. Never
   renumber an ID that has landed, and never ask the other side to. This was decided twice
   already; writing it down stops it being re-decided a third time.
3. **A retired ID is burned — never reassign it.** Deleting `E54-E61` is fine. Reusing `E48`
   for a new claim is not: every citation elsewhere still resolves and now points at
   something else. A deleted ID fails loudly; a reused one does not.
4. **Never hand-merge a generated file.** For `BRIEF.md` and `control-room.html`, take either
   side and rerun the generator. Hand-resolving produces a file no generator would emit.
5. **Re-verify citations after any merge that touched a ledger.** For every `E{n}` in the
   files you changed, confirm it still says what you cited it for — not merely that it exists.

When you do have to merge a ledger, merge it at **entry granularity, not as text**: for each
id, take whichever side changed it against the merge base. Two sides appending at the same
offset is not a conflict, it is two additions — resolving that as text is what lost the
three contacts.

Rules 1–3 are enforced by `check_ledger_ids` in `validate_repo.py`, which runs on every
commit through the pre-commit hook. That check, not the review flow, is what actually keeps
these ledgers well-shaped — which is why working on `main` is safe here.

---

## External Strategy Docs

Founder-authored operating docs, whiteboard dumps and landscape maps are **decomposed into
pipeline artifacts on arrival, never kept as living context files** — a monolith mixes
durable belief, mutable hypotheses, evidence and week-lifetime detail, and rots as one.
Durable parts → `belief.md`; hypotheses and kill conditions → `hunch-lineage.md`/`graph.md`;
evidence → `evidence.md`; versioned synthesis → `04-mutation/thesis-v{N}.md`; operational
to-dos → nowhere, they are tasks. The original stays as a dated, immutable snapshot in
`input-context/` only when its raw form has reference value.

Two standing rules:

1. **Grade evidence once.** The founder-label mapping (`[V]`, `[T]`, `[C]`, `[I]`, `[H]`,
   `[U]`) is declared in `schemas/vocabularies.yaml` → `maps.founder_label_to_entry_confidence`.
   `[C]`/`[I]`/`[H]`/`[U]` are not evidence — they become assumptions.
2. **Papers and announcements may kill technical claims; only [T]/[V]-grade buyer or site
   evidence may create or kill a thesis, hunch, or lane.** A full ideation shotgun is for
   hunch changes, not for every pivot discussion.

---

## Gap Capture — `gap:` in any session

**When the founder's message starts with `gap:`, append it to `signals/gaps-log.md` and reply
with one line. Nothing else.** No follow-up questions, no evaluation, no relating it to the
active idea. The method (`methods/practices/background-noticing-process.md`) depends on
capture being frictionless — the moment logging costs more than four seconds it stops
happening.

Format per the spec at the top of that file, `type: founder-ambient`, `unprompted: n/a`,
`status: open`, appended under `## Entries`. If the message says where they were, put it in
`source:`; otherwise `source: (unspecified)` — don't ask.

Reply is literally: `Logged (gaps-log · N entries).`

---

## To-do Capture — `todo:` in any session

**When the founder's message starts with `todo:`, or says to log / add something as a to-do
or put it on the board, log it on the shared kanban board and reply with one line. Nothing
else.** No follow-up questions, no evaluation. The board has one author, `data/kanban.json`
on `main`, and it is written only through git from each founder's own clone — never through
a hosted API (founder decision 2026-09-09).

1. **Whose to-do.** If the message names a founder ("for Sandra", "Izgin should…"), it is
   theirs. Otherwise it belongs to the founder typing — the one this clone's git identity
   names (`founder.md` → `git_identities`; the script resolves it). Never guess a default
   founder; if the clone matches nobody, ask which founder in one line and stop.
2. **Log it.** `.venv/bin/python scripts/add_task.py --title "<their words>"`, adding
   `--owner <first name>` only when the to-do is the other founder's, `--detail` for anything
   that did not fit the title, `--priority high` only if they said so. The script pulls,
   appends the task in the board's own format, commits and pushes, so the other founder's
   board shows it on its next read.
3. **Reply** with the script's one line, literally: `Board: added "<title>" for <Founder>
   (backlog · N open).`

Moving, editing and deleting cards happens on the board itself or by editing
`data/kanban.json` and pushing; a session does neither unless asked.

---

## Routing

**Route from the skill descriptions already in your context** — every `description:` is
injected into every session, so a table here would be a stale second copy. Too vague to route
on? Fix the description.

Only the answers that are **not** a skill need writing down:

| Request | Do this instead |
|---|---|
| Brainstorming / designing architecture | Work inline against `ARCHITECTURE.md`, and say you did |
| Rebuilding the control room | `python3 scripts/build_control_room.py` |
| Browsing hunches → assumptions → evidence | The **Hunches** tab of that same `control-room.html` |
| Opening any other report | The **Pages** tab of `control-room.html`, which lists everything in `reports/pages/` with its status. Never build a second dashboard — there is exactly one generated control room |
| Refreshing the session brief | `python3 scripts/build_brief.py` |
| Rebuilding the methods index | `python3 scripts/build_methods_index.py` |
| Shared Reddit/HN problem reconnaissance | `scripts.data.community_recon` directly — or `/startup-ideate-shotgun` for the full workflow |
| Mining news / procurement / hiring / grants for one assumption | The relevant `scripts/data/*` CLI — or `/startup-outreach-intel` |

**Methods are lenses, not a checklist.** `methods/ideation/` is the shotgun's pool; every
other folder's cards carry an `excluded_because:` saying why they cannot be shotgun-run.
No belief → `/startup-belief-intake`, which writes the belief and nothing else — it never
authors a hunch, and neither do you. Belief but no hunch → `/startup-ideate-shotgun` in
explore mode, which proposes candidates from a corpus. Confirmed H1 → the same skill in
initial-test mode. Interview evidence that moves the segment or root cause → reframe mode
with the explicit delta. One "why now" assumption → apply that method or validation skill
directly; do not invoke the shotgun.

---

## Skills

**Absorption.** When the founder asks for something manually that a skill could own, ask:
*"want me to do it manually now AND bake it into `/skill-name`, or just manually?"* If yes,
update the SKILL.md in the same session. Skills should get smarter every time a gap shows up.

**Creation.** Use `skill-creator` — never write a SKILL.md by hand. Skills get written when
the workflow makes them obvious, not upfront.

**The contract.** Every `SKILL.md`: **≤200 lines** (trigger, decision procedure, guardrails,
handoff — mechanics go to `references/`), **zero idea state** (no dated ledgers, no contact
IDs, no idea or company names — the framework must survive the next pivot), **zero founder names** (write "the founder"; per-founder facts live in
`founders/*.md`), **zero absolute paths outside the repo**, and a **`description:` true on its
own** — it is the only part read before routing.

**Testing.** Do not run eval agents for skills that call an external API; without credentials
the eval burns budget for zero signal. Evals are for organic skills only (reasoning + file I/O
+ web search).

**Validation.** `python3 scripts/validate_skill_catalog.py` — frontmatter, kebab-case names
matching directories, resolving `.agents/skills/` bridges, and the whole contract above.

---
