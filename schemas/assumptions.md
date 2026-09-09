# Schema: Assumption Graph

One file per idea. Structured as a DAG — parent assumptions gate their children.
Test root nodes before children. Never validate technical assumptions before confirming pain.

```yaml
idea: Example idea                # the idea name — links back to input-context/belief.md
hunch_id: H1                      # founder-confirmed active hunch(es) this DAG decomposes.
                                  # A list when two hunches run in parallel (vocab:hunch_status).
belief_file: input-context/example-idea/belief.md
last_updated:
active_assumption:                # the ID currently being tested — usually the START HERE

assumptions:
  - id: A1
    assumption: ""
    hunch:                        # which hunch this node belongs to: an H-ID, `shared`
                                  # (serves every live hunch), or a superseded H-ID kept
                                  # for history. Drives the grouped dashboard view.
    category:                     # market / pain / buyer / timing / technical / trust / distribution / competition / founder-market-fit
    lens:                         # desirability / viability / feasibility  (DVF three-lens sweep)
    validation_track:             # customer_adoption | strategic_partnership | investor_thesis
                                  # customer_adoption = will they use and pay for it
                                  # strategic_partnership = will they co-develop, co-invest, or co-distribute
                                  # investor_thesis = will financial/VC investors fund this bet
    why_it_matters: ""
    importance:                   # low / medium / high     (2×2 Y-axis)
    # Evidence strength is NOT authored here. The generators derive it per node
    # from the ledger's linked entries (scripts/idea.py derive_assumption_evidence):
    # best entry grade, entry count, verdict counts, and a low/medium/high
    # confidence (best ≤2 → low, =3 → medium, ≥4 → high). Hand-set
    # evidence_quality/confidence fields are rejected by validate_repo.py.
    quadrant:                     # leap_of_faith / known_important / uncertain_minor / ignore
    uncertainty_score:            # 1–5  (populate only if quadrant = leap_of_faith)
    kill_power:                   # 1–5
    test_cost:                    # 1–5  (use the proxy cost if you're testing via a proxy)
    parent_assumptions: []        # IDs — if these fail, this assumption dissolves
    child_assumptions: []         # IDs — don't test these until this is confirmed
    evidence_for: []              # brief refs — full entries in /reports/03-validation/evidence.md
    evidence_against: []
    status:                       # untested / testing / weakly_supported / confirmed / contested / killed
    next_action: ""               # cheapest concrete test (or proxy) to get a verdict
    disconfirmation: ""           # WHAT WOULD FALSIFY THIS. Observable outcome that constitutes rejection.
                                  # Must be measurable and time-bound. Example:
                                  # "If fewer than 2 of 10 cold outreach attempts yield a discovery meeting,
                                  # reject this GTM hypothesis."
    stop_rule: ""                 # WHEN TO QUIT. Resource cap after which we declare inconclusive and move on.
                                  # Example: "Stop after 10 cold calls or 4 weeks, whichever comes first."

    # ─── ICP declaration (MANDATORY for any assumption that will be tested via customer conversations) ───
    # Purpose: force the filter used by startup:outreach-targets to derive its ICP from
    # this assumption's specific claim, NOT from a hardcoded list I chose ad-hoc.
    # If these fields are missing, outreach-targets refuses to add any contacts for
    # this assumption — the human must fill them in first.
    icp_segment: ""               # One-line description of the population whose behavior
                                  # this assumption claims something about.
                                  # Example for A2: "Operators + service firms in the target
                                  # vertical whose P&L directly includes the recurring cost
                                  # this idea removes."
    icp_valid_tiers: []           # The tier vocabulary for THIS idea — declared here,
                                  # never hardcoded in code. Each tier is {name, side}
                                  # where side ∈ demand | supply | competitor | expert.
                                  # `name` is whatever fits your market (fully idea-defined);
                                  # `side` is the only thing the pipeline routes on.
                                  # List each side in priority order (first = that side's default).
                                  # Shape (names below are illustrative only —
                                  # derive yours from the idea's own market):
                                  #   - {name: <who pays>,      side: demand}
                                  #   - {name: <who is paid>,   side: supply}
                                  #   - {name: <who else>,      side: supply}
                                  # (omit pure sellers if they aren't payers of the pain)
    domain_data_sources: []       # OPT-IN vertical data sources for this idea (default:
                                  # none, and NO adapter is currently registered — see
                                  # api-registry.yaml's domain-specific section). Decoupled
                                  # from tier names: a source fires only if named here.
    icp_valid_titles: []          # Role titles that qualify — used as OR-match against
                                  # candidate headline. Not exhaustive; the filter should
                                  # accept variants (e.g. "Head of Ops" matches "Head of
                                  # Operations").
                                  # Example for A2: [Head of Operations, VP Operations,
                                  # Asset Manager, Portfolio Director,
                                  # Head of Service, Reliability Engineer,
                                  # Operations Director]
    icp_out_of_scope: []          # Explicit REJECTS. Any candidate whose company/industry
                                  # matches an entry here is dropped no matter what.
                                  # Example for A2:
                                  #   - "tool/hardware vendors (feasibility side,
                                  #      not demand — that's a different assumption)"
                                  #   - "adjacent-industry automation (wrong buyer)"
                                  #   - "component vendors (they're the SELLER not the payer;
                                  #     but ex-employees who left the vendor
                                  #     may qualify as expert)"
                                  #   - "any unrelated industry outside the target vertical"
```

**Status lifecycle:**
- `untested` — no evidence collected yet
- `testing` — active investigation in flight
- `weakly_supported` — evidence leans true but is not decisive
- `confirmed` — strong, corroborated evidence
- `contested` — evidence points both ways, or new evidence contradicts a previously
  confirmed claim. Contested assumptions rejoin the ranking pool.
- `killed` — decisive evidence against

---

## Mandatory foundations (always A1 / A2 / A3a / A3b / A3c)

Every idea must extract these unless already confirmed:

1. **A1 — Why Now** (Feasibility / timing) — what specifically changed in the last 12–36
   months that makes this possible or necessary now? Name the threshold, not a trend.
2. **A2 — Pain is real and expensive** (Desirability / pain) — do target users actively
   suffer, and does that suffering cost them enough to pay for a fix?
3. **A3a — Technical FMF** (Feasibility / team) — does this team have the domain depth to
   build the technical core (engineering capability, relevant prior work, understanding of
   the hardest sub-component)?
4. **A3b — Commercial FMF** (Feasibility / team) — does this team have the sales instincts
   and process to close deals in this market (enterprise vs. SMB, government procurement,
   consultative vs. transactional)?
5. **A3c — Relationship FMF** (Feasibility / team) — does this team have existing buyer
   relationships or a credible path to the first 5 conversations without cold outreach
   from scratch?

A3a/b/c are separate because they can have different answers. A team may have deep
technical FMF (A3a confirmed) but no commercial FMF (A3b untested or weak) — that's a
hiring gap, not a company-level kill. Treat them as siblings with no parent/child
relationship between them.

---

## The three-lens sweep (DVF)

Every assumption belongs to one of three lenses. Use the forcing prompt on each:

> **"For this idea to succeed on [lens], what must be true about ___?"**

- **Desirability** — do target users want this enough to change behavior?
  (pain, buyer, switching cost, solution shape, buyer language)
- **Viability** — can this be a durable business?
  (market size, WTP, distribution, competition, defensibility, unit economics)
- **Feasibility** — can this be delivered here-and-now?
  (technology, timing, team, regulation/trust)

Aim for 4–8 assumptions per lens. Fewer than 3 in any lens means you missed something.

---

## The Leap-of-Faith 2×2

Every assumption sits in a 2×2 grid: **importance (Y)** × **uncertainty (X)**.

```
                       HIGH IMPORTANCE
                              │
   Known & Important          │       ★ LEAP OF FAITH ★
   (monitor / verify)         │       (TEST THESE FIRST)
                              │
   ───────────────────────────┼──────────────────────────
                              │
   Ignore                     │       Uncertain & Minor
                              │       (defer)
                              │
                       LOW IMPORTANCE
      ← LOW UNCERTAINTY                       HIGH UNCERTAINTY →
```

Only Leap-of-Faith assumptions (top-right) enter the ranking pool. Everything else is
monitored, deferred, or ignored.

---

## Ranking within Leap of Faith (lexicographic — no arithmetic)

Score each Leap-of-Faith assumption on three 1–5 dimensions:
- `kill_power` (1–5) — 5 = if false, the whole idea dissolves; 1 = minor pivot
- `uncertainty_score` (1–5) — 5 = total guess; 1 = essentially proven
- `test_cost` (1–5) — 5 = years + capital; 1 = one afternoon of desk research. Use the
  *proxy* cost if you chose a proxy test (LOI vs. actual sale, bench spike vs. full
  prototype). Otherwise the ordering systematically deprioritizes the riskiest
  assumptions in capital-intensive ideas.

Rank by lexicographic ordering — apply the criteria in sequence, stopping at the first
one that decides:

1. **Gate:** must be in the Leap of Faith quadrant, and unsettled. Everything else exits here.
2. **DAG position:** roots test before their unconfirmed children — no exceptions.
3. **kill_power tier:** higher first.
4. **uncertainty tier:** higher first.
5. **test_cost tie-break:** cheaper first.

> **The implementation is authoritative for the ordering itself:**
> `scripts/build_brief.py` → `rank_assumptions()`, which every `BRIEF.md` runs. The five
> steps above are here for the *reasoning* — why these criteria, in this order, rather than
> a formula — because that is what a schema is for and it exists nowhere else. If the list
> and the function ever disagree, the function is what actually ranked your assumptions;
> fix whichever is wrong, and do not resolve it by editing only this file.
>
> This ordering went unexecuted from the day it was written until 2026-08-07, so "top 3"
> meant whatever each session judged. That is the failure mode a written-down procedure
> with no implementation always has.

No `u × k ÷ c` ratio, no computed priority number, no ~20% tie window. The scores are LLM
judgments — they wobble by a point between runs, and a ratio propagates that noise
straight into the ranking. A dominance ordering lets the strongest criterion (kill_power)
absorb wobble in the weaker ones. The scored fields still matter as the **interface for
human override**: disagree with a specific score, re-run the ordering.

Note: `importance` is the 2×2 quadrant filter, not a ranking input. `importance` and
`kill_power` measure the same underlying dimension at different resolutions (coarse gate
vs. fine rank) — score them consistently. An `importance: high` assumption should not
receive `kill_power: 1`.

**DAG override.** Never rank a child assumption above its unconfirmed parent — the child's
score is meaningless until the parent is confirmed. Root nodes (no unconfirmed parent)
always test first. The `active_assumption` at the top of the file must be a
Leap-of-Faith root node.

---

## Evidence strength — derived, never authored

There is ONE hand-assigned evidence grade in the repo: the per-entry `confidence`
1–5 in the evidence ledger (`vocab:evidence_confidence`). Assumption-level strength
is computed from the linked entries by `scripts/idea.py` and rendered in BRIEF.md
and the dashboard as `best/5 · N entries (supports+/contradicts-)`, with
`confidence` low (best ≤2), medium (=3), or high (≥4).

Grade the entry once, when it is logged; never re-judge strength at the assumption.
Three parallel ladders used to exist for this and drifted — that is why the node
carries no strength fields at all.

---

## Disconfirmation and stop rules

Every Leap-of-Faith assumption must have both fields filled before testing begins.

**`disconfirmation`** — the observable outcome that constitutes REJECTION.
- Must name a specific threshold, not a vague feeling.
- Bad: "If people don't seem interested."
- Good: "If fewer than 2 of 10 cold outreach attempts result in a discovery meeting within
  4 weeks, reject this GTM hypothesis."

**`stop_rule`** — the resource cap after which you declare "inconclusive" and move on.
- Name a time cap, spend cap, or interview count.
- Example: "Stop after 10 cold calls or 4 weeks, whichever comes first."
- Without a stop rule, testing continues indefinitely. An inconclusive result after
  hitting the stop rule is information — it means the assumption resists cheap testing
  and the proxy may not be valid. Redesign the test, or accept the cost of a more
  expensive method.
