---
purpose: The pitch for this idea — every audience variant as a claim-traced deck or script, the one-slide block, and the version log of how the story changed and what forced it.
idea: industrial-process-data-infrastructure
last_updated: 2026-09-14
variants: [investor]
---

# Pitch

## Investor deck — seven slides

Drafted 2026-09-14 for an investor audience (the EF Investment Committee at the end of The
Bridge is the nearest one; the ask is not yet decided). Slide order is the founder's: Title,
Problem, Solution, Why now, Team, Traction, Why the future. Every bullet carries its source tag;
the claim table under the deck resolves each tag. `[OPEN]` marks a founder decision the deck
cannot make.

### 1 · Title

- **{Company name}** `[OPEN]`: nothing in the repo records the company name for this idea.
  Baltic Jungle Lab is the co-founder's existing company; whether the deck is BJL's, and
  what Izgin's role in it is, is not recorded (`founders/sandra-zalas.md` flags it).
- One-liner, three candidates, strongest first:
  1. *"Real-time microfibre monitoring for textile mills: the number and the polymer, per
     batch, at the drain."* The wedge, stated as a product. `belief` (ladder: first product)
  2. *"Every microplastic number today comes from a lab, weeks late. We put it in the pipe."*
     Mechanism-first. `C3`, `C5`
  3. *"Real-time particle intelligence for industrial water."* The founders' own wedge line,
     and the vaguest of the three. `belief`
- Subline: founder names, date, "Pre-seed".

### 2 · Problem

Headline: **Mills are now graded on microfibre release, and the only instrument they own
cannot see a fibre.**

- The largest fashion buyer grades its dyeing, printing, finishing and washing mills on it:
  Inditex Green to Wear 3.2 (July 2026) drops a mill from A to B if "fibers and microfibers
  are released into the environment without any internal control." `C1 ← E4`
- The industry rulebook answers with a proxy. ZDHC Wastewater Guidelines Part C require a TSS
  figure, which every mill already logs, and only *recommend* a one-off lab fibre profile.
  `C2 ← E3`
- TSS is a weight. It cannot tell a polyester fibre from a cotton one or from dye sludge, and
  in textile effluent most counted fibres can be cellulosic. `C4 ← map`
- Every published measurement of a mill's own effluent is a lab grab sample. None of them is
  continuous or at-line, and two labs on the same water differing tenfold is normal.
  `C3 ← map`, `C5 ← map`
- Wet processing is where release happens: up to 25× more microfibre than home laundering,
  and dyeing alone is about 95% of wet-process emissions (Wang et al. 2023, global model;
  6.4 kt in 2020). `C6 ← map`

Say out loud: whether a mill *feels* this as a cost today is untested. We know what they are
being asked for, but we have not yet heard a mill describe what answering it costs them.
`C1`, `E4 next_question`

### 3 · Solution

Headline: **A monitor that sits at the dyehouse drain and reports fibres by count, size and
synthetic-vs-natural, batch by batch.**

- **What it measures:** fibres imaged under crossed polarisers. Polyester is about four times
  more birefringent than cotton (retardation 3.4 µm vs 0.7 µm at typical diameters), so they
  separate optically without a spectrometer. `C8 ← edge (cad/imaging-station)`
- **What it adds over TSS:** polymer class and per-batch timing, which a TSS number cannot
  carry. That is the gap the rulebook's own proxy leaves. `C9 ← map T50`
- **What it adds over existing inline instruments:** particle probes (Mettler ParticleTrack,
  Malvern Insitec) have counted and sized particles in pipes for twenty years, but none of
  them says what a particle is. We found no commercial product that identifies microplastics
  in a flow. `C7 ← belief boundaries, map`
- **The loop:** a number tied to the machine and recipe that produced it, so the mill can
  change the process and show the auditor that something changed. `lineage H1`
- **Built today:** a phone-based imaging rig that produces labelled fibre images to train
  the counter (CAD complete, 4.4 µm per pixel). **Not built yet:** the inline sensor.
  `C10 ← edge`

Say out loud: no performance figure exists yet. The rig's first experiments (known polyester
and cotton counts, then a real sample) have not been run. `C10`

### 4 · Why now

Headline: **In 2026 the number stopped being optional on three fronts, and none of them has
an instrument.**

- **Brands:** Inditex writes fibre release into supplier grading from July 2026. `C1 ← E4`
- **Rulebook:** ZDHC says its TSS limits "are likely to be revised downwards", and the
  TMC/ZDHC Phase 2 study (15 facilities, launched April 2026) is testing whether TSS works as
  a fibre proxy at all. `C2 ← E3`, `C11 ← map T50`
- **Regulators:**
  - California drinking water: Phase II treated-water monitoring is on the State Water
    Board's own timeline for autumn 2026 to autumn 2028, with lab Raman/FTIR as the method
    and positive results printed in the utility's public Consumer Confidence Report.
    `C12 ← E1, E2`
  - EU Urban Wastewater Treatment Directive (in force 2025): every plant above 10,000
    population-equivalents monitors microplastics at inlet and outlet, with the method due by
    July 2027. `C13 ← lineage H4, map T46`
  - California DTSC lists microplastics as a Candidate Chemical from 2026-10-01; textiles
    and apparel are under preliminary research for a Priority Product. `C14 ← map T52`

Say out loud: none of these is a discharge limit on a mill. They are grading and monitoring
duties, and every one is met today by a lab sample. `C13`, `C14`

### 5 · Team

- **Izgin Ozdas.** Ran CNC-line robot automation and ERP rollout at IMTEK Cryogenics
  (2022–24), the manual measure-and-readjust loop this company automates. Cambridge MPhil
  (IfM) on manufacturing-data interoperability: an LLM annotator scoring 100% F1 on DXF and
  74% on STEP metadata. SPIE 2025 paper. Georgia Tech BS ME. Designed the imaging rig.
  `C15 ← edge`
- **Sandra Zalas.** Founder and CEO of Baltic Jungle Lab, microfibre monitoring for textile
  factories since 2025. Won the PFR School of Pioneers; semi-finalist in the H&M Foundation
  Global Change Award. Fashion-side access and the problem narrative. `C16 ← edge, unconfirmed`
- `[OPEN]` Whether BJL's CTO is on this slide. `founders/sandra-zalas.md` says not to list
  him until the team structure is confirmed.

### 6 · Traction

Headline: **Three buyer segments mapped and 142 people targeted; the first conversations
start now.**

- 142 decision-makers qualified from live profile reads across three segments: textile
  wet-processing mills, California water utilities, and RO/UF membrane makers. 98 connection
  requests sent, 22 accepted. `C17 ← contacts.md totals`
- The technical landscape is mapped: 34 detection methods plus the 21 standards that
  prescribe how the number must be reported, each graded on how close to a running pipe it
  has actually got. `C18 ← map`
- `[OPEN]` Pilot scoping with an SF research lab, from the co-founder's public post. It is
  unconfirmed and the lab is unnamed, so it stays off the slide until she confirms.
  `C19 ← UNSOURCED`

Say out loud: zero customer conversations so far. This is the slide that can change most
before the committee. Ten conversations with wet-processing leads, the test graph.md already
names for H1A2, would replace the headline.

### 7 · Why the future

Headline: **The sensor is the wedge. The company is the layer that tells a production line
what its data means.**

- The belief: models will not run production lines until real-time process data arrives
  with identity and meaning attached, and nobody is building that layer. `belief`
- The instrument sees the same gap from three sides: mills graded on release (H1),
  utilities reporting a lab number (H3), and membrane makers settling fouling claims without
  knowing the foulant (H5). One instrument, three budgets to test. `lineage`
- The platform path: sensing, then existing machine data, then interoperability, then models,
  then recommendations. Every installed monitor adds to a cross-factory benchmark nobody else
  holds. `belief ladder`
- `[OPEN]` The ask: money, an introduction, or judgement on one question. This has to be
  decided before the meeting.

Say out loud: we have not sized the market. No scale arithmetic exists yet, and we would
rather say that than show a top-down number. `C20 ← UNSOURCED`

### Claim table — investor deck

| # | Claim | Source | Grade / note |
|---|---|---|---|
| C1 | Inditex GTW 3.2 drops a mill A→B for uncontrolled fibre release | `E4` | 4 · asks for "control", not a number |
| C2 | ZDHC Part C requires TSS only; fibre profile recommended; limits likely revised down | `E3` | 4 · ambiguous for H1A2 |
| C3 | Every published mill-effluent measurement is a lab grab sample | `map` technology-map "Textile-mill effluent measured so far" | desk batch, 2026-09-10 |
| C4 | TSS cannot separate synthetic from cellulosic; many effluent fibres are cellulosic | `map` reading notes, T50 | not a ledger entry |
| C5 | Inter-lab spread of 10× on the same water; fibres ID'd 76% (IR) / 30% (Raman) in CA trial | `map` reading notes | not a ledger entry |
| C6 | Wet processing up to 25× home laundering; dyeing ~95%; 6.4 kt (2020) | `map` Wang et al. 2023, ES&T | denominator: global wet-process microfibre emissions, modelled |
| C7 | Inline counters exist; none identifies microplastics in flow | `belief` boundaries + `map` T31 et al. | founder-confirmed precedent check |
| C8 | Crossed-polariser birefringence separates polyester from cotton | `edge` cad/imaging-station README | physics, not yet measured on the rig |
| C9 | TSS misses polymer identity and per-batch timing | `map` T50 note | inference |
| C10 | Imaging rig designed; inline sensor not built; experiments not run | `edge` cad/imaging-station README | — |
| C11 | TMC/ZDHC Phase 2, 15 facilities, April 2026 | `map` T50 | not a ledger entry |
| C12 | CA Phase II autumn 2026–28; CCR public disclosure | `E1`, `E2` | 4 · plan, no order issued yet |
| C13 | UWWTD Art. 21 monitoring ≥10k p.e., method by July 2027 | `lineage` H4, `map` T46 | monitoring, no limit |
| C14 | DTSC Candidate Chemical from 2026-10-01; textiles under preliminary research | `map` T52 | no duty yet |
| C15 | Izgin's background | `edge` founders/izgin-ozdas.md | patent ID unverified, not used |
| C16 | Sandra's background | `edge` founders/sandra-zalas.md | **unconfirmed by her** |
| C17 | 142 targeted / 98 invited / 22 accepted / 0 conversations | contacts.md `totals` | counts change daily; re-read before pitching |
| C18 | Technology map scope | `map` technology-map.md | — |
| C19 | SF research-lab pilot scoping | **UNSOURCED** | public post only |
| C20 | Market size | **UNSOURCED** | none computed |

## Drift check — 2026-09-14

First draft, so there is no older pitch to drift from. Checked against the whole ledger (E1–E4)
and the three active hunches.

**Forward: the deck is ahead of the evidence.**

- **Market size (C20).** Nothing in the repo. Options: build bottom-up arithmetic (number of
  ZDHC-audited wet-processing sites × a price) as a ledger entry, or keep the volunteered
  hole. Do not use a top-down "microplastics testing market" figure; its denominator would be
  lab services, not this product.
- **Price and buyer.** H1's plausible buyer is "unknown" in the lineage, and no price exists.
  The deck avoids both. An investor will ask "who pays", and the honest answer today is "the
  mill, for the Inditex audit — untested."
- **Device performance (C8, C10).** Physics only. The deck states "designed to", never "does".
- **Sandra's claims (C16, C19).** Her file says to ask her before citing anything. Needs her
  sign-off before the deck leaves the repo.
- **Map-sourced claims (C3–C6, C9, C11, C13, C14).** These are sourced with URLs but are not
  graded ledger entries. If any of them becomes load-bearing in Q&A (C4 and C6 most likely),
  log it in `evidence.md` against H1A2 or H1A5 so it gets a grade.

**Backward: the evidence is ahead of the hunch wording.**

- **H1's statement says "there are no sensors to detect microplastics."** The technology map
  contradicts the literal wording: inline counters exist. The deck uses the sharper claim
  that survives, "no inline sensor says what the particle is" (C7). Rewording H1 is a founder
  decision, and this pitch does not make it.
- **E3 cuts against "a mill cannot produce the number".** The number the rulebook asks for is
  TSS, which mills already have. The deck turns this into the argument (the proxy is weak,
  and the industry is testing it in Phase 2) rather than hiding it. If Phase 2 validates TSS
  as a good-enough proxy, slide 2 loses its centre.

**Open founder decisions:** company name (slide 1); the lead door (the deck leads with textiles
because that is where E3/E4 sit and where the first product was aimed, with H3/H5 as
expansion); the CTO on slide 5; Sandra's sign-off; the ask.

## One-slide version

```yaml
slide:
  one_liner:
    text: "Real-time microfibre monitoring for textile mills: the number and the polymer, per batch, at the drain."
    cite: belief
  problem:
    - {text: "Inditex now grades wet-process mills on microfibre release (GTW 3.2, July 2026).", cite: E4}
    - {text: "The industry rulebook answers with TSS, a weight that cannot tell polyester from cotton.", cite: E3}
    - {text: "Every published mill-effluent measurement is a lab grab sample.", cite: map}
  solution:
    - {text: "Polarised-light imaging at the drain: count, size, synthetic vs natural, per batch.", cite: edge}
    - {text: "Inline counters exist; none says what the particle is.", cite: belief}
  team:
    - {text: "Izgin Ozdas: CNC-line automation at IMTEK; Cambridge MPhil in manufacturing-data interoperability.", cite: edge}
    - {text: "Sandra Zalas: founder of Baltic Jungle Lab; PFR School of Pioneers winner.", cite: "edge (unconfirmed)"}
  market:
    - {text: "Not yet sized.", cite: UNSOURCED}
  open_questions:
    - "Does a mill experience the Inditex grade as a cost?"
    - "Who pays: mill, brand, or effluent operator?"
    - "Does TSS survive TMC/ZDHC Phase 2 as a proxy?"
```

No slide renderer exists in `scripts/` yet, so this block is not rendered to a page.

## Version log

### 2026-09-14 · investor · first draft, seven slides
Forced by: founder request (deck structure: Title, Problem, Solution, Why now, Team, Traction,
Why the future); E1–E4.
Cut: "no sensors to detect microplastics" (H1 wording) narrowed to "no inline sensor
identifies them", because the technology map shows inline counters exist.
Added: C1–C20 as above; market size and pilot deliberately left UNSOURCED and marked.
