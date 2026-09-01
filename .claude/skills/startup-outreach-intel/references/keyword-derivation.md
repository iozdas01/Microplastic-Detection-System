# Keyword Derivation — from assumption text to procurement search terms

The procurement APIs (TED EU, UK Contracts Finder), the grants APIs (SBIR, CORDIS), and the filings API (EDGAR) all take keyword queries. The quality of the entire discovery pass depends on picking the right keywords. Bad keywords → wrong companies → wasted LinkedIn searches downstream.

This file is the protocol Claude follows to extract those keywords from the assumption node. The
**method** is universal — there are no industry lookup tables anywhere in it, and nothing is
carried between runs. What changes per assumption is the input.

The three worked examples below are from three different verticals on purpose. Read them for the
*shape* of a derivation, never as a term list: copying a term out of an example is the one failure
this protocol exists to prevent.

---

## The rule

Procurement documents, job descriptions, and grant abstracts describe the WORK BEING PROCURED — not the outcome, not the pain, not the sales pitch. Your keywords must sound like something a procurement officer would type into their internal contract catalogue.

**Good keyword forms:**
- Concrete noun-phrases: "{repair task}", "compliance audit", "penetration testing", "warehouse automation"
- Domain-specific verbs+nouns: "{asset} inspection", "medical device labelling"
- Named categories: "rope access services", "SOC 2 attestation"

**Bad keyword forms:**
- Adjectival descriptions: "efficient", "innovative", "cost-effective" — buyers don't tender for adjectives
- Outcome language: "reduce downtime", "increase uptime" — that's a sales deck, not a contract
- Broad category names: "energy", "software", "healthcare" — millions of hits, all noise
- Conversational fragments: "why can't we", "what if we", "should we" — nothing to match

---

## The derivation steps

Given an assumption node, run these five steps.

### Step 1 — Extract the WORK from the assumption

Look at the assumption sentence. What is the target segment DOING that costs them money? Underline the verb phrase.

```
Assumption: "For UK council estates teams, the scheduling lag between chiller
fault detection and engineer mobilisation is the primary driver of
tenant downtime."

Work identified: "chiller fault detection", "engineer mobilisation",
"reactive maintenance scheduling"
```

Discard the outcome ("tenant downtime") — that's what the pain feels like to the buyer, not what they'd write in a contract.

### Step 2 — Cross-reference the disconfirmation field

`disconfirmation` tells you what a "no" looks like. It usually mentions specific artefacts, roles, or budget lines. Extract those.

```
Disconfirmation: "If ≥3 UK estates managers show that inspection
and repair are typically scheduled as a single mobilisation with the
same engineer, the assumption is falsified."

Extracted artefacts: "planned maintenance", "chiller inspection", "repair mobilisation"
```

Merge into the Step 1 list. Deduplicate.

### Step 3 — Add domain-anchor terms

To avoid false positives from adjacent industries, prepend or append a domain anchor to some of your terms. Example: "inspection" alone matches every industry. "Chiller inspection" only matches yours.

Draw domain anchors from `icp_segment`:
- `icp_segment: "UK council estates teams"` → domain anchor: `HVAC` (or `chiller`, `building services` if scoped)
- `icp_segment: "SME manufacturers subject to ISO 9001 compliance audits"` → anchor: `ISO 9001` or `compliance audit`
- `icp_segment: "Series B SaaS companies undergoing SOC 2 Type II"` → anchor: `SOC 2`

Anchor selection heuristic: pick the term in `icp_segment` that most narrowly identifies the industry without being so specific that a procurement officer wouldn't use it in their contract title.

### Step 4 — Add regional variants where the domain has geographic split

Some domains use different terminology by region:
- UK "rope access" ↔ US "vertical access" ↔ EU "IRATA-certified access"
- UK "O&M" ↔ US "maintenance services" for the same activity
- EU "framework agreement" ↔ US "master service agreement"

If `icp_segment` implies a specific geography, use that geography's terminology. If the geography is global, include 2-3 regional variants. Do not overload — 6-8 keywords total is the target.

### Step 5 — Sanity-check by imagining the contract

For each derived keyword, ask: "if I typed this into a public procurement search, would the results plausibly be relevant to this assumption?"

- "HVAC maintenance" → yes, this is a real contract line item
- "downtime optimisation" → no, this is a sales phrase, no one procures against it
- "building services" → too broad, will hit every FM vendor pitch, drop
- "chiller inspection services" → yes, contract-shaped

Drop any keyword that fails this check. Better to have 4 good keywords than 8 that dilute the search.

---

## Worked examples

### Example 1 — Reactive HVAC maintenance

```yaml
assumption: "For UK council estates teams, the scheduling lag between
             chiller fault detection and engineer mobilisation is
             the primary driver of tenant downtime."
icp_segment: "UK council and housing-association estates teams"
disconfirmation: "≥3 estates managers show inspection and repair are
                  scheduled as a single mobilisation with the same engineer"
category: pain
```

**Derived keywords:**
- `HVAC maintenance` — from assumption verb phrase + domain anchor
- `chiller inspection` — from disconfirmation artefact
- `reactive repairs` — regional variant (UK procurement terminology)
- `planned maintenance` — from disconfirmation
- `mechanical services` — synonym, catches contracts titled differently

That's 5 terms. Enough for a good pass without diluting.

### Example 2 — SaaS SOC 2 compliance

```yaml
assumption: "Series A/B SaaS companies underestimate the ongoing personnel
             cost of maintaining SOC 2 Type II compliance after the initial audit."
icp_segment: "Series A/B SaaS companies with an active SOC 2 Type II"
disconfirmation: "≥3 compliance leads at target companies show total
                  SOC 2 maintenance FTE is <0.25"
category: pain
```

**Derived keywords:**
- `SOC 2 attestation` — from assumption noun phrase (the artefact)
- `SOC 2 audit services` — buyer-side procurement of the audit itself
- `security compliance consulting` — the ongoing maintenance work
- `GRC platform` — infrastructure buyers typically procure alongside
- `penetration testing` — related annual procurement that shows up in same buyer's contract history

Note: this is a private-sector assumption, so TED EU + UK Contracts Finder will return less than in Example 1. That's fine — SBIR / CORDIS / EDGAR will pick up the slack. The keywords are derived the same way regardless of which APIs will use them.

### Example 3 — Warehouse robotics ROI

```yaml
assumption: "European 3PL warehouse operators cannot achieve <18-month
             payback on goods-to-person robotics deployments below
             10,000 sqm facility size."
icp_segment: "European 3PL warehouse operators, facility 5,000-15,000 sqm"
disconfirmation: "≥3 3PL operators show <18-month payback at target facility size"
category: economic
```

**Derived keywords:**
- `warehouse automation` — from assumption
- `goods-to-person system` — specific technology named in assumption
- `AS/RS installation` — related contract category (automated storage/retrieval)
- `3PL warehouse services` — buyer-side services (finds 3PL operators procuring for their clients)
- `warehouse management system` — WMS integration is often bundled with G2P deployments

### Example 4 — Medical device labelling

```yaml
assumption: "EU medical device manufacturers underestimate the total cost
             of MDR-compliant labelling across their SKU catalogue."
icp_segment: "EU MDR Class II/III medical device manufacturers"
disconfirmation: "≥3 QA/RA leads confirm labelling cost was budgeted at <20% actual"
category: pain
```

**Derived keywords:**
- `MDR compliance` — from assumption
- `medical device labelling` — the specific work
- `IFU translation services` — Instructions For Use translation is a major MDR line item
- `UDI implementation` — Unique Device Identification is another
- `regulatory affairs consulting` — external RA support is heavily procured

---

## Anti-patterns to avoid

**Do not use the exact assumption text as a query.** The assumption is a hypothesis — no procurement officer writes a contract that reads like a hypothesis. Extract the noun-phrases, not the sentence.

**Do not use the pain outcome.** "downtime", "revenue impact", "lost output" describe how the pain feels to the buyer — not what they procure to address it. The keyword goes on the fix, not the wound.

**Do not overload with synonyms.** Diminishing returns after 8 terms. TED EU rate-limits by query, and duplicate results waste dedup effort.

**Do not hardcode terms from previous runs.** Every assumption gets a fresh derivation. If two assumptions sit in the same domain and share a term, that's fine — but derive it fresh each time, don't copy from an old manifest.

---

## Manifest logging

At the end of the derivation, log the terms + reasoning to the manifest so future maintainers (and the founder) can see how each pass was constructed:

```jsonl
{"phase": "derive_keywords", "assumption": "A2",
 "terms": ["HVAC maintenance", "chiller inspection", "reactive repairs",
           "planned maintenance", "mechanical services"],
 "derivation": {"from_assumption_verb": ["chiller fault detection", "engineer mobilisation"],
                "from_disconfirmation": ["planned maintenance", "chiller inspection"],
                "regional_variants_added": ["reactive repairs"],
                "dropped": [{"term": "downtime optimisation", "reason": "sales phrase, not procurement"}]}}
```
