# Public Signal Stage

Read this reference for shotgun steps 2–3a. The run subject is the exact belief
and active hunch copied into `context-manifest.json`.

## Run the registered sources

Read `methods/ideation/public-signal-reconnaissance.md` and
`api-registry.yaml`. Use enabled, available sources assigned to
`startup:ideate-shotgun`, respecting credentials, rate limits, costs, and cache
policies. Run the Reddit/HN collector when available. Use Adzuna, reviews,
filings, procurement, professional posts, or another registered source only for
a named evidence gap.

For Reddit, use self-hosted Firecrawl as the primary discovery provider. It
searches the public web with results restricted to Reddit and needs neither a
Reddit API key nor a Firecrawl cloud key. Its local Playwright service extracts
the main post and visible comments when accessible; title and description
remain the fallback. PRAW/OAuth is optional enrichment; Reddit JSON is a last
fallback. Start or inspect the local service with
`scripts/firecrawl-service.sh`.

Record every attempted, skipped, unavailable, empty, and failed source in
`source-status.json`. An unavailable source is never negative evidence.

Build searches from the current hunch:

- problem existence and recurrence for the stated segment;
- workarounds, substitutes, switching, hiring, and spending;
- satisfaction, low urgency, and already-solved counter-queries;
- timing and predecessor evidence tied to the why-now component.

Broader field searches may reveal adjacent evidence, but label it
`out_of_scope_alternative`. For `possible`, `probable`, or `unresolved` SISP,
complete the solution-free search before using solution-shaped vocabulary.

Do not call GDELT during the shotgun. Its repository adapter is company-scoped
and belongs to the later outreach-intel enrichment pass, after target companies
exist. Use Firecrawl/Reddit, Hacker News, and another registered source only
when a named evidence gap requires it.

For Reddit/HN, follow the plan schema in `scripts/data/community_recon.py`:

```json
{
  "belief": "<verbatim>",
  "current_hunch": {
    "id": "H1",
    "statement": "<verbatim canonical statement>"
  },
  "mode": "initial_test",
  "hypotheses": []
}
```

Here `hypotheses` are neutral search facets about components of the one current
hunch; they are not candidate hunches. Copy `belief`, `current_hunch`, and
`mode` directly from the run manifest.

```sh
python -m scripts.data.community_recon \
  --plan <round-1-query-plan.json> \
  --time-filter year
```

Save stdout as `round-1-corpus.json`. The normalized Reddit records identify
their provider (`firecrawl`, `reddit_oauth`, or `reddit_json`).

## Expand and normalize

Cluster round one by workflow and mechanism, then decide whether round two is
warranted. **Round two is conditional, not automatic.** It tests recurrence,
workaround intensity, switching, named alternatives, and counterevidence for the
same run subject — run it only when round one leaves a gap that could change the
verdict:

- fewer than three independent clusters, or every cluster from one community;
- the strongest cluster is `uncertain` rather than supports or contradicts;
- no counter-query was run, so "already solved" was never tested;
- a hunch component — workaround, plausible buyer, why-now — has zero
  attributable records.

Name the triggering gap in `source-status.json` before collecting. When round one
already answers the run subject, record `round_2: skipped` with the reason. A
second round that re-confirms the first costs a full corpus and moves no verdict.

Normalize all source records into `raw-corpus.json`; write
`pain-clusters.json`, `source-status.json`, and `evidence-matrix.md`. Each
cluster is one of:

- `supports_current_hunch`;
- `contradicts_current_hunch`;
- `uncertain`;
- `out_of_scope_alternative`.

Votes and virality do not establish market size or willingness to pay. Reddit,
LinkedIn, jobs, reviews, public proof, and triangulation are source modes in
this one stage, not separate lens agents.

## Scout gate

**This is a stop, not a status line.** Write the summary below into the shotgun
report and `source-status.json`, present it, and wait for the founder.

The gate exists because the corpus carries most of a run's decision value while
the lens portfolio carries most of its cost. A hunch the recon has already
contradicted should be killed for the price of the recon, not after four lens
agents and a synthesis have written it up. It also puts conditional lenses where
they belong: the founder opts one in here, by name, or the run stays at four.

```text
SCOUT — {slug} · {mode}
Belief: {one-line verbatim}
Hunch under test: {H_ID} — {canonical statement}
Packet: {N} records across {source types, communities, and organizations}
Source limitations: {failures, empty sources, fallbacks}

Evidence against the current hunch:
  {strongest contradiction or missing expected signal}

Evidence for the current hunch:
  {strongest recurring behavioral evidence and source mix}

Belief-level threat: {none seen | exact threat}
Out-of-scope alternatives: {N; do not switch subjects}

Proposed portfolio: the 4 required lenses — five-whys, jtbd-substitute-map,
  segment-wedge-map, why-now-predecessor — in {A} agent tasks, max 3 concurrent,
  then one synthesis agent.
Conditional lenses available (each adds one research agent, none run by default):
  {family: question, for the families whose conditions the corpus actually shows}

Proceed with the 4 required lenses? Or: add {family}, revise the queries and
re-collect, or stop here.
```

Then stop and wait.

State a recommendation with the summary — proceed, stop, or re-collect — and say
why in one line. Recommend **stopping** rather than proceeding when all enabled
sources failed or returned zero usable records, the manifest is inconsistent, the
evidence credibly threatens the belief itself, or the packet already contradicts
the hunch clearly enough that four lenses would only annotate the verdict. A
packet with attributable evidence and some limited sources is a normal proceed —
record the limitations and recommend continuing.

The founder may also ask for the scout alone ("scout this first", "just the
recon"). That is a complete run: the packet, the summary and the report's scout
section are written, and the run ends there with no lineage change.

If the founder is asked to adjust queries and re-collect, reuse the existing
packet metadata and do not silently replace the run subject.

## Resume and freshness

Reuse only a packet whose manifest has the same hunch ID and identical hunch
statement. A stable belief is not enough. Apply each source's TTL from
`api-registry.yaml`, refreshing stale sources while preserving valid records.
If no TTL exists, state the source age and ask before recollecting.

Report:

```text
Found recon packet for {H_ID}: {path} · {N} records · source freshness {status}
Refreshing stale sources: {list or none}. Say "re-collect all" for a fresh packet.
```
