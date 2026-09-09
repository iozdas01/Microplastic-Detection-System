---
name: startup-paper-mine
description: >-
  Turns recent research papers into research-map rows and contactable outreach targets for one idea. Scans arXiv on a brownfield-axis keyword score, classifies each paper's METHOD against the map's declared axes, mines author-published emails out of the paper's own source package, and routes the emailable ones into an email campaign. Use whenever the founder asks for a new batch of papers, wants more researchers to write to, asks who else is worth emailing, says the paper strategy is working and wants more, or wants an existing research map cleaned up or re-mined for addresses. Also use when a research-map row has no contactable address — an unreachable row is the failure this skill exists to prevent. Not for validating one assumption against the literature; that is a targeted reading task, not a batch.
---

# Startup Paper Mine

Papers are the one outreach source where the target hands you their reasoning before you
write. A row in `outreach/research-map.md` records what a paper's **method** reveals about
where a team works and where its training data comes from — revealed behaviour, not stated
intent — and the author-published address makes that team reachable.

**The failure this skill exists to prevent:** a batch that classifies well and reaches nobody.
The first run of this workflow produced ten rows and eight had no address, because scanning
and email-mining were separate steps and only the first one ran. A row you cannot write to is
research, not outreach. Mine the address in the same pass that writes the row.

## Prerequisites

- `reports/outreach/research-map.md` — created on first run if absent
- **The axes are per-idea and the map declares them.** `axes:` in the map's own frontmatter
  is the one author of what this idea classifies papers on and which values each axis accepts
  (see `references/batch-format.md`). Nothing about a vertical is declared globally: an axis
  set that fits one idea's market is noise in the next one's, so a global enum here would be
  per-idea state in a shared file.
- The door/reading fields are likewise per-idea. Read the map's own `method_note:` for which
  doors this idea splits evidence across before classifying anything.
- Read the whole `axes:` block before the first row. An undeclared value is a typo or a new
  axis value — decide which, and add it to `axes:` with what it means before using it.

## The four passes

### Pass 1 — Scan

```bash
python -m scripts.data.arxiv --since {YYYY-MM-DD} --max 400 \
  --shortlist reports/outreach/research-map-shortlist.csv \
  --exclude-map reports/outreach/research-map.md
```

`--exclude-map` drops papers already classified, so batches resume instead of re-reading.
`--shortlist` persists the full ranked on-axis list; without it a batch keeps only its counts
and the next batch cannot resume — which already cost one batch's 211 on-axis papers.

**Check the window you actually got.** `--max` caps results, and arXiv returns newest first,
so a 400-cap on a busy category is a ~10-day slice regardless of `--since`. Record the real
date range in the map's frontmatter. Claiming a year and delivering ten days is how a gap
becomes invisible.

### Pass 2 — Mine addresses BEFORE classifying

```bash
python -m scripts.data.arxiv --emails 2607.29231,2608.04196,...
```

Reads each paper's arXiv source package and returns only addresses the authors themselves
published in it. Nothing is guessed from a name and a domain and no enrichment provider is
called — a mined address is one the author chose to publish, which is what makes cold contact
on it defensible.

Mining first is deliberate: classification is the expensive part, and a paper nobody can be
reached at earns that spend only if its finding is worth logging on its own. Sort the
shortlist by "has an address" and start there.

An empty result means either the authors published no address or the fetch failed. The script
retries truncated downloads and reports failures in `errors` — treat a non-empty `errors` as
unknown, not as absent, and re-run those ids before concluding anything.

### Pass 3 — Classify from the method

One row per paper. Read what the team DID, not what the abstract promises. The axes ask where
the work ran, where its data came from, how much real data, whether it transfers off the site,
and how much integration labour appears — all answerable from the method section.

Two habits carry most of the value:

- **Record the decisive number.** "Under 20 minutes of real data per task" is what kills or
  saves a data-purchase claim; "uses little real data" is not. A row without a quantity cannot
  be argued with later.
- **A contradicting paper is a better target than a confirming one.** The team arguing your
  assumption is wrong has thought hardest about it and will say so in a reply.

Write what the row does NOT show whenever the over-read is obvious — a paper needing real data
is not a paper buying real data, and conflating those is the most common way this map lies.

### Pass 4 — Route the reachable ones

Emailable rows go to the idea's email campaign (`outreach/email/{campaign}/targets.csv` plus
its log), carrying the paper URL as the grounding source so the draft can quote the team's own
finding. Set `outreach_status` from the map's declared vocabulary, and screen against
`companies.md` first — a vendor validating in its own factory is a control case, not a lead.

## Rows with no address

Do not leave them sitting in the map as permanent noise, and do not silently delete them
either — several will be the batch's strongest disconfirmation.

Decide per row:

- **The finding matters** → log it in `03-validation/evidence.md` as a proper entry with its
  verdict and the paper as `source`, then drop the row. The evidence survives where evidence
  belongs and the map stays a list of people you can reach.
- **The finding is redundant** with a row you already have → drop it, and say in the batch
  note how many went this way. A count is enough; the shortlist still holds the ids.

Either way the map should end a run with every remaining row reachable. Report the yield
plainly — "N classified, M with addresses" — because a falling ratio is the signal that the
scan is drifting off-axis, and it is invisible if only the total is reported.

## Guardrails

- **The founder sends every message.** This skill writes rows and drafts; it never sends.
- **Papers may kill a technical claim; only buyer or site evidence may kill a thesis or
  hunch.** A batch that contradicts a technical premise is a finding, not a pivot.
- **Never hand-edit a generated file.** After writing rows, rerun the brief and control-room
  generators rather than editing their output.
- **Append, never renumber.** Evidence entries added here take the next free id. If the ledger
  moved underneath the run, the side that has not reached `main` renumbers — see CLAUDE.md.

## Mechanics

Per-batch bookkeeping, the frontmatter counter fields, and the row template live in
`references/batch-format.md`. Read it before writing the first row of a batch.
