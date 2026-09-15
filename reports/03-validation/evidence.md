---
purpose: The evidence ledger — every graded claim that moves an assumption, each linked to the node it updates and the direction it moves it.
idea: industrial-process-data-infrastructure
last_updated: 2026-09-14
next_evidence_id: E17
---

# Evidence ledger

Started 2026-09-14 with the H3 timing desk check. Entries are appended, never renumbered; a retired ID is burned.

```yaml
entries:
  - id: E3
    date: 2026-09-14
    source: "ZDHC Wastewater Guidelines Version 2.2, September 2024, Part C 'Microfibres/fibre fragmentation', pp. 79-80, incl. 'Requirements for monitoring microfibre discharge'. https://downloads.roadmaptozero.com/output/ZDHC-Wastewater-Guidelines (PDF read 2026-09-14)"
    source_type: industry_standard
    claim: "The guideline that H&M, Inditex and most brands make mills test against does address fibre fragmentation, but the only requirement is on TSS: 'Monitor the TSS results and ensure that it meets at least the Foundational Level ... If the values of TSS are higher than the Foundational Level, suppliers must undertake a RCA and upload a CAP to the ZDHC Gateway.' Microfibre counting itself is only recommended: 'Facilities should consider determining their own microfibre release profile using a Dynamic Image Analysis (DIA) method, after which TSS tests can be used to monitor microfibre releases.' It also states 'limits are likely to be revised downwards in future updates.'"
    assumption_linked: H1A2
    verdict: ambiguous
    confidence: 4
    notes: "Supports the half of H1A2 that says mills ARE being asked about fibre release by their brands' standard, and undercuts the half that says they cannot produce the number: the number they are asked for is TSS, which every mill already measures. A microfibre count is optional. This is the 'existing workaround' H1A5 asks about, stated in the industry's own rulebook."
    next_question_raised: "Has any mill actually run the recommended DIA release profile, and did a brand ever ask to see it?"
  - id: E4
    date: 2026-09-14
    source: "Inditex, 'Green to Wear 3.2 July 2026 — Sustainability Standard for wet process facilities (Pre-treatment, Dyeing, Printing, Finishing, Washing, Tanneries and Synthetic leather)', PDF created 2026-06-19, B-ranking non-compliance list. https://www.inditex.com/itxcomweb/api/media/9af42004-8584-4681-917f-eca403026167/GTW%202.1%20English%202023.pdf (URL serves the 3.2 text; read 2026-09-14; the address returns 403 to scripts and download tools but opens in a browser; local copy input-context/inditex-green-to-wear-3.2-july-2026.pdf, clause on p.5 wet process and p.11 dry process, B ranking, WASTE)"
    source_type: industry_standard
    claim: "A wet-processing mill is rated 'B' rather than best-in-class 'A' if 'Fibers and microfibers are released into the environment without any internal control.' The same standard requires wastewater to be 'tested according to ZDHC Wastewater Guidelines twice a year', results disclosed on the ZDHC Gateway, and direct discharge to meet the ZDHC Progressive level."
    assumption_linked: H1A2
    verdict: supports
    confidence: 4
    notes: "The largest fashion buyer now writes fibre release into its supplier grading for dyeing, printing, finishing and washing plants, effective July 2026. It asks for 'internal control', not a measured number, and the rating cost of a B is not stated. A mill supplying Inditex is therefore asked about microfibres today; what answering costs, and whether anyone asks for a figure, is still the interview question."
    next_question_raised: "What does an Inditex-audited mill show the auditor as 'internal control' of fibre release, and did the B/A distinction ever cost it an order?"
  - id: E5
    date: 2026-09-04
    source: "Matter (Bristol; industrial microfibre filtration), video call with Lattice (Jeffrey Chang, Sandra Zalas), 2026-09-04. Speakers: Paul (industrial filtration) and Mark (engineering). Held under NDA; raw transcript kept out of git at private/matter-call/. Capture: reports/03-validation/H1A5-2026-09-04/interviews/matter-2026-09-04-notes.md"
    source_type: customer_interview
    claim: "A filtration vendor running industrial pilots in textile mills cannot measure what its own filter removes. Its pilots rely on lab TSS, COD and BOD results that take 'around about a four week average' to come back, and it estimates microplastics from TSS. It tried a Hach TSS probe in the field and stopped deploying it: 'Wild inconsistencies that almost like damaged what we were going there to try and show.' Mark: 'all of the suspended fibers could just be shooting through because they're very low weight', while sites achieve their TSS goals."
    assumption_linked: H1A5
    verdict: supports
    confidence: 4
    notes: "Unprompted: Matter opened the call by asking for 'live microfibre analysis on the performance of our filter'. The pain is the vendor's, not the mill's, but it describes the mill's measurement situation first-hand from live pilots. Matter's own capture figures and site details are NDA and deliberately not recorded here."
    next_question_raised: "Would a mill (not the filter vendor) pay for the per-batch number, or only for the filter it proves?"
  - id: E6
    date: 2026-09-04
    source: "Matter call 2026-09-04 (see E5)"
    source_type: customer_interview
    claim: "Matter offered to put Lattice's instrument on one of its already-contracted textile-factory pilot sites, one unit moved between sites, between now and February 2027, with access to its flow, pressure and wastewater-analysis data: 'we would be quite happy to open the doors to… Piloting together' and 'we won't expect it necessary to work perfectly'. Its success criterion is live microfibre analysis 'going in and out of our system… because it ultimately proves the efficacy of what we're doing', with cotton-vs-polyester differentiation first and polymer type not needed."
    assumption_linked: H1A9
    verdict: supports
    confidence: 3
    notes: "Graded down from 4: site access is offered by the filter vendor, not by the mill that owns the water, and it is conditional on Lattice showing an integration plan. Paul also said: 'we don't need it to make our system functional… It improves the narrative.' Nice-to-have for Matter; no price, budget or LOI on this call. Lattice is pre-revenue and pre-funding."
    next_question_raised: "Did the promised follow-up (slides, integration plan, request for historian export) go to Matter, and what came back?"
  - id: E7
    date: 2026-09-14
    source: "H&M Group innovation lead (Martin) and water lead, Bangladesh (Sharif), video call with Baltic Jungle Lab (Sandra Zalas, Igor Veredyn). Call date not recorded; transcript received 2026-09-14, raw kept at private/brand-calls/. Capture: reports/03-validation/H1A2-2026-09-14/interviews/hm-group-2026-09-14-notes.md"
    source_type: customer_interview
    claim: "H&M controls its suppliers on TSS, not on a microfibre count: '30 mg per liter is the kind of a limit which you cannot cross… we do not necessarily control microfiber, but due to our heavy controlling on TSS, we can assume that… a significant part of the microfiber has been kind of already controlled'. It will set requirements on a microfibre measurement only once regulation exists: 'before we have a regulation, we can't say… what kind of demands we have to put on your solution.'"
    assumption_linked: H1A2
    verdict: ambiguous
    confidence: 2
    notes: "Interview classified weak for H1A2: the brand asks mills for TSS, which confirms E3's mechanism with a concrete limit, and does not ask for a fibre number. It does confirm that ESRS currently asks H&M whether it knows its microfibre release, with no industry standard to answer it."
    next_question_raised: "Which brand, if any, already asks a mill for a fibre count rather than TSS?"
  - id: E8
    date: 2026-09-14
    source: "H&M call (see E7)"
    source_type: customer_interview
    claim: "H&M's innovation lead knows of no monitoring product: 'we don't have anyone else working on these kind of sensors. We have a lot of companies working on filters… and ETP treatments… but no one is… monitoring'. The water lead: microfiber 'is a really an area that everyone talks about, but it's mostly talks about when we know nothing'. Both would find live measurement before and after the effluent treatment plant interesting, if it does not stop the flow."
    assumption_linked: H1A5
    verdict: supports
    confidence: 2
    notes: "Confidence follows the weak classification of the call; the 'no one is monitoring' statement is unprompted and specific to H1A5."
    next_question_raised: "What would H&M's water team accept as proof the reading is valid against its lab TSS?"
  - id: E9
    date: 2026-09-14
    source: "Adidas microfibre lead (Varija Subasingha) call, and H&M call (E7); both run by Baltic Jungle Lab, dates not recorded"
    source_type: customer_interview
    claim: "Both brands offered a route to mills, conditional on a working product. Adidas: 'if you could come up with a good prototype, I can introduce you to some brand partners and maybe… Fashion ForGood, they're also looking for technologies.' H&M: 'we can probably arrange for the actual visits and the access to… the supplier. I can't promise that', with the founders paying their own travel, and 'it will be difficult if you come… not… backed by a brand'."
    assumption_linked: H1A8
    verdict: supports
    confidence: 3
    notes: "Conditional offers, not introductions made. Adidas's lead said she would 'get back to you' on a dyeing-plant introduction."
    next_question_raised: "What minimum prototype evidence unlocks the Adidas introduction?"
  - id: E10
    date: 2026-09-14
    source: "Adidas call: Varija Subasingha, polymer chemist, Adidas point person for microfibres (3 years), with Baltic Jungle Lab (Sandra Zalas, Igor Veredyn). Call date not recorded; transcript received 2026-09-14, raw at private/brand-calls/. Capture: reports/03-validation/H1A5-2026-09-14/interviews/varija-subasingha-2026-09-14-notes.md"
    source_type: customer_interview
    claim: "Brands cannot attribute shedding to a fabric with today's gravimetric methods, and suppliers dispute lab numbers: 'if you had to go back to our supply chain… \"Hey, this fabric is shedding this much.\" They would say like, \"You are crazy because it doesn't shed.\"' Per-fabric shedding in production is 'the real shedding potential of the fabric which you cannot get from any other method currently available.' Her own FTIR microscopy: 'Just to analyze one sample, it takes one day.' On the device: 'this is the first time I've come across such a device.'"
    assumption_linked: H1A5
    verdict: supports
    confidence: 3
    notes: "Classified moderate_confirm: specific and partly unprompted, but the pain is the brand's, not the mill's. Technical risks she named: dye colour noise (10-20% of batches are over-dyed black), small particles invisible to visible-light imaging, a stable noise floor (suggests a diluting bypass line); size distribution first, polymer identity second."
    next_question_raised: "Does per-batch size distribution alone, without polymer identity, satisfy the brand's technical team?"
  - id: E11
    date: 2026-09-14
    source: "Adidas call (see E10)"
    source_type: customer_interview
    claim: "The brand's microfibre lead expects no near-term regulatory or claims pull: 'I don't foresee any claims on microplastics in the maybe foreseeable future, next five to 10 years'; 'a real robust regulation will take another three, four, five years to come. Even if it comes, it will be on the consumer phase because manufacturing doesn't happen in Europe'; ESPR requirements are expected around 2028 and may be delayed. Brands will nonetheless 'have a responsibility to report on microfiber'."
    assumption_linked: H1A1
    verdict: contradicts
    confidence: 3
    notes: "One informed brand view, not a regulatory document. She also reported a Nike/Patagonia consortium to report plant-level release; desk search 2026-09-14 could not verify it."
    next_question_raised: "Is there any dated effluent rule on fibre fragments before 2028, from ZDHC if not from a regulator?"
  - id: E12
    date: 2026-09-14
    source: "European Commission, 'Commission adopts revised sustainability reporting standards', 2026-07-03, and delegated-act annex. https://finance.ec.europa.eu/news/commission-adopts-revised-sustainability-reporting-standards-2026-07-03_en"
    source_type: regulatory_document
    claim: "The revised ESRS adopted 2026-07-03 keep only primary microplastics in the pollution standard; textile microfibre release drops out of mandatory disclosure from FY2027."
    assumption_linked: H1A1
    verdict: contradicts
    confidence: 4
    notes: "From the why-now research pass 2026-09-14. It removes the disclosure pull H&M cited on its call (E7), from FY2027."
    next_question_raised: "Do brands keep voluntary microfibre reporting after FY2027?"
  - id: E13
    date: 2026-09-14
    source: "ZDHC / The Microfibre Consortium, 'The Microfibre Consortium and ZDHC advance joint research to strengthen wastewater monitoring of fibre fragmentation', April 2026. https://www.roadmaptozero.com/post/the-microfibre-consortium-and-zdhc-advance-joint-research-to-strengthen-wastewater-monitoring-of-fibre-fragmentation"
    source_type: article
    claim: "Phase 2 of the TMC/ZDHC study, launched April 2026 at 15 facilities and co-funded by adidas, lululemon, Primark and Tesco, tests TSS against image-based fibre counts (Dynamic Image Analysis) to validate TSS as the wastewater indicator for fibre fragments."
    assumption_linked: H1A5
    verdict: ambiguous
    confidence: 2
    notes: "Cuts both ways: if TSS validates, mills have a good-enough proxy and H1A5 weakens; if not, direct fibre counting becomes the reference. The industry's reference for the correlation is itself image-based."
    next_question_raised: "When does Phase 2 report, and does it publish the TSS-to-count scatter?"
  - id: E14
    date: 2026-09-14
    source: "Fashion for Good and The Microfibre Consortium, 'Behind the Break: Exploring Fibre Fragmentation', 2025, pp. 15, 46, 49 (PDF read 2026-09-14)"
    source_type: market_report
    claim: "TMC and ZDHC are working on fibre fragments in manufacturing effluent 'with the intent to set maximum allowable limits for fibre fragments in discharged effluent'. The report states 'Monitoring ETP performance is vital' and that 'further studies are needed to confirm TSS as a reliable metric for assessing ETP performance in capturing fibre fragments.'"
    assumption_linked: H1A1
    verdict: supports
    confidence: 2
    notes: "Stated intent with no date. A ZDHC limit would bind mills through brand supplier standards, which is the 'effluent rule binds the mill' route H1A1's disconfirmation names. Fashion for Good's corporate partners listed in the report include adidas, Inditex, Paradise Textiles and Patagonia."
    next_question_raised: "Has ZDHC published a draft fibre-fragment limit or timeline?"
  - id: E15
    date: 2026-09-14
    source: "Measurlabs, 'Microplastics in water and wastewater (micro-Raman)' product page, accessed 2026-09-14. https://measurlabs.com/products/microplastics-in-water-and-wastewater-micro-raman/"
    source_type: commercial_data
    claim: "An EU lab's public price for microplastic analysis of wastewater is €390 per sample plus a €97 order fee, with results 4 weeks after receipt of samples."
    assumption_linked: H1A5
    verdict: supports
    confidence: 4
    notes: "Graded down from 5: a list price, not a paid invoice. Other labs found publish neither price nor turnaround; the observed range is about 5 business days to 6 weeks and €190-950 per sample. Matter reported a similar ~4-week turnaround even for TSS (E5)."
    next_question_raised: "What does a mill pay per year for its ZDHC wastewater testing today?"
  - id: E16
    date: 2026-09-14
    source: "ZAITRUS GmbH (Bayreuth): IFAT press release 2026-04-08 and zaitrus.de/en/technologie, accessed 2026-09-14. https://www.zaitrus.de/en/technologie/"
    source_type: article
    claim: "The nearest commercial effort to inline microplastic monitoring, ZAITRUS, uses machine-learning impedance spectroscopy to classify particles as plastic, metal, glass, biological or bubble in real time. It is in pilots targeting wastewater treatment, food and process water, claims no polymer type and no textile fibre case, and expects a monitoring-as-a-service offer from the turn of 2026/27."
    assumption_linked: H1A5
    verdict: supports
    confidence: 2
    notes: "Supports the 'no inline microfibre sensor in use at mills' half of H1A5 as of 2026-09-14. It is also the closest competitor: an inline sensor sold as a service, government-backed, about 18 months ahead. Wasser 3.0 (stain plus microscope, at-line) claims hourly monitoring at one unnamed textile company with no published data."
    next_question_raised: "Does ZAITRUS's impedance method separate fibres from particles in dyed, conductive textile effluent?"
```
