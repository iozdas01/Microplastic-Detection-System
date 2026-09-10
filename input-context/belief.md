---
idea: industrial-process-data-infrastructure
created: 2026-08-31
last_confirmed:
purpose: The founder-owned durable belief this idea rests on, plus its boundaries and SISP check.
status: in_intake
---

# Belief

> The bottleneck to running production lines with models isn't the models, it's that real-time
> process data arrives as numbers with no identity or meaning attached, and nobody is building
> the infrastructure that identifies and interprets it.

Confirmed as the one-liner on 2026-09-09 ("I like C!!!! ... we can lock it down now"). It
replaced, in the same session, a first draft that read "...the infrastructure to collect
real-time data from the physical process doesn't exist yet and nobody is building it" — that
version did not survive the precedent check (see Belief boundaries): inline real-time
measurement of process liquids has been a product category for about twenty years, so the
founder moved the claim from *collection* to *identification and interpretation* ("YES
IDENTIFICATION AND INTERPRETATION"). Compressed from the founder's own sentences: *"Before you
build intelligence layers/models for execution of the line - you need to build the
infrastructure to collect the data - no one is building this infra, we are"* and *"It says tag
0047 but what does tag 0047 mean?"* The founder's requirement for the line: nobody reading it
should need any other context.

## How the founder states it

Session of 2026-09-09, verbatim:

> "You should have this real-time data. If you connect this to the software you build, the
> interoperability software you build, then the mathematics models and so on are going to make
> better decisions because they are going to count everything. In a very fragmented
> unstructured environment we are going to put structure in."

> "The problem layer that I'm obsessed with, which is the adjustment, starts from the
> collection. Before you can adjust you first have to collect."

> "We believe that this manual re-entry or this manual decision layer that is inside of the
> processes is hindering progress."

> "If you're talking about an OPC-UA protocol or a Modbus protocol, that can be mapped into one
> layer but there's no meaning there. It says tag 003, it says tag 0047 but what does tag 0047
> mean? That's when you need to go into the operator's knowledge."

> "If there was going to be any type of agentic implementation or any type of agents that are
> orchestrating these machines by themselves, then there has to be a need for this data
> collection."

The founder's worked example of the milder case: a CNC machine cuts the part, a CMM measures
it, a person reads the measurement and re-adjusts the machine — "it all has to be manual". The
extreme case, in the founder's words: "within microplastics if there's no way to collect the
data initially, then you can't act on it."

The company-level statement ("no one is building this infra, **we are**") is recorded here and
kept out of the one-liner, which is a claim about the world.

**Two links, and they do not rest on the same evidence:**

1. **Collection is missing.** In physical processes the real-time data that would let a model
   adjust the line is either not collected at all, or collected without meaning (tags, not
   properties). First-hand: IMTEK CNC/CMM loop (2022-2024) and the Cambridge interoperability
   measurement carry over from v3.
2. **Nobody is building the collection layer.** This is the contrarian half and the checkable
   one. It arrived as an assertion in this session; no named search or named competitor set is
   behind it yet. Step 4 (definitional research) owes this link its examples.

## Belief boundaries

Drawn 2026-09-09 by the precedent check, with the founder confirming each line.

- In scope: physical production processes where real-time data is, or can be, collected but
  arrives without identity (what was measured) or meaning (what it implies for the line), so
  a person still closes the loop — the CNC → CMM → manual re-adjust case, and the inline
  particle sensor that reports size and count but not what the particle is.
- Out of scope, because it already exists and the belief does not claim otherwise:
  - **Real-time measurement itself.** Mettler Toledo's [ParticleTrack G600](https://www.mt.com/us/en/home/products/L1_AutochemProducts/particle-size-analyzers/particletrack-fbrm/particletrack-g600.html)
    is a probe inserted into vessels or pipelines that tracks particle count and size in real
    time at full process concentration (0.5-1000 µm); Malvern Panalytical's [Insitec Wet](https://www.malvernpanalytical.com/en/products/product-range/insitec-range/insitec-wet)
    does online laser-diffraction sizing on wet process streams (0.1-2500 µm). Both are sold
    to manufacturers today. The founder's first draft said this infrastructure "doesn't exist
    yet"; it does, and the belief was narrowed rather than defended.
  - **Machine-health sensing.** Augury's [Halo R4000](https://www.augury.com/machine-health-solutions/cr/halo/)
    puts vibration, temperature and magnetic sensors with edge AI on the machine. It measures
    the machine, not the product or the process stream, and is not what the belief is about.
  - **Plant data historians.** OSIsoft PI and its kind collect and store real-time tags from
    instruments the plant already has. They are the "tag 0047" the belief says has no meaning.
  - **Fleet and site telematics** (Samsara). Raised and struck in-session: not manufacturing.
- Deliberately NOT a boundary: the industry. Microplastics in water pipes and microfibers in
  textile manufacturing are where the founder intends to start, and they enter as candidates
  for the shotgun, not as a filter on what it may propose. The belief has to hold for the
  CNC/CMM loop as well as the pipe, or it is a product claim rather than a belief.
- Precedent noted, for the shotgun rather than settled here: no commercial inline product
  identifies microplastics in a flow. What exists in 2026 is research — a
  [microwave resonant sensor for seawater](https://www.nature.com/articles/s41378-026-01413-y),
  an [electrokinetic focusing concept for pipe flow](https://pmc.ncbi.nlm.nih.gov/articles/PMC13259111/),
  a [multispectral laser-diode concept](https://pmc.ncbi.nlm.nih.gov/articles/PMC13431368/) — and a
  [2026 review](https://link.springer.com/article/10.1007/s41101-026-00496-y) calling
  standardized real-time detection "limited". That supports the *identification* half of the
  belief for one property in one medium; it says nothing yet about *interpretation*.

## Starting point and SISP check

- Starting solution, technology, or analogy: the ladder the founder pasted to open the
  session, verbatim (part of it forwarded from a chat with Sandra, 2026-09-09 07:45-07:46):
  - VISION — "Build the observability layer for physical industrial processes."
  - MISSION — "Make industrial processes measurable, understandable and optimizable in real time."
  - CORE TECHNOLOGY THESIS — "Physical process observability stack."
  - CURRENT CORE TECHNOLOGY / WEDGE — "Real-time particle intelligence in complex industrial liquids."
  - FIRST PRODUCT — "Microfiber Process Monitor for textile manufacturing."
  - DATA LAYER — "Proprietary process datasets and cross-factory benchmarks."
  - PLATFORM EVOLUTION — "sensing + existing machine data + interoperability + models + recommendations."
  - Also stated mid-session: "we are solving the problem of benchmarking and detection of
    microplastics inside of water pipes" and "that's why we're starting with microplastics."
- Origin: solution_or_analogy_first
- Problem stated without the solution: "Before you can adjust you first have to collect."
  Expanded, in the founder's words: the adjustment loop on a production line is closed by a
  person reading a measurement and re-entering it, and in some processes there is no
  measurement to read at all.
- Founder-reported observations (context, not independent evidence):
  - CNC → CMM → manual re-adjust loop, seen first-hand at IMTEK Cryogenics.
  - OPC-UA / Modbus tags carrying no meaning without the operator, from the same environment
    and the Cambridge MPhil work.
  - Anthropic's hardware standard (the founder calls it "AHS"; recorded in the archived ledger
    as the Model Hardware Standard, previewed 2026-08-27) as the reference architecture for a
    semantic layer between machine signal and actuator — a public announcement, not an
    observation of a factory.
  - Microplastics in water pipes: "there is no data to be able to adjust for them because
    there is no way to collect that data." Asserted; no site, operator or measurement named yet.
- SISP status: **probable**
  - The solution ladder (observability stack → particle sensor → microfiber monitor) arrived
    fully formed and before the belief was stated; the belief was produced by compression on
    request ("u need to package everything I sent to you and find the contrarian belief").
  - The wedge (microplastics, water pipes, textile microfibers) was fixed before any belief-level
    boundary was drawn, and the founder's own reason for it is that it is the case where
    collection is zero — a property of the solution's difficulty, not of a buyer's pain.
  - A CAD-viewer folder for a "membrane fouling cell" instrument (`cad/`) was committed to this
    repo on 2026-09-08, before intake. The instrument predates the belief.
  - `probable` records how the founder arrived. It is not a verdict.
- What the shotgun must test independently:
  - Whether "nobody is building it" survives a named search for the *identification and
    interpretation* layer specifically — measurement vendors were found in-session; who, if
    anyone, sells the step after the number, and what they call it.
  - Whether the missing-collection pain is described by operators in their own words, without
    the vocabulary of AI, agents or observability.
  - Whether microplastics / water pipes / textile microfibers is the right first case against
    other physical processes where collection is zero. It enters as one candidate, not the answer.

## What would threaten the belief itself

Asked 2026-09-09. The founder did not name a disconfirmer: *"there are already partnerships so
I am unsure!"*, then closed the session — *"we will iterate on the belief as needed"*. Recorded
as-is rather than filled in. The two shapes offered in the session, which the founder neither
accepted nor rejected, stand as the working threats until the founder replaces them:

- **Someone is building it.** A measurement vendor (Mettler Toledo, Malvern Panalytical,
  Emerson, Endress+Hauser) or a partnership between one of them and a software company ships a
  product that tells the operator *what* was measured and *what to change*, and plants buy it.
  This kills the "nobody is building it" half. The founder's own "there are already
  partnerships" belongs here and is unnamed — naming them is the first job of the shotgun's
  recon, and it may move this from threat to fact.
- **The loop is not the bottleneck.** Plants already have a person interpreting the numbers
  fast enough that the line never waits on it, and would say so unprompted. This kills the
  bottleneck half and leaves identification as a nice-to-have.

A belief nothing could falsify absorbs any evidence and never updates; this one has two named
threats but the founder has not yet owned either.

## Version history

_Oldest first. Never overwrite or delete a prior statement; the founder's requirement is exact
iterations of every belief._

### v1 — created 2026-08-31, last_confirmed 2026-08-31

Displaced 2026-08-31: the founder raised the belief a level. The statement below is a claim
about one industry (fitted cabinetry) and one cost driver (design labour); the founder
reframed it as a claim about manufacturing generally, at which point the cabinet statement
became a candidate *hunch* beneath the new belief rather than the belief itself. H1 is
re-statused from `active` to `proposed` in `hunch-lineage.md` and keeps its evidence and
assumption graph intact.

> Custom cabinetry costs roughly three times stock cabinetry, and most of that premium is
> not manufacturing — it is a person at a desk drawing the kitchen. That design labour is
> now automatable, and whoever automates it can sell a custom kitchen at a semi-custom price.

v1 in-scope: fitted cabinetry and joinery — kitchens first — where the product is engineered
per job from a room's real dimensions, and where a designer currently stands between the
customer and the price. Frameless (European 32mm) construction from pre-finished sheet goods,
doors and fronts bought in.

v1 out-of-scope: freestanding furniture sold from a catalogue (measured demand for "custom"
there runs under 1% of generic, fourteen times thinner than cabinets); anything requiring
upholstery, foam or sewing; anything needing a finishing department — no spray booth, no cure
room, no moulder. Also out of scope: automating the shop floor, which is the station with 40%
spare capacity.

v1 SISP status: possible. Starting solution recorded as "an autonomous panel factory selling
configurable furniture direct to consumers"; origin `solution_or_analogy_first`. The v2 belief
returns to that starting position, which is why v2's SISP status is raised to `probable`.

### v2 — created 2026-08-31, last_confirmed 2026-08-31

Displaced 2026-09-03 by founder correction, stated twice in one session: *"the belief is that
manufacturing will be done via an app - and that interoperability is required for this to
happen"* and *"the both ends thing is an OPTION BUT NOT THE BELIEF"*. Not a change of mind —
a correction of the record. The v3 body was already present in v2's own "How the founder states
it" section ("vibe manufacturing… go into a website and just manufacture what they need";
"there is no interoperability at all within the system"); the headline statement below simply
did not carry it, and the headline is what propagates into BRIEF.md and every pitch. Three
separate sessions quoted the headline back as the belief and got the emphasis wrong.

> The problem is that software and machines don't talk, and you have to own both to fix it.

v2 in-scope: manufacturing where the design-to-machine handoff is per-order and currently
manual. v2 out-of-scope: unknown until the wedge is chosen. v2 SISP status: probable.

v2 structured the belief as two links — (1) the coupling is broken, first-hand and measured;
(2) therefore the fix requires owning both ends, which was advice rather than observation. v3
keeps link 1, adds the prediction and the batch-size-one conditional that v2 held only in its
prose, and demotes link 2 to an implementation option. Link 2's weakness was already recorded
in v2 ("Asked twice for a specific occasion behind link 2, the founder gave the general
statement rather than a named event"), so the demotion follows the file's own evidence.

### v3 — created 2026-09-03, last_confirmed 2026-09-03

Displaced 2026-09-09 by v4. The founder reset the idea folder that morning (window-coverings
lineage retired, IDs burned) and re-entered intake the same day saying "the interoperability
belief is basically the same" but "the problem is different". v4 keeps interoperability and
moves the claim one step upstream: v3 assumed the process data existed and failed to connect;
v4 says that in the physical process it mostly is not collected at all, and that nobody is
building the layer that would collect it. The lineage continues rather than restarting.

> Manufacturing will be done through an app, and interoperability is the precondition for it.

v3 SISP status: probable. Starting solution: "vibe manufacturing", furniture as the entry
wedge on angel advice. v3's own boundaries and threat list, verbatim:

## Belief boundaries

- In scope: manufacturing where **the design-to-machine handoff is per-order and currently
  manual** — every job needs its own geometry, toolpath, cost and schedule, and a person
  moves that information between CAD, CAM, ERP and the floor by hand. This is narrower than
  "high-mix low-volume", deliberately: it excludes high-mix *assembly* with no per-order
  design step, and repeat job-shop reorders where the engineering was done once and is
  simply re-run. **The industry is still deliberately not fixed** — which vertical to enter
  is the open question this belief was sharpened to answer, and it is the shotgun's job, not
  the belief's. The narrowing makes that question aimable rather than answerable in advance.
  (Scope tightened 2026-08-31: the earlier wording, "high-mix low-volume, industry not
  fixed", covered most of manufacturing and would have returned a list rather than a wedge.)
- Out of scope: unknown until the wedge is chosen. The prior belief's exclusions (upholstery,
  finishing departments, freestanding catalogue furniture) were properties of the cabinet
  hunch, not of this belief, and do not carry up.
- Deliberately NOT a boundary: direct-to-consumer. The founder's position is that D2C plus
  owned factories is required for control, but that entered as a preference rather than an
  observation, so it is carried as a testable hypothesis the shotgun may challenge — not a
  filter on which candidates it is allowed to propose (founder decision, 2026-08-31).

## What would threaten the belief itself

**Rewritten for v3.** Both v2 threats attacked link 2 — "you have to own both ends" — which v3
demotes out of the belief. Under v3 they no longer threaten the belief at all; they are
evidence about which implementation to pick, and they moved here from the threat list
deliberately rather than being deleted:

- A Xometry/Protolabs/Zoo-style layer reaching batch-size-one economics on machines it does not
  own is now **consistent with** the belief — it would be app-driven manufacturing happening.
  It threatens the owned-factory option, not the belief.
- Owned-factory operators failing at the same rate as asset-light ones remains a question about
  the company, as the founder ruled on 2026-08-31.

What actually threatens v3:

- **Interoperability stops being the bottleneck.** STEP AP242, MTConnect, UMATI or QIF maturing,
  or one vendor's stack becoming dominant enough that CAD, CAM, ERP and machine simply pass data.
  Then app-driven manufacturing arrives without anyone having to fix interoperability, and the
  precondition half of the belief is wrong. This was already on the v2 list and is promoted to
  the primary threat, because v3 rests on it far more heavily than v2 did. **It is no longer
  hypothetical: Anthropic previewed the Model Hardware Standard on 2026-08-27 and intends to
  open-source it (E20).** That does not falsify the belief — it dates it, and it moves the
  defensible part from connecting machines to knowing what to send them.
- **App-driven manufacturing arrives without interoperability.** A single closed stack — one
  machine maker's cloud, end to end — delivers the outcome by eliminating the interoperability
  problem rather than solving it. Same result, and the belief's causal claim is still wrong.
- **Manufacturing does not go through an app.** The per-order coordination stays human because
  the residual judgement in it does not automate. This falsifies the belief head-on and is the
  only one of the three that kills it rather than reroutes it.
- **The batch-size-one conditional fails.** App-driven manufacturing shows up first in high
  volume rather than high-mix. That would not kill the belief but would falsify the reason the
  founder expects to be early, which is what the wedge choice rests on.
