---
purpose: The research map — one row per paper or group on contaminant detection in water, classified by what its method actually did, so the crowded and empty method families are visible before anyone is written to.
idea: Microplastic Detection System
last_updated: 2026-09-09
batch: 0
shortlist: research-map-shortlist.csv
# ─── Axes (proposed 2026-09-09, awaiting founder confirmation) ───────────────────
# Every axis records REVEALED method — what the team actually did in the paper — never
# the aim in the abstract. Bias of the map: methods that could run on a factory effluent
# line, not oceanography. Two honest readers must agree on every value.
axes:
  principle:
    means: "The physical principle the measurement actually rests on."
    values:
      raman: "Raman micro-spectroscopy, incl. automated single-particle Raman."
      ftir: "FTIR — µFTIR, QCL/LDIR imaging, ATR."
      optical_imaging_ml: "Visible-light imaging (microscopy, flow imaging, smartphone) with machine classification."
      holography: "Lensless / digital holographic imaging."
      fluorescence: "Dye-based (Nile red etc.) fluorescence detection or counting."
      flow_cytometry: "Particle-by-particle optical counting in a flow cell."
      impedance: "Coulter-type electrical impedance counting."
      light_scattering: "Laser diffraction, DLS or turbidity-class scattering."
      thermal_pygcms: "Mass-based thermal analysis — Py-GC-MS, TED-GC-MS."
      hyperspectral: "Hyperspectral or NIR imaging."
      sampling_preconcentration: "The paper's contribution is the sampling, filtration or pre-concentration step, not the detector."
      other: "Anything not above — say what in principle_detail."
  size_class:
    means: "The smallest size class the paper actually measured, not the instrument's nominal limit."
    values:
      over_300um: "Only particles above 300 µm."
      100_300um: "Down to 100 µm."
      10_100um: "Down to 10 µm — the band most fibre-shedding studies stop at."
      1_10um: "Down to 1 µm."
      sub_micron: "Below 1 µm (nanoplastics)."
      unknown: "Not stated."
  matrix:
    means: "The water the method was actually demonstrated in."
    values:
      textile_effluent: "Dyeing, finishing or washing effluent from a textile plant."
      laundry_effluent: "Domestic or industrial laundry discharge."
      industrial_effluent: "Other industrial process or discharge water."
      municipal_wastewater: "Influent, effluent or process streams of a municipal WWTP."
      drinking_water: "Treated or raw drinking water."
      surface_marine: "Rivers, lakes, seawater, sediment."
      sludge: "Sewage or industrial sludge."
      lab_spiked: "Clean water spiked with reference particles only."
  deployment:
    means: "How far from a plant floor the method ran."
    values:
      lab_offline: "Sample shipped or carried to a lab bench."
      at_line: "Measured beside the process on a grab or autosampler, minutes to hours later."
      inline_realtime: "Measured in or on the flow, continuously or near-continuously."
  validation:
    means: "What the reported numbers were checked against."
    values:
      none: "No recovery, reference or field check reported."
      spiked_recovery: "Recovery of known spiked particles."
      vs_reference_method: "Compared against µFTIR, Raman or Py-GC-MS on the same samples."
      interlab: "Part of an interlaboratory comparison."
      field_trial: "Ran on a real plant or site for a stated period."
  polymer_id:
    means: "Whether the method says what the particle is made of."
    values:
      none: "Counts or mass only."
      class_level: "Plastic vs not-plastic, or a few broad classes."
      polymer_level: "Names the polymer (PET, PA, PP...)."
---

# Research map — contaminant detection in water

No rows yet. Batch 1 (2026-09-09) was scoped — imaging/ML, fluorescence and cytometry;
impedance, scattering, thermal and inline; sampling, harmonisation and WWTP; textile and
laundry effluent — and its scans were cut off by a session limit before any row was
written. Re-run per `startup-paper-mine`, writing one row per paper in the format that
skill declares, with every axis value taken from the `axes:` block above.
