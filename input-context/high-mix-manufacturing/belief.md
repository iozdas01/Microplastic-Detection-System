---
idea_slug: high-mix-manufacturing
created: 2026-08-31
last_confirmed: 2026-08-31
purpose: The founder-owned durable belief this idea rests on, plus its boundaries and SISP check.
---

# Belief

> The problem is that software and machines don't talk, and you have to own both to fix it.

## How the founder states it

The founder's own term for where this goes is **vibe manufacturing**: "in the future there
will be vibe manufacturing where one will be able to go into a website and just manufacture
what they need."

On why the company has to own production rather than sell into someone else's factory:

> "the company has to be direct to consumer because that is how we can have the most control
> by building our own factories"

> "i basically need to solve every problem myself and make the most fucking efficient
> furniture manufacturing possible"

On the state of the systems:

> "everything is broken - there is no interoperability at all within the system"

The belief has two links, and they do not rest on the same evidence:

1. **The coupling is broken.** A CAD file knows the shape, the CNC needs a toolpath, the ERP
   needs a cost, and nothing passes cleanly between them — so a person retypes it. This link
   is first-hand. The founder's profile records the environment (CNC and high-precision
   production where drawings, machine data, ERP records and operator knowledge do not connect
   cleanly, IMTEK 2022-2024), and the Cambridge MPhil went and measured it: 100% F1 on DXF
   metadata annotation, 74% F1 on STEP.
2. **Therefore the fix requires owning both ends.** This link was not observed. It arrived as
   advice the founder came to agree with, having previously held the opposite. Bridging a
   broken thread is also a live answer to a broken thread, and it is the one the founder's own
   research pursued. Recorded in the SISP section below, not as an observation.

Asked twice for a specific occasion behind link 2, the founder gave the general statement
above rather than a named event. That is recorded as-is rather than upgraded.

**Note that this belief reverses a durable position on the founder's own record.** The
`mess_is_the_market` thesis in `founders/izgin-ozdas.md` holds that brownfield beats
greenfield and the messy installed base *is* the opportunity; `platform_is_the_execution_layer`
holds that the winner is an orchestration company rather than an asset owner. Owning the
factory is the greenfield, asset-heavy play. The founder made this change knowingly on
2026-08-31 after advice from Daniel Theobald and others conflicted with the prior view.

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

## Starting point and SISP check

- Starting solution, technology, or analogy: "vibe manufacturing" — a direct-to-consumer
  website where a customer specifies what they need and a factory the company owns makes it.
  Furniture as the entry wedge came from angel investor **Daniel Theobald** (founder/CIO of
  Vecna Robotics, co-founder of MassRobotics), whose stated reason was that "wood is easier
  to deal with compared to metal."
- Origin: solution_or_analogy_first
- Problem stated without the solution: "Software and machines don't talk to each other. To get
  anything made that isn't already in a catalogue, a person has to re-enter the same
  information across CAD, CAM, ERP and the shop floor — which is why one-off production is
  slow and expensive."
- Founder-reported observations (context, not independent evidence):
  - Firsthand exposure to disconnected CAD / machine / ERP data at IMTEK Cryogenics, a
    high-mix low-volume precision manufacturer (2022-2024).
  - Cambridge MPhil research measuring exactly this interoperability gap.
  - Angel advice from Daniel Theobald that furniture is the easiest entry because wood is more
    tractable than metal. This is a manufacturability claim inside his competence; the
    "therefore furniture" step carries a demand claim that is not.
- SISP status: **probable**
  - The favoured solution (autonomous panel factory, D2C, configurable furniture) predates the
    problem statement — it is recorded as the starting point of the *previous* belief too.
  - Desk measurement in `reports/*/research/` had already moved the founder off that position
    once, toward the trade channel and fitted cabinetry. This belief returns to the original
    position, and the thing that moved it back was advice rather than new measurement.
  - Link 2 (own both ends) has no named observation behind it.
  - `probable` is not a verdict. It records how the founder arrived, and it sets what the
    shotgun has to establish on its own rather than inherit.
- What the shotgun must test independently:
  - Whether the design-to-machine handoff is a described, costly pain in whichever industries
    it examines — in operators' own words, without the vocabulary of AI, automation or
    interoperability.
  - Whether owning the factory is actually required, or whether the same economics are
    reachable by a layer over machines the company does not own. The shotgun may return a
    candidate that contradicts the D2C/owned-factory preference; that is permitted.
  - Whether furniture is the right wedge at all, against other high-mix low-volume candidates.
    Theobald's advice enters as one hypothesis among several, not as the answer.
  - Whether the founder's own prior measurement — freestanding furniture custom demand under
    1% of generic, 14x thinner than cabinets (E1, E2) — survives contact with the wider
    industry set.

## What would threaten the belief itself

- A company reaching batch-size-one economics on machines it does not own — a Xometry,
  Protolabs or Zoo/KittyCAD-style layer pricing, engineering and dispatching one-off jobs
  across third-party shops at catalogue-like cost and lead time. That falsifies link 2
  directly, and link 2 is what makes this an asset-heavy company rather than a software one.
- Interoperability standards closing the gap without anyone owning both ends — STEP AP242,
  MTConnect, UMATI or QIF reaching the point where CAD, CAM, ERP and machine actually pass
  data cleanly. If the coupling stops being broken, owning it stops being worth anything.
- NOT accepted as a belief-level threat (founder decision, 2026-08-31): "owned-factory
  operators fail at the same rate as asset-light ones." It was offered and rejected, and the
  rejection is recorded so it is not re-proposed. The reasoning that made it weak: the D2C
  custom-goods graveyard mostly died of customer-acquisition cost, not manufacturing —
  Interior Define died in 2022-23 on contract-factory and shipping costs while asset-light;
  Model No. owned its Oakland factory and parametric configurator and was absorbed by its
  3D-printing supplier. Owning a factory does not fix CAC. A finding that D2C custom goods
  have an acquisition-cost problem threatens the **company**, not this belief. Do not let
  those two get logged as the same thing.

The two accepted threats share a shape worth naming: both attack link 2, not link 1. Nothing
the founder accepted would falsify "the coupling is broken" — only "you have to own both ends
to fix it." That is the correct place for the risk to sit, since link 1 is the first-hand half.

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
