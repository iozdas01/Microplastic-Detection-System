# Tier Inference — mapping API responses to the assumption's tiers

Every discovered company must be assigned a tier drawn from the assumption's `icp_valid_tiers`. Tier assignment is the highest-consequence decision the discovery phase makes — a wrong tier sends the outreach skill searching LinkedIn for the wrong roles at the right company, wasting weeks.

**Tiers are idea-defined, never hardcoded.** Each assumption declares its own tier vocabulary in `icp_valid_tiers`, and every tier is tagged with a structural **side**:

```yaml
icp_valid_tiers:
  - {name: <who pays>,      side: demand}
  - {name: <who is paid>,   side: supply}
  - {name: <who else>,      side: supply}
```

The tier *names* are whatever fits the vertical. The only thing inference routes on is the **side** — which is domain-neutral and universal.

The core principle: **tier assignment is derived from the role the API returned the company in, not from the company's identity in isolation.** The same company can appear demand-side in one query and supply-side in another — because in each context it plays a different role. Log both, prefer the strongest.

---

## The universal role → side mapping

Every discovery API returns companies playing one of these roles. The role maps to a **side**, which is domain-neutral:

| Role in API response | Universal meaning | Side |
|---|---|---|
| Contracting authority (procurement) | The entity paying for the work | demand |
| Supplier / winner (procurement) | The entity doing the work | supply |
| Operator (asset database) | The entity operating the asset | demand (owns operational pain) |
| Owner (asset database) | The financial owner of the asset | demand (owns economic pain) |
| Developer (asset database) | The entity that built the asset | supply (often a vendor) |
| Filer (SEC EDGAR) | The entity making the disclosure | depends on excerpt — see below |
| Grant recipient (SBIR / CORDIS) | The entity building new capability | supply (usually a competitor) |
| Employer (hiring API) | The entity hiring | depends on role type — see below |

Your job: resolve the role to a **side**, then pick the assumption's tier on that side.

---

## The mapping procedure

For each discovered company + role pairing:

### Step 1 — Identify the side

Use the universal table above. This is a domain-neutral judgment: the entity paying is demand-side, the entity being paid is supply-side.

### Step 2 — Pick the assumption's tier for that side

Read `icp_valid_tiers` from the assumption node. Each tier carries a `side`. Pick the tier whose side matches — **the first tier the founder listed on that side is the default** (declaration order is priority).

- Role is demand-side → use the first `side: demand` tier in the whitelist.
- Role is supply-side → use the first `side: supply` tier in the whitelist.
- If the whitelist has no tier on the resolved side → the company is off-scope for this assumption; drop it (unless it fits the competitor bucket below).

If the whitelist has multiple tiers on the same side and you can disambiguate (the API's role name is specific, or a secondary signal resolves it), prefer the more specific match; otherwise use the first-declared one.

### Step 3 — Validate with a secondary signal

Before finalizing, cross-check the side with at least one secondary signal if available:

- **Industry classification codes** (e.g. Companies House SIC, GLEIF industry code) — confirm the company's sector matches the demand/supply role you assigned.
- **Website domain in the API response** — a well-known operator vs. a well-known vendor resolves ambiguity.

If the secondary signal contradicts the primary role, log the conflict to the manifest and default to the role-based assignment. Do not silently override.

### Step 4 — Handle the "both sides" case

Some companies appear on both sides of the market (e.g. a manufacturer that also operates its own assets, or an operator that also sells services). 

Rule: assign the tier under which the company appeared in the *current* API response. If it appears as a `supplier` in a procurement contract, use the supply-side tier; if it appears as an `operator` in an asset database, use the demand-side tier.

If the same canonical company (post GLEIF dedup) appears with different sides across APIs, keep the strongest tier for the assumption's `icp_valid_tiers`, and record the alternatives in `also_seen_as` in the companies.md row:

```yaml
company: "Example Holdings A/S"
tier: <supply tier>                  # strongest role for this assumption's ICP (supply)
also_seen_as: [<demand tier>]        # noted for future assumptions (demand)
rationale: >
  Supplier on 4 procurement contracts in the last 24 months → supply-side tier.
  Also appears in an asset database as an operator (demand-side) — not the
  primary role for this assumption.
```

---

## Hiring-API tier inference from job titles

A hiring API returns companies by the job they're hiring for, not by contract role. Assign the side by comparing the posted titles against the assumption's `icp_valid_titles` and `icp_segment`:

- Titles describing operating/owning the asset or workflow → demand-side.
- Titles describing doing the work for hire, or selling into the space → supply-side.
- Senior leadership titles (VP / Director / Head of X for the domain) → side depends on the employer's identity, not the title alone.
- Procurement / category-manager titles → demand-side.
- Product / sales-engineer titles → supply-side (usually a vendor).

**When ambiguous:** if the job title alone doesn't disambiguate, look at salary band, location (corporate HQ vs. site-based), and the full JD (mentions of "our fleet"/"our sites" imply demand-side ownership). If still ambiguous, tier = `other` and surface for founder review. Do NOT guess.

---

## Grant recipients — the competitor default

Grant recipients (SBIR / CORDIS) are almost always building something new in the space. They are usually named competitors, occasionally incumbents.

**Default:** treat as `competitor` (a side of its own — captured separately from the outreach registry).

**Handling:**
- If a `competitor` tier is in `icp_valid_tiers` → add to `companies.md` with that tier.
- Otherwise → add to `.competitors-detected.md` (a separate file) for founder review. Do NOT add to the outreach registry — you don't want to accidentally outreach competitors when the assumption is testing demand.

Log every grant recipient with the decision made:

```jsonl
{"phase": "tier_infer", "company": "Example Robotics Inc",
 "role": "grant_recipient", "api": "sbir",
 "decision": "surface_for_review", "would_be_side": "competitor",
 "reason": "no competitor tier in icp_valid_tiers for A2"}
```

---

## EDGAR filers — read the excerpt

EDGAR full-text search returns companies whose filings mention the keywords. The company is a filer, but the ROLE they play depends entirely on the excerpt content:

- Excerpt discusses the pain as a cost they bear ("we incurred $X in …") → **demand-side**.
- Excerpt discusses the pain as a service they provide ("we offer … services") → **supply-side**.
- Excerpt discusses the pain as a risk to a competitor ("competitors face rising … costs") → the filer is likely a supplier/competitor; the filing still helps validate that demand exists.

Because the excerpt requires semantic judgment, the library does NOT auto-assign the side for EDGAR results. `intel_lib.query_edgar_fulltext()` returns the excerpt in the response dict; read it to decide the side, then pick the assumption's tier on that side. Log the decision:

```jsonl
{"phase": "tier_infer", "company": "Example Energy Inc",
 "role": "edgar_filer", "excerpt": "our operations incurred $47M in unscheduled repairs...",
 "decision_side": "demand", "decision_tier": "<the demand tier>",
 "reason": "excerpt shows filer bears the pain as an operating cost"}
```

---

## When to drop a company entirely

Drop the company from this assumption's discovery pass if:
- Its resolved side has no matching tier in `icp_valid_tiers` AND it doesn't fit the competitor bucket.
- Its role or company name matches an entry in `icp_out_of_scope`.
- It's a subsidiary of a company already added (GLEIF parent resolution handles this in Phase 1.4).
- It's a shell entity with no operational fingerprint (dissolved or dormant status).

Log every drop to the manifest with the reason. Drops are not failures — they're evidence the filter is working.

---

## Anti-patterns

**Do not assign a tier from the company name alone.** A generic-sounding company could be an operator, a vendor, a service provider, or a consultancy. Always assign from the role in the API response.

**Do not use a tier name that isn't in `icp_valid_tiers`.** The whitelist is the founder's declared contract — respect it. The only exceptions are `competitor`/`other`, which are captured separately.

**Do not silently keep the first assignment when a later API contradicts it.** Log the conflict, prefer the strongest signal for the assumption's ICP, note the alternative in `also_seen_as`.

**Do not use model knowledge to assign the side.** "I know this company is an operator" is not evidence — the API record IS evidence. If no API returned them in that role for this assumption, don't assign it just because you know it's true. Wait for the evidence.
