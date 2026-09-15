---
purpose: The technology map — one entry per way of detecting microplastics or microfibres in water (what it physically measures, how small it goes, how far from the process it has actually run, who sells it) plus one entry per standard or rule that prescribes how the number must be reported.
idea: Microplastic Detection System
schema_version: 1
last_updated: 2026-09-14
# ─── Map axes (proposed 2026-09-10, awaiting founder confirmation) ───────────────
# The question this map answers is "how could anyone measure this, and how close to a
# running pipe has each way actually got?" Every value records what has been DEMONSTRATED
# in water, never what a vendor page or abstract claims is possible. Two honest readers
# of the same sources should agree on every value; a judgement call goes in the entry's
# notes and is graded conservatively (the less mature, the less process-near option).
map_axes:
  x: deployment
  y: polymer_id
  colour: maturity
  size: size_class
  family: family
map_axis_labels:
  deployment: "How close to the process it has run"
  polymer_id: "What it says about the particle"
  maturity: "Maturity"
  size_class: "Smallest particle it resolves"
  family: "Family"
map_vocabularies:
  kind: [technology, standard]
  # Ordered lab bench → pipe. The value is the most process-near deployment actually
  # demonstrated in water, not the most process-near one claimed.
  deployment: [lab_offline, at_line, inline_realtime]
  # Ordered by how much the number says about the particle.
  polymer_id: [none, class_level, polymer_level]
  # Ordered by how real it is for a buyer today.
  maturity: [research, commercial_prototype, commercial_instrument, standard_method]
  # Same keys as research-map.md `size_class`, so a paper row and a technology entry
  # can be read against each other. Ordered coarse → fine.
  size_class: [over_300um, 100_300um, 10_100um, 1_10um, sub_micron]
  family: [vibrational_spectroscopy, thermal_mass, optical_imaging, flow_counting, inline_particle, emerging_sensor, sampling_prep]
  outputs: [count, size, shape, polymer_class, polymer_identity, mass, concentration]
map_value_labels:
  deployment: {lab_offline: "lab, offline", at_line: "at-line", inline_realtime: "inline, real time"}
  polymer_id: {none: "count / size only", class_level: "plastic or not", polymer_level: "names the polymer"}
  maturity: {research: "research", commercial_prototype: "commercial prototype", commercial_instrument: "commercial instrument", standard_method: "standard method"}
  size_class: {over_300um: "> 300 µm", 100_300um: "100–300 µm", 10_100um: "10–100 µm", 1_10um: "1–10 µm", sub_micron: "< 1 µm"}
  family: {vibrational_spectroscopy: "Vibrational spectroscopy", thermal_mass: "Thermal & mass-based", optical_imaging: "Optical imaging & staining", flow_counting: "Flow counting & imaging", inline_particle: "Inline particle instruments", emerging_sensor: "Emerging real-time sensors", sampling_prep: "Sampling & preparation"}
map_family_notes:
  vibrational_spectroscopy: "Shine infrared or laser light on a particle and read the molecular fingerprint. The reference methods; slow, lab-bound, and the only ones that name the polymer particle by particle."
  thermal_mass: "Burn or dissolve the whole sample and weigh the plastic by polymer. Mass, not counts; destructive; the only route to a µg/L number."
  optical_imaging: "Take a picture and decide what it is from shape, colour or a dye. Cheap and fast; cannot say what the particle is made of."
  flow_counting: "Push the water past a detector and count particles one by one. Counts and sizes at speed; polymer only if a spectrometer is bolted on."
  inline_particle: "Probes and analysers the process industry already buys to count and size particles in a pipe. Twenty years old; blind to what the particle is."
  emerging_sensor: "Concepts from 2022–2026 aiming at identification in flow. Research grade unless stated; here so the empty corner of the map has names in it."
  sampling_prep: "Not detectors: the steps before the detector that decide whether the number means anything."
reading_notes:
  - "A particle counter tells you there are particles, not that they are plastic. Inline counters and sizers have existed for 20-30 years; what does not exist is inline identification."
  - "Mass and count answer different questions. One 500 µm fragment weighs as much as about a million 1 × 100 µm fibres; mass methods are dominated by the few biggest particles, count methods by the smallest you can see. Regulators currently want counts."
  - "Microfibre is not microplastic. In textile effluent most counted fibres can be cotton, wool or viscose; every mass method reports zero for those, and every gravimetric shedding test (TMC, ISO 4484-1, TM212) counts them."
  - "FTIR and Raman are complements, not competitors. FTIR imaging is fast and reliable from 50 to 500 µm; Raman is the only routine route to 1-20 µm but four times slower and fluorescence-prone. Neither measures water: every method is filter, digest, dry, then measure."
  - "Fibres are the weak spot of the whole field. In the 22-lab California trial fibres were identified correctly 76% of the time by infrared and 30% by Raman, against 91-95% for particles, so the state exempted fibres from QC."
  - "The detector is rarely the bottleneck; sampling and prep are. Recovery through sampling and clean-up runs 9-92% depending on shape and size, blanks average 91 ± 141 particles, and two labs on the same water differing by ten times is normal."
  - "Size floors are set by recovery, not optics. Europe and California set 20 µm (50 µm for infrared) because recovery collapsed below that. Claiming 1 µm detection in effluent invites a recovery question you cannot answer."
  - "Textile effluent is the opposite regime from drinking water: 100 to a million fibres per litre, so volume is trivial, but solids, dyes, sizing agents and cellulosics blind filters and spectrometers. Do not port a drinking-water design."
  - "Most fibre is created dry and released wet. Cutting and abrasion make the fragments; desizing, scouring and dyeing wash them out, and dyeing is about 95% of wet-process release. Measure at the dye-house drain, not the outfall."
  - "The industry's current effluent proxy is a TSS probe the mill already owns (TMC/ZDHC 2024). A new instrument competes with that probe until it shows what TSS misses, which is the polymer split."
  - "Every physical contrast that identifies plastic (Raman bands, permittivity, impedance) is weak, and every effluent confounder (dye fluorescence, salinity, temperature, surfactants) attacks exactly that contrast. Class-level (plastic or not) and polymer-level (PET or PA6) are different products."
  - "No standard exists yet for microplastics in high-solids water. ISO 16094-2 and -3 are for low-solids water; the EU wastewater method arrives by July 2027; ASTM D8401-24 covers high solids but is a benchtop pyrolysis run."
---

# Technology map — contaminant detection in water

Started 2026-09-10 from five desk batches (vibrational spectroscopy; thermal and mass-based;
optical imaging and flow counting; inline instruments and emerging real-time sensors; sampling,
preparation, standards and the textile test landscape). Every entry was written from sources
opened that day; vendor list prices were public for none of the instruments. Entries marked
research rest on one or two papers and should be re-read before anything is built on them.

## µFTIR imaging with focal-plane-array detectors

id: T1
kind: technology
family: vibrational_spectroscopy
short: µFTIR imaging (FPA)
principle: Broadband mid-infrared light through the filter, a camera-like detector records an IR spectrum at every pixel
plain_language: >
  The filter holding the particles is lit with mid-infrared light while a camera-like detector
  (64×64 or 128×128 pixels) records a full infrared spectrum at every pixel. Software finds the
  pixels whose spectra look like a plastic, groups them into particles, and reports each particle's
  polymer, size and shape. You get a chemical map of the whole filter without a person choosing
  which particle to point at.
outputs: [count, size, shape, polymer_identity, concentration]
size_min_um: 11
size_max_um: 5000
size_class: 10_100um
polymer_id: polymer_level
deployment: lab_offline
maturity: standard_method
time_per_sample: hours per filter for imaging; about 4× faster than automated Raman on the same filter; digestion, filtration and drying add 1-3 days
sample_prep: filtration; Fenton or H2O2 and enzymatic digestion of organics; density separation for solids-rich water; transfer onto an IR-transparent Anodisc on CaF2 (transmission) or gold-coated polycarbonate (reflection); dry
matrices_demonstrated: [drinking water, WWTP effluent and river water, North Sea surface water, Arctic snow and sea ice, industrial laundry wastewater (polyester dominant; up to 40 000 fibres/L; 20 µm floor), Italian textile-company WWTP inflow and outflow (µFTIR polymer ID; 893-4452 fibres/L in, 310-2404 out; acrylic, polyester, PP, PA, viscose), Italian textile dyeing factory water and sludge (two µFTIR systems and three filter materials compared)]
vendors:
  - {name: Bruker, instrument: "LUMOS II (FPA, also ATR) / HYPERION II (FT-IR + QCL)", url: https://www.bruker.com/en/products-and-solutions/infrared-and-raman/ft-ir-microscopes/lumos-ii-ft-ir-microscope.html, price: not public}
  - {name: Thermo Fisher, instrument: "Nicolet iN10 MX / RaptIR (linear-array or imaging MCT)", url: https://www.thermofisher.com, price: not public}
  - {name: PerkinElmer, instrument: "Spotlight 400 (linear-array imaging)", url: https://www.perkinelmer.com, price: not public}
limitations:
  - "Diffraction limit near 10 µm: misses the 1-10 µm fraction that Raman sees; FTIR imaging under-counted by about 35% versus Raman, mostly below 20 µm"
  - Water absorbs strongly in the mid-infrared, so the sample must be dry; no measurement in water
  - Fibres narrower than the 11 µm pixel are partly or wholly lost
  - Anodisc filters block the region below 1250 cm-1; diatom bands interfere
  - Mass estimated from FTIR counts over-estimated Py-GC/MS mass by up to 6×
  - Millions of spectra per filter; different analysis pipelines disagree on the smallest size classes
fibre_performance: >
  Poor at the thin end. In the California 22-lab trial infrared methods identified fibres correctly
  76% of the time against 95% for particles, and the state SOP gives fibres no recovery requirement.
  The 11 µm pixel straddles typical textile fibre widths: 58% of effluent fibres in one WWTP study
  were 10-30 µm wide.
textile_effluent_relevance: >
  µFTIR is the method the textile-effluent literature actually identifies fibres with: an Italian
  textile-company WWTP (2022), an Italian dyeing factory (2025) and an industrial laundry (2024) all
  report micro-FTIR polymer IDs, so this is the reference a mill-side number will be judged against.
  Whether those studies used FPA imaging or point mapping is not established (added 2026-09-11).
  Lab-only: hours per filter, a day of digestion, a spectroscopist to judge matches; a mill buys the
  result from a contract lab, per filter, and the reference itself undercounts thin fibres.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC6113679/
  - https://doi.org/10.3390/microplastics1040040
  - https://doi.org/10.1016/j.scitotenv.2024.175907
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC8440246/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10284987/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC7680748/
  - https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/documents/microplastics/swb-mp1-rev1.pdf
first_added: 2026-09-10
source_date: 2026-09-10

## Laser-direct infrared imaging (QCL / LDIR)

id: T2
kind: technology
family: vibrational_spectroscopy
short: LDIR (QCL imaging)
principle: A tunable mid-infrared laser scans the filter at one wavelength to find particles, then revisits each one to record its spectrum
plain_language: >
  Instead of a lamp, a tunable infrared laser scans the filter at one wavelength to find every
  particle in minutes, then goes back to each particle and sweeps the laser to record its spectrum.
  Only particles get a full spectrum, not empty filter, so it is far faster than FTIR imaging. The
  software runs the find-then-identify loop unattended and outputs a spreadsheet of particles with
  polymer, size and shape class.
outputs: [count, size, shape, polymer_identity, concentration]
size_min_um: 20
size_max_um: 5000
size_class: 10_100um
polymer_id: polymer_level
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: survey of 144 mm² in 36 min; about 8 s per particle, so a filter with 1,500-6,000 particles takes 3-14 h unattended; prep adds 1-2 days
sample_prep: sieve; Fenton oxidation; filter 25-100 mL onto gold-coated polyester (5 µm pore) or dry a 1 mL ethanol suspension on a reflective low-E slide at 100 °C; particle-dense filters need subsampling
matrices_demonstrated: [urban creeks and surface water, WWTP influent and effluent, septic-tank water, seawater and Antarctic water, beverages]
vendors:
  - {name: Agilent, instrument: "8700 LDIR Chemical Imaging System with Clarity software", url: https://www.agilent.com/en/product/molecular-spectroscopy/ftir-spectroscopy/ftir-imaging-systems/8700-ldir-chemical-imaging-system, price: not public}
  - {name: Bruker, instrument: "HYPERION II (hybrid FT-IR + QCL microscope)", url: https://www.bruker.com/en/products-and-solutions/infrared-and-raman/ft-ir-microscopes.html, price: not public}
limitations:
  - Spectral window only 975-1800 cm-1, so oxidised or weathered polymers and some classes are harder to separate
  - 20 µm practical floor; nothing on the 1-20 µm fraction
  - Needs a reflective substrate; low-E slides corrode after acid digestion
  - Single-vendor ecosystem (Agilent library and software); match-quality thresholds are software-specific
  - Particle-dense filters need subsampling, with about 25% relative error
fibre_performance: >
  The software classes shape by aspect ratio (fibre, fibrous fragment, fragment, sphere) and counted
  fibres as 25-39% of WWTP particles. No fibre-specific recovery or width-limit data was found; long
  fibres crossing the scan field and dyed fibres are not separately validated.
textile_effluent_relevance: >
  Run on municipal WWTP influent and effluent, not on a textile mill. The unattended multi-hour run
  is the closest thing in this family to "load and walk away", but prep is still bench chemistry, so
  it is a plant-laboratory instrument, not at-line.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9805365/
  - https://doi.org/10.1021/acs.est.0c05722
  - https://doi.org/10.1016/j.talanta.2024.127284
  - https://doi.org/10.1016/j.scitotenv.2025.178817
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11341343/
first_added: 2026-09-10
source_date: 2026-09-10

## ATR-FTIR on hand-picked particles

id: T3
kind: technology
family: vibrational_spectroscopy
short: ATR-FTIR (picked)
principle: One particle pressed against a diamond crystal gives its infrared spectrum in seconds
plain_language: >
  A technician picks one particle with tweezers, presses it against a diamond or germanium crystal,
  and records its infrared spectrum in seconds. It is the cheapest and most robust polymer
  identification there is, but each particle must be big enough to see and handle, and pressing
  can destroy it.
outputs: [polymer_identity]
size_min_um: 300
size_max_um: 10000
size_class: over_300um
polymer_id: polymer_level
deployment: lab_offline
maturity: standard_method
time_per_sample: under a minute per spectrum; 12 ± 9 min per particle once picking, photographing and matching are included; scales with particle count
sample_prep: sieve to the fraction above 212 or 500 µm; pick under a stereo microscope; no special filter
matrices_demonstrated: [drinking water (California interlab trial), textile-industry WWTP effluent residue (Portugal), marine debris]
vendors:
  - {name: Bruker, instrument: "LUMOS II ATR / ALPHA II with diamond ATR", url: https://www.bruker.com/en/products-and-solutions/infrared-and-raman/ft-ir-microscopes/lumos-ii-ft-ir-microscope.html, price: not public}
  - {name: "PerkinElmer, Thermo Fisher, Agilent, Shimadzu", instrument: any benchtop FTIR with a diamond ATR, url: "", price: not public}
limitations:
  - Cannot address anything below a few hundred µm without a microscope ATR objective
  - Destructive contact; the particle is lost for archiving
  - Operator-limited throughput; selection bias toward large, visible, light-coloured particles
  - Bulk-residue ATR gives polymer presence, not counts
fibre_performance: >
  Single fibres are hard to press flat on the crystal and thin fibres give weak spectra, which is why
  the Portuguese textile-effluent study analysed dried residue in bulk rather than single fibres. No
  fibre-specific ATR accuracy figure found.
textile_effluent_relevance: >
  The only textile-mill effluent spectroscopy found in this family: 7.45 to 3.36 mg per 100 mL across
  a bleaching plant's in-house WWTP and 2.11 to 1.57 for a dyeing and printing plant, PET and
  polyamide dominant. A crude at-line version (filter, dry, press the residue) could give polymer
  presence but not counts or sizes.
sources:
  - https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/documents/microplastics/swb-mp1-rev1.pdf
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11478531/
  - https://doi.org/10.1016/j.marpolbul.2017.12.061
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10566227/
first_added: 2026-09-10
source_date: 2026-09-10

## Raman micro-spectroscopy

id: T4
kind: technology
family: vibrational_spectroscopy
short: Raman microscopy
principle: A focused laser; the tiny fraction of light scattered back with shifted colour is the particle's bond fingerprint
plain_language: >
  A visible or near-infrared laser is focused on one particle and a tiny fraction of the light
  scatters back shifted in colour by the particle's bond vibrations, giving a fingerprint spectrum.
  The laser spot can be under a micron, so this is the only routine technique that identifies the
  1-20 µm fraction. Automated systems photograph the filter, find every particle, then visit each
  one with the laser.
outputs: [count, size, shape, polymer_identity, concentration]
size_min_um: 1
size_max_um: 5000
size_class: 1_10um
polymer_id: polymer_level
deployment: lab_offline
maturity: standard_method
time_per_sample: 5-20 s per particle, so 7,000 particles is 12-48 h; a full-filter WWTP effluent scan was 72 h, so 32% of the filter was measured and extrapolated; prep adds 1-3 days
sample_prep: filtration; Fenton or enzymatic digestion; density separation for solids-rich water; transfer to silicon, gold- or aluminium-coated polycarbonate filters
matrices_demonstrated: [drinking and bottled water, municipal WWTP effluent (mostly PET fibres), North Sea surface water]
vendors:
  - {name: HORIBA, instrument: "XploRA PLUS / LabRAM Soleil with ParticleFinder and IDFinder", url: https://www.horiba.com/int/scientific/applications/environment/pages/microplastics/, price: not public}
  - {name: Oxford Instruments WITec, instrument: "witec360 / alpha300 with ParticleScout", url: https://raman.oxinst.com/products/software/particlescout, price: not public}
  - {name: Renishaw, instrument: "inVia with WiRE particle analysis", url: https://www.renishaw.com, price: not public}
  - {name: Thermo Fisher, instrument: "DXR3 / DXR3xi with particle analysis", url: https://www.thermofisher.com, price: not public}
  - {name: Bruker, instrument: "SENTERRA II / RamanScope", url: https://www.bruker.com, price: not public}
  - {name: TU Munich (academic), instrument: "TUM-ParticleTyper software", url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7310837/, price: free}
limitations:
  - Fluorescence from dyes, pigments, humics, biofilm and clay is the major disadvantage in real samples; mitigated by 785 nm lasers, photobleaching and lower power
  - Black and carbon-black particles absorb, heat and burn under the laser
  - Slow; seconds per particle, thousands of particles per filter
  - Weak signal; match-quality values are not comparable across software
  - Non-uniform deposition makes sub-area extrapolation vary 47-71%
fibre_performance: >
  Worst in class in the interlab trial: Raman labs identified fibres correctly only 30% of the time
  against 91% for particles, driven by dye fluorescence and thin curved geometry; California imposes
  no recovery requirement on fibres. Yet Raman is the method that actually resolved PET effluent
  fibres 10-30 µm wide.
textile_effluent_relevance: >
  No mill-water Raman study found; municipal effluent is the nearest. Dyed fibres are the
  fluorescence worst case, so an at-line textile Raman would need 785 or 1064 nm excitation and a
  bleaching step. In-flow Raman prototypes have only been shown in clean lab water.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC8440246/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC6549938/
  - https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/documents/microplastics/swb-mp2-rev1.pdf
  - https://doi.org/10.1021/acs.est.8b03438
  - https://www.horiba.com/int/scientific/applications/environment/pages/microplastics/
first_added: 2026-09-10
source_date: 2026-09-10

## Surface-enhanced Raman (SERS) for nanoplastics

id: T5
kind: technology
family: vibrational_spectroscopy
short: SERS
principle: A nanostructured gold or silver surface amplifies the Raman signal by orders of magnitude
plain_language: >
  Particles are dried onto or drawn into a nanostructured gold or silver surface; the metal
  amplifies the Raman signal by orders of magnitude, so particles far below the microscope's
  resolution become detectable. You get a polymer fingerprint and, with calibration, a
  concentration, but not individual counts or sizes without a second technique.
outputs: [polymer_class, polymer_identity, concentration]
size_min_um: 0.05
size_max_um: 262
size_class: sub_micron
polymer_id: polymer_level
deployment: lab_offline
maturity: research
time_per_sample: minutes per spectrum; 2-4 samples per hour end to end with a pretreatment-free silver foam; substrate fabrication and drying dominate
sample_prep: 0.1 µm filtration or concentration and drop-drying on the substrate, or a direct dip of porous silver foam without pretreatment
matrices_demonstrated: [bottled drinking water (PET near 88 nm), spiked groundwater and synthetic seawater, humic acid, algae, sediment and soil extracts]
vendors: []
limitations:
  - Sample dispersion on the substrate is an open problem and detection limits are insufficient for real environmental concentrations; nearly all work is on spiked beads
  - Organic matter co-adsorbs and swamps spectra in real water
  - Substrate-to-substrate reproducibility and silver shelf life
  - About 4,000 training spectra needed per new polymer for the classifiers
  - No particle count or size without an added technique
fibre_performance: Only a 20 µm-thick PET fibre has been shown on silver foam; nothing on dyed or thin textile fibres.
textile_effluent_relevance: None found. Dye-laden effluent is the worst matrix for SERS (organic fouling, dye fluorescence). Not a near-term at-line option.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10249414/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11133413/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10100025/
first_added: 2026-09-10
source_date: 2026-09-10

## Spectral-library and particle-analysis software

id: T6
kind: technology
family: vibrational_spectroscopy
short: Spectral software
principle: Turns thousands to millions of spectra per filter into "N particles of PET, 20-50 µm" by library matching or a trained classifier
plain_language: >
  Every spectroscope produces thousands to millions of spectra per filter; the software is what
  turns them into "N particles of PET, 20-50 µm". Options differ in whether they are free, which
  instruments they read, and whether they match spectra to a library or run a trained classifier.
  Any at-line product lives or dies on this layer.
outputs: [count, size, shape, polymer_identity, concentration]
size_min_um: 
size_max_um: 
size_class: 
polymer_id: polymer_level
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: automated FTIR pipelines process a filter in minutes to an hour; manual single-spectrum work is days per sample
sample_prep: n/a (reads the instrument's output)
matrices_demonstrated: [as per the instrument feeding it]
vendors:
  - {name: "Aalborg University and AWI", instrument: "siMPle (freeware for µFTIR imaging, 32-polymer reference database)", url: https://simple-plastics.eu/, price: free}
  - {name: "Open Specy (Cowger et al.)", instrument: "Open Specy 1.0: over 40,000 open Raman and FTIR spectra, CC-BY, hyperspectral batch processing, two ML classifiers", url: https://github.com/wincowgerDEV/OpenSpecy-package, price: free}
  - {name: University of Bayreuth, instrument: "Bayreuth Particle Finder for FTIR imaging", url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10284987/, price: academic}
  - {name: TU Munich, instrument: "TUM-ParticleTyper (Raman and optical particle and fibre detection)", url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7310837/, price: free}
  - {name: Agilent, instrument: "Clarity (LDIR; aspect-ratio shape classes)", url: https://www.agilent.com, price: bundled}
  - {name: Bruker, instrument: "OPUS Find Particles and Cluster ID", url: https://www.bruker.com, price: bundled}
  - {name: HORIBA, instrument: "ParticleFinder and IDFinder", url: https://www.horiba.com/int/scientific/applications/environment/pages/microplastics/, price: not public}
  - {name: Purency (Vienna), instrument: "Microplastics Finder (random-forest classifier on FTIR, LDIR and Raman data); on 2026-09-10 purency.ai served unrelated content, so company status is unverified", url: https://link.springer.com/article/10.1007/s00216-023-04630-w, price: not public}
limitations:
  - Different pipelines on the same FTIR data disagree for specific polymers and the smallest size classes
  - Match-quality thresholds are not transferable between vendors' software, yet regulators pin them (California ≥60% match)
  - Libraries are dominated by pristine reference polymers; weathered, dyed and additive-laden textile fibres match poorly
fibre_performance: Aspect-ratio fibre classing exists in Clarity, TUM-ParticleTyper and the Bayreuth finder; none of the sources report fibre-specific classification accuracy.
textile_effluent_relevance: The open tools (Open Specy, siMPle) are the realistic base for a custom dyed-textile-fibre library; today's options are lab batch tools.
sources:
  - https://simple-plastics.eu/
  - https://github.com/wincowgerDEV/OpenSpecy-package
  - https://doi.org/10.1021/acs.analchem.5c00962
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10284987/
first_added: 2026-09-10
source_date: 2026-09-10

## Pyrolysis-GC/MS

id: T7
kind: technology
family: thermal_mass
short: Py-GC/MS
principle: Burn the whole filter at 600 °C without oxygen; each polymer breaks into marker molecules a mass spectrometer weighs
plain_language: >
  Everything on a filter is dropped into a tiny furnace at about 600 °C in an oxygen-free stream.
  Each polymer breaks into its own set of small molecules; a gas chromatograph separates them and a
  mass spectrometer identifies them, and peak areas against a calibration give micrograms of each
  polymer in the whole sample. No particle count, no sizes, no shapes: a mass per litre.
outputs: [polymer_identity, mass, concentration]
size_min_um: 
size_max_um: 
size_class: sub_micron
polymer_id: polymer_level
deployment: lab_offline
maturity: standard_method
time_per_sample: 20-60 min instrument run; 1-3 days wall-clock with digestion; an autosampler runs overnight
sample_prep: filter a known volume (100 mL to thousands of litres); remove organics (peroxide plus enzymatic digestion); optional density separation; dry; weigh 0.1-0.5 mg into a cup with an internal standard; often TMAH thermochemolysis for PET and PA
matrices_demonstrated: [drinking and river water, WWTP influent and effluent including the 0.01-1 µm fraction, WWTP effluent at 3,500 L, German Bight seawater, fish, marine air]
vendors:
  - {name: Frontier Lab, instrument: "Multi-Shot Pyrolyzer with Auto-Shot sampler; 12-polymer microplastics calibration set; F-Search MPs software", url: https://www.frontier-lab.com/technical-information/mp-analysis/, price: not public}
  - {name: Shimadzu, instrument: "Py-GC/MS (Frontier pyrolyser on a Shimadzu GCMS)", url: https://www.shimadzu.com/an/industries/environment/microplastics/index.html, price: not public}
  - {name: Agilent, instrument: "Py-GC/MS (resells the Frontier pyrolyser)", url: https://www.agilent.com/en/solutions/environmental/microplastics-analysis, price: not public}
  - {name: Gerstel, instrument: "PYRO option for the TDU 2 with automatic loading", url: https://www.gerstel.com/en/products/sample-introduction/pyrolysis/tdu-pyrolysis, price: not public}
limitations:
  - Destructive; no particle count, size or shape
  - Absolute limits of quantification are micrograms per polymer in a 0.5 mg cup, so the µg/L figure depends on how many litres were filtered (0.009 µg/L needed 3,500 L)
  - "Calibration is the hard part: PE and PP curves are quadratic, calibrants must go through identical prep on the same filter type"
  - Alkanes from fats and oils mimic PE; cellulose fibre signals look like natural plant matter; PVC often excluded for interference
  - Sample-mass ceiling of 0.1-0.5 mg represents lumpy samples badly
  - Between-lab reproducibility 62-117% (PE) and 46-62% (PET) in the 84-lab VAMAS comparison; a six-figure instrument needing a GC/MS operator
fibre_performance: >
  Fibres are just mass: ASTM D8401-24 explicitly covers particles and fibres, and PET and PA are
  quantified via their markers. Cotton, viscose and lyocell are not plastics and produce no marker,
  so a cellulosic fibre load reads as zero while still adding to the cup mass. No study quantified
  textile-mill microfibres by Py-GC/MS; a BAM campaign on municipal wastewater found no PET or PA at all.
textile_effluent_relevance: >
  The reference method a regulator or auditor will eventually point to: micrograms of PET or PA per
  litre that can be compared against a discharge limit, indifferent to fibre shape. It cannot tell a
  mill how many fibres it emits and reports zero for a cotton or viscose mill.
sources:
  - https://store.astm.org/d8401-24.html
  - https://www.frontier-lab.com/technical-information/mp-analysis/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10330118/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC7152672/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12044667/
  - https://doi.org/10.1016/j.chroma.2024.465153
first_added: 2026-09-10
source_date: 2026-09-10

## Thermal extraction desorption GC/MS (TED-GC/MS)

id: T8
kind: technology
family: thermal_mass
short: TED-GC/MS
principle: A thermobalance heats 20-100 mg of sample while the decomposition gases are trapped and then desorbed into a GC/MS
plain_language: >
  A thermogravimetric balance heats 20-100 mg of sample, 40-200 times more than a pyrolysis cup,
  while the decomposition gases are trapped on a solid adsorber; the adsorber is then heated into a
  GC/MS. Same "micrograms per polymer" answer as Py-GC/MS, from a much bigger and more
  representative sample, which matters for lumpy environmental material.
outputs: [polymer_identity, mass, concentration]
size_min_um: 
size_max_um: 
size_class: sub_micron
polymer_id: polymer_level
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: a TGA ramp plus a GC/MS run, commonly quoted as 2-3 h per sample (not verified from a primary source); prep is days, as for Py-GC/MS; a fully automated version exists
sample_prep: filter, dry, optionally digest; weigh 20-100 mg into a TGA crucible
matrices_demonstrated: [municipal wastewater fractions (grey, mixed, effluent), river suspended matter and biogas plant, treated wastewater, soil reference material, roadside soil and tyre wear]
vendors:
  - {name: Gerstel, instrument: "TED-GC/MS (TGA + thermal desorption unit + GC/MS, up to 100 mg, optionally fully automated)", url: https://www.gerstel.com/en/products/sample-introduction/pyrolysis/thermal-extraction-desorption-gcms, price: not public}
limitations:
  - Destructive; no count, size or shape
  - Same calibration and marker-interference issues as Py-GC/MS, plus an adsorber transfer-efficiency term
  - Effectively one commercial supplier; fewer labs run it
  - Recovery 80-110% across size classes down to 5 µm in the BAM wastewater work
fibre_performance: Same as Py-GC/MS; fibres are mass and cellulosics are invisible. The BAM wastewater campaign detected no PET or PA, so there is no evidence yet of fibre-mass recovery in real effluent.
textile_effluent_relevance: The larger sample mass suits high-solids mill effluent better than a 0.5 mg pyrolysis cup; otherwise the same role and the same blind spot on cellulosics as Py-GC/MS.
sources:
  - https://doi.org/10.1016/j.watres.2015.09.002
  - https://doi.org/10.1016/j.chemosphere.2017.02.010
  - https://doi.org/10.1016/j.watres.2018.10.045
  - https://www.gerstel.com/en/products/sample-introduction/pyrolysis/thermal-extraction-desorption-gcms
  - https://www.gerstel.com/en/Publications/News/GERSTEL-Publications/Wastewater_treatment_efficiency_check
first_added: 2026-09-10
source_date: 2026-09-10

## TGA and DSC thermal analysis

id: T9
kind: technology
family: thermal_mass
short: TGA / DSC
principle: Heat the residue; each semi-crystalline polymer melts at its own temperature and the melting energy is proportional to its mass
plain_language: >
  The sample is heated on a balance (TGA) or against a reference (DSC). Each semi-crystalline
  polymer melts at a characteristic temperature and the melting energy is proportional to its
  mass, so a peak near 130 °C says "this much PE" and one near 250 °C says "this much PET". Cheap
  and fast, but only for polymers that melt cleanly, and peaks overlap.
outputs: [polymer_class, mass, concentration]
size_min_um: 
size_max_um: 
size_class: 10_100um
polymer_id: class_level
deployment: lab_offline
maturity: research
time_per_sample: a DSC run is about an hour; filtration, digestion, density separation and drying make it 1-2 days
sample_prep: filter, remove organics, dry, weigh milligrams into a pan; the whole residue is measured
matrices_demonstrated: [municipal WWTP effluent (TGA-DSC), industrial wastewaters at three sites (DSC), four municipal secondary effluents and post-filters (DSC)]
vendors:
  - {name: "Any DSC or TGA maker (Netzsch, TA Instruments, Mettler Toledo, PerkinElmer)", instrument: generic DSC / TGA, url: "", price: not public}
limitations:
  - Phase-transition signals of polymers other than PE and PP largely overlap; one study could only clearly identify PE and PP among seven polymers
  - Limited to semi-crystalline thermoplastics (PE, PP, PA, PET); amorphous PS, PVC, acrylics and elastomers are not seen
  - No particle information; destructive; no standardised microplastics method
fibre_performance: PET and PA are semi-crystalline, so their melting peaks are usable; cellulosics do not melt and are invisible. No textile-fibre-specific DSC validation found.
textile_effluent_relevance: >
  The one mass method actually applied to industrial wastewater: grams per litre in industrial
  influent and micrograms per litre in effluent with over 99.99% removal. A DSC costs a fraction of
  a Py-GC/MS and is a plausible at-line screening tool for PET and PA mass if peak overlap can be
  tolerated.
sources:
  - https://doi.org/10.1016/j.scitotenv.2016.06.017
  - https://doi.org/10.1016/j.chemosphere.2020.127388
  - https://doi.org/10.1016/j.wroa.2022.100156
first_added: 2026-09-10
source_date: 2026-09-10

## Depolymerisation and LC-MS/MS

id: T10
kind: technology
family: thermal_mass
short: LC-MS (depolymerised)
principle: Boil the sample in strong base to cut PET, PC or PA back into monomers, then weigh the monomers by liquid chromatography mass spectrometry
plain_language: >
  The sample is boiled in strong base, which cuts condensation polymers back into their monomers:
  terephthalic acid from PET, bisphenol A from polycarbonate, caprolactam-type products from
  polyamide. The monomers are measured by liquid chromatography mass spectrometry, which is
  extremely sensitive. It only works for polymers that can be hydrolysed, so PE, PP and PS are
  invisible. MALDI-TOF is a separate research route that fingerprints polymer fragments after heating.
outputs: [polymer_identity, mass, concentration]
size_min_um: 
size_max_um: 
size_class: sub_micron
polymer_id: polymer_level
deployment: lab_offline
maturity: research
time_per_sample: hours of hydrolysis plus a 10-20 min LC-MS/MS run; about a day per batch
sample_prep: dry, weigh, alkaline thermal hydrolysis, neutralise, filter, inject
matrices_demonstrated: [pet food and faeces, indoor and outdoor dust in 39 Chinese cities, landfill refuse, polymer standards (MALDI-TOF)]
vendors:
  - {name: Any LC-MS/MS maker, instrument: generic triple-quadrupole LC-MS/MS, url: "", price: not public}
limitations:
  - Free monomer already present (BPA, terephthalate additives, dye chemistry) is counted as polymer unless subtracted
  - Only hydrolysable polymers; PE, PP, PS and acrylic are invisible
  - No water-matrix validation and no standard
fibre_performance: In principle ideal for PET and PA6/PA66 fibres, both hydrolyse, and cellulose is inert to the marker chemistry. Textile effluent contains dye intermediates and terephthalate-type chemicals that would inflate the monomer signal, an untested interference.
textile_effluent_relevance: Attractive on paper for a PET-and-PA-only question, unproven in effluent; a research collaboration topic, not a product basis today.
sources:
  - https://doi.org/10.1021/acs.est.9b03912
  - https://doi.org/10.1016/j.envint.2019.04.024
  - https://doi.org/10.1021/acs.est.1c02772
  - https://doi.org/10.1016/j.talanta.2019.120478
first_added: 2026-09-10
source_date: 2026-09-10

## Nanoplastic sizing (NTA, DLS, field-flow fractionation)

id: T11
kind: technology
family: thermal_mass
short: NTA / DLS / AF4
principle: Laser light scattering and Brownian motion give a size distribution and a count for sub-micron particles, with no chemical identity
plain_language: >
  A laser lights up particles suspended in water; nanoparticle tracking films the Brownian jiggle
  of each one and dynamic light scattering measures the flicker of the whole suspension. Faster
  jiggle means a smaller particle, so you get a size distribution and, for NTA, a count per
  millilitre. Field-flow fractionation sorts particles by size in a thin channel before detectors.
  None of them can tell plastic from clay, bacteria or oil droplets unless a Raman or pyrolysis
  step is bolted on.
outputs: [count, size, concentration]
size_min_um: 0.03
size_max_um: 2
size_class: sub_micron
polymer_id: none
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: minutes per measurement, but the sample must be fractionated below 1 µm and diluted to 10^7-10^9 particles per mL; a fractionation run is about an hour
sample_prep: filtration or ultrafiltration to remove microparticles; dilution; identity needs a separate technique
matrices_demonstrated: [lab-degraded polystyrene, polyester washing and abrasion liquor (3.3×10^11 particles per gram of textile), weathered beach nanoplastics (AF4-DLS), spiked fish tissue and spiked suspensions (AF4-Raman)]
vendors:
  - {name: Malvern Panalytical, instrument: "NanoSight (NTA) and Zetasizer (DLS)", url: https://www.malvernpanalytical.com, price: not public}
  - {name: "Postnova, Wyatt (Waters)", instrument: "AF2000 and Eclipse field-flow fractionation with light scattering", url: "", price: not public}
limitations:
  - No chemical identity; in real water natural colloids outnumber plastics by orders of magnitude
  - Polydisperse and fibrillar particles distort DLS badly; membrane adsorption losses in fractionation
  - PE undetectable in complex matrices with fractionation; only spiked or food matrices demonstrated
fibre_performance: Polyester washing was shown to release nanoplastics and "fibrils", counted by NTA, but polyester identity below 100 nm could not be confirmed. Fibrillar shapes elute anomalously in field-flow fractionation.
textile_effluent_relevance: A lab research tool to show that a fibre-shedding process also emits sub-micron material; useless as a compliance or product sensor because it cannot say "plastic".
sources:
  - https://doi.org/10.1016/j.chemosphere.2015.11.078
  - https://doi.org/10.1021/acs.est.1c04826
  - https://doi.org/10.1007/s00216-018-0919-8
  - https://doi.org/10.1021/acs.analchem.9b05336
first_added: 2026-09-10
source_date: 2026-09-10

## Nanoplastics research methods (sp-ICP-MS, TD-PTR-MS, SRS microscopy)

id: T12
kind: technology
family: thermal_mass
short: Nanoplastics research (ICP-MS, PTR-MS, SRS)
principle: Single-particle plasma mass spectrometry, thermal-desorption proton-transfer mass spectrometry and stimulated Raman imaging, each run by a handful of groups
plain_language: >
  Three research-grade routes to particles below a micron. Single-particle ICP-MS sprays a dilute
  suspension into a 6,000 °C plasma and counts each particle's ion burst, but plastics only show as
  carbon and work well only when doped with a metal tracer. Thermal-desorption PTR-MS heats a dried
  sample and soft-ionises the vapour to give whole-sample polymer mass at sub-nanogram sensitivity.
  Stimulated Raman scattering microscopy images and identifies individual particles below 100 nm.
outputs: [count, size, mass, polymer_identity, concentration]
size_min_um: 0.01
size_max_um: 5
size_class: sub_micron
polymer_id: polymer_level
deployment: lab_offline
maturity: research
time_per_sample: minutes per run for ICP-MS; hours per sample plus pre-concentration for the others; all single-lab instruments
sample_prep: filter below 1 µm, concentrate and dry (PTR-MS); dilute to 100-1,000 particles per mL and remove dissolved carbon (ICP-MS); doped particles synthesised for tracer studies
matrices_demonstrated: [spiked consumer products (ICP-MS, 13C), metal-doped nanoplastics through a wastewater treatment simulation, Alpine snow and polar ice, North Atlantic water column (1.5-32 mg/m³ of sub-micron PET, PS and PVC), bottled water (SRS, about 2.4×10^5 particles per litre)]
vendors:
  - {name: "Agilent, Thermo Fisher, PerkinElmer, TOFWERK", instrument: ICP-MS or ICP-TOFMS in single-particle mode, url: "", price: not public}
  - {name: Ionicon, instrument: "PTR-TOF with a custom thermal-desorption inlet", url: https://www.ionicon.com, price: not public}
limitations:
  - 13C background limits unlabeled ICP-MS detection to above 1 µm; tracer studies need custom doped particles
  - A handful of groups worldwide; no standard; PE and PP quantification by PTR-MS is weaker than PET and PS
  - Fingerprint overlap with natural organics needs a reference library per matrix
fibre_performance: Not demonstrated for fibres; fibres clog nebulisers.
textile_effluent_relevance: Shows that sub-micron PET mass in water is measurable in principle, and offers a tracer route to follow doped PET nanoparticles through a mill's treatment train. Irrelevant to a first product.
sources:
  - https://doi.org/10.1016/j.talanta.2020.121486
  - https://doi.org/10.1038/s41565-018-0360-3
  - https://doi.org/10.1038/s41586-025-09218-1
  - https://doi.org/10.1073/pnas.2300582121
first_added: 2026-09-10
source_date: 2026-09-10

## Visual sorting under a stereo microscope

id: T13
kind: technology
family: optical_imaging
short: Visual microscopy
principle: A person judges each particle on a filter by eye — colour, shine, shape, no cell structure
plain_language: >
  Water is filtered, the filter goes under a low-power microscope, and a technician looks at every
  particle and decides by eye whether it is plastic, then counts and measures it. You get a count,
  sizes, shapes and colours, and a human guess at "plastic or not". It is what most labs and every
  mill that measures anything today actually does.
outputs: [count, size, shape]
size_min_um: 300
size_max_um: 5000
size_class: over_300um
polymer_id: none
deployment: lab_offline
maturity: standard_method
time_per_sample: hours per filter, fully manual and operator-dependent
sample_prep: filtration; usually H2O2 or enzymatic digestion of organics; density separation for solids
matrices_demonstrated: [marine sediment and surface water, textile-company WWTP inflow and outflow]
vendors:
  - {name: "Any stereo-microscope maker (Leica, Zeiss, Evident, Nikon)", instrument: stereo microscope + camera, url: "", price: not public}
limitations:
  - Visual-only error is 20-70% and rises as particles get smaller; below 500 µm misidentification is "very high"
  - More than 60% of particles can be misassigned without chemical confirmation
  - Two expert operators differ by up to 30% on the same filter
  - Cannot tell cotton, wool or viscose fibres from polyester or nylon by eye
fibre_performance: >
  Fibres are the easiest thing to see and the hardest to classify: natural, regenerated and synthetic
  fibres look alike. In a textile-company WWTP study, µFTIR reassigned most visually counted
  "microfibres" to cotton and wool. Dark dyed fibres vanish on dark filters, transparent ones on white.
textile_effluent_relevance: >
  It is the baseline every mill or lab already has, so it defines the counts a new product gets
  compared against. Those counts are polymer-blind and operator-dependent, which is the gap.
sources:
  - https://link.springer.com/chapter/10.1007/978-3-319-16510-3_8
  - https://pubs.acs.org/doi/abs/10.1021/es2031505
  - https://www.sciencedirect.com/science/article/abs/pii/S0025326X21011358
  - https://www.mdpi.com/2673-8929/1/4/40
first_added: 2026-09-10
source_date: 2026-09-10

## Nile Red fluorescence staining and imaging

id: T14
kind: technology
family: optical_imaging
short: Nile Red staining
principle: A dye that glows only on oily or plastic-like surfaces is imaged under blue or green light
plain_language: >
  A dye is dropped on the filter that lights up when it sits on a hydrophobic surface such as plastic,
  while most minerals and cellulose stay dark. A camera photographs the glowing spots and software
  counts and sizes them. Cheap and fast; the colour of the glow gives at best a rough polymer class,
  and anything oily glows too.
outputs: [count, size, shape, polymer_class]
size_min_um: 10
size_max_um: 5000
size_class: 10_100um
polymer_id: class_level
deployment: lab_offline
maturity: research
time_per_sample: 1-3 h including 30 min to 24 h staining; imaging and counting take minutes
sample_prep: filtration; H2O2 digestion strongly recommended because the dye also stains lipids and organics; stain, rinse, dry
matrices_demonstrated: [marine sediment, drinking water microfibres, seafood tissue, lab-spiked water]
vendors:
  - {name: MP-VAT / MP-ACT (open-source ImageJ macros), instrument: software, url: https://www.sciencedirect.com/science/article/pii/S2213343723004360, price: free}
  - {name: FIMAP (research), instrument: multispectral fluorescence camera, url: https://arxiv.org/abs/2502.17997, price: n/a}
  - {name: YOLOv8 Nile Red box (research), instrument: "digital microscope + 395 nm UV + Raspberry Pi", url: https://www.sciencedirect.com/science/article/pii/S2772416625001986, price: "$139 parts claimed"}
limitations:
  - False positives from lipids, chitin, algae and any hydrophobic organic; digestion removes 48-94% of false events
  - The dye itself precipitates into fluorescent aggregates that look like particles
  - Emission depends on solvent, polymer, excitation and additives; no standard protocol
  - Polymer class from colour degrades below about 100 µm
  - Stains PET and PVC poorly; PET is polyester, the main textile fibre
fibre_performance: >
  Poor. The dye often stains only the ends of a fibre and does not improve PET detection; PET fibres
  are under-counted in drinking water. Dark disperse-dyed polyester absorbs the excitation light. A
  2025 study only got fibre counts up by pre-dyeing the fabric with a fluorescent dye, which a mill's
  real effluent does not have.
textile_effluent_relevance: >
  Its weakest polymer is polyester and its weakest shape is a dyed fibre, exactly the target. Dye-bath
  water also carries surfactants, sizing agents and oils that all stain. A screening count after
  digestion at most, and it cannot separate cotton from PET.
sources:
  - https://pubmed.ncbi.nlm.nih.gov/35124051/
  - https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1818345/full
  - https://www.sciencedirect.com/science/article/pii/S2213343723004360
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11870216/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12859020/
first_added: 2026-09-10
source_date: 2026-09-10

## Machine vision on filter images

id: T15
kind: technology
family: optical_imaging
short: Machine vision
principle: White-light photos of the filter, with a neural network trained on human-labelled particles
plain_language: >
  A camera, a phone with a clip-on lens or a fixed imaging box photographs the whole filter under
  white light, and a neural network finds particles and labels shape, colour and "fibre or fragment".
  Cheap and quick, but the network only sees what a human sees, so it learns to imitate visual
  sorting, including its mistakes.
outputs: [count, size, shape]
size_min_um: 50
size_max_um: 5000
size_class: 10_100um
polymer_id: none
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: filtration and imaging 10-60 min; inference in seconds
sample_prep: filtration; digestion optional; often Nile Red staining to raise contrast
matrices_demonstrated: [consumer-product extracts, clam tissue extracts, single-lab lab-water datasets, beach and net debris]
vendors:
  - {name: Ocean Diagnostics, instrument: "Saturna imaging box (>400 µm net debris; 13 size, shape and colour metrics)", url: https://shop.oceandiagnostics.com/products/saturna-imaging-system, price: "CAD 649"}
  - {name: "Open-source (MP-VAT, MP-Net)", instrument: software, url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9200300/, price: free}
limitations:
  - Ground truth is human labels, so it inherits the 20-70% visual error unless spectroscopy labelled the training set
  - Small single-lab datasets, no external validation; transparent-vs-white and film-vs-fragment confusions
  - Colour is a property of the dye, not the polymer; a model trained on a mill's samples learns that mill's dye lots
  - Explicitly does not attempt polymer identification
fibre_performance: >
  Thin, curled, overlapping fibres are the known weak spot of every filter-image tool; length is only
  measurable when the fibre lies flat and unbroken in frame. No paper found validates machine-vision
  fibre counts on real textile effluent against spectroscopy.
textile_effluent_relevance: >
  Useful as the counting layer on top of a filter and cheap enough for a mill's lab bench, but on its
  own it delivers a fibre count with no polymer claim, which is what the technician with a microscope
  already gives them.
sources:
  - https://www.sciencedirect.com/science/article/pii/S2666911022000053
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC13503812/
  - https://pubs.rsc.org/ra/article/15/14/10473/867916/
  - https://oceandiagnostics.com/saturna
first_added: 2026-09-10
source_date: 2026-09-10

## Hyperspectral and near-infrared imaging

id: T16
kind: technology
family: optical_imaging
short: Hyperspectral NIR
principle: A line-scan camera records a near-infrared reflectance spectrum for every pixel of a dried filter
plain_language: >
  A camera records a full near-infrared spectrum (900-2500 nm) for every pixel of a filter. Plastics
  absorb at wavelengths set by their carbon-hydrogen bonds, so a classifier assigns each pixel a
  polymer and you get a polymer map of the whole filter in one scan of seconds. The pixels are tens
  of microns, so small particles and thin fibres vanish.
outputs: [count, size, shape, polymer_identity]
size_min_um: 100
size_max_um: 10000
size_class: 100_300um
polymer_id: polymer_level
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: seconds to minutes per filter scan; sample prep dominates
sample_prep: filtration onto a reflective substrate (gold-coated polycarbonate); drying; 2024 work images submerged particles with computational water removal
matrices_demonstrated: [dried filters with 11 polymers, sea-salt filters, lab water with ten polymers imaged directly, shipboard net-collected marine microplastics]
vendors:
  - {name: Specim (Konica Minolta), instrument: "FX17 / SWIR cameras with LabScanner and macro lens (19-24 µm pixels)", url: https://www.specim.com/hyperspectral-imaging-for-microplastic-detection-using-specim-fx17-and-swir-cameras/, price: not public}
  - {name: Resonon, instrument: "Pika NIR-640 (14.8 µm pixel, modified)", url: https://pmc.ncbi.nlm.nih.gov/articles/PMC7744770/, price: not public}
limitations:
  - Practical floor 100-300 µm; below that too few pixels per particle for a spectrum
  - Water absorbs NIR strongly, so samples are dried or computationally corrected
  - Black and dark pigments kill the reflectance signal
  - Camera, lens and software cost in the tens of thousands of dollars
fibre_performance: >
  A 15-20 µm fibre is at most one pixel wide even with the macro lens, so identity comes from a handful
  of mixed pixels. No study reports fibre-specific accuracy on effluent. Dark dyes reduce reflectance
  further.
textile_effluent_relevance: >
  Attractive for polymer maps of coarse lint and debris above 300 µm, but textile effluent fibres are
  mostly thinner than the pixel, and dark dyed fibres are the worst case. Not a fit for the target size.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC7744770/
  - https://www.specim.com/hyperspectral-imaging-for-microplastic-detection-using-specim-fx17-and-swir-cameras/
  - https://www.sciencedirect.com/science/article/pii/S004896972406786X
  - https://pubmed.ncbi.nlm.nih.gov/38852867/
  - https://www.epj-conferences.org/articles/epjconf/abs/2024/19/epjconf_eosam2024_10017.html
first_added: 2026-09-10
source_date: 2026-09-10

## Digital holographic and lensless microscopy

id: T17
kind: technology
family: optical_imaging
short: Holographic imaging
principle: A bare image sensor records the interference pattern each particle makes in coherent light; software refocuses every particle afterwards
plain_language: >
  A laser or LED shines through the water onto a bare image sensor with no lens, recording the
  interference pattern each particle makes. Software refocuses every particle numerically, so a
  whole deep flow channel is in focus at once, and the optical phase and (in polarised versions)
  birefringence become extra clues. Cheap hardware, a huge field of view, and it works in flowing
  water; polymer discrimination is early research.
outputs: [count, size, shape, polymer_class]
size_min_um: 5
size_max_um: 5000
size_class: 1_10um
polymer_id: class_level
deployment: at_line
maturity: research
time_per_sample: about 5 min imaging for a static lensless rig; in-flow holographic cameras run continuously at up to 20 holograms per second
sample_prep: minimal; dilution and a coarse pre-filter; no staining
matrices_demonstrated: [distilled-water leachate from PP containers, prepared fibre slides (six fibre classes), seawater flocs and plankton in situ]
vendors:
  - {name: Sequoia Scientific, instrument: "LISST-Holo2 submersible holographic camera (10-5000 µm, not sold for microplastics)", url: https://www.sequoiasci.com/product/lisst-holo/, price: not public}
  - {name: "Research groups (Palacký University, ISASI-CNR Naples, STIIMA-CNR Biella)", instrument: polarisation-resolved holographic microscope, url: https://arxiv.org/html/2601.15769v3, price: n/a}
limitations:
  - Polymer discrimination rests on small lab datasets (296 fibres) with no field validation
  - Phase signal saturates for thick or strongly absorbing (dark-dyed) particles
  - Twin-image and speckle noise limit the lensless variant; particle overlap in dense samples
  - No vendor has productised microplastic classification
fibre_performance: >
  The most promising label-free optical route for fibres: birefringence is a bulk property of drawn
  synthetic fibres, so it survives surface dye and needs no stain. The 2026 preprint separated PET,
  PA6, PA6.6 and PP from cotton and wool at 96.7% validation accuracy on prepared slides. Unknown in
  flow and unknown on black fibres.
textile_effluent_relevance: >
  The one optical route with a plausible path to "synthetic or natural fibre" in flow at a few
  microns with cheap hardware, and it came out of a textile-research institute. Technology readiness
  is roughly level 3-4 for this use.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12434492/
  - https://arxiv.org/html/2601.15769v3
  - https://www.sequoiasci.com/product/lisst-holo/
  - https://opg.optica.org/ao/abstract.cfm?uri=ao-62-10-D104
first_added: 2026-09-10
source_date: 2026-09-10

## Flow imaging microscopy

id: T18
kind: technology
family: flow_counting
short: Flow imaging (FlowCam)
principle: Water is pumped through a thin flow cell in front of a microscope and every passing particle is photographed and measured
plain_language: >
  The sample is pumped through a thin glass flow cell in front of a microscope objective while a
  camera fires continuously; every particle passing gets photographed, sized and described by forty
  or more shape parameters. It is a particle counter that shows you the particles. Some models add
  a laser and fluorescence channels so dye-stained particles can be flagged.
outputs: [count, size, shape, concentration]
size_min_um: 2
size_max_um: 1000
size_class: 1_10um
polymer_id: class_level
deployment: at_line
maturity: commercial_instrument
time_per_sample: minutes of run time per sample, plus 45 min Nile Red incubation if used
sample_prep: sieve out particles larger than the flow cell; dilute if turbid; optional Nile Red staining
matrices_demonstrated: [purified polymer suspensions 1-50 µm, WWTP PE and PA particles before and after membrane filtration, laundry wastewater fibres through ceramic membranes, dryer-lint fibres, cosmetics]
vendors:
  - {name: Yokogawa Fluid Imaging Technologies, instrument: "FlowCam 5000 / 8000 series (8100 and 8400 with lasers) / LO / Nano", url: https://www.yokogawa.com/us/solutions/products-and-services/life-science/flowcam-flow-imaging-microscopy/, price: not public}
limitations:
  - "The vendor's own words: 'not intended to replace FT-IR or Raman'; a screening tool"
  - Coincidence and clogging at high particle loads; polyamide particles clogged membranes in the WWTP study
  - Field of view is fixed per objective; you choose small-particle resolution or large-particle range, not both
  - No commercial FlowCam-plus-Raman coupling exists
fibre_performance: >
  The best of the optical options for fibre shape: it computes fibre length, width, straightness and
  curl. Long fibres are the classic clog-and-tangle case in a 300 µm cell, and fibres longer than the
  field of view are truncated. Dyed fibres image fine in colour, but dye says nothing about polymer.
textile_effluent_relevance: >
  The closest existing product to "count and shape fibres at line in a mill lab", and the one a
  competitor would resell into textiles. Its ceiling is polymer blindness; its practical problem is
  fibre loading and clogging in raw dye-house effluent.
sources:
  - https://www.yokogawa.com/us/solutions/products-and-services/life-science/flowcam-flow-imaging-microscopy/flowcam-lo/
  - https://www.fluidimaging.com/blog/flow-imaging-microscopy-rapid-microplastics-detection
  - https://www.fluidimaging.com/blog/microplastics-detection-analysis-recyling-wastewater
  - https://www.sciencedirect.com/science/article/abs/pii/S1385894722055085
  - https://www.fluidimaging.com/blog/flow-imaging-fiber-characterization-dryer-lint
first_added: 2026-09-10
source_date: 2026-09-10

## Flow cytometry with fluorescent staining

id: T19
kind: technology
family: flow_counting
short: Flow cytometry
principle: Particles stream single-file past a laser; scattered light gives size, dye fluorescence flags "plastic"
plain_language: >
  Particles stream single-file past a laser while detectors record scattered light (a size proxy) and
  fluorescence from a dye. Thousands of particles per second are counted, and "plastic" is whatever
  falls inside a gate drawn around the bright events. It reaches far smaller sizes than any
  microscope and says nothing about which polymer.
outputs: [count, size, concentration]
size_min_um: 0.2
size_max_um: 50
size_class: sub_micron
polymer_id: none
deployment: lab_offline
maturity: research
time_per_sample: 30-60 min including staining; acquisition takes minutes
sample_prep: pre-filtration at 45-50 µm to avoid clogging; Nile Red in DMSO or Tween; H2O2 digestion of organics
matrices_demonstrated: [tap and bottled water, coastal marine water, river and lake water, sediment extracts, human plasma]
vendors:
  - {name: CytoBuoy, instrument: "CytoSense / CytoSense XR imaging cytometer (wide cell, moored or mobile; sold for plankton)", url: https://www.cytobuoy.com/products/cytosense-xr/, price: not public}
  - {name: "Thermo Fisher, BD, Beckman Coulter, Bio-Rad, Luminex", instrument: "Attune NxT, Accuri C6, Influx, CytoFLEX, ZE5, Guava (all used in microplastic papers)", url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11870216/, price: not public}
limitations:
  - Dye aggregates produce a continuum of events indistinguishable from small plastics
  - Detection limit around 10,000 particles per mL in one study, far above real effluent concentrations
  - Scatter "size" is calibrated on spheres; a fibre's scatter depends on orientation
  - Clogging above about 50 µm on conventional cytometers; no standard protocol exists
fibre_performance: >
  Conventional cytometers remove fibres by pre-filtration. CytoSense's wide cell handles long
  filaments with imaging, but no textile-fibre study using it was found. Dye-quenched dark fibres
  fall out of the fluorescence gate.
textile_effluent_relevance: >
  Relevant only for the sub-20 µm fragment tail that microscopes miss. For fibre counting it is the
  wrong tool, and staining false positives are worst in surfactant-rich dye-house water.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11870216/
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10540628/
  - https://www.cytobuoy.com/products/cytosense-xr/
  - https://pubs.rsc.org/en/content/articlehtml/2025/ay/d5ay01093d
first_added: 2026-09-10
source_date: 2026-09-10

## Focused-beam reflectance probe (FBRM)

id: T20
kind: technology
family: inline_particle
short: FBRM probe
principle: A spinning focused laser in the pipe records how long each reflection lasts, giving a chord length, a random slice through the particle
plain_language: >
  A probe with a spinning focused laser sits directly in the pipe or tank. Each time the spot
  crosses a particle it records how long the reflection lasts, giving a "chord length", a random
  slice through the particle rather than its diameter. It reports thousands of chords per second
  and is the workhorse for crystallisation and flocculation control.
outputs: [count, size]
size_min_um: 0.25
size_max_um: 4000
size_class: sub_micron
polymer_id: none
deployment: inline_realtime
maturity: commercial_instrument
time_per_sample: continuous; 10 s intervals typical
sample_prep: none; in-situ probe, window fouling handled by probe geometry or wipers
matrices_demonstrated: [crystallisation slurries, emulsions, flocculating clay tailings in seawater, microcapsule suspensions]
vendors:
  - {name: Mettler Toledo, instrument: "ParticleTrack G400 / G600 (FBRM)", url: https://www.mt.com/us/en/home/products/L1_AutochemProducts/particle-size-analyzers/particletrack-fbrm/particletrack-g600.html, price: not public}
limitations:
  - "Chord length is not size: even monodisperse particles give a broad chord distribution, and a conversion model is needed"
  - Reflects anything that scatters; sand, flocs, fibres and bubbles look the same
  - Designed for percent-level solids; at hundreds of particles per litre counts are statistically thin
  - No microplastic-specific use found
fibre_performance: A fibre gives chords dominated by its diameter when crossed sideways and rare long chords when crossed lengthwise; fibre length is unrecoverable from the chord distribution.
textile_effluent_relevance: Would report "something is there" in raw mill effluent but cannot separate polyester fibres from cotton lint, dye flocs or sizing agents; a coarse solids trend that a TSS probe already gives cheaper.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC8481503/
  - https://doi.org/10.1021/acsomega.5c11155
  - https://doi.org/10.3390/polym16101441
first_added: 2026-09-10
source_date: 2026-09-10

## Inline laser diffraction and other process sizers

id: T21
kind: technology
family: inline_particle
short: Laser diffraction (inline)
principle: The angular pattern of laser light scattered by the flowing sample is inverted into a volume-weighted size distribution
plain_language: >
  A laser shines through the flowing sample and the angular pattern of scattered light is inverted
  into a volume-weighted size distribution. It is a bulk measurement, it never sees an individual
  particle, and it is the standard online sizer for slurries and emulsions. Submersible versions
  (LISST) do the same in rivers and oceans; ultrasonic (OPUS) and spatial-filter (Parsum) probes
  serve even denser streams.
outputs: [size, concentration]
size_min_um: 0.1
size_max_um: 2500
size_class: sub_micron
polymer_id: none
deployment: inline_realtime
maturity: commercial_instrument
time_per_sample: continuous; a full distribution in under a second
sample_prep: sampling loop or in-line; cascade diluters for concentrated slurries; antifouling block on submersibles
matrices_demonstrated: [pharmaceutical, minerals and battery slurries, seawater and estuaries, lab tanks with known microplastics, ore slurries and paints (ultrasonic), granulation and powders (spatial filter)]
vendors:
  - {name: Malvern Panalytical, instrument: "Insitec Wet (0.1-2500 µm)", url: https://www.malvernpanalytical.com/en/products/product-range/insitec-range/insitec-wet, price: not public}
  - {name: Sympatec, instrument: "MYTOS / HELOS laser diffraction; OPUS ultrasonic extinction", url: https://www.sympatec.com/en/particle-measurement/sensors/laser-diffraction/, price: not public}
  - {name: Sequoia Scientific, instrument: "LISST-200X submersible (1-500 µm)", url: https://www.sequoiasci.com/product/lisst-200x/, price: not public}
  - {name: Parsum, instrument: "IPP 70-S spatial-filter velocimetry (50-6000 µm)", url: https://www.parsum.de/en/products/ipp-70-s/, price: not public}
limitations:
  - Ensemble volume distribution; a handful of fibres per litre is invisible against any background solids
  - Needs measurable obscuration, so designed for percent solids not micrograms per litre
  - Assumes spheres; fibres distort the inversion
  - Cannot distinguish plastic from sediment, flocs or plankton; every microplastic use is a controlled experiment
fibre_performance: Poor; the inversion assumes spherical scatterers, so a long fibre reports as a smear of sizes.
textile_effluent_relevance: Not viable for counting fibres at post-treatment concentrations; possible as a solids-load sensor upstream of filtration.
sources:
  - https://www.malvernpanalytical.com/en/products/product-range/insitec-range/insitec-wet
  - https://www.sympatec.com/en/particle-measurement/sensors/laser-diffraction/
  - https://www.sequoiasci.com/article/lisst-200x-applications-in-microplastics-research/
  - https://www.parsum.de/en/products/ipp-70-s/
first_added: 2026-09-10
source_date: 2026-09-10

## Coulter counter (electrical sensing zone)

id: T22
kind: technology
family: inline_particle
short: Coulter counter
principle: Particles in a salty electrolyte pass one at a time through a tiny hole; each displaces conductive fluid and causes a resistance pulse proportional to its volume
plain_language: >
  Particles in a salty electrolyte are pulled one at a time through a tiny hole between two
  electrodes; each particle displaces conductive fluid and causes a resistance pulse proportional
  to its volume. It is the reference method for cell counting and gives a true number-based size
  distribution regardless of colour or transparency.
outputs: [count, size, concentration]
size_min_um: 0.2
size_max_um: 1600
size_class: sub_micron
polymer_id: none
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: minutes per sample; batch
sample_prep: suspend in a conductive electrolyte; the aperture must be 30-50× the largest particle
matrices_demonstrated: [bench suspensions, resistive-pulse channel in microwave cytometry of 10-24 µm microplastics]
vendors:
  - {name: Beckman Coulter, instrument: Multisizer 4e, url: https://www.mybeckman.uk/cell-counters-and-analyzers/multisizer-4e, price: not public}
limitations:
  - Requires electrolyte and a clean, clog-prone aperture; incompatible with raw effluent
  - Volume-equivalent sphere only; no material information
  - No dedicated microplastic-in-water study found
fibre_performance: Reports fibre volume as an equivalent sphere (a 500 × 15 µm fibre reads as about 45 µm); long fibres clog small apertures.
textile_effluent_relevance: A bench sizing tool only.
sources:
  - https://www.mybeckman.uk/cell-counters-and-analyzers/multisizer-4e
  - https://doi.org/10.1021/acssensors.4c03268
first_added: 2026-09-10
source_date: 2026-09-10

## Online optical particle counters

id: T23
kind: technology
family: inline_particle
short: Online particle counter
principle: Each particle in a narrow lit flow cell casts a shadow or a flash on a photodiode and is binned by size
plain_language: >
  Water flows through a narrow lit cell; each particle casts a shadow (light blockage) or a flash
  (scatter) on a photodiode and is binned by size. Drinking-water plants have used these for over
  twenty years to watch filter breakthrough. They count everything, silt, flocs, bubbles and
  plastic, and cannot say which is which.
outputs: [count, size, concentration]
size_min_um: 1
size_max_um: 100
size_class: 1_10um
polymer_id: none
deployment: inline_realtime
maturity: commercial_instrument
time_per_sample: continuous; 5-50 mL/min side-stream
sample_prep: pressurised side-stream at 0.5-4 bar; automated sensor cleaning; multiplexers for up to eight sampling points
matrices_demonstrated: [potable water, wastewater, industrial water, pool water, coagulation and filter control, hydraulic and lube oil]
vendors:
  - {name: PAMAS, instrument: "WaterViewer (1-100 µm, 25 mL/min) and S50 (4-70 µm)", url: https://www.pamas.de/particle-counters/products-by-name/pamas-waterviewer, price: not public}
  - {name: Chemtrac, instrument: "PC3400 / PC6", url: https://www.chemtrac.com/particle-counters, price: not public}
  - {name: Hach, instrument: "2200 PCX", url: https://www.hach.com, price: not public}
limitations:
  - Coincidence limit around 24,000 particles per mL; dirty water with silt saturates
  - Bubbles count as particles; colour and refractive index bias sizing
  - Cannot tell plastic from sand; no microplastic-specific validation found
fibre_performance: A fibre passing lengthwise or crosswise gives very different extinction; the reported size is an equivalent-shadow diameter. Fibres over 100 µm exceed most water-counter ranges and can bridge the cell.
textile_effluent_relevance: The cheapest existing way to get a continuous count trend of particles 1-100 µm in a treated-effluent side-stream; a differential count across a filter could quantify filter performance, but it will never say "polyester".
sources:
  - https://www.pamas.de/particle-counters/products-by-name/pamas-waterviewer
  - https://www.pamas.de/particle-counters/products-by-name/pamas-s50
  - https://www.chemtrac.com/particle-counters
first_added: 2026-09-10
source_date: 2026-09-10

## Turbidity and TSS probes

id: T24
kind: technology
family: inline_particle
short: Turbidity / TSS
principle: A submersible optical probe converts scattered light into a bulk suspended-solids number
plain_language: >
  A submersible optical probe measures how much light the water scatters and converts it to a bulk
  suspended-solids number. Every wastewater plant already has one. The Microfibre Consortium and
  ZDHC found that TSS correlates with microfibre concentration in mill effluent, so it is the only
  "microfibre proxy" the textile industry uses today.
outputs: [concentration]
size_min_um: 
size_max_um: 
size_class: 
polymer_id: none
deployment: inline_realtime
maturity: standard_method
time_per_sample: continuous, seconds
sample_prep: none; wiper or air-blast cleaning
matrices_demonstrated: [aeration tanks, sludge return, drinking-water and industrial utilities (0-4000 FNU, 0-300 g/L), textile-mill effluent as a fibre proxy]
vendors:
  - {name: Endress+Hauser, instrument: Turbimax CUS51D, url: https://www.endress.com/CUS51D, price: not public}
  - {name: "Hach, Xylem / YSI", instrument: equivalent turbidity and TSS probes, url: "", price: not public}
limitations:
  - No particle size or count, no identity
  - The achievable range depends on the medium; dyes and colour interfere
  - Proxy only; the TMC/ZDHC correlation coefficient and sample count sit behind a form
fibre_performance: Fibres contribute weakly to scatter relative to fine flocs; the proxy is empirical per mill.
textile_effluent_relevance: The baseline. This is what a mill's compliance already runs, and the TMC/ZDHC feasibility study "TSS as an Indicator of Fibre Fragments in Wastewater" (September 2024) is the current industry answer to "how do we monitor fibre loss". A new instrument competes with this probe until it shows what TSS misses.
sources:
  - https://www.endress.com/CUS51D
  - https://www.microfibreconsortium.com/manufacturing
  - https://www.microfibreconsortium.com/tss-report
first_added: 2026-09-10
source_date: 2026-09-10

## Flow Raman with acoustic focusing

id: T25
kind: technology
family: emerging_sensor
short: Flow Raman (acoustic)
principle: Ultrasound pushes every particle onto the axis of a 2 mm channel, where a laser reads its Raman fingerprint in 10-40 ms
plain_language: >
  Water flows through a 2 mm square glass channel; piezo transducers on the walls set up a standing
  ultrasound wave that pushes every particle onto the channel axis, where a 532 nm laser reads its
  Raman fingerprint in 10-40 milliseconds. Each particle is identified by polymer as it passes.
  The closest thing to a true inline identifier found anywhere, and still a bench system.
outputs: [count, size, polymer_identity]
size_min_um: 2
size_max_um: 200
size_class: 1_10um
polymer_id: polymer_level
deployment: at_line
maturity: research
time_per_sample: semi-continuous; 0.5 mL/min at 10 ms integration; up to 1,500 particles per minute with detection efficiency over 85%
sample_prep: 200 µm prefilter; 0.3-0.5 mL/min means a bypass micro-stream, not the pipe; fouling not addressed
matrices_demonstrated: [river water (Selb, Germany), PE in a calcium-carbonate-filled matrix, wastewater with minimal preparation]
vendors:
  - {name: "ILM Ulm with SKZ-KFE / EZD Selb (KoDeKa-Plast project)", instrument: "bench flow-Raman with acoustophoretic focusing; industrial follow-on partnership planned", url: https://www.ilm-ulm.de/ueber-uns/news.html, price: n/a}
limitations:
  - Much more background noise from fluorescence of non-plastic particles in soiled samples
  - Abraded flakes give weaker signal than spheres; intensity varies across the focal spot
  - 0.5 mL/min throughput samples a fraction of a litre per hour; concentration statistics need large volumes
  - A 5.7 W laser; not a cheap or explosion-safe package
fibre_performance: >
  Fibres were not the test objects. Acoustic focusing aligns elongated particles along the axis,
  which helps, but a fibre longer than the 21 µm beam waist is read at one point only, so polymer
  yes, length no.
textile_effluent_relevance: The most direct route to "polyester or cotton, per particle, in effluent". The barriers are dye fluorescence (textile effluent is the worst case), the tiny sample stream, and no packaged product.
sources:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC11902776/
  - https://doi.org/10.1021/acssensors.6c02417
  - https://www.ilm-ulm.de/ueber-uns/news.html
first_added: 2026-09-10
source_date: 2026-09-10

## Dielectrophoretic focusing with Raman

id: T26
kind: technology
family: emerging_sensor
short: DEP + Raman
principle: Electrodes on a glass chip pull particles onto the channel centreline with non-uniform AC fields, where Raman reads them one by one
plain_language: >
  Instead of sound, electrodes on the top and bottom of a glass chip use non-uniform AC fields to
  pull particles onto the channel centreline, where Raman reads them one by one. A related
  simulation study proposes ring electrodes to concentrate particles in a pipe before any sensor.
outputs: [count, polymer_identity]
size_min_um: 25
size_max_um: 50
size_class: 10_100um
polymer_id: polymer_level
deployment: lab_offline
maturity: research
time_per_sample: real time in flow; flow rate not stated
sample_prep: clean aqueous suspensions; conductivity must be controlled for the field to work
matrices_demonstrated: [mono- and polydisperse lab suspensions (PS, PP, PE, PVC, PET), groundwater with a portable DEP assembly plus machine-vision imaging, pipe-scale focusing in simulation only]
vendors: []
limitations:
  - The dielectrophoretic force collapses in conductive water; effluent is saline and dye-laden
  - Above 25 µm only so far; microfluidic channels clog
  - Pipe-scale focusing exists only as a simulation
fibre_performance: Not tested; the field would align fibres, which could help, but it is untested.
textile_effluent_relevance: Low near term; the conductivity of mill effluent is the physics problem.
sources:
  - https://doi.org/10.1039/d5ra04700e
  - https://doi.org/10.1039/d6lc00683c
  - https://doi.org/10.3390/s26113395
first_added: 2026-09-10
source_date: 2026-09-10

## Microwave and RF resonant sensors

id: T27
kind: technology
family: emerging_sensor
short: Microwave resonator
principle: A printed resonator shifts frequency when the permittivity of the liquid over it changes; plastic has a lower permittivity than water
plain_language: >
  A small printed resonator shifts its resonance frequency when the dielectric constant of the
  liquid over it changes. Plastics have a lower permittivity than water, so particles passing or
  settling over the resonator shift the frequency. Cheap and electronic, but the shift depends on
  size, count and material together, so machine learning is used to untangle them.
outputs: [count, size, concentration, polymer_class]
size_min_um: 6.5
size_max_um: 400
size_class: 1_10um
polymer_id: class_level
deployment: at_line
maturity: research
time_per_sample: continuous in flow at about 10 mL/min; a settling-based version needs minutes
sample_prep: microfluidic channels; carrier-specific baseline referencing; disposable holders under a dollar
matrices_demonstrated: [deionised, tap, salt and urea solutions at 10^5-10^7 particles per litre, real seawater (PVC, 96% recognition, portable Bluetooth prototype), single particles 20-300 µm in several carriers]
vendors: []
limitations:
  - Temperature, salinity and dissolved organics all shift permittivity; validated only at 10-30 °C in simple salts
  - Single- or two-polymer demonstrations; no fibre or mixed-matrix work
  - Below 10 µm needs microfluidic channels that clog
fibre_performance: Untested; a fibre's dielectric volume is tiny, so signal per particle would sit near the noise floor.
textile_effluent_relevance: An attractive cost profile, but dye, surfactant and salt in effluent are exactly the confounders these sensors cannot yet reject.
sources:
  - https://doi.org/10.1021/acs.est.6c06373
  - https://doi.org/10.1016/j.jhazmat.2025.139000
  - https://doi.org/10.1038/s41378-026-01413-y
  - https://doi.org/10.1021/acssensors.4c03268
first_added: 2026-09-10
source_date: 2026-09-10

## Impedance spectroscopy and impedance cytometry

id: T28
kind: technology
family: emerging_sensor
short: Impedance (ZAITRUS)
principle: Electrodes in a flow channel read each particle's electrical impedance at several frequencies; insulating plastic separates from conductive biology and grit
plain_language: >
  Electrodes in a flow channel measure each particle's electrical impedance at two or more
  frequencies; size comes from the low-frequency signal and the particle's interior from the
  high-frequency one. Plastic, which is insulating with no cytoplasm, separates from algae and
  sand-like conductive material. ZAITRUS in Bayreuth is commercialising an inline version with
  machine-learning classification.
outputs: [count, size, polymer_class]
size_min_um: 1.5
size_max_um: 1000
size_class: 1_10um
polymer_id: class_level
deployment: inline_realtime
maturity: commercial_prototype
time_per_sample: continuous; the vendor claims 24-hour online measurement
sample_prep: a clean flow channel; the vendor claims none, "directly in the process"
matrices_demonstrated: [tap water with biological material (PE beads 212-1000 µm at 103 mL/min, 90% recovery, 1% false positives), seawater-like medium (1.5 µm plastics against phytoplankton), vendor pilots at unnamed wastewater plants (matrices not public)]
vendors:
  - {name: ZAITRUS GmbH (Bayreuth, founded 2024), instrument: "ZAITRUS Smart Sensor with AI dashboard, monitoring as a service; datasheet on request", url: https://www.zaitrus.de/en/technologie/, price: not public}
limitations:
  - Distinguishes material classes (microplastic, metal, glass, biological, bubbles), not polymer types; PET versus PA is not claimed
  - The vendor publishes no size range, flow rate, matrices or pilot data; the inline claim is not independently documented
  - Conductivity changes (dye baths, salt) shift baselines
fibre_performance: Not published by anyone in this group; the academic work used beads.
textile_effluent_relevance: The one company claiming an inline "microplastic" sensor for wastewater today. Asking for the datasheet and a fibre test is a one-email diligence item.
sources:
  - https://www.zaitrus.de/en/technologie/
  - https://doi.org/10.1021/acssensors.0c02223
  - https://doi.org/10.1021/acssensors.4c01353
  - https://doi.org/10.1002/adma.202304072
first_added: 2026-09-10
source_date: 2026-09-10

## Optofluidic force induction with Raman (OF2i)

id: T29
kind: technology
family: emerging_sensor
short: OF2i + Raman
principle: A laser pushes particles along a capillary while tracking each one; an added Raman channel identifies them
plain_language: >
  A laser beam pushes particles along a capillary while their scattering is tracked one by one;
  adding a Raman channel identifies them chemically. Sold as a process-analytics sensor for
  pharma, and the company also markets microplastic analysis "without sample preparation".
outputs: [count, size, concentration, polymer_identity]
size_min_um: 0.005
size_max_um: 80
size_class: sub_micron
polymer_id: polymer_level
deployment: at_line
maturity: commercial_instrument
time_per_sample: continuous chemical analysis of particles in flow; rates not public
sample_prep: capillary flow; clean liquids
matrices_demonstrated: [pharmaceutical formulations and nanomaterials (customers Fresenius Kabi, Fluidinova, Lignovations), single 5 µm polystyrene in high-carbon matrices with OF2i-Raman-ICP-MS]
vendors:
  - {name: BRAVE Analytics GmbH (Graz), instrument: "OF2i / OF2i + Raman", url: https://www.braveanalytics.eu/, price: not public}
limitations:
  - Designed for clean, low-turbidity liquids; capillary optics foul in effluent
  - No environmental-water deployment named
fibre_performance: Not published.
textile_effluent_relevance: Low; a lab-grade tool that could characterise filter permeate.
sources:
  - https://www.braveanalytics.eu/
  - https://doi.org/10.1021/acs.analchem.5c05030
first_added: 2026-09-10
source_date: 2026-09-10

## Other research concepts (LIBS, terahertz, photoacoustic, multispectral extinction)

id: T30
kind: technology
family: emerging_sensor
short: Other research concepts
principle: Laser plasma emission, sub-millimetre waves, light-to-sound conversion and multi-wavelength extinction, each shown once in a lab
plain_language: >
  Four ideas that appear in the literature but have not left the lab. Laser-induced breakdown
  vaporises a spot into plasma and reads element lines (weak for polymers, which are all carbon
  and hydrogen); a breakdown-counting cousin counts nanoparticles in clean permeate. Terahertz
  waves pass through plastic but are swallowed by water. Photoacoustic imaging turns absorbed
  light pulses into ultrasound and classifies shape, not polymer. A multispectral laser-diode
  extinction sensor exists only as a model.
outputs: [count, concentration, polymer_class]
size_min_um: 
size_max_um: 
size_class: 
polymer_id: class_level
deployment: lab_offline
maturity: research
time_per_sample: seconds to minutes, static; breakdown detection runs inline on nanofiltration permeate
sample_prep: dried particles on a substrate; thin microfluidic films; clean permeate at 1-500 µg/L
matrices_demonstrated: [nanofiltration permeate, human tonsils, polymer microbeads, agricultural soil at 1-15% LDPE, mouse tissue]
vendors: []
limitations:
  - LIBS cannot separate polymers reliably and is destructive; breakdown detection counts any particle with no identity
  - Water absorption limits terahertz path length to tens of microns; sensitivity only at percent-level loading
  - No flow implementation for photoacoustic; the multispectral concept has no experiment
fibre_performance: Not applicable, except that photoacoustic recognises fibre morphology as one of six shape classes.
textile_effluent_relevance: None at effluent concentrations; listed so the map closes the "what else has been tried" question.
sources:
  - https://doi.org/10.1016/j.watres.2026.126362
  - https://doi.org/10.1021/acs.analchem.4c05736
  - https://doi.org/10.1016/j.jenvman.2024.120954
  - https://doi.org/10.3390/s26144594
first_added: 2026-09-10
source_date: 2026-09-10

## Real-time AI camera counting in open flow

id: T31
kind: technology
family: emerging_sensor
short: AI camera (open flow)
principle: A camera with object detection and tracking counts visible particles in a flume or river in real time
plain_language: >
  A camera plus an object-detection network (YOLO) and a tracker counts and follows visible
  particles in a flume or river as they pass. It runs in real time on an actual water body, and it
  only works for particles big enough to see and already known to be plastic.
outputs: [count, size, shape]
size_min_um: 2000
size_max_um: 5000
size_class: over_300um
polymer_id: none
deployment: inline_realtime
maturity: research
time_per_sample: continuous (28 fps at 1280x720 on a laptop GPU)
sample_prep: none; but a white backdrop behind the flow, a funnel releasing one known particle at a time, and sunlight blocked with a black cloth
matrices_demonstrated: [lab flume with clear water at 15-46 cm/s (97% counting precision real time; 87-91% offline), the Raquette River at 5 cm/s (96%; 20 released particles in total, five per size)]
vendors: []
limitations:
  - "Test particles were 2-5 mm coloured spheres bought for the purpose (PS, acrylic, cellulose acetate); the model was trained on them and the authors say natural-source data is still to be collected"
  - "Precision is TP/(TP+FP) on releases of known particles into clear water with a white backdrop; no recall, no natural-debris load, one false positive in the field"
  - "Working distance 190-330 mm gives 0.086-0.13 mm per pixel, so a 2 mm bead is ~15-25 px; anything under ~1 mm is invisible to this optics"
  - "Ambient light broke detection in both flume and river; contrast collapsed in darker water; the 60° LEDs gave sharp shadows; the 3D camera saw only reflections"
  - "Tracker (DeepSORT) loses identity on few-pixel objects; counting had to fall back to a virtual crossing line; detection confidence 40-70% was the workable band"
  - Cannot separate plastic from natural particles; sensor quality mattered more than megapixels; fixed focus beat autofocus
fibre_performance: Not tested. A 20 µm textile fibre would be a quarter of one pixel wide at this working distance.
textile_effluent_relevance: >
  Low as a detector: two orders of magnitude too coarse, and dye-house water is dark, turbid and without a
  white wall behind it. Useful as a pattern: detector plus tracker plus crossing-line count, fixed-focus
  camera, diffuse wide lighting, and the confidence-versus-tracking trade-off are the same design questions a
  flow-cell fibre counter faces at 4 µm per pixel instead of 86.
sources:
  - https://doi.org/10.3390/s24134394
first_added: 2026-09-10
source_date: 2026-09-13

## Sampling: grab, composite and pumped cascade filtration

id: T32
kind: technology
family: sampling_prep
short: Sampling & cascade filtration
principle: Push a metered volume through a stack of sieves so each size fraction lands on its own filter
plain_language: >
  You cannot count microplastics in a bottle of water: concentrations are so low and so patchy
  that you must push tens to thousands of litres through a stack of sieves and count what stays on
  them. Grab bottles (0.5-10 L) only work where concentrations are very high, such as raw textile
  effluent. Regulators have converged on pumped, fractionated filtration with a metered volume.
outputs: [concentration]
size_min_um: 10
size_max_um: 5000
size_class: 10_100um
polymer_id: none
deployment: at_line
maturity: standard_method
time_per_sample: minutes for a grab; 1-10 h of pumping for a cubic metre of drinking water; effluent cascades clog at 10 µm within tens of litres
sample_prep: none at this stage; filters go on to digestion and density separation
matrices_demonstrated: [drinking water, WWTP influent and effluent, river water, textile effluent (grab, 1-10 L)]
vendors:
  - {name: Ocean Diagnostics, instrument: "Ascension depth sampler (in-situ filtration)", url: https://oceandiagnostics.com/, price: not public}
  - {name: "UBA / Bannick design (open, non-commercial)", instrument: fractionated pressure-filtration cascade, url: https://doi.org/10.1016/j.watres.2018.10.045, price: n/a}
  - {name: "Generic autosamplers (Hach Sigma, Teledyne ISCO)", instrument: "composite autosampler; not microplastic-clean, tubing and bottles are plastic", url: "", price: not public}
limitations:
  - Recovery through sampling alone is size- and shape-dependent; one validated cascade recovered 92% of PE spheres but 32% of PE fragments, and 27 ± 10% overall for PP with 9% below 50 µm
  - Fibres wrap around mesh wires and each other
  - Number concentrations in freshwater span ten orders of magnitude across studies, and only 4 of 50 studies met all quality criteria
fibre_performance: >
  Poor and rarely validated. Spike-recovery studies use spheres and fragments, and where fibre
  recoveries are reported they are the lowest class.
textile_effluent_relevance: >
  Textile effluent runs at 10^2-10^6 fibres per litre, so 0.5-5 L grabs give usable counts, a
  different regime from drinking water where the EU demands 1,000 L. But solids load, dyes and
  sizing agents blind any filter within litres. To count 100 objects you need about a cubic metre
  of tap water, 0.1-1 L of WWTP influent, and 1-100 mL of raw textile effluent.
sources:
  - https://eur-lex.europa.eu/eli/dec_del/2024/1441/oj
  - https://doi.org/10.1016/j.watres.2018.10.045
  - https://doi.org/10.1016/j.watres.2022.118549
  - https://doi.org/10.1016/j.watres.2020.116572
  - https://doi.org/10.1007/s00216-022-04447-z
  - https://doi.org/10.1016/j.watres.2019.02.054
first_added: 2026-09-10
source_date: 2026-09-10

## Clean-up: density separation and digestion

id: T33
kind: technology
family: sampling_prep
short: Digestion & density separation
principle: Float the plastics in brine and destroy everything organic with peroxide, enzymes or alkali so the detector sees bare polymer
plain_language: >
  What sits on the filter is mostly not plastic: cellulose, fibre-finish oils, sizing, dye,
  biofilm, grit. Prep removes that so the detector sees bare polymer, by floating plastics in
  dense brine and destroying organics with peroxide, enzymes or alkali. Every step loses particles
  and adds contamination, and it is the dominant source of disagreement between labs.
outputs: [concentration]
size_min_um: 10
size_max_um: 5000
size_class: 10_100um
polymer_id: none
deployment: lab_offline
maturity: standard_method
time_per_sample: Fenton 1-24 h; enzymatic 3-10 days; potassium hydroxide 1-3 days; density separation 2-24 h settling; typically 2-8 h of analyst time per sample before any spectroscopy
sample_prep: this is the prep step
matrices_demonstrated: [sediment, WWTP sludge and effluent, surface water, biota, textile wastewater (Fenton removed 78% of organics; zinc chloride recovered 90% of spiked PET, PA and PU)]
vendors:
  - {name: Hydro-Bios, instrument: "MPSS sediment-microplastic separator (density)", url: "", price: not public}
  - {name: JRC, instrument: "PET-in-water reference material", url: https://doi.org/10.1007/s00216-021-03198-7, price: n/a}
limitations:
  - Every protocol degrades some polymers; Fenton is the usual optimum; sodium chloride brine misses PET and PVC
  - Procedural blanks in a 12-lab study held 7-511 particles (mean 80), mostly black fibres 20-212 µm; a clean bench cut airborne fibre fallout by 96.5%
  - 22 accredited labs on the same spiked bottle averaged 76 ± 10% recovery with blanks of 91 ± 141 particles; 34 labs varied 29-91% in particle counts
  - Most of 50 reviewed studies met only 4 of 10 contamination controls
fibre_performance: The worst class. Fibres float or sink unpredictably (surface tension, finish oils), fragment during stirring or sonication, and are indistinguishable from lab-coat and air fallout unless every blank is counted and subtracted by colour and polymer.
textile_effluent_relevance: >
  Textile effluent is the hardest matrix. High solids, dyes that fluoresce and quench Raman, sizing
  agents that coat fibres and mask IR bands, and a cellulosic background Fenton does not fully
  remove. Expect prep, not detection, to set throughput and error bars.
sources:
  - https://doi.org/10.1021/acs.est.8b01517
  - https://doi.org/10.1021/acs.est.7b03055
  - https://doi.org/10.3390/polym15061394
  - https://doi.org/10.1016/j.chemosphere.2023.138883
  - https://doi.org/10.1038/s41598-017-05838-4
  - https://doi.org/10.1016/j.chemosphere.2022.134282
  - https://doi.org/10.1016/j.scitotenv.2021.145071
first_added: 2026-09-10
source_date: 2026-09-10

## Analysis filter substrates

id: T34
kind: technology
family: sampling_prep
short: Filter substrates
principle: The final filter is part of the detector; the wrong one silently deletes half the spectrum
plain_language: >
  The final filter is part of the detector. FTIR needs a substrate that is either transparent to
  infrared or mirror-like; Raman needs low background fluorescence; imaging needs flat, uniform,
  non-fibrous surfaces. Alumina (Anodisc) filters lose the fingerprint region, silicon filters see
  everything but are small and expensive, metal-coated filters are the usual compromise.
outputs: []
size_min_um: 0.2
size_max_um: 
size_class: 
polymer_id: none
deployment: lab_offline
maturity: commercial_instrument
time_per_sample: n/a
sample_prep: final filtration after clean-up onto a 10-25 mm filter to keep the scan area small
matrices_demonstrated: [all]
vendors:
  - {name: Cytiva / Whatman, instrument: "Anodisc 25 mm, 0.2 µm alumina", url: "", price: not public}
  - {name: SmartMembranes GmbH, instrument: silicon microfilters, url: "", price: not public}
  - {name: Sterlitech, instrument: silver membrane filters, url: "", price: not public}
limitations:
  - Fingerprint-region loss below 1250 cm-1 on alumina; fluorescence from polycarbonate; cost and fragility of silicon
  - Particle loading must stay sparse with no overlap, which caps volume per filter and forces sub-sampling
fibre_performance: Fibres lying across pores or curling out of the focal plane defeat automated infrared mapping; long fibres exceed one field of view.
textile_effluent_relevance: Dyed fibres fluoresce under Raman and sizing coats fibres; reflection FTIR on metal-coated filters is the usual compromise in textile and laundry effluent studies.
sources:
  - https://doi.org/10.1007/s00216-015-8850-8
  - https://doi.org/10.1007/s00216-021-03498-y
  - https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/microplastics.html
first_added: 2026-09-10
source_date: 2026-09-10

## ISO 16094-2:2025 — vibrational spectroscopy, low-solids water

id: T35
kind: standard
body: ISO
status: published 2025-09-24; adopted as BS EN (2025-10), CSN EN (2026-04), UNE EN (2026-07)
prescribes: µFTIR, µRaman or QCL-IR on filtered samples; drinking, ultrapure and raw groundwater with suspended solids up to about 100 mg/L; high-solids water explicitly excluded; no shape characterisation
size_classes: 1-5,000 µm scope
unit: particles per volume by polymer (PE, PP, PET, PC, PS, PTFE, PVC, PA, PMMA, PU)
textile_effluent_relevance: Excludes high-solids water such as raw mill effluent, so it constrains the lab a mill's treated discharge would be sent to, not the mill.
url: https://www.en-standard.eu/iso-16094-2-2025-water-quality-analysis-of-microplastic-in-water-part-2-vibrational-spectroscopy-methods-for-waters-with-low-content-of-suspended-solids-including-drinking-water/
first_added: 2026-09-10

## EU Delegated Decision 2024/1441 — drinking-water microplastics methodology

id: T36
kind: standard
body: European Commission
status: in force since 2024-05-21
prescribes: at least 1,000 L sampled; µFTIR, µRaman or QCL-IR; analyse all particles ≥20 µm on sub-areas covering ≥20% of the filter; spike recovery 60-140%; ≥10 procedural blanks per filter type
size_classes: particles 20 µm-5 mm and fibres 20 µm-15 mm, reported in five bins (20-50, 50-100, 100-300, 300-1000, 1000-5000 µm)
unit: number per m³, particle vs fibre, ten priority polymers plus "other synthetic" and "unidentified"
textile_effluent_relevance: Puts QCL/LDIR on equal footing with FTIR and Raman and fixes the 20 µm floor and five size bins that any water-side number will be compared against.
url: https://eur-lex.europa.eu/eli/dec_del/2024/1441/oj
first_added: 2026-09-10

## California SWB-MP1 and SWB-MP2 — drinking-water methods (IR and Raman)

id: T37
kind: standard
body: California State Water Resources Control Board
status: adopted 2022-09-07 (Resolution 2022-0032) for a four-year monitoring programme; revision 1, May 2022
prescribes: treated drinking water; sieves at 500, 212 and 20 µm; IR floor 50 µm (FTIR, LDIR, O-PTIR), Raman floor 20 µm; ≥3 subsample sets per size fraction each ≥30 particles; match score ≥60%; lab-fortified blanks; fibres have NO recovery or QC requirement
size_classes: 20 (Raman) or 50 (IR) to 5,000 µm
unit: particles per litre by size fraction, shape and polymer
textile_effluent_relevance: The 22-lab trial behind it measured fibre identification at 76% (IR) and 30% (Raman) versus 91-95% for particles, which is why fibres were exempted from QC; the honest statement of how unreliable fibre numbers are today.
url: https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/microplastics.html
first_added: 2026-09-10

## ASTM D8332-20 and D8333-20 — sampling and preparation practices

id: T38
kind: standard
body: ASTM International
status: current practices (2020)
prescribes: D8332 collection — at least 1,500 L for low- and medium-solids water, or 1 gal/min for 24 h (about 5,450 L) for high-solids water, through stacked sieves; D8333 preparation — wet peroxide oxidation then progressive enzymatic digestion for cellulose, lipids and chitin
size_classes: set by the sieve stack
unit: n/a (practices, not measurement methods)
textile_effluent_relevance: The only standards whose scope names wastewater influent and effluent; they say how much water and how much chemistry a defensible mill number costs.
url: https://store.astm.org/d8332-20.html
first_added: 2026-09-10

## ISO 24187:2023 — principles for the analysis of microplastics

id: T39
kind: standard
body: ISO (TC 61)
status: published 2023-09-20; adopted as EN ISO 24187 (BS 2023-09, DIN 2024-04, UNE 2024-05)
prescribes: umbrella principles only, definitions, size classes, apparatus, representative sample quantities, QA/QC and reporting; no measurement method
size_classes: defines the size classes the method standards use
unit: n/a
textile_effluent_relevance: The vocabulary every lab report will use; commercial labs (SGS) state they follow it.
url: https://www.en-standard.eu/search/?q=ISO+24187
first_added: 2026-09-10

## ISO/FDIS 16094-3 — thermo-analytical methods, low-solids water

id: T40
kind: standard
body: ISO (TC 147 / SC 2)
status: final draft registered 2026-05-18; not yet published as of 2026-09-10
prescribes: Py-GC/MS and TED-GC/MS mass quantification for water with low natural suspended solids, including drinking water
size_classes: none (mass methods)
unit: µg/L by polymer
textile_effluent_relevance: Not written for high-solids mill effluent; the mass counterpart to 16094-2 that a treated discharge could be reported against.
url: https://www.iso.org/standard/84463.html
first_added: 2026-09-10

## ASTM D8401-24 — Py-GC/MS polymer type and quantity in water

id: T41
kind: standard
body: ASTM International (D19)
status: revised 2024
prescribes: pyrolysis-GC/MS at 600 °C on drinking, surface, wastewater influent and effluent, and marine water with high to low suspended solids; particles and fibres, including nanoparticle sizes; final particle size under 0.2 mm
size_classes: none (mass method)
unit: µg/L by polymer
textile_effluent_relevance: The only published test method whose scope includes high-solids wastewater and fibres; Frontier Lab markets its microplastics workflow as conforming to it.
url: https://store.astm.org/d8401-24.html
first_added: 2026-09-10

## ISO 4484-1, -2, -3:2023 — microplastics from textile sources

id: T42
kind: standard
body: ISO (TC 38)
status: published 2023
prescribes: Part 1 lab-scale wash (Gyrowash-type) with filtration and weighing, 4 specimens, no detergent; Part 2 counting and identifying fibre fragments by microscopy or spectroscopy with length classes; Part 3 real domestic washing machine with effluent filtration and weighing
size_classes: fibre length classes in Part 2
unit: mg or % mass loss per fabric (Parts 1 and 3); fibre counts (Part 2)
textile_effluent_relevance: Tests the fabric, not the mill's water; Parts 1 and 3 weigh everything shed including cotton, so the brand-facing number does not identify plastic.
url: https://www.en-standard.eu/search/?q=ISO+4484
first_added: 2026-09-10

## AATCC TM212-2021 — fibre fragment release during home laundering

id: T43
kind: standard
body: AATCC
status: published 2021
prescribes: accelerated laundering, filtration, mass of fragments; synthetic and natural fibres; optional standard detergent; 4 specimens
size_classes: none
unit: mg of fragments per specimen
textile_effluent_relevance: The US brand-facing shedding test; gravimetric, so it cannot tell polyester from cotton.
url: https://www.aatcc.org/tm212/
first_added: 2026-09-10

## The Microfibre Consortium (TMC) Test Method

id: T44
kind: standard
body: The Microfibre Consortium
status: in use; over 60 accredited labs and 1,500+ fabrics in the Microfibre Data Portal (April 2025)
prescribes: Gyrowash, filtration, weighing; 8 specimens; no detergent; the method itself says it "does not distinguish fibre types"
size_classes: none
unit: mean fibre loss in g/kg fabric (industry usually quotes mg/kg)
textile_effluent_relevance: This is how brands currently ask mills and suppliers for a microfibre number, per fabric not per litre of effluent. The 2024 TMC/ZDHC feasibility study proposes TSS as the effluent proxy.
url: https://www.microfibreconsortium.com/the-tmc-test-method
first_added: 2026-09-10

## Hohenstein microplastic analysis (dynamic image analysis)

id: T45
kind: standard
body: Hohenstein Institute
status: commercial service; DIN SPEC 4872
prescribes: dynamic image analysis giving fibre count, length distribution and mass, applied to fabrics, washing-machine effluent and "process and wastewater samples"; gravimetric tests per TM212 and ISO 4484-1 also offered
size_classes: fibre length distribution
unit: fibre count, length distribution, mass
textile_effluent_relevance: The one commercial lab explicitly offering fibre counting on mill process and wastewater samples; offline, sample by sample.
url: https://www.hohenstein.com/en/expertise/sustainability/microplastic-analysis
first_added: 2026-09-10

## EU Urban Wastewater Treatment Directive 2024/3019 — microplastics monitoring

id: T46
kind: standard
body: European Parliament and Council
status: in force (OJ 2024-12-12); transposition 2027; measurement methodology due from the Commission by 2 July 2027
prescribes: Article 21(3)(d) — all agglomerations of 10,000 population-equivalent and above monitor the presence of microplastics at inlets and outlets, and in sludge when reused in agriculture; at least 2 samples a year above 150,000 p.e., 1 every 2 years at 10,000-150,000 p.e.; storm overflows where relevant
size_classes: not yet defined
unit: not yet defined; microplastics are not defined in Article 2
textile_effluent_relevance: The first mandatory microplastics monitoring in Europe, but at municipal plants, not at the mill; a textile mill discharging to a municipal plant becomes a source the plant will start looking for.
url: https://eur-lex.europa.eu/eli/dir/2024/3019/oj
first_added: 2026-09-10

## EU REACH restriction 2023/2055 — synthetic polymer microparticles

id: T47
kind: standard
body: European Commission (ECHA)
status: in force 2023-10-17, staged bans to 2035; industrial-site use derogated with annual reporting to ECHA from 2026/2027; amended by Regulation (EU) 2026/1168 (medicinal and PPORD derogations clarified from 2023-10-17; solid-matrix derogation narrowed from 2028-06-22)
prescribes: intentionally added microplastics only; particles at or below 5 mm, fibre-like at or below 15 mm with length-to-diameter over 3; enforcement floor 0.1 µm (0.3 µm fibres)
size_classes: 0.1 µm-5 mm; fibres 0.3 µm-15 mm
unit: n/a (restriction)
textile_effluent_relevance: Excludes unintentional release, so textile fibre shedding and mill effluent are out of its scope.
url: https://eur-lex.europa.eu/eli/reg/2023/2055/oj
first_added: 2026-09-10

## France — loi AGEC washing-machine microfibre filters

id: T48
kind: standard
body: France
status: in force; new washing machines sold from 2025-01-01 must carry a plastic-microfibre retention device (article number and enforcement decree not verified)
prescribes: a retention device on new domestic washing machines
size_classes: not specified
unit: n/a
textile_effluent_relevance: Consumer end of the chain; creates the filter market (PlanetCare, Xeros) rather than a mill obligation.
url: https://www.ecologie.gouv.fr/politiques-publiques/loi-anti-gaspillage-economie-circulaire
first_added: 2026-09-10

## EU Ecodesign for Sustainable Products Regulation 2024/1781 — textiles

id: T49
kind: standard
body: European Parliament and Council
status: in force 2024; textiles in the 2025-2030 working plan; textile delegated act expected end-2027 with a Digital Product Passport for textiles around 2028; the expected information requirement covers possible release of non-biodegradable microplastics (JRC preparatory studies published; not yet law)
prescribes: "'release of nano- and microplastics' is listed as an ecodesign performance parameter; the test method is not yet fixed"
size_classes: not yet defined
unit: not yet defined
textile_effluent_relevance: The regulation most likely to put a shedding or release number on a product label; which test it adopts (TMC, ISO 4484, TM212) decides what mills are asked for.
url: https://eur-lex.europa.eu/eli/reg/2024/1781/oj
first_added: 2026-09-10

## TMC / ZDHC — TSS as an indicator of fibre fragments in wastewater

id: T50
kind: standard
body: The Microfibre Consortium with ZDHC
status: ZDHC Wastewater Guidelines V2.2 (Sept 2024) Part C 'Microfibres/fibre fragmentation' is in force as a supplier requirement; TMC/ZDHC feasibility study Sept 2024; Phase 2 (15 facilities, TSS-as-proxy validation) launched April 2026
prescribes: Part C requires suppliers to monitor TSS to at least the Foundational level and file a root-cause analysis and corrective action plan on the ZDHC Gateway if exceeded; recommends, but does not require, a one-off microfibre release profile by Dynamic Image Analysis, after which TSS is the monitoring parameter; states limits are likely to be revised downwards. Progressive and Aspirational TSS levels are claimed to cut microfibre release by ~70% and ~94%.
size_classes: none
unit: mg/L TSS
textile_effluent_relevance: Corrected 2026-09-14 (earlier line said the guidelines carried no microfibre parameter; Part C exists, read from the PDF). The industry's rulebook already names fibre fragmentation and answers it with the TSS probe the mill owns plus an optional lab DIA profile; an inline instrument competes with that pairing and must show what TSS misses, which is polymer identity and per-batch timing. Evidence ledger E3.
url: https://www.microfibreconsortium.com/manufacturing
first_added: 2026-09-10

## California AB 1628 — washing-machine filters (vetoed)

id: T51
kind: standard
body: California Legislature
status: vetoed by the Governor 2023-10-08; as of 2026-09 New York S5605/A4716 (filters on all washing machines sold; Assembly bill in Consumer Protection committee 2026-03-18) and S10638, Oregon SB 405 and Illinois HB 1370 (2030 mandate) are pending, none enacted
prescribes: would have required a filter of 100 µm or finer on new washing machines from 2029
size_classes: 100 µm
unit: n/a
textile_effluent_relevance: No US consumer-side filter rule is in force; three state bills are pending (2026-09-14 check). None touches a mill.
url: https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240AB1628
first_added: 2026-09-10

## Inditex Green to Wear 3.2 (July 2026) — supplier standard for wet-process mills

id: T53
kind: standard
body: Inditex (brand; supplier sustainability standard)
status: version 3.2 dated July 2026 (PDF created 2026-06-19), in force for Inditex wet-process suppliers
prescribes: Grades dyeing, printing, finishing, washing and tannery facilities A to D. A mill drops from A to B if "Fibers and microfibers are released into the environment without any internal control." Wastewater must be tested to the ZDHC Wastewater Guidelines twice a year with results on the ZDHC Gateway; direct discharge must meet the ZDHC Progressive level; process water needs at least biological or physico-chemical treatment plus high-rate filtration before discharge to natural media.
size_classes: none
unit: none; "internal control" of fibre release, not a measured value
textile_effluent_relevance: The clearest brand-side ask on mills found so far: the largest fashion buyer now grades its wet-processing suppliers on fibre release. It asks for control, not a number, and nothing says what evidence satisfies the auditor. Evidence ledger E4; the interview question is what a mill shows as control and what a B rating costs. Read 2026-09-15: the companion 'Green to Wear Supporting Documents v1.10' (2026, 36 pp, audits by independent external auditors) never defines the fibre control. Its audit-document list asks for wastewater test reports, discharge records, ETP flow and meter data, and solid-waste evidence for textile waste (inventory, storage, disposal registers), plus 'information on fiber type per process'. No item asks for a fibre count, a filter or a fibre-release measurement, so the clause is most plausibly met with a lint and fibre waste procedure and the existing wastewater tests.
url: https://www.inditex.com/itxcomweb/api/media/9af42004-8584-4681-917f-eca403026167/GTW%202.1%20English%202023.pdf
first_added: 2026-09-14

## UK — Microplastic Filters (Washing Machines) Bill [HL] 2026-27

id: T54
kind: standard
body: UK Parliament, House of Lords private member's bill (Lord Randall of Uxbridge)
status: HL Bill 21 of 2026-27; second reading scheduled 2026-09-11; private member's bill with no government sponsorship, low odds of passage; an earlier Commons version (2021-22) lapsed
prescribes: Would oblige the Secretary of State to require microfibre filters on new washing machines in England by 2030 and to promote awareness of microfibre pollution.
size_classes: none
unit: none
textile_effluent_relevance: Consumer end only; no UK instrument touches mill effluent for microfibres. The Environment Agency regulates UK dyehouses' discharges under permits with TSS and chemical limits, not fibre counts.
url: https://lordslibrary.parliament.uk/research-briefings/lln-2026-0046/
first_added: 2026-09-14

## EU Regulation 2025/2365 — preventing plastic pellet losses

id: T55
kind: standard
body: European Parliament and Council
status: in force; published OJ 2025-11-26; first provisions applicable 2025-12-16; operator notifications and the prevention hierarchy apply from 2027-12-17
prescribes: Operators handling over 5 tonnes of pellets a year, cleaning installations and carriers must prevent, contain and clean up pellet losses and notify installations to authorities.
size_classes: pellets (pre-production plastic granules)
unit: none
textile_effluent_relevance: Not textiles: pellets, not fibres. Listed only so the "EU microplastics regulation" umbrella is read correctly; it creates no obligation on a mill or a brand.
url: https://eur-lex.europa.eu/eli/reg/2025/2365/oj/eng
first_added: 2026-09-14

## California DTSC — microplastics on the Safer Consumer Products Candidate Chemicals List

id: T52
kind: standard
body: California Department of Toxic Substances Control (Safer Consumer Products programme)
status: final rule 2026-06-18 (regulation R-2023-05R); effective 2026-10-01; no Priority Product named yet
prescribes: Lists "microplastics", defined as solid polymeric materials under 5 mm in their longest dimension whether manufactured at that size or created by fragmentation, as a Candidate Chemical. Listing alone imposes no duty on any product maker; it lets DTSC propose product-chemical pairs as Priority Products through separate rulemaking (45-day notice, peer review), after which makers must notify DTSC within 60 days and run an Alternatives Analysis leading to reformulation, disclosure, restriction or redesign. The 2024-2026 Priority Product Work Plan names "textiles and apparel (including synthetic fabrics and performance wear)" among the categories under preliminary research. One automatic knock-on exists today: AB 1200 requires cookware makers to disclose any Candidate Chemical in handles or food-contact surfaces, so cookware disclosures are due from 2026-10-01.
size_classes: under 5 mm, no lower bound stated
unit: none; no measurement method specified
textile_effluent_relevance: Not a regulation on anyone yet, and it regulates consumer products sold in California, not mills or their water. If DTSC later names synthetic apparel a Priority Product, the regulated entity is the brand or manufacturer selling in California, and the obligation is an Alternatives Analysis on the garment, not a measurement of mill effluent. It is a "why now" signal for brands, not a mill obligation; earliest plausible product designation is a multi-year rulemaking.
url: https://www.bdlaw.com/publications/california-lists-microplastics-under-safer-consumer-products-program/
sources:
  - https://ceqanet.lci.ca.gov/2026061032
  - https://www.crowell.com/en/insights/client-alerts/warning-californias-listing-of-microplastics-as-a-candidate-chemical-may-result-in-unexpected-and-imminent-compliance-obligations-under-ab-1200-california-safer-food-packaging-and-cookware-act
  - https://www.hklaw.com/en/insights/publications/2025/07/californias-microplastics-proposal-impacts-on-the-consumer-products
  - https://dtsc.ca.gov/wp-content/uploads/sites/31/2024/10/2024-2026-Priority-Product-Work-Plan.pdf
first_added: 2026-09-14

## Textile-mill effluent measured so far

Dated 2026-09-10. Every published measurement of a mill's own water found by the batch, all grab
samples counted in a lab by microscopy with or without spectroscopy; none continuous, none at-line.
Not a technology entry (no `id:`), so the generators skip it.

| Study | Water | Method | Numbers |
|---|---|---|---|
| Xu et al. 2018, Water Sci Technol (doi:10.2166/wst.2018.476) | 30,000 t/day textile-dyeing WWTP, China | microscope counts | 334 → 16 items/L, 95% removal, 4.9×10⁸ fibres/day discharged |
| Zhou et al. 2020, Sci Total Environ (doi:10.1016/j.scitotenv.2020.140329) | dyeing and printing industrial park, China | not stated | 54,100 fibres/L raw; 537.5/L effluent; over 85% removal; polyester dominant |
| "Rathinamoorthy 2023, screen-printing units, India" | screen-printing effluent | not stated | 1.39 million fibres/L as quoted in the batch notes; UNVERIFIED on 2026-09-11, no DOI resolves to this figure; the nearest real paper (Raja Balasaraswathi and Rathinamoorthy 2025, doi:10.1016/j.emcon.2025.100559) is about cutting-floor airborne release, 2.9×10⁶ fibres/m²/day |
| Magalhães et al. 2024, Polymers (PMC11478531) | two mills' in-house WWTP in and out, Portugal | ATR-FTIR on residue plus fluorescence microscopy | 7.45 → 3.36 and 2.11 → 1.57 mg per 100 mL; PET and PA; mostly fibre-like; textile removal about 55% vs municipal 71% |
| Prantor et al. 2026, J Environ Sci (doi:10.1016/j.jes.2026.03.002) | four full-scale textile WWTPs, Bangladesh | not stated | 549-823 particles/L influent, under 28/L effluent, nylon fibres dominant; tertiary 95.6% |
| Iordachescu et al. 2024, Water Res (doi:10.1016/j.watres.2024.121696) | industrial laundry | FPA-µFTIR | 6,900 counts/L, 716 µg/L |
| Wang et al. 2023, Environ Sci Technol (doi:10.1021/acs.est.3c06210) | wet processing, global model | review and model | wet processing releases up to 25× more microfibres than home laundering; dyeing is 95% of wet-process emissions; 6.4 kt globally in 2020 |
| Badruddin et al. 2026, Environ Toxicol Chem (doi:10.1093/etojnl/vgag200) | manufacturing, review | review | wet processing about 1,300 fibres/g fabric vs dry about 700; dyeing about 800/g; wet-process fibres 57% shorter |

The spread of 10² to 10⁶ fibres/L across "textile effluent" is partly real (screen printing vs
dyeing) and mostly method: mesh size, whether cellulosics were counted, and grab timing against
batch cycles. Guangzhou printing and dyeing wastewater at COD 700-900 mg/L needed Fenton digestion
(78% organics removal) before any spectroscopy (PMC10051233).
