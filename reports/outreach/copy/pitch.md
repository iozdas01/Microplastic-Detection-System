---
purpose: The pitch for this idea — every audience variant as a claim-traced deck or script, the one-slide block, and the version log of how the story changed and what forced it.
idea: industrial-process-data-infrastructure
last_updated: 2026-09-14
variants: [investor]
---

# Pitch

## Investor deck v2 — slide-by-slide build brief

Seven slides in the founders' order, plus two optional appendix slides. For each slide: what it
has to do, the exact copy that goes on it, the visual, what to say out loud, and where every
claim comes from. `[OPEN]` is a founder decision the brief cannot make; resolve these before the
deck leaves the team.

Source tags: `E{n}` ledger entry · `call:adidas` = E9–E11 and `call:hm` = E7–E9 (Baltic Jungle Lab
brand calls, captured 2026-09-14) · Matter call = E5–E6 (NDA) · `web` a public source, URL given ·
`edge` founder file or repo artefact · `ASSUMPTION` a number we chose, labelled on the slide.

### Design system

Taken from the Lattice title reference (black ground, false-colour micrograph, dithered data).

- **Ground:** pure black `#000000` on every slide. No white slides.
- **Palette:**
  - Violet `#8A4FC7` (primary image tone; the fibre)
  - Cyan `#3CC8D8` (the detection highlight; use sparingly, one element per slide)
  - Cream `#E9E4D6` (dithered pixel blocks, secondary text)
  - White `#FFFFFF` (headlines and body)
- **Type:**
  - Headlines: heavy grotesk (Helvetica Neue Bold, Inter Black or Neue Haas Display Bold), tight tracking, set large (title 160pt+, slide headlines 44–56pt).
  - Body: the same family at Regular, 18–22pt, white.
  - Numbers: Bold, cyan or white.
  - Sources: 9–10pt cream at 60% opacity, bottom-left.
- **Motifs, and what they mean.** Use them with that meaning, not as decoration.
  - **False-colour micrograph** (violet fibres, spiky texture): the physical world, the fibre itself.
  - **Thin white outline squares:** a detection box. Wherever the deck says "we see it", draw one around the thing being seen.
  - **Dithered cream pixel blocks dissolving off the image:** the physical becoming data. Heavier dithering on the Solution and Why-the-future slides.
  - **Cyan inset tile:** the one thing on the slide identified correctly. Use it for the number or image that carries the slide.
- **Layout rule:** at most one headline, one number and three short lines per slide, and every slide readable in 10 seconds. The detail lives in the speaker notes, not on the slide.
- **Imagery:** use real micrographs of polyester and cotton fibres, ideally from the imaging rig (`cad/imaging-station`) or an SEM library with its licence recorded. No stock "ocean plastic" photos: they signal consumer awareness, and the deck is about industrial measurement.

---

### Slide 1 · Title

**Job:** name and promise in one look.

**On slide**
- `Lattice` (huge, left third, white)
- Tagline: `Sensing the impossible.`
- Subline (small, cream): `Observability for physical industrial processes`
- Footer (tiny): `Sandra Zalas · Izgin Ozdas · Pre-seed · {month} 2026`

**Visual:** the reference image as is. The violet micrograph fills the right two-thirds, one cyan
inset tile, and outline squares on two fibres so they read as detected.

**Say out loud:** "Every microfibre number in textile manufacturing today arrives weeks after
the batch it describes. We measure it while the batch is still in the machine."

**Sources:** `belief` (vision/mission ladder, `input-context/belief.md`).

**Open:**
- `[OPEN]` whether "Lattice" is the registered name, and its relation to Baltic Jungle Lab.

---

### Slide 2 · Problem

**Job:** make the investor feel that nobody can currently prove how much fibre a fabric, a batch or a filter releases.

**On slide**
- Headline: `Nobody can prove how much fibre a factory lets go.`
- Three lines:
  1. `A lab result takes ~4 weeks and €390 a sample. The batch is long gone.`
  2. `Suppliers dispute the number: "You are crazy, it doesn't shed."`
  3. `A filter sold at 90% capture measured 68%.`
- Big number (cyan tile): `25×`, with the label `more microfibre from wet processing than from home laundry`.

**Visual:** split frame. On the left, a filter paper under a microscope, labelled "lab: 4 weeks". On the right, the dye
machine outlet, labelled "now: nothing". A single outline square sits empty over the outlet.

**Say out loud:**
- Today the industry manages fibre with a proxy. H&M's supplier limit is TSS at 30 mg/L, and its own water lead says "we do not necessarily control microfiber."
- The one brand chemist who ran the analysis herself says a single FTIR sample takes a day.
- Filters get sold on capture rates that independent tests do not reproduce.

**Sources**
- €390 per wastewater sample plus a €97 order fee, results 4 weeks after receipt: Measurlabs, accessed 2026-09-14 — https://measurlabs.com/products/microplastics-in-water-and-wastewater-micro-raman/ (the range across US/EU labs is 5 business days to 6 weeks, €190–950).
- "You are crazy because it doesn't shed" and "one sample, it takes one day": `call:adidas`.
- 30 mg/L TSS limit, "we do not necessarily control microfiber": `call:hm`.
- 90% claimed vs 68% measured (Politecnico di Torino, Aug 2025), and the maker's reply "Results obtained with the more precise method will be significantly lower" — https://blog.planetcare.org/independent-study-confirms-planetcare-as-the-best-washing-machine-microfiber-filter/
- 25×, and dyeing at about 95% of wet-process emissions: Wang et al. 2023, *Environ. Sci. Technol.*, doi:10.1021/acs.est.3c06210. This is a single-factory model; say so if asked.
- TSS as the rulebook proxy: `E3`.

**Do not use**
- "8 hours to 14 days" (from the v1 one-pager). No lab publishes a turnaround in hours.

---

### Slide 3 · Solution

**Job:** show the thing, and show that the loop closes.

**On slide**
- Headline: `Every discharge, measured before the next one starts.`
- Three lines:
  1. `An at-line module on the dye machine's discharge line captures fibres on a membrane and images them under polarised light.`
  2. `Counts and sizes every fibre, and splits synthetic from natural by polarisation: per stage, per batch, per kg of fabric.`
  3. `Feeds the number back to the process, and measures before and after the treatment plant to prove filtration works.`

**Visual:** the block diagram from the optical technology brief, redrawn on black.
- Discharge line → isokinetic bypass (50–200 mL/min) → degas, cool, prefilter.
- Capture-and-image cell: 10 µm membrane, 530 nm LED, crossed polarisers, global-shutter camera. This is the cyan tile.
- Classifier → fibres/kg per step → dashboard.
- Membrane tape advances between measurements.
- Synthetic fibres glow violet in the crossed field; natural fibres stay dark.

**Say out loud**
- We automate the lab reference method (filtration → microscopy → polarised light). It is not new physics.
- A fibre is long and, if synthetic, birefringent:
  - Shape rejects bubbles and dye aggregates.
  - Polarisation brightens synthetics whatever the dye colour.
  - Optics do not care about the conductivity, salt or heat that break electrical sensors.
- What we claim:
  - Counting from about 5–10 µm width.
  - Synthetic vs natural from about 20–30 µm at first.
  - Polymer identity stays with periodic lab µFTIR/Raman, through a retention-sample port.
- The main risk is contrast in dyed water. A "Stage 0" contrast experiment (known polyester and cotton fibres in dyed, salted, surfactant water) settles it in days on a minimal budget. That known-concentration spike test is exactly what adidas's microfibre lead told us to run first.

**Sources**
- Optical technology brief (Detection and counting of microfibers in wastewater from wet textile processes, 2026-09-07; kept at `private/tech/`).
- Output priority (size distribution first, material second): `E10`.
- Before/after-ETP placement and no flow stoppage: `E8`.
- Imaging rig for training data: `edge` `cad/imaging-station/README.md`.

**Be honest:** nothing is built beyond the imaging-rig design. Stage 0 has not run, and the
lab kit for it is planned for after investment. Never state an accuracy on the slide.

---

### Slide 4 · Why now

**Job:** three dated forces that make 2026–27 the window.

**On slide**
- Headline: `The number stopped being optional.`
- Three columns:
  - **Claims** · `27 Sept 2026` · `EU bans unsubstantiated green claims (Dir. 2024/825).`
  - **Industry** · `April 2026` · `adidas, lululemon, Primark and Tesco fund a 15-mill test of whether TSS can stand in for fibre counts.`
  - **Tech** · `<$1,000` · `open flow imagers reach 2.8 µm/px; classifiers separate synthetic from natural fibre at up to 98%.`
- Second footer line: `TMC and ZDHC intend maximum allowable limits for fibre fragments in discharged effluent (Fashion for Good / TMC, 2025).` (`E14`)
- Footer line: `Also: Inditex grades mills on fibre release (July 2026) · EU wastewater plants must monitor microplastics, method due July 2027 · EU textile ecodesign act Q4 2027.`

**Visual:** a timeline strip on black (2026 → 2028) with cyan dots on the dated events. The
micrograph appears only as a thin band along the bottom edge.

**Say out loud:**
- The industry is testing, this year, whether its cheap proxy is good enough.
- Either the proxy fails and direct counting becomes the standard, or it passes and mills need per-batch data to stay under it.
- Both roads need a number per batch that nobody can currently produce.

**Sources**
- Directive (EU) 2024/825, applies 27 Sept 2026 — https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng
- TMC and ZDHC Phase 2, 15 facilities, April 2026 — https://www.roadmaptozero.com/post/the-microfibre-consortium-and-zdhc-advance-joint-research-to-strengthen-wastewater-monitoring-of-fibre-fragmentation
- Inditex GTW 3.2: `E4`.
- UWWTD 2024/3019 Art. 21, method due 2 July 2027: technology-map T46.
- ESPR textiles act planned Q4 2027, with microplastic release "including manufacturing" as a parameter: technology-map T49 plus JRC prep study — https://susproc.jrc.ec.europa.eu/product-bureau/sites/default/files/2025-12/Textile-Prep-Study_3rd-Milestone_20251212.pdf
- PlanktoScope, under $1k in parts, 2.8 µm/px — https://prakashlab.stanford.edu/projects/planktoscope
- 96.7–98.6% synthetic vs natural classification — https://arxiv.org/abs/2601.15769
- $10 phone microscope with YOLOv5, 98% — https://pubs.rsc.org/ra/article/15/14/10473/867916/

**Do not say**
- "Greenwashing is dead." The broad Green Claims Directive is stalled.
- "Regulation is forcing mills." None of these duties is a discharge limit on a mill.

**Volunteer if asked:**
- The revised EU reporting standards (3 July 2026) drop textile microfibre disclosure from FY2027.
- Adidas's lead expects no brand microplastic claims for 5–10 years.

---

### Slide 5 · Team

**Job:** why these people can build a sensor and sell it into a dyehouse.

**On slide**
- Founder tiles, photo plus one line each:
  - `Sandra Zalas — CEO.` `Founder, Baltic Jungle Lab. PFR School of Pioneers winner. Ran the brand discovery calls.`
  - `Izgin Ozdas — CTO.` `Ran CNC-line automation at IMTEK. Cambridge MPhil in manufacturing interoperability.`
  - `Jeffrey Chang — Founding engineer, ML.` `Imperial. Physics-informed neural networks at NVIDIA; computer vision.`
  - `Irfan Ali — Textile data and machine optimisation.`
- Advisors row, smaller:
  - `Manu Prakash — Stanford Bioengineering, MacArthur Fellow 2016. Foldscope, PlanktoScope. The Stanford lab we are building with.`
  - `Dr Sam Brooks — Cambridge IfM, Distributed Information & Automation Lab. Connected factories.`
  - `Daniel Theobald — Co-founder Vecna, Vecna Robotics, MassRobotics. MIT. 60+ US patents.`

**Visual:** square photo tiles, each inside a thin white outline square (the detection-box
motif); the advisors row in cream.

**Say out loud:**
- Hardware and factory automation, the textile side, and ML.
- Manu Prakash's lab builds the cheapest quantitative imagers in the world, and we are working with it on the optics.

**Sources**
- Founder files: `founders/izgin-ozdas.md`, `founders/sandra-zalas.md`.
- Jeffrey's background: self-described on the Matter call, 2026-09-04.
- Prakash as the Stanford collaborator: founder confirmation, 2026-09-14. It was also referenced on the Matter call ("working with the professor at Stanford").
- Advisor bios verified 2026-09-14: PlanktoScope images plankton; Theobald has 61 granted US patents.

**Open**
- `[OPEN]` Igor Veredyn introduced himself on the H&M call as "the technical co-founder". Is he on this slide?
- `[OPEN]` Irfan Ali's one-liner, in his own words.
- `[OPEN]` Has each advisor agreed to be named?
- `[OPEN]` Sandra's lines to be confirmed by her.

---

### Slide 6 · Traction

**Job:** show that the people who would buy this have looked at it and leaned in. Pre-revenue
and pre-funding, stated plainly.

**On slide**
- Headline: `Design partners are asking for the number.`
- Three partner cards:
  1. **Matter** (industrial microfibre filtration; Earthshot Prize finalist). `In conversations under NDA. Invited us to co-pilot on a contracted textile-mill site.` `[CHECK NDA: agree this wording with Matter before external use]`
  2. **adidas.** `"This is the first time I've come across such a device."` — microfibre lead. `Introductions to brand partners and Fashion for Good once the prototype works.`
  3. **H&M Group.** `"No one is… monitoring."` — innovation and water team. `Open to arranging a supplier-site visit.`
- Bottom strip (small):
  - `CyFract: first-site talks` `[OPEN: status]`
  - `Fashion for Good` `[OPEN: add once the call is logged]`
  - `142 decision-makers targeted across mills, utilities and membrane makers`
  - `Pre-revenue · pre-funding`

**Visual:** three black cards, partner logos only with permission, with quote text in cream. One
cyan outline around the adidas quote.

**Say out loud**
- None of these pays us yet, and we say so.
- **Matter** has to prove, site by site, what its filters remove, and today it waits on the lab. We are the measurement.
- **adidas and H&M** both told us the same two things: the industry manages fibre with a TSS proxy, and nobody measures fibres in the plant.
- **Next milestones:** the Stage 0 contrast test, then the Matter co-pilot.

**Sources**
- Matter: `E5`, `E6` (call 2026-09-04, NDA; capture at `reports/03-validation/H1A5-2026-09-04/`); company entry CO13.
- adidas: `E9`, `E10`.
- H&M: `E7`, `E8`, `E9`.
- CyFract first-site talks: recorded in the H2 change_reason, removed from the lineage 2026-09-15 (git history; CyFract is a site, not a payer).
- 142 targeted: `reports/outreach/contacts.md` totals.

**Do not claim**
- A signed LOI or any pilot, until the ledger holds one.
- "25+ discovery calls / 2 design partnerships", until those calls are logged.
- Matter's call contents or numbers (NDA).

---

### Slide 7 · Why the future

**Job:** the beachhead is countable; the company is bigger.

**On slide**
- Headline: `Every dye machine first. Every industrial liquid next.`
- Market, bottom-up, three stacked numbers:
  - `~3,000` `dyeing machines shipped a year`
  - `50–150k` `in service`
  - `$0.4–2.3B` `hardware + $60–450M/yr software`
- Expansion arrow: `Dye outlets → treatment-plant performance → filter makers → municipal wastewater (EU monitoring duty) → any industrial liquid`
- Closing line: `Lattice: the observability layer for physical processes.`

**Visual:** the heaviest dithering in the deck. The violet micrograph fully dissolves into
cream pixel blocks that resolve into a grid, the "lattice".

**Say out loud**
- The beachhead is a place to learn, not the destination.
- Every installed module adds to a cross-factory shedding benchmark that no lab, brand or regulator holds.
- That dataset, and the loop back to the machine, is the platform: sensing, then the machine data we already read, then models that tell the line what to change.

**Sources**
- ITMF overflow and air-jet dyeing machine shipments: 2,389 (2022), about 2,837 (2023), 3,128 (2024), about 3,802 (2025) — https://www.textileworld.com/textile-world/2026/07/itmf-global-textile-machinery-shipments-shrunk-in-2025-except-for-spinning/
- `ASSUMPTION` 15–20 year machine life, plus local makers ITMF misses → 50–150k.
- `ASSUMPTION` $8–15k hardware and $100–250 per machine per month software. No public comparable price exists; label both on the slide as assumptions.
- EU wastewater monitoring: technology-map T46. Vision: `belief`.

**Open**
- `[OPEN]` the ask: the amount, and what it buys (a prototype validated against known concentrations, then the first plant pilot).
- `[OPEN]` the "silica microballoon" sketch from the handwritten notes. What is it, and does it belong here?

---

### Appendix A · Competition (optional; use if asked "who else")

**On slide:** a 2×2.
- **x-axis:** lab sample → inline.
- **y-axis:** counts only → says what the particle is.
- **Quadrants:**
  - Top-left: Agilent LDIR, HORIBA, Purency, Hohenstein (lab; identify).
  - Bottom-right: Mettler FBRM, Malvern, TSS probes, Process Imaging ViPA (inline; count only).
  - Top-right, alone: Lattice, with ZAITRUS just below it (inline; plastic/metal/biological, sewage and food, pilots).
  - Wasser 3.0 near the centre (stain-and-microscope samples, markets "hourly monitoring" in textiles).

**Say out loud:** "The inline instruments can't say what a particle is; the ones that can are lab-only.
The nearest to us is ZAITRUS, which targets sewage and food and does not claim fibre identity."

**Sources:** competitor research 2026-09-14
- https://www.zaitrus.de/en/technologie/
- https://wasserdreinull.de/en/blog/microplastic-analysis-analytics/
- technology-map T24–T31

### Appendix B · Risks (optional; volunteering beats being caught)

1. The TMC/ZDHC study shows TSS is a good-enough proxy. Then mills use probes they already own, and we sell per-batch resolution rather than the only number.
2. Dye colour and background noise defeat optical detection in untreated effluent, the first technical risk Adidas's chemist raised. Mitigation: a bypass line with dilution, and training on known concentrations.
3. Dye-machine controller makers (Setex, Sedo) accept sensor inputs, but no public route lets a third party write back into the dye programme.
4. Brands wait for regulation (H&M), and microplastic claims are 5–10 years out (Adidas). The first buyer is the mill under an Inditex-type grade, or a filter maker proving performance.

---

## Drift check — 2026-09-14 (v2)

**Changed from v1:**
- The company is named (Lattice).
- The problem widens from "brand grading" to "nobody can prove the number", which covers fabric, batch and filter.
- Traction now rests on two brand calls and Matter.

**Forward (deck ahead of evidence)**
- Both brand calls are not yet in `evidence.md`. The capture needs:
  - the call dates;
  - contact cards for three people;
  - confirmed outcomes (proposed: H&M weak for H1A2, Adidas moderate_confirm).
- The Matter LOI status, "25+ calls" and the GCA year are unsourced.
- The market prices are ASSUMPTION and labelled as such.
- Web facts on slides 2, 4 and 7 (Measurlabs, PlanetCare, 2024/825, TMC Phase 2, ITMF, arXiv, RSC) are sourced but not graded ledger entries. Log the ones that carry a slide.

**Backward (evidence ahead of the hunch)**
- H&M says its supplier ask is a TSS limit, not a fibre count. That cuts against H1A2's "being asked for a microfibre number", as E3 did.
- The Adidas call supports a different pain: the brand cannot get per-fabric shedding data, and suppliers dispute lab numbers. That may be a new or reframed assumption. It is a founder decision, not made here.

## One-slide version

```yaml
slide:
  one_liner:
    text: "Lattice measures microfibre release at the dye-machine outlet in seconds, per batch, instead of a lab result four weeks later."
    cite: "call:adidas; web (Measurlabs)"
  problem:
    - {text: "A lab microplastic result takes ~4 weeks and €390 a sample.", cite: web}
    - {text: "The industry manages fibre with a TSS proxy (H&M: 30 mg/L) that cannot see fibres.", cite: "E3; call:hm"}
    - {text: "Filter capture claims do not survive independent tests (90% claimed, 68% measured).", cite: web}
  solution:
    - {text: "In-water imaging module: size distribution first, synthetic vs natural next, tagged to batch and machine.", cite: "call:adidas; edge"}
  team:
    - {text: "Sandra Zalas (CEO), Izgin Ozdas (CTO); advisors Manu Prakash, Dr Sam Brooks, Daniel Theobald.", cite: "edge (partly unconfirmed)"}
  market:
    - {text: "~3,000 dyeing machines shipped a year; 50–150k in service; $0.4–2.3B hardware at assumed prices.", cite: "web (ITMF) + ASSUMPTION"}
  open_questions:
    - "Does TSS survive the 15-mill TMC/ZDHC study as a proxy?"
    - "Who pays first: the graded mill, the filter maker, or the brand?"
    - "Does the optical module hold up in coloured, untreated effluent?"
```

No slide renderer exists in `scripts/` yet, so this block is not rendered to a page.

## Version log

### 2026-09-14 · investor · first draft, seven slides
Forced by: founder request (deck structure: Title, Problem, Solution, Why now, Team, Traction,
Why the future); E1–E4.
Cut: "no sensors to detect microplastics" (H1 wording) narrowed to "no inline sensor
identifies them", because the technology map shows inline counters exist.
Added: C1–C20; market size and pilot deliberately left UNSOURCED and marked.

### 2026-09-14 · investor · v2, slide-by-slide build brief with design system
Forced by:
- The founder's handwritten outline, the draft one-pager, and the Lattice title design.
- The Adidas and H&M call transcripts.
- Five research passes (advisors, filtration, dye-machine market, why-now, competitors).

Cut:
- "8 hours to 14 days" lab turnaround: no lab publishes hours; replaced by Measurlabs, ~4 weeks and €390.
- "Greenwashing is dead": the broad Green Claims Directive is stalled; replaced by Dir. 2024/825, 27 Sept 2026.
- "Ships" as a use case: IMO does not regulate microplastics in greywater, and ballast rules count organisms.
- "67 patents" (Theobald) → 60+.
- PlanktoScope "particles in water" → plankton.
- "25+ discovery calls / 2 design partnerships": only two transcripts on file.

Added:
- Design system.
- The problem broadened to fabric, batch and filter.
- The 15-mill TMC/ZDHC study as the lead why-now.
- Matter's benchmarking programme as the reason for the LOI.
- Bottom-up dyeing-machine market, with prices labelled as assumptions.
- A competition 2×2 and a risks appendix.

### 2026-09-14 · investor · v3, calls logged, partners named, solution per tech brief
Forced by:
- Evidence E5–E16: the Matter call (NDA), the adidas and H&M calls, and the desk facts.
- The optical technology brief.
- Founder decisions: name adidas and H&M; Matter is in conversations under NDA; "clients/partners/design partners" mean the same thing; pre-revenue and pre-funding; Prakash is the Stanford collaborator.

Cut:
- "Matter LOI in discussion": no LOI on the 2026-09-04 call; replaced by the pilot invitation, pending NDA wording.
- The camera-in-water MVP description: replaced by the at-line polarised-membrane architecture.

Added:
- Named partner cards.
- The Stage 0 contrast test as the next milestone.
- TMC/ZDHC effluent-limit intent (E14).
- CyFract and Fashion for Good as open items.
