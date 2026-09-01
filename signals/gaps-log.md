# Gaps & Anomalies Log

Standing, cross-idea, append-only. Implements **Background Noticing Process**
(`methods/practices/background-noticing-process.md`) — pre-loop capture of observations
that may become idea seeds. Record what you noticed, one or two lines, **no evaluation**.

Two sources: `founder-ambient` (the founder types `gap: ...` in any session) and
`interview-residue` (a contact raised a pain mapping to no assumption in the graph —
harvested by `startup-interview-capture`; higher review weight because unprompted).

**Never in this file:** findings about any active idea (no assumption IDs, scores, or
grades), and no conclusions — "invoices are reconciled by hand" is an observation,
"there's a business in invoice automation" is not. Interview entries carry a path
pointer to the notes file, not a summary.

Entry format (append under `## Entries`, chronologically):

```markdown
- YYYY-MM-DD — <the observation>
  type: founder-ambient | interview-residue
  source: <where / what doing, or {contact_id} ({role}) · {path to notes}>
  unprompted: yes | no | n/a        # n/a for founder-ambient
  status: open                      # review sets: promoted → belief intake | dismissed (reason)
```

**Review** roughly monthly, not more often than the log grows: cluster by underlying
absence, not surface topic. A cluster with independent sightings starts a new idea via
`/startup-belief-intake`. Entries are never deleted — a dismissed observation that
recurs years later is itself a signal.

---

## Entries

- 2026-08-12 — Automated-warehouse engineer uploads electrical drawings to ChatGPT during faults to get candidate failure lists; says it cuts downtime significantly; wants the same capability hands-free via smart glasses scanning conveyors and panels.
  type: interview-residue
  source: C221 (Automated Warehouse Engineer, glass container manufacturing) · reports/physical-ai-deployment/03-validation/H12A1-2026-08-12/interviews/karl-thomas-2026-08-12-notes.md
  unprompted: yes
  status: open

- 2026-08-25 — Same part, different supplier bar machines differently despite meeting spec; shop president names material consistency as the biggest challenge in the shop.
  type: interview-residue
  source: C56 (President, CNC job shop) · reports/manufacturing-execution-layer/03-validation/H1A2-2026-08-25/interviews/matt-guse-2026-08-25-notes.md
  unprompted: no
  status: open

- 2026-08-25 — Counting customer parts out of tubs is a live bottleneck; barcode system tracks raw material inventory live but extending it to customer parts is still in progress.
  type: interview-residue
  source: C56 (President, CNC job shop) · reports/manufacturing-execution-layer/03-validation/H1A2-2026-08-25/interviews/matt-guse-2026-08-25-notes.md
  unprompted: no
  status: open

- 2026-08-23 — Even on robotized aircraft pre-final assembly lines, ~10% error rate persists, attributed to human interaction with machines, maintenance gaps, and product orientation issues.
  type: interview-residue
  source: C3 (Executive Manufacturing Engineer, aerospace) · reports/manufacturing-execution-layer/03-validation/H1A2-2026-08-23/interviews/akshaya-satish-2026-08-23-notes.md
  unprompted: yes
  status: open

---

## Review history

_(no review passes yet)_
