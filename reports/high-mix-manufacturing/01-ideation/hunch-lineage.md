---
idea_slug: high-mix-manufacturing
belief_file: input-context/high-mix-manufacturing/belief.md
active_hunch: H3
next_hunch_id: H5
last_updated: 2026-09-07
purpose: The hunch lineage for this idea — which falsifiable interpretation of the belief is under test, and why.
---

# Hunch Lineage

_Restarted 2026-09-02. The first lineage — four desk-research candidates retired without a
single customer conversation — is archived whole at
`archive/hunch-lineage-cabinets-2026-09-02.md`, with its assumption graph in
`../02-assumptions/archive/`. Those IDs are burned; nothing live cites them._

## H1

status: superseded
validation_status: untested
superseded_on: 2026-09-02
superseded_reason: >-
  Founder attention moved to H2 before any call was made. NOT falsified — the furniture
  remanufacturing question is untouched and may be revived. It is superseded because the
  founder has manufacturing capacity available now and chose to test a lane that can be
  sold into this month rather than one that needs a robotics build first.
parent_hunch: null
created: 2026-09-02
created_by: founder
change_reason: >-
  Founder-originated after a phone call. Reframes the idea from "manufacture new things to
  order" to "remanufacture what already exists". The shotgun did not find this — it came from
  a conversation, which is itself the finding after a day of desk research produced nothing
  testable.
evidence_delta: []

### Statement

We believe **the organisations that currently pay to dispose of furniture** are throwing away
material with recoverable value because **remanufacturing is labour-heavy, the input is wildly
variable, and the industry has therefore stayed manual and price-capped for 77 years**, and
**computer vision plus robotics for inspection, disassembly, defect detection and refinishing**
could make automated remanufacturing economic for the first time.

### Components

- Segment: unknown. Candidates: home movers, junk removal operators, office facilities
  managers, office furniture liquidators, municipal waste authorities. Narrowing this is the
  first job of the calls.
- Problem: 12.1M tons of US furniture discarded annually — 80.1% landfilled, 19.5% burned,
  **0.3% recycled**. ~$652M a year in tipping fees alone. Consumers pay $75-700 per junk
  removal.
- Mechanism: the input variability that keeps remanufacturing manual is a perception and
  handling problem — which is what vision models and robotics got good at in 2024-26.
- Why now: UNVERIFIED. The honest question is why 77 years of remanufacturers did not
  automate, and whether the answer is "could not" or "not yet".
- Existing workaround: landfill, energy recovery, donation (Goodwill, Habitat ReStore), paid
  junk removal (1-800-GOT-JUNK, LoadUp, Remoov).
- Plausible buyer: unknown. The input may carry NEGATIVE cost — collection is already a paid
  service — which changes the economics materially if it holds.
- Cheapest next test: call five home movers and five junk removal operators. Ask what
  actually happens to furniture people leave behind, how often, and who pays whom.
- Hunch disconfirmation: if 3 of 5 remanufacturers say input variability is not what keeps
  them manual, or that labour is not the binding cost, the mechanism is wrong. It also dies
  if the recoverable fraction is too small — most discarded furniture is MDF or particleboard,
  which cannot be recycled into new board at all.

### Evidence

- Supports: the waste numbers (12.1M tons, 0.3% recycled); potentially negative-cost input;
  office furniture passes all four tests that make pallet recycling work — standardised,
  aggregated, short-haul, gradeable.
- Contradicts: **Kaiyo raised ~$50m to do the easier version** — collect and resell, no
  remanufacturing — and wound down in 2024 on "high logistics costs, the complexity of
  handling used goods, and cyclical demand". MDF and particleboard cannot be recycled into new
  boards. The remanufactured office furniture industry is 77 years old, sells at ~80% off new,
  and is too small to have a published market size.
- Still unknown: everything a buyer would say. **Zero conversations held.**

## H2

status: superseded
validation_status: untested
superseded_on: 2026-09-03
superseded_reason: >-
  Founder conviction moved to H3 (window coverings) before any conversation was held. NOT
  falsified — the blocked-part question is untouched and revivable. Two things pushed it:
  the demand sweep measured inbound demand for the parts_repair lane at exactly zero, so
  every customer would have to be found outbound; and the window-coverings recon produced a
  costed, published pain within a day. Neither is buyer evidence against H2.
parent_hunch: null
created: 2026-09-02
created_by: founder
change_reason: >-
  Founder-originated. Redirects the idea from remanufacturing discarded goods to selling
  high-variability custom machining out of an already-accessible Turkish CNC shop, aimed at
  parts that are blocked in the supply chain. Chosen over H1 because it monetises existing
  capacity immediately and produces the estimating dataset the belief actually points at,
  rather than requiring a robotics build before the first sale.
evidence_delta: [E2, E3]

### Statement

We believe **the people who keep industrial equipment and production lines running** absorb
real, costed delay when a part is blocked — discontinued, single-sourced, or quoted at a lead
time they cannot wait for — because **the shops that could make that part cannot quote
one-off, high-variability work fast or confidently enough to be a live option**, and
**owning both the CNC capacity and the quoting method** could close that gap.

### Components

- Segment: supply chain, procurement and maintenance/reliability people inside manufacturers
  and asset-heavy operators — narrowed from "furniture manufacturers and artists" by founder
  decision 2026-09-02 after the network audit showed zero furniture manufacturers reachable
  and the blocked-part question being answerable by people already in the network.
- Problem: a blocked part stops a line or a build. The cost is downtime, not the part.
- Mechanism: automated quoting platforms price by matching a CAD file against a known process
  envelope, so they reject or defensively over-price exactly the variable, no-drawing,
  mixed-process jobs where the buyer has nowhere else to go.
- Why now: UNVERIFIED. Candidate answers are post-2020 supply chain fragility, OEM
  obsolescence cycles, and reshoring — none tested.
- Existing workaround: wait for the OEM, cannibalise another machine, pay an expeditor, run
  degraded, or find a local shop by word of mouth.
- Plausible buyer: unknown. Maintenance budget and procurement budget behave differently and
  the calls must find out which one pays.
- Founder's unfair access: IMTEK CNC capacity in Türkiye, plus EU customs union freight.
  Note the network audit finding — this access is real but is NOT on LinkedIn.
- Cheapest next test: ask supply chain, procurement and maintenance contacts to describe the
  last part they could not get, what they did instead, and what the wait cost.
- Hunch disconfirmation: if contacts cannot name a recent blocked part unprompted, or name one
  but report it cost them nothing material, the pain is not there. It also dies if they can
  name the pain but say they would never accept a non-OEM machined replacement — that is
  H2A2, and it is where the digital-spares companies died.

### Evidence

- Supports: nothing yet. Zero conversations held.
- Contradicts: Spare Parts 3D, Replique and Ivaldi all pursued digital/on-demand spares with
  funding and none broke out; the recurring stated reason is that the OEM owns the drawing
  and the qualification envelope. Recorded here as a prior, not as evidence against this
  specific framing. **E2 rules out the founder's intended acquisition channel for this
  segment** — the blocked-part vocabulary has no measurable US search volume, so nobody
  arrives at a website looking for this. That is a channel finding, not a pain finding:
  H2A1 is untouched by it, and H2 now carries H2A4 to hold the question.
- Still unknown: everything a buyer would say. Zero conversations held.

## H3

status: active
validation_status: untested
activated_on: 2026-09-03
parent_hunch: null
created: 2026-09-03
created_by: founder
change_reason: >-
  Founder-originated and activated the same day, 2026-09-03: "right now we have to go in on
  the custom window coverings hunch". Activation rests on founder conviction and desk
  reconnaissance, not on buyer evidence — no conversation had been held when it was
  activated, so the first ten are load bearing. If they produce no misfit rate, nothing sits
  under this hunch.
evidence_delta: []

### Lane and entry point

**Lane:** made-to-measure furniture and interiors. **Entry point:** window coverings — the
wedge, not the market.

Window coverings first because the misfit is already priced and published there, a blind is
a handful of dimensions so one person can build the path, and the same gap widens into
alcoves and fitted wardrobes at higher unit value.

### Statement

Made-to-measure window coverings stay a home-visit business because nothing can verify a
measurement except a person standing at the window, and that single step caps the category's
online share.

### Components

- Segment: unknown. Candidates are independent fitters, made-to-measure retailers, online
  retailers, and the manufacturers who absorb the remakes. Whichever names the sharper rate
  and says "we eat it" is the segment.
- Problem: a misfit is a total loss, not a discount. Sun Glow tells its dealers "you pay the
  product cost twice and the labour twice while collecting once." At 40% margin one remake
  wipes out 1.5 similar jobs; at 30%, 2.3.
- Mechanism: nothing checks the number taken at the window against the real opening until
  the finished product arrives.
- Why now: UNVERIFIED, and the weakest link. Candidate answer is that a depth-capable phone
  and a vision model can now verify a measurement against the opening it came from.
- Existing workaround: free-remake guarantees (SelectBlinds FIT Protection covers the
  customer's own measuring error; AmericanBlinds and Blinds.com run similar), paid measuring
  services, and deduct-a-bit rules of thumb.
- Plausible buyer: unknown. The recon shows all three parties eating it in different cases —
  manufacturer, dealer, and the consumer whose claim is declined.
- Founder's unfair access: IMTEK CNC capacity, EU customs union freight, and a measured
  Cambridge result on this class of handoff.
- Cheapest next test: ten conversations with people who fit or sell made-to-measure. One
  question — the last one that came back wrong.
- Hunch disconfirmation: if fewer than 4 of 10 name a recent misfit unprompted, or name one
  and report it absorbed without thought, the pain is too soft to price against. It also dies
  if the rate is low enough that the guarantees are marketing rather than priced risk.
- Expansion path: window coverings → alcove and fitted storage → wardrobes and fitted
  furniture. Claimed by nobody and under test by nobody — it says what the wedge is a wedge
  into, nothing more.

### Evidence

- Supports: **SelectBlinds gives away a free remake when the CUSTOMER mismeasured** — revealed
  behaviour, not opinion, and a company does not absorb that unless the rate is high enough
  that fear of mismeasuring was blocking sales. Sun Glow publishes the remake arithmetic to
  its own dealers. Negative reviews cluster on remake turnaround: 3-4 weeks to six months.
- Contradicts: nothing yet, and that is a warning rather than a comfort — no source has been
  read that would have contradicted it.
- Still unknown: **the misfit rate.** No source gives a percentage of orders remade. Without
  it the lane cannot be sized, and it is the one number the first conversations must produce.
  Also unknown: the causal split between customer mismeasure, dealer error, manufacturing
  tolerance and out-of-square windows.
- Source: `recon/2026-09-03-window-coverings/findings.md`. Review samples are self-selected
  and describe the tail, not the distribution.

## H4

status: proposed
validation_status: untested
parent_hunch: H3
created: 2026-09-07
created_by: drift-check (startup-outreach-reply)
change_reason: >-
  Two contradicting entries now sit against H3's MECHANISM clause, and a third trigger fired
  at the same time. E30: asked whether blinds arrive not matching the customer's
  measurements, a UK installations manager rejected the premise and said what the survey is
  actually for — obstructions, how a given blind has to operate, per-product clearance. E32:
  the same source named the incumbent fix for the intent gap and dosed it at six months of
  training per technician plus factory floor time, with no tool involved. Separately, the
  founder's own outgoing messages on 2026-09-07 tested rework rate and margin, which is the
  belief-level framing and appears nowhere in H3's statement.
  H3 keeps the observation (the category stays a home-visit business) and loses the reason.
  This proposal changes ONLY the mechanism clause; segment, lane and entry point are H3's.
evidence_delta: [E30, E32]

### Lane and entry point

Unchanged from H3. Lane: made-to-measure furniture and interiors. Entry point: window
coverings.

### Statement

Made-to-measure window coverings stay a home-visit business because what the visit produces
is a fit judgement rather than a number — which product can operate in this opening, what
obstructions are in the way, how much clearance the mechanism needs — and that judgement is
what cannot be sent down the wire. A verified dimension does not carry it.

_Grounding: "customers don't always know to look out for obstructions or understand how some
blinds need to operate or fit. Different blinds require more space" — Richard Jones (C43),
verbatim, E30. The clauses "fit judgement rather than a number" and "cannot be sent down the
wire" are AGENT-PHRASED and need the founder's word before they stand._

### Components

- Segment: unchanged from H3 and still unknown. E30 adds one candidate the H3 framing did not
  distinguish: the vertically integrated seller who surveys, manufactures and installs, and
  therefore never experiences the handoff H3 was built around.
- Problem: the constraint on remote selling is not that the number might be wrong, it is that
  a correct number is insufficient. AGENT-PHRASED.
- Mechanism: product-fit constraints (obstruction, operating clearance, stack space, per-product
  minimums) live in a trained person's head and are applied at the window. Nothing in the order
  carries them, which is the same shape as the belief's "machines don't register manufacturing
  intent", one step upstream of the machine.
- Why now: UNVERIFIED, and weaker than H3's. H3 could at least point at depth-capable phones.
  A fit-judgement hunch needs a reason those constraints became encodable recently, and no
  candidate answer has been written. This is the clause most likely to sink the proposal.
- Existing workaround: **six months of technician training plus factory floor exposure**, which
  a UK operator says works and pays for itself (E32). This is the first named incumbent
  solution in the H3 lane that its own user says SUCCEEDS, and any version of this hunch has
  to beat it, not ignore it.
- Plausible buyer: unknown, and the training answer makes it harder — a firm that has already
  paid for six-month ramps has bought the fix and retains the asset.
- Cheapest next test: the same-or-different fork, asked of every seller already in the H3 pool.
  Is the list of things that catch a customer out the same list at every window, or a different
  one every time? Same means the judgement is a rule set and encodable. Different means it is
  irreducibly a person's, and this hunch is a consultancy at best.
- Hunch disconfirmation: if sellers describe the fit call as different at every window, or if
  they rank fabric, colour or installation above fit judgement as the reason people do not buy
  online, this dies alongside H3A5 rather than replacing it.

### Evidence

- Supports: nothing yet. E30 supports the mechanism only in the sense that it contradicts H3's.
- Contradicts: not tested.
- Still unknown: everything. **n=1, one market, one company, one conversation, and the half of
  it that named training arrived after the founder disclosed what she was looking for.** This
  proposal exists so the finding is not lost, not because it is established.
