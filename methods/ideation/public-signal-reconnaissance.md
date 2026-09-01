---
name: Public Signal Reconnaissance
category: market-signal
applicable_at: [ideation, validation]
assumption_categories_it_helps: [pain, buyer, market, competition, distribution]
shotgun_role: pre_lens
shotgun_family: pre_lens
requires: [belief]                 # plus current_hunch in the test modes — see shotgun-routing.yaml
source:
  title: "Internal — consolidated public-signal workflow"
  author: "Izgin Ozdas"
  date: "2026-07-27"
  note: "Consolidates Community Gap Observation, Reddit Pain Thread Mining, LinkedIn Signal Mining, Job Posting Pain Extraction, Public-Proof Workflow, and Pain Signal Triangulation."
---

## Core Insight

Public signals are one evidence pipeline, not six independent ideation lenses.
Communities reveal pain language and workarounds; professional posts attach
roles and companies; job postings show budgeted manual work; reviews and switch
stories expose failed substitutes; procurement, filings, and news show
institutional demand and timing. Each source is biased differently, so the
signal comes from convergence and contradiction across sources—not the volume
inside one channel.

Run this once before interpretive lenses. Its subject is whatever the run manifest
declares for the mode — belief plus active hunch in a test mode, belief plus belief
boundaries in explore mode. Its output is the shared evidence packet every lens reads.
It is orchestration work performed by the main shotgun process, not a parallel
research-agent assignment.

**Why this is the one method that may run without a hunch.** Every other card in the
pool interprets a claim, and a card handed no claim invents one. This card collects:
its output is posts, postings and filings that exist, plus the clusters they fall into.
A cluster with no sources under it is visibly empty rather than plausibly wrong, so the
usual failure cannot hide here.

## Process

1. **Start from the run subject in neutral problem language**, never in product
   categories. Search workflows, incidents, workarounds, costs, delays, and failed
   outcomes.
   - *Test modes:* use the current hunch's exact segment and problem, the belief,
     founder-reported observations, and any solution-free SISP test.
   - *Explore mode:* there is no segment or problem yet, so the frame comes from the
     belief statement and the `## Belief boundaries` in-scope list. Derive search
     language from the WORK those boundaries describe — the roles, artifacts and
     recurring tasks inside them. Do not narrow to one segment to make searching
     easier; picking the segment is the output of this run, not an input to it. If the
     boundaries are too broad to yield search language, that is a finding to report,
     not a gap to fill with a guess.
2. **Run two-round community reconnaissance.** Use
   `scripts.data.community_recon` for Reddit and HN. Round one maps broad pains;
   round two tests recurrence, substitutes, switching, satisfaction with current
   approaches, and counterevidence around at most three clusters.

   **Anchor every HN query in the domain.** A subreddit scopes its queries
   implicitly — "changeover between jobs" inside r/Machinists can only mean one
   thing. HN has no community scoping, so the same query matches all of tech, and
   Algolia degrades unmatched long queries to near-anything. Give each HN-bound
   query at least one word that only the target domain uses ("machining",
   "toolpath", "job shop", "CNC"); treat HN records without a domain anchor as
   noise at clustering time, not as weak signal.
3. **Expand only where the community packet has a named gap:**
   - **Jobs:** Adzuna and company career pages for responsibility verbs, named
     tools, salaries, posting age, and recurring headcount.
   - **Professional voice:** public LinkedIn posts/comments when accessible,
     industry publications, Stack Exchange, and practitioner forums for named
     roles and organizations. Never treat an inaccessible source as negative
     evidence.
   - **Reviews and switching:** G2, Capterra, Trustpilot, comparison posts,
     "[competitor] alternatives," and "switched from" stories.
   - **Institutional evidence:** TED procurement, EDGAR, grants, regulatory
     material, and company news when budget, buyer, or timing evidence is
     missing.
4. **Normalize every record.** Preserve source, URL, date, community or
   organization, stated role when available, verbatim pain language, workaround
   or substitute, budget/hiring behavior, and counterevidence. Do not infer a
   role from an anonymous account or scrape private profile data.
5. **Cluster by workflow and mechanism, not keywords.** Separate the incident,
   underlying workflow, affected role, substitute, and claimed consequence.
   Mark each cluster as supporting, contradicting, uncertain, or outside the
   current hunch. Do not replace the run subject with a more exciting cluster.
6. **Build an evidence matrix for each pain cluster:**

   ```text
   cluster | communities | jobs | professional | reviews/switching |
   institutional | workaround | counterevidence | source limitations
   ```

   Record independent sources and organizations, not raw mention counts.
7. **Interpret source patterns.** Community + jobs suggests operator pain with
   organizational spend. Professional + jobs without community signal may be
   management or compliance pain. Community-only signal may be real but
   unbudgeted. Institutional-only signal may reflect mandates rather than user
   urgency.
8. **Write the shared packet.** Produce `raw-corpus.json`,
   `pain-clusters.json`, and `source-status.json`. Each cluster must show
   support, counterevidence, missing evidence, and the exact source mix.

## Output

For every cluster, include:

- solution-free problem statement;
- affected segment and role;
- verbatim language;
- observed workaround or substitute;
- behavioral evidence such as hiring, switching, building, or spending;
- independent source coverage;
- counterevidence and signs the problem is already solved;
- SISP-test result when applicable;
- relationship to the current hunch: support, contradiction, uncertain, or
  out-of-scope alternative;
- confidence and source limitations.

## Example

A scheduling complaint repeated across Reddit is a candidate signal. Similar
responsibility language in current job postings shows organizations fund humans
to manage it. A review explaining why a buyer abandoned an incumbent identifies
the failed substitute. A professional post from a named operations director
locates the role. The convergence supports a workflow hypothesis; it still does
not establish willingness to pay for a new product.

## Limitations

- Public sources underrepresent defense, regulated enterprise work, senior
  buyers, and problems people cannot discuss openly.
- Communities overrepresent vocal users; LinkedIn is performative; jobs skew
  toward larger employers and lag current conditions; reviews overrepresent
  extremes.
- Source count is a heuristic. Three sources repeating one press release are
  not independent convergence.
- Comments, upvotes, job counts, and search results do not establish market
  size or willingness to pay.
- Absence from an inaccessible or culturally quiet channel is not evidence that
  the pain is absent.

## Connection to the Loop

This is the mandatory pre-lens stage of `startup-ideate-shotgun`. Its shared
packet lets every selected method examine the same belief and active hunch. It
does not consume a parallel-agent slot.
