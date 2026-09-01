# Batch format — research-map rows and bookkeeping

Read before writing the first row of a batch. The row template is second; the bookkeeping is
first because it is the part that gets skipped and the part that makes the next batch possible.

## Frontmatter bookkeeping

The map's frontmatter carries one counter set per batch, plus the window that batch actually
covered:

```yaml
batch: {N}
batch_{N}_scanned: {int}        # what the scan returned
batch_{N}_on_axis: {int}        # scored at or above the keyword threshold
batch_{N}_classified: {int}     # rows written
batch_{N}_window: "{YYYY-MM-DD} to {YYYY-MM-DD}"   # the REAL date range, not --since
shortlist: research-map-shortlist.csv
axes:                           # THIS idea's classification axes — see below
  {axis_name}:
    means: "What this axis records about a paper's method."
    values:
      {value}: "What this value means."
```

### `axes:` — the one author of what this idea classifies on

Declared here, in the map, and nowhere else. The axes that separate a good paper from a
useless one are a property of the market being tested, not of the pipeline: a set that fits
one idea reads as noise in the next, so putting them in `schemas/vocabularies.yaml` would be
per-idea state parked in a shared file.

Pick three to six axes, and hold each to one test: **could two honest readers of the same
paper disagree about which value applies?** If yes, the values are too vague to argue with
and the column will fill up with the classifier's mood. Every axis records *revealed method* —
what the team actually did — never what the abstract claims they were aiming at.

An axis is added or a value is added by editing this block first, then using it. A value that
appears in a row but not in `axes:` is either a typo or an undeclared axis value; both are
bugs, and both are caught by reading `axes:` before the batch rather than after it.

`batch_{N}_window` is the field that keeps the map honest. `--max` caps results and arXiv
returns newest first, so a large cap on a busy category yields a slice measured in days no
matter what `--since` says. Write the range the scan actually covered, and when it does not
reach the previous batch's window, say so in the `method_note:` — an unscanned gap between
batches is invisible otherwise, and a later reader will take the map for complete coverage.

Update `last_updated:` and `batch:` in the same edit. Leave earlier batches' counters alone;
they are history, and rewriting them destroys the yield trend that tells you whether the scan
is drifting off-axis.

## Row template

One `##` heading per paper, `{arxiv_id} — {short name}`. Fields, in this order:

```yaml
canonical_name: {org, or "(multi-institution)"}
paper_date: {YYYY-MM-DD}
{axis}: {a value declared for that axis in the map's `axes:` block}
  # …one line per axis in `axes:`, in the order declared there
{axis}_detail: >
  The decisive quantity behind the axis value, and what it is worth outside the setting
  it was measured in. Write this for the one or two axes the batch actually turns on.
bottleneck_named: "The team's own words for what blocked them."
{door}_reading: {a value per the map's method_note}
{door}_detail: >
  Why the method supports or contradicts that door, with the number that decides it.
outreach_status: {vocab}
outreach_note: "Why this is or is not a target."
published_emails: [addresses mined from the source package, or []]
source_url: {arxiv abs URL, or the project page when it is the better landing}
```

Only fields that carry something go in. An empty `{door}_detail` is worse than an absent one —
it reads as "examined and found neutral" when nothing was examined.

## What a good detail field looks like

The difference between a row that can be argued with and one that cannot:

**Weak:** "Uses very little real-world data, suggesting real data may not be the bottleneck."

**Strong:** "Under 20 min of real data PER TASK for cable insertion and soldering. Two tasks,
one line, one factory the team owns; no carry to another site claimed or tested. The batch's
decisive number: a quantity you capture during commissioning, not one you procure."

The second names the quantity, its scope, and what it implies for the claim under test. The
first could be written without reading the paper.

## Recording what a row does not show

Where the over-read is obvious, write the limit into the row. A paper that needs real data is
not a paper that buys real data; a paper that transfers across objects is not a paper that
transfers across sites. These conflations are the most common way a research map ends up
asserting more than its rows support, and one clause prevents each.

## Retired rows

When a row is dropped for having no contactable address, its finding goes to
`03-validation/evidence.md` first if it carries one — the paper as `source`, the reading as
`verdict`, the next free entry id. Note in the batch's `method_note:` how many rows were
dropped and how many were promoted to evidence. The shortlist CSV still holds every id, so a
dropped row is recoverable; an unrecorded finding is not.
