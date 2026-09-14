---
purpose: The hunch lineage — every hunch ever held under the belief, its status, and which one is active.
belief_file: input-context/belief.md
active_hunch: [H1, H2]
next_hunch_id: H6
last_updated: 2026-09-14
---

# Hunch Lineage

_Founder-originated lineage. The founders arrived with the first product and wedge already
chosen, so H1 was written from their words on 2026-09-09 rather than proposed by a shotgun;
the shotgun runs against it in initial-test mode. Further hunches are expected after the
founder's own research into detection across other industries, and enter here as H2, H3…_

## H1

status: active
validation_status: untested
activated_on: 2026-09-09
parent_hunch: null
created: 2026-09-09
created_by: founder
created_by_artifact: input-context/belief.md
change_reason: >-
  Founder-originated in the same session as belief v4, confirmed verbatim ("yes H1 is good
  in that sense I agree"). The founders already held the product (a microfiber process
  monitor), the wedge (fashion / textile manufacturing) and the beachhead (the first sensor
  feedback loop); this records that position as the first falsifiable interpretation of the
  belief so it can be tested rather than assumed. No buyer conversation is behind it yet.
evidence_delta: []

### Statement

In the fashion industry there are no sensors to detect microplastics, so a textile
manufacturer cannot see or act on the microfibers their process releases; a real-time sensor
with a feedback loop is the first product, and the first sensor feedback loop is the beachhead.

### Components

- Segment: textile / fashion manufacturing. Which step of the process (dyeing, washing,
  finishing, effluent) and which size of manufacturer are unknown.
- Problem: microfibers released by the process cannot be seen in real time, so nothing can be
  adjusted against them. Whether a manufacturer experiences this as a problem today is
  untested — it may be felt only once regulation or a brand demands the number.
- Mechanism: the belief's identification-and-interpretation gap in its extreme form —
  collection is zero, so identification and interpretation cannot even begin. Inline particle
  sensors exist (Mettler Toledo ParticleTrack, Malvern Insitec Wet, see belief.md) but count
  and size particles without saying what they are; no commercial inline product identifies
  microplastics in a flow, only 2026 research concepts.
- Why now: UNVERIFIED. Candidate: microfiber and microplastic regulation and brand
  disclosure requirements arriving in the EU and elsewhere. Not yet named or dated.
- Existing workaround: lab test methods on samples (e.g. The Microfibre Consortium's test
  method), not inline and not real time. Unverified which manufacturers use them and why.
- Plausible buyer: unknown. Candidates are the manufacturer, the brand buying from them, or
  the effluent-treatment operator; who holds the budget and the obligation is the first
  thing the calls must find.
- Cheapest next test: ask people who run textile wet-processing what they measure in their
  process water today, what they are asked to report about microfibers, by whom, and what
  they did the last time that question came up.
- Hunch disconfirmation: if textile manufacturers cannot name anyone asking them for a
  microfiber number, or already have a measurement they consider good enough, the pain is
  not there and this hunch dies without touching the belief. It also dies if an inline
  microfiber sensor is already sold and used.

### Evidence

- Supports: nothing yet. Zero conversations held.
- Contradicts: nothing yet.
- Still unknown: everything a buyer would say.

### Relationship to belief

- How this hunch expresses the belief: the case where the real-time data does not exist at
  all, so identification and interpretation have nothing to work on — the belief's gap at
  its widest.
- Evidence that would threaten only this hunch: no textile buyer for the number; an inline
  microfiber sensor already in use; the loop closed adequately by lab sampling.
- Evidence that would threaten the underlying belief: a measurement vendor shipping a
  product that identifies what was measured and tells the operator what to change, in any
  industry, and plants buying it (belief.md → threats).

## H2

status: active
validation_status: untested
activated_on: 2026-09-14
parent_hunch: null
created: 2026-09-14
created_by: founder
created_by_artifact: reports/outreach/companies.md
change_reason: >-
  Founder-originated 2026-09-14 while researching which industry CyFract (Munich, uniflow
  hydrocyclone pre-treatment) is building for. CyFract's own funder and careers pages name
  seawater desalination pre-treatment as the primary market; the founders are in talks with
  CyFract as a first site, but CyFract cannot pay, so the buyer under this hunch is the plant
  operator. Statement drafted by Claude from standard SWRO practice and accepted by the
  founder for logging; no operator conversation is behind it yet. Activated 2026-09-14 by
  founder decision ("let's go with this hunch right now") to run in parallel with H1, whose
  outreach is live; H1 is not retired.
evidence_delta: []

### Statement

Reverse-osmosis desalination operators gate pre-treatment with a manual silt index and
clean membranes on a lagging pressure-drop trigger, and neither tells them which foulant or
which upstream stage is responsible, so cleaning chemistry and pre-treatment tuning are
chosen by rule of thumb and the only identification step is a destructive membrane autopsy
weeks later.

### Components

- Segment: seawater reverse-osmosis desalination plants; which size and which pre-treatment
  train (media filtration vs ultrafiltration) is unknown.
- Problem: fouling is detected only after it has happened (normalised flow and differential
  pressure), and the pre-treatment gate (Silt Density Index, ASTM D4189, a 15-minute manual
  grab test) reports fouling potential without particle identity.
- Mechanism: the belief's gap with data present — SDI, turbidity, particle counts and
  membrane ΔP all exist as numbers, none carries what the particle is or where it entered,
  so a person picks the clean-in-place recipe (acid vs caustic) by rule of thumb.
- Why now: UNVERIFIED. Candidates: chemical-free pre-treatment vendors (CyFract) needing to
  prove downstream effect to sell; membrane cost and CIP chemical cost pressure. Not dated.
- Existing workaround: SDI/MFI grab tests, online turbidity and particle counters, membrane
  autopsy (offline, destructive, weeks).
- Plausible buyer: the plant operator (process or O&M manager) — CyFract is a site and a
  channel, not a payer (founder, 2026-09-14). Membrane manufacturers are a second candidate
  (see H5).
- Cheapest next test: ask five SWRO plant operators how they decided the last clean-in-place
  (trigger, recipe, and how they knew what the foulant was), and what the last autopsy cost
  and told them.
- Hunch disconfirmation: operators say the CIP recipe choice is not a problem (one recipe
  works), or an inline foulant-identification product is already in use, or the SDI gate is
  considered good enough.

### Evidence

- Supports: nothing yet. Zero conversations held. CyFract's market choice is context, not
  evidence.
- Contradicts: nothing yet.
- Still unknown: everything an operator would say.

### Relationship to belief

- How this hunch expresses the belief: measurement exists at three points and none of it
  carries identity; the loop is closed by a person guessing.
- Evidence that would threaten only this hunch: operators satisfied with rule-of-thumb CIP;
  autopsies rare and cheap; an existing inline fouling-identification product.
- Evidence that would threaten the underlying belief: as H1.

## H3

status: proposed
validation_status: untested
parent_hunch: null
created: 2026-09-14
created_by: founder
created_by_artifact: reports/01-ideation/hunch-lineage.md
change_reason: >-
  Founder-supplied segment 2026-09-14, pasted from the founder's own market research:
  "California drinking water utilities: strictly bound by state-mandated microplastics
  testing and monitoring frameworks." Premise checked the same day: the mandate is real
  (SB 1422; State Water Board policy handbook 2022) but it is a monitoring programme using
  lab methods, not a treatment limit, and Phase 2 on treated water starts autumn 2026 only
  if the Board proceeds. "Strictly bound" is the founder's reading, not a source's.
evidence_delta: []

### Statement

Large California community water systems must report microplastics in source water (Phase
1, 2023-2025) and treated water (Phase 2, from autumn 2026), and the only way to produce the
number is a periodic lab analysis, so utilities carry a compliance obligation with no way to
see the number move between samples or act on it.

### Components

- Segment: California community water systems selected for SB 1422 monitoring; which
  systems and how many is unknown.
- Problem: compliance is a lab number delivered weeks after the sample; nothing inline.
- Mechanism: the belief's gap at its widest for this industry — no real-time data at all,
  as in H1.
- Why now: [T] SB 1422 monitoring, Phase 2 treated-water monitoring from autumn 2026
  (State Water Board handbook). Whether Phase 2 proceeds is the Board's decision.
- Existing workaround: certified-lab Raman or FTIR analysis per the Board's standard
  method; whether utilities see it as a pain or a line item is unknown.
- Plausible buyer: the utility's water-quality or compliance lead; unknown whether a budget
  exists beyond the lab fee.
- Cheapest next test: ask five Phase 1 utilities what the monitoring cost them, what they
  did with the result, and whether anyone asked for more than the report.
- Hunch disconfirmation: utilities treat it as a lab line item with no operational
  consequence, or the Board does not proceed to Phase 2.

### Evidence

- Supports: nothing yet.
- Contradicts: nothing yet.
- Still unknown: whether any utility wants more than the compliance report.

### Relationship to belief

- How this hunch expresses the belief: no real-time data; the loop is a lab report.
- Evidence that would threaten only this hunch: monitoring is a line item with no
  operational decision behind it.
- Evidence that would threaten the underlying belief: as H1.

## H4

status: proposed
validation_status: untested
parent_hunch: null
created: 2026-09-14
created_by: founder
created_by_artifact: reports/01-ideation/hunch-lineage.md
change_reason: >-
  Founder-supplied segment 2026-09-14, pasted from the founder's own market research:
  "Municipal and industrial wastewater treatment plants facing imminent regulatory
  discharge limits, particularly across the textiles, plastics recycling and chemical
  manufacturing sectors." Premise checked the same day: the EU Urban Wastewater Treatment
  Directive recast (2024/3019, in force 2025-01-01, Art. 21) requires microplastics
  MONITORING at inlets and outlets of plants above 10,000 p.e., methods by July 2027; no
  discharge LIMIT was found, and nothing sector-specific for textiles, recycling or
  chemicals. "Imminent limits" is unverified [U].
evidence_delta: []

### Statement

Wastewater treatment plants above 10,000 population-equivalents in the EU will have to
monitor microplastics at inlet and outlet under the recast directive, and industrial
dischargers upstream of them (textiles, plastics recycling, chemicals) will be asked for
their share, so both sides need a number they cannot currently produce inline.

### Components

- Segment: EU municipal WWTPs above 10,000 p.e. and the industrial dischargers feeding
  them; which sectors actually get asked is unknown.
- Problem: a monitoring obligation with no inline method; lab methods only, and the
  official method does not exist until July 2027.
- Mechanism: as H1 and H3 — no real-time data.
- Why now: [T] UWWTD recast Art. 21 monitoring; [U] any discharge limit; [U] any
  sector-specific obligation.
- Existing workaround: none required yet; lab sampling once methods land.
- Plausible buyer: unknown — the municipal plant, or the industrial discharger the plant
  passes the question to.
- Cheapest next test: ask five EU WWTP operators above 10,000 p.e. whether they have started
  preparing for Art. 21 and whether they intend to pass the question upstream.
- Hunch disconfirmation: operators wait for the 2027 method and buy lab tests; no
  discharger is asked for a number.

### Evidence

- Supports: nothing yet.
- Contradicts: nothing yet.
- Still unknown: whether anyone is preparing before 2027.

### Relationship to belief

- How this hunch expresses the belief: no real-time data; regulation may create the need.
- Evidence that would threaten only this hunch: the obligation is met by lab sampling
  with no operational decision behind it.
- Evidence that would threaten the underlying belief: as H1.

## H5

status: proposed
validation_status: untested
parent_hunch: null
created: 2026-09-14
created_by: founder
created_by_artifact: reports/01-ideation/hunch-lineage.md
change_reason: >-
  Founder-supplied segment 2026-09-14, pasted from the founder's own market research:
  "R&D departments of membrane manufacturers (DuPont, Hydranautics, Toray) actively seeking
  inline anti-fouling and particle-characterisation technologies to protect high-value
  RO/UF membranes." Premise checked the same day: no public statement, partnership or open
  call from any of the three was found. "Actively seeking" is unverified [H].
evidence_delta: []

### Statement

Membrane manufacturers lose warranty claims and reputation to fouling they did not cause,
and have no inline way to show a plant which foulant reached the membrane, so their R&D
groups would pay for inline particle characterisation as a warranty and diagnostic tool.

### Components

- Segment: RO/UF membrane manufacturers' R&D or technical-service groups.
- Problem: UNVERIFIED — that warranty disputes over fouling are frequent and costly.
- Mechanism: identity gap at the membrane inlet, as H2, seen from the supplier side.
- Why now: unknown.
- Existing workaround: membrane autopsy services, which the manufacturers themselves run.
- Plausible buyer: technical-service or R&D lead at a membrane maker; unknown whether any
  budget exists.
- Cheapest next test: ask three membrane technical-service engineers how a fouling warranty
  claim is settled today and what an autopsy costs them.
- Hunch disconfirmation: autopsy is cheap and settles claims; no one at a membrane maker
  can name a claim lost for want of inline data.

### Evidence

- Supports: nothing yet.
- Contradicts: nothing yet.
- Still unknown: whether the problem exists on the supplier side at all.

### Relationship to belief

- How this hunch expresses the belief: the identity gap seen from the supplier who bears
  its cost.
- Evidence that would threaten only this hunch: warranty claims are rare or settled cheaply.
- Evidence that would threaten the underlying belief: as H1.
