---
purpose: What each recent paper's METHOD reveals about where the design-to-machine handoff is actually being closed, who is closing it, and which of those teams is reachable by email.
idea: high-mix-manufacturing
last_updated: 2026-09-02
batch: 3
batch_1_scanned: 200
batch_1_on_axis: 166
batch_1_classified: 18
batch_1_window: "2026-02-09 to 2026-09-01"
batch_2_scanned: 200
batch_2_on_axis: 82
batch_2_classified: 8
batch_2_window: "2026-02-20 to 2026-08-25"
batch_3_scanned: 221
batch_3_on_axis: 221
batch_3_classified: 4
batch_3_window: "2026-03-25 to 2026-08-29"
shortlist: research-map-shortlist.csv

method_note: >-
  Batch 3 (same day) finally landed the digital-thread and interoperability queries after
  repeated 429s. It is the smallest batch and the most on-belief: four rows, two reachable.
  The CNC/machining query STILL has not returned and remains the outstanding gap.

  Batch 2 (same day) landed the CAD+LLM query that batch 1 could not fetch: 82 papers in
  window, 8 classified, 6 reachable. It is the closer batch to the belief — batch 1 is mostly
  robots doing work, batch 2 is software reading drawings, and the belief is about the
  reading. TWO queries are still unrun and still 429-ing: digital thread / OPC UA / MES, and
  CNC / machining. Those remain the gap. Note also that the MES and machining literature
  lives largely in journals (CIRP Annals, Journal of Manufacturing Systems, Robotics and CIM)
  rather than on arXiv, so an arXiv-only scan will under-report it however many times it is
  re-run; OpenAlex is the better source for that slice.

  Batch 1 scanned two arXiv queries that returned cleanly — cs.RO restricted to manufacturing
  terms, and an unrestricted furniture/woodworking/cabinet query. Three further queries
  (CAD+LLM, digital thread / OPC UA / MES, CNC / machining) were written and are NOT in this
  batch: arXiv returned 429s and truncated XML on every attempt during the run. That is a
  REAL GAP, not an absence of work — the interoperability and machining literature is
  precisely what this idea most needs and precisely what did not arrive. Re-run those three
  before treating this map as coverage of the belief.
  The `--max` cap combined with newest-first ordering means the effective window is the one
  recorded above, not an exhaustive read of it.

  This idea splits evidence across the belief's two links, and they do not rest on the same
  method. `coupling_door` reads whether the paper's method shows the design-to-machine
  handoff genuinely broken (link 1, first-hand for the founder). `ownership_door` reads
  whether it shows you must OWN both ends to fix it (link 2, which arrived as advice and has
  no observation behind it). A paper can support one and contradict the other; most do.

axes:
  site_control:
    means: "Where the work physically ran, and who owned the equipment it ran on."
    values:
      simulation_only: "No physical hardware in the evaluation."
      lab_cell: "Real hardware in a cell the authors own and control."
      partner_line: "Real hardware on a line owned by someone else, running that owner's real product."
      own_line: "Real hardware on a line the authors' own organisation produces on commercially."
  handoff_automated:
    means: "Which link of the design-to-machine chain the method actually automates. This is the axis the belief turns on."
    values:
      none: "Assumes the program or toolpath already exists; improves execution only."
      design_to_program: "Consumes a design artifact (CAD, DXF, STEP, engineering drawing) and emits machine-executable output."
      intent_to_program: "Consumes natural language or operator intent and emits machine-executable output."
      program_to_verified: "Takes an existing program and closes a simulation or verification loop around it."
      data_to_skill: "Learns the behaviour from demonstration; no program is authored at all."
  integration_labour:
    means: "What it cost to connect to equipment and software the team did not build — the retrofit tax."
    values:
      not_reported: "The paper does not say. Never read this as low."
      bespoke_per_cell: "Hand integration per cell; nothing claimed to carry to another cell."
      vendor_stack: "Rides one vendor's own toolchain and inherits exactly its reach."
      standards_layer: "Built on an open layer (OPC UA, MCP, AAS, MTConnect) claimed to carry across vendors."
  variability_handled:
    means: "How much the job is allowed to change between runs — the high-mix question."
    values:
      single_task: "One task, one fixture, one part."
      task_family: "A bounded family of related parts or operations."
      open_set: "Unseen parts or operations at run time, and tested as such."
  real_data_cost:
    means: "The quantity of real-world data the method needed, as a number the paper states."
    values:
      none: "No real data — simulation or zero-shot."
      minutes: "Tens of minutes of real data per task."
      hours: "Hours to tens of hours per task."
      not_quantified: "Ran on real hardware but never states the data cost."

doors:
  coupling_door:
    values: {supports_broken: "Method shows the handoff is genuinely broken and costly.",
             supports_closing: "Method shows the handoff closing without anyone owning both ends.",
             neutral: "The method says nothing either way."}
  ownership_door:
    values: {supports_owning: "Only worked because the team controlled both the software and the machines.",
             supports_layer: "Worked as a layer over machines the team did not own.",
             neutral: "The method says nothing either way."}
---

# Research map — high-mix-manufacturing

Batch 1, 2026-09-02. Eighteen rows, **seventeen reachable**. Rows are ordered by how directly
the method bears on the belief, not by date.

**The batch's finding, stated once so it is not diluted across the rows:** every team that
automated the design-to-machine handoff did it inside one vendor's stack or one cell they
owned. Not one row demonstrates a handoff layer that carried across equipment the team did
not control. That is the strongest available support for link 2 (own both ends) and it comes
from revealed method rather than from anyone's opinion — but note what it is NOT. It is a
statement about what has been *published*, in a literature that mostly reports on cells the
authors own, so the absence is partly a sampling artefact of who writes papers. The three
unrun queries are the ones that would test it properly.

---

## 2606.16078 — Robotic apparel automation, DXF digital thread

canonical_name: "(multi-institution) Siemens Technology · Sewbo · Levi Strauss & Co."
paper_date: 2026-06-15
site_control: partner_line
handoff_automated: design_to_program
integration_labour: bespoke_per_cell
variability_handled: task_family
real_data_cost: not_quantified
handoff_automated_detail: >
  A digital thread module parses **DXF production drawings** directly into process parameters
  and executable robot trajectories for sewing operations, explicitly to remove manual
  programming and allow rapid re-targeting across operations. This is the founder's own
  Cambridge result in production form — the MPhil measured DXF metadata annotation at 100% F1
  and STEP at 74%, and this team built the DXF half into a working denim line. **The single
  most relevant row in the batch.**
integration_labour_detail: >
  Integration is via an explicit "interoperability layer" joining a collaborative robot to
  conventional sewing equipment, welding, suction fixtures and machine-level controllers.
  The layer is named but not standardised — no OPC UA, no AAS. Two staged factory deployments.
  Read as: they had to build the coupling by hand, per cell, and said so.
bottleneck_named: "Deformable fabric manipulation; commissioning risk; operator adoption."
coupling_door: supports_broken
coupling_door_detail: >
  The whole engineering contribution exists because DXF drawings did not reach the machine.
  A team with Siemens' automation stack still had to write a parser. That is link 1 confirmed
  from inside the largest industrial-software vendor on earth.
ownership_door: supports_owning
ownership_door_detail: >
  Deployment required control of the workcell layout, the fixtures and the controllers
  simultaneously. Nothing here suggests the same thread would land on a line they did not
  co-design. What it does NOT show: that owning the *factory* is required — Levi's owns the
  factory, Siemens owns the stack, and the two cooperated. That is a partnership, not
  vertical integration, and it is the cheapest counter-model to the founder's link 2.
outreach_status: pending
outreach_note: "Jon Zornow (Sewbo) is a founder who has been doing robotic sewing for a decade — highest-value single conversation in the batch. Carlos Calle is Levi's side: the buyer's view of the same deployment."
published_emails: [jon@sewbo.com, ccalle@levi.com, aherrero@bwdefense.com]
source_url: https://arxiv.org/abs/2606.16078

## 2608.21417 — MCP server between an LLM and ABB RobotStudio

canonical_name: Chalmers University of Technology
paper_date: 2026-08-13
site_control: simulation_only
handoff_automated: intent_to_program
integration_labour: vendor_stack
variability_handled: task_family
real_data_cost: none
handoff_automated_detail: >
  Natural language to ABB RAPID programs, grounded by dual-stream RAG over verified technical
  documentation and production templates, with a **custom Model Context Protocol server**
  connecting the model client directly to RobotStudio for upload, simulation and diagnostic
  feedback. The decisive sentence is the authors' own limit: the loop reduces "but does not
  eliminate expert setup and final supervision."
integration_labour_detail: >
  MCP is the transport, but everything downstream of it is ABB. The server talks to
  RobotStudio; the output is RAPID. Nothing here carries to a Fanuc or a Haas without being
  rebuilt. Classified vendor_stack rather than standards_layer for exactly that reason — the
  protocol is open, the integration is not.
bottleneck_named: "Expert setup and final supervision; failures only visible in simulation."
coupling_door: supports_broken
coupling_door_detail: >
  Their simulation loop caught suction release-height errors, unreachable placement targets
  and configuration-dependent recovery motions that static and semantic checks both missed.
  A generated program that passes every text-level check and still fails on the machine is
  the coupling gap made measurable.
ownership_door: supports_layer
ownership_door_detail: >
  This is the batch's clearest counter-example to link 2: a layer over a vendor's simulator,
  owning no machines, closing a real part of the loop. Its limit is that it never left
  simulation — the paper claims no physical cell.
outreach_status: pending
outreach_note: "Stahre and Skoogh run Chalmers Production Systems — senior, well-connected in European manufacturing research, strong intro multipliers. Salunkhe/Chen are the hands on the MCP server and will answer the technical question."
published_emails: [johan.stahre@chalmers.se, anders.skoogh@chalmers.se, omkar.salunkhe@chalmers.se, siyuan.chen@chalmers.se, ebrut@chalmers.se]
source_url: https://arxiv.org/abs/2608.21417

## 2608.24039 — Design-to-Plan: CAD and 2D drawings to a process plan

canonical_name: Nanyang Technological University
paper_date: 2026-08-25
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  An orchestrator coordinating specialised agents for 3D feature recognition, 2D drawing
  analysis, 2D-3D context fusion, knowledge retrieval, process sequencing, tool selection and
  report generation — evaluated on **300 benchmark cases**. LLMs are used as reasoning agents
  over deterministic modules rather than as generators, which is the same architectural choice
  the KTH row makes independently.
handoff_automated_limit: >
  Process PLANNING is not quoting and not machining. The framework outputs a plan; nobody cut
  metal from it and no cost or lead time is attached. Conflating "can sequence operations"
  with "can quote a one-off" is the obvious over-read and this row does not support it.
bottleneck_named: "Existing approaches handle isolated subtasks and cannot support the full reasoning chain from design artifact to process plan."
coupling_door: supports_broken
coupling_door_detail: >
  Their motivation is the founder's belief restated in academic form: design information is
  heterogeneous — 3D models, 2D drawings, materials, domain rules — and no existing method
  spans it. That is the digital thread's absence, named as the research gap.
ownership_door: neutral
ownership_door_detail: "Pure software; owns nothing, and never tested against a machine."
outreach_status: pending
outreach_note: "Closest paper in the batch to H2A3 — quote speed and confidence on a variable one-off. Seung Ki Moon is the PI; Khan is first author and will have the failure cases the paper does not print."
published_emails: [skmoon@ntu.edu.sg, khan0022@e.ntu.edu.sg, chen1470@e.ntu.edu.sg]
source_url: https://arxiv.org/abs/2608.24039

## 2606.08214 — Agentic neuro-symbolic planning and commissioning

canonical_name: KTH Royal Institute of Technology
paper_date: 2026-06-06
site_control: lab_cell
handoff_automated: intent_to_program
integration_labour: bespoke_per_cell
variability_handled: task_family
real_data_cost: none
handoff_automated_detail: >
  A Specifier-Designer-Inspector architecture where LLMs do only language understanding and
  contextual reasoning while **all verification, sequencing and execution remain
  deterministic**, with LangGraph routing for failure recovery and a Unity3D digital twin for
  human inspection before physical execution. Ablation confirms each of structured command
  expansion, symbolic verification, selective LLM routing and recovery skills is individually
  necessary — i.e. the naive "just prompt it" version does not work, and they proved it.
integration_labour_detail: >
  Commissioning is in the title and is the honest signal: the value is in reducing the
  pre-deployment engineering, which means the pre-deployment engineering is large.
bottleneck_named: "Interpreting operator intent, verifying physical feasibility, recovering from execution failures across planning AND execution."
coupling_door: supports_broken
ownership_door: supports_owning
ownership_door_detail: >
  A digital twin accurate enough to verify against presupposes you know the cell exactly.
  You cannot build that for a machine you do not control.
outreach_status: pending
outreach_note: "Lihui Wang is a major figure in cloud/adaptive manufacturing and Dimarogonas in formal verification — senior, and the kind of names who answer a specific technical question. Strong intro sources into European production research."
published_emails: [lihuiw@kth.se, wangxi@kth.se, dimos@kth.se, tianyuwa@kth.se, qiangq@kth.se, vnfa@kth.se]
source_url: https://arxiv.org/abs/2606.08214

## 2604.22235 — Learning-augmented robotic automation on a live production line

canonical_name: Neuromeka
paper_date: 2026-04-24
site_control: own_line
handoff_automated: data_to_skill
integration_labour: bespoke_per_cell
variability_handled: single_task
real_data_cost: minutes
real_data_cost_detail: >
  **Under 20 minutes of real-world data PER TASK** — cable insertion and soldering — then
  5 h 10 min of continuous unfenced operation producing 108 motors at a 99.4% product-level
  QC pass rate, at near-human takt. This is the batch's decisive quantity: a data cost you
  absorb during commissioning, not one you procure. Two tasks, one line. No carry to another
  site is claimed or tested, and the row must not be read as if it were.
bottleneck_named: "Fixed waypoint scripts brittle to environmental change; whether learned control can sustain hours of reliable operation safely around people."
coupling_door: neutral
coupling_door_detail: "No design artifact enters this pipeline at all — the skill is learned from demonstration, which routes around the handoff rather than closing it."
ownership_door: supports_owning
ownership_door_detail: >
  A robot vendor deployed on a production line, without fencing, and reported the numbers.
  That is only publishable when you control the line. **Screen before writing: Neuromeka is
  a cobot manufacturer validating on its own process — a control case, not a pain case.**
outreach_status: pending
outreach_note: "Verified deployment numbers make this the best single source for 'what does it actually take'. Treat their answers as vendor-side, not buyer-side evidence."
published_emails: [yunho.kim@neuromeka.com]
source_url: https://arxiv.org/abs/2604.22235

## 2604.06949 — Composite skills and residual RL for peg-in-hole

canonical_name: "DFKI Innovative Factory Systems · RPTU Kaiserslautern"
paper_date: 2026-04-08
site_control: simulation_only
handoff_automated: data_to_skill
integration_labour: standards_layer
variability_handled: task_family
real_data_cost: none
handoff_automated_detail: >
  Composite skills carrying explicit pre-, post- and invariant conditions, adapted by Residual
  RL that is restricted to refinements inside each skill while the skill structure stays
  invariant. Evaluated in MuJoCo on a UR5e — **simulation only**, which is the row's limit.
integration_labour_detail: >
  Classified standards_layer on the strength of the group rather than this paper: Ruskowski
  directs DFKI Innovative Factory Systems and SmartFactory-KL, the German reference
  implementation for modular, vendor-neutral production with Asset Administration Shell.
  The skill-encapsulation formalism here is the software half of that programme.
bottleneck_named: "Tight geometric tolerances, frictional variability and uncertain contact dynamics on position-controlled industrial manipulators."
coupling_door: supports_closing
ownership_door: supports_layer
outreach_status: pending
outreach_note: "Ruskowski is the highest-leverage contact in the batch for the interoperability question specifically — SmartFactory-KL exists to answer whether a vendor-neutral layer can work, which is exactly the founder's link 2. Write to him about the belief, not about peg-in-hole."
published_emails: [martin.ruskowski@dfki.de, achim.wagner@dfki.de, khalil.abuibaid@rptu.de, aleksandr.sidorenko@dfki.de]
source_url: https://arxiv.org/abs/2604.06949

## 2606.25754 — Stage-aware, roughness-constrained diffusion policy for polishing

canonical_name: Huazhong University of Science and Technology
paper_date: 2026-06-24
site_control: lab_cell
handoff_automated: data_to_skill
integration_labour: not_reported
variability_handled: task_family
real_data_cost: not_quantified
handoff_automated_detail: >
  Infers the process-stage posterior from multimodal observation history without external
  stage labels at execution, and constrains diffusion sampling on a surface-roughness
  objective. Polishing is the closest published analogue to furniture finishing — the
  operation the founder's earlier cabinet scope excluded for needing a finishing department.
bottleneck_named: "Long-horizon dependencies, uncertain stage transitions, and coupled process parameters that are hard to model and regulate."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Han Ding leads one of the strongest robotic-machining groups anywhere. If sanding and finishing ever return to scope, this is the group that already knows what it costs."
published_emails: [huanzhao@hust.edu.cn, dinghan@hust.edu.cn, keshuai@hust.edu.cn, zhangjiexin@hust.edu.cn]
source_url: https://arxiv.org/abs/2606.25754

## 2608.17962 — PRISM industrial contact-rich dataset

canonical_name: Peking University
paper_date: 2026-08-18
site_control: lab_cell
handoff_automated: data_to_skill
integration_labour: not_reported
variability_handled: task_family
real_data_cost: hours
real_data_cost_detail: >
  **More than 5,000 trajectories, 45 hours of teleoperated demonstration** across 25+
  industrial manipulation tasks with synchronised multi-view RGB-D, force/torque, tactile and
  robot state. Set this against the Neuromeka row's 20 minutes per task: the gap between them
  is the difference between building a general model and commissioning one cell, and it is
  the most useful number-pair in the batch.
bottleneck_named: "Existing datasets are short-horizon and low-contact; they do not capture the precision, force regulation and multimodal feedback industrial assembly needs."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Dataset authors answer data questions readily. Ask what fraction of the 45 hours transferred to a task not in the set."
published_emails: [hx.liu@pku.edu.cn, yutengbo26@stu.pku.edu.cn]
source_url: https://arxiv.org/abs/2608.17962

## 2609.01596 — Facet-0, contact-rich precise manipulation foundation model

canonical_name: Nanyang Technological University
paper_date: 2026-09-01
site_control: lab_cell
handoff_automated: data_to_skill
integration_labour: not_reported
variability_handled: task_family
real_data_cost: not_quantified
handoff_automated_detail: >
  Predicts the contact consequences of its own actions — a joint action-wrench proposal where
  flow matching generates each action chunk together with the wrist-wrench profile it expects
  to induce, plus a distributional Action-Wrench Critic trained on deployment rollouts.
  Targets sub-millimetre assembly tolerances. Published the day before this batch.
bottleneck_named: "Sub-millimetre real-world assembly needs spatial precision, compliant interaction and robustness to contact failure simultaneously."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Newest paper in the batch — a 24-hour-old citation is the strongest possible proof the email is not a template."
published_emails: [ziwei.wang@ntu.edu.sg]
source_url: https://arxiv.org/abs/2609.01596

## 2608.28175 — Bin picking to empty, in Mercedes-Benz production

canonical_name: Mercedes-Benz
paper_date: 2026-08-28
site_control: own_line
handoff_automated: none
integration_labour: bespoke_per_cell
variability_handled: open_set
real_data_cost: not_quantified
handoff_automated_detail: >
  A four-tier hybrid: a model-based pipeline as the reliable backbone, with a model-free
  "exploration agent" that resolves deadlocks and discovers new grasp points online. The
  named pain is the founder's pain in a different costume — "labour-intensive fine-tuning of
  grasp points is commonly required to reach satisfactory performance **for new parts**."
  Per-new-part engineering labour is precisely what kills high-mix economics.
bottleneck_named: "Model-based methods deadlock when grasps are occluded; model-free ones lack the repeatability production requires."
coupling_door: supports_broken
ownership_door: supports_owning
outreach_status: pending
outreach_note: "An OEM automation engineer writing candidly about per-part setup cost. Rare, and directly on the high-mix question."
published_emails: [florian.toeper@mercedes-benz.com]
source_url: https://arxiv.org/abs/2608.28175

## 2605.21625 — Flat-Pack Bench: VLM understanding of furniture assembly

canonical_name: Cornell University
paper_date: 2026-05-20
site_control: simulation_only
handoff_automated: none
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  A benchmark, not a system: temporal ordering of assembly actions and fine-grained
  spatio-temporal localisation in furniture-assembly video, built because existing benchmarks
  test only coarse tasks over verbally-obvious household objects.
handoff_automated_limit: "Video understanding of assembly is not assembly. This row supports no claim about robots building furniture."
bottleneck_named: "Current benchmarks do not evaluate the step-by-step fine-grained spatio-temporal understanding real assembly needs."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Furniture-specific and reachable. Ask where the best models actually fail — the benchmark's failure modes are the useful part."
published_emails: [achetan@cs.cornell.edu]
source_url: https://arxiv.org/abs/2605.21625

## 2604.20468 — MOMO: physical, verbal and graphical skill adaptation

canonical_name: "(multi-institution) — corresponding address is TU München"
paper_date: 2026-04-22
site_control: lab_cell
handoff_automated: intent_to_program
integration_labour: not_reported
variability_handled: task_family
real_data_cost: none
handoff_automated_detail: >
  Three modalities for a non-expert to adapt a robot skill: kinesthetic touch for spatial
  correction, natural language for semantic change, and a web GUI for drag-and-drop via-point
  editing. Architecturally the same discipline as the KTH and NTU rows — **the LLM selects
  and parameterises predefined functions rather than generating code**. Three independent
  groups reached that constraint separately, which makes it the batch's most reliable design
  finding.
bottleneck_named: "Non-expert users need to adapt industrial robots, and different adaptations need different interaction modalities."
coupling_door: supports_closing
ownership_door: supports_layer
outreach_status: pending
outreach_note: "Directly relevant to whoever ends up operating the founder's machines. Good feasibility conversation, low seniority barrier."
published_emails: [m.knauer@tum.de]
source_url: https://arxiv.org/abs/2604.20468

## 2607.24770 — ProcAgent: procedural task guidance on edge

canonical_name: "(multi-institution) University of Tennessee Knoxville · Worcester Polytechnic Institute"
paper_date: 2026-06-09
site_control: lab_cell
handoff_automated: none
integration_labour: not_reported
variability_handled: task_family
real_data_cost: not_quantified
bottleneck_named: "Procedural guidance with a human in the loop, under edge compute constraints."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Lower priority. NOTE: the mined set contained five ACM template placeholders (trovato@corporation.com, jsmith@affiliation.org, webmaster@marysville-ohio.com, jpkumquat@consortium.net, cpalmer@prl.com) left in the LaTeX. Only the four .edu addresses below are real — the placeholders are deliverable domains and would have reached strangers."
published_emails: [azahid@vols.utk.edu, sswamin6@utk.edu, bislam@wpi.edu, sbiswas@wpi.edu]
source_url: https://arxiv.org/abs/2607.24770

## 2604.18627 — Human-awareness estimation for AMRs in industrial warehouses

canonical_name: Fraunhofer Austria
paper_date: 2026-04-18
site_control: partner_line
handoff_automated: none
integration_labour: not_reported
variability_handled: single_task
real_data_cost: not_quantified
bottleneck_named: "AMR safety and throughput both degrade without knowing whether a nearby human has seen the robot."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Fraunhofer applied-research contacts know who in industry has the problem; better as an intro source than as a technical conversation."
published_emails: [maximilian.haug@fraunhofer.at]
source_url: https://arxiv.org/abs/2604.18627

## 2608.25509 — Welding torch umbilical dynamics

canonical_name: "(multi-institution) CNRS/LS2N · IMT Atlantique · Weez-U Welding"
paper_date: 2026-08-26
site_control: lab_cell
handoff_automated: none
integration_labour: not_reported
variability_handled: single_task
real_data_cost: not_quantified
bottleneck_named: "The umbilical's own dynamics measurably perturb the robot carrying the torch."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Narrow, but a research-lab-plus-startup pairing on a real process. NOTE: 'name@email.address' appeared in the mined set and is a template placeholder — do not use it."
published_emails: [damien.chablat@cnrs.fr, mathieu.porez@imt-atlantique.fr, ygt@weez-u-welding.com, ngr@weez-u-welding.com, frt@weez-u-welding.com]
source_url: https://arxiv.org/abs/2608.25509

## 2608.00369 — Robotic manufacture of dielectric elastomer actuators

canonical_name: University of Toronto
paper_date: 2026-08-01
site_control: lab_cell
handoff_automated: none
integration_labour: not_reported
variability_handled: single_task
real_data_cost: not_quantified
bottleneck_named: "Hand-fabrication of multilayer actuators does not scale or repeat."
coupling_door: neutral
ownership_door: supports_owning
outreach_status: pending
outreach_note: "A group that built its own production process because none existed to buy — the founder's link-2 argument, arrived at independently and at lab scale."
published_emails: [duduta@mie.utoronto.ca]
source_url: https://arxiv.org/abs/2608.00369

## 2607.01212 — FurnitureVLA: real-scale bimanual furniture assembly

canonical_name: "Mitsubishi Electric Research Laboratories · Oxford · UNC Chapel Hill"
paper_date: 2026-07-01
site_control: lab_cell
handoff_automated: data_to_skill
integration_labour: not_reported
variability_handled: task_family
real_data_cost: hours
real_data_cost_detail: >
  Up to 7 subtasks and **1,550 control steps** per assembly, with a VR teleoperation rig built
  for single-operator bimanual collection. The first systematic study of real-scale (not
  toy-scale) bimanual furniture assembly. A progress signal predicted jointly with actions
  drives automatic subtask transitions.
bottleneck_named: "Extreme long-horizon compounding error; prior furniture work is toy-scale or single-arm."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: >
  **THE ONLY UNREACHABLE ROW. Kept deliberately.** It is the single closest paper in the batch
  to "furniture robots", so dropping it would delete the batch's most on-theme finding. No
  address is printed in the source package or the HTML render — checked both. Diego Romeres
  is the corresponding author and MERL publishes its researchers' contact details on its own
  people pages; look it up there rather than guessing at a pattern.
published_emails: []
source_url: https://arxiv.org/abs/2607.01212

## 2605.08831 — AssemPlanner: multi-agent planning for flexible assembly

canonical_name: "(unidentified)"
paper_date: 2026-05-09
site_control: simulation_only
handoff_automated: intent_to_program
integration_labour: not_reported
variability_handled: task_family
real_data_cost: none
bottleneck_named: "Task planning across a reconfigurable assembly system."
coupling_door: neutral
ownership_door: neutral
outreach_status: off_scope
outreach_note: "Dropped as a target. The only address in the source package was 'f@sx.yh' — malformed, not a contactable author. Finding is redundant with the KTH and NTU rows, which cover the same architecture with real evaluation, so nothing is promoted to the evidence ledger."
published_emails: []
source_url: https://arxiv.org/abs/2605.08831


---

# BATCH 2 — CAD, drawings and code (2026-09-02)

The scan that batch 1 could not fetch. Where batch 1 is robots doing work, batch 2 is software
reading engineering intent — which is the half of the belief the founder measured personally.

**Batch 2's finding:** four independent groups converged on *deterministic-first* — parse the
geometry with a real kernel (OpenCASCADE, B-Rep, face-adjacency graphs), then let the model
reason over the parsed result, never over the raw file. Nobody who evaluated seriously let an
LLM read a STEP file directly. That is a design constraint arrived at by four teams
separately, and it is the most transferable thing in either batch.

## 2602.18296 — Binding 2D drawing annotations to 3D CAD features

canonical_name: Nanyang Technological University
paper_date: 2026-02-20
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  A deterministic-first framework mapping 2D drawing entities — GD&T callouts, datum
  definitions, surface requirements — onto the 3D CAD features they govern, to produce one
  unified manufacturing specification. **This is the founder's MPhil, done by someone else,
  six months later, and published.** The founder measured DXF metadata annotation at 100% F1
  and STEP at 74%; this team built the binding layer that sits on top of that measurement.
  Same first author as 2608.24039 — Khan has now published twice on precisely this seam.
bottleneck_named: >
  "2D drawings remain the primary carrier of manufacturing intent in automotive, aerospace,
  shipbuilding and heavy-machinery industries" despite MBD existing — and linking their
  annotations to 3D features is hard because of contextual ambiguity, repeated feature
  patterns, and the need for traceable decisions.
coupling_door: supports_broken
coupling_door_detail: >
  The single best statement of link 1 in either batch, and it comes from a disinterested
  party. Model-Based Definition has existed for twenty years and the drawing is STILL the
  carrier. That is not a technology gap, it is a revealed preference of four industries, and
  it means the coupling stays broken for reasons no standard has fixed.
ownership_door: neutral
outreach_status: pending
outreach_note: "Merge into the Design-to-Plan approach — one email citing both papers, not two emails. A second author writing about the same seam twice is the strongest evidence the founder is not alone in it."
published_emails: [khan0022@e.ntu.edu.sg]
source_url: https://arxiv.org/abs/2602.18296

## 2605.10568 — Correct-by-construction G-code via separation logic

canonical_name: "Sling AI (Korea) — solo author"
paper_date: 2026-05-11
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: task_family
real_data_cost: none
handoff_automated_detail: >
  STEP file → deterministic B-Rep extraction via OpenCASCADE → LLM generates G-code → a
  Separation Logic prover with a Spatial Heap model checks it, treating physical collisions as
  **Spatial Data Races**, and condenses proof failures into bounding boxes fed back as
  correction directives. The closest thing in either batch to CAD-to-cut with a guarantee
  attached rather than a benchmark score.
handoff_automated_limit: "A framework paper — no machine ran this G-code. Do not read it as a demonstrated cutting result."
bottleneck_named: "Ungrounded LLM G-code is unverifiable, so a human must check every line — which is the cost the method attacks."
coupling_door: supports_broken
ownership_door: supports_layer
outreach_status: pending
outreach_note: "Solo author at a small company — the profile most likely to answer a cold email in full, and the topic is the founder's CNC question exactly."
published_emails: [ylee@sling.ai.kr]
source_url: https://arxiv.org/abs/2605.10568

## 2607.02448 — AgentsCAD: automated DFM for FDM parts

canonical_name: Carnegie Mellon University
paper_date: 2026-07-02
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  Parses a STEP file, detects overhangs past a 45° threshold, builds a face-adjacency topology
  graph, optionally injects semantic feature labels from a **GraphSAGE model trained on
  MFCAD++ (59,665 parts)**, then dispatches an LLM design-reasoning agent that recommends
  reorientations, fillets and chamfers, with a vision-language verifier on rendered views.
  Outputs a modified STEP. The pipeline is deterministic geometry first, model second — the
  batch's design finding, stated most explicitly here.
handoff_automated_limit: "DFM for FDM is not DFM for machining. Overhang rules do not transfer to tool access, workholding or setup count."
bottleneck_named: "Slicers can identify defects such as steep overhangs but cannot modify the underlying geometry."
coupling_door: supports_broken
ownership_door: supports_layer
outreach_status: pending
outreach_note: "Barati Farimani's group at CMU. Strong lab, US-based, and the 59,665-part training set is a number worth asking about."
published_emails: [barati@cmu.edu]
source_url: https://arxiv.org/abs/2607.02448

## 2607.27558 — Drawing-Recode: raster 2D drawings to parametric CAD code

canonical_name: Chungnam National University
paper_date: 2026-07-30
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  Recovers parametric CAD sequences from **raster** drawings — the scanned and printed legacy
  stock accumulated before digital transformation — grounding dimensional annotations to
  geometry through a cross-attention Annotation Grounding Loss rather than leaving the LLM to
  associate them. Prior work handled vector drawings only.
bottleneck_named: "Existing methods process only vector drawings, or are domain-limited, and never explicitly connect dimensional annotations to geometry."
coupling_door: supports_broken
coupling_door_detail: >
  Directly relevant to H2: a blocked part is very often blocked because the only drawing is a
  scan, or a paper print, or nothing at all. This is the brownfield case in its purest form.
ownership_door: supports_layer
outreach_status: pending
outreach_note: "The legacy-drawing angle is the one nobody else in either batch works on, and it is the one a spare-parts business actually hits."
published_emails: [hk.kim@cnu.ac.kr, kimit@g.cnu.ac.kr, mingi@o.cnu.ac.kr]
source_url: https://arxiv.org/abs/2607.27558

## 2605.10865 — BenchCAD: industrial programmatic CAD benchmark

canonical_name: "Rice University · University of Virginia"
paper_date: 2026-05-11
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  **17,900 execution-verified CadQuery programs across 106 industrial part families** — bevel
  gears, compression springs, twist drills — evaluated on VQA, code QA, image-to-code and
  instruction-guided editing. Real engineering parts rather than the toy CAD sequences most
  benchmarks use, which makes its scores the most honest available read on whether models can
  do industrial CAD at all.
bottleneck_named: "MLLMs are rarely evaluated on whether shape recognition, 3D structural understanding and engineering-parameter inference jointly hold in a realistic industrial setting."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Ask for the headline failure rate on the industrial families. A benchmark author knows exactly where the ceiling is and will usually say."
published_emails: [hanjie@rice.edu, hz5sq@virginia.edu]
source_url: https://arxiv.org/abs/2605.10865

## 2608.22128 — Task-driven printability assistance

canonical_name: Colorado School of Mines
paper_date: 2026-08-22
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  STL plus a natural-language description of intended use → structured pre-print
  recommendations, grounded on geometry evidence and structured material/printer knowledge.
  The framing is what earns the row: printability is checked before printing, **task
  suitability only after**, so a non-expert discovers the wrong material choice by holding the
  wrong part.
bottleneck_named: "Unsuitable material or process choices are identified only after fabrication — repeated printing, waste, frustration."
coupling_door: supports_broken
ownership_door: supports_layer
outreach_status: pending
outreach_note: "Additive rather than subtractive, so secondary — but 'the buyer cannot tell whether the process suits the job until after it is made' is the same information gap H2A3 describes at a quote."
published_emails: [xlzhang@mines.edu, zheng@mines.edu, zhaoda_du@mines.edu]
source_url: https://arxiv.org/abs/2608.22128

## 2607.05750 — ArtisanCAD: industrial CAD agent with expert-grounded distillation

canonical_name: "(multi-institution) EIT · Renmin University · IM Motors"
paper_date: 2026-07-07
site_control: simulation_only
handoff_automated: design_to_program
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
bottleneck_named: "General CAD agents lack the expert knowledge industrial parts require."
coupling_door: neutral
ownership_door: neutral
outreach_status: pending
outreach_note: "Lower priority — an OEM co-author (IM Motors) makes it interesting, but the row adds nothing the CMU and Rice rows do not already carry. No draft written."
published_emails: [ybin@eitech.edu.cn, qingsongyao@ruc.edu.cn, luowenfa@immotors.com]
source_url: https://arxiv.org/abs/2607.05750

## 2604.09633 — Agentic AI in engineering and manufacturing: industry perspectives

canonical_name: "(unidentified)"
paper_date: 2026-03-19
site_control: simulation_only
handoff_automated: none
integration_labour: not_reported
variability_handled: open_set
real_data_cost: none
bottleneck_named: "Industry-reported utility, adoption and challenge factors for agentic AI."
coupling_door: neutral
ownership_door: neutral
outreach_status: off_scope
outreach_note: >
  **Dropped as a target — but READ IT.** No address in the source package. It is a survey of
  practitioner perspectives on agentic AI adoption in engineering and manufacturing, which
  makes it secondary literature on H2A3's question rather than a team to talk to. Not promoted
  to the evidence ledger: a perspectives survey is not [T]/[V]-grade buyer evidence and must
  not enter as if it were.
published_emails: []
source_url: https://arxiv.org/abs/2604.09633


---

# BATCH 3 — digital thread and interoperability (2026-09-02)

The query the belief was written for. Four rows, **two reachable** — the worst yield of the
three batches, and the reason is worth recording: the two most relevant papers in the entire
sweep are by a solo author who redacted his arXiv address.

**Batch 3's finding:** the interoperability problem is being attacked from two directions that
do not talk to each other. One is ontology-and-standards (RDF, ISA-95, OPC UA, AAS, RAMI 4.0)
— comprehensive, slow, and the approach that has been "about to work" for fifteen years. The
other is MCP adapters wrapping the protocols directly — crude, fast, and three months old.
The founder's belief is compatible with both, and the choice between them is a real
architectural fork this map can now name.

## 2603.24703 — IndustriConnect: MCP adapters for industrial protocols

canonical_name: "Luleå University of Technology · IndustriAgents"
paper_date: 2026-03-25
site_control: simulation_only
handoff_automated: intent_to_program
integration_labour: standards_layer
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  The observation the paper opens on is the whole belief in one line: AI assistants can
  decompose multi-step workflows but **do not natively speak Modbus, MQTT/Sparkplug B or
  OPC UA**. So they built MCP adapters exposing industrial operations as schema-discoverable
  tools, with a mock-first workflow that lets adapter behaviour be exercised before it touches
  plant equipment. Benchmarked over **870 runs and 2,820 tool calls** across 7 fault and 12
  stress scenarios; the normal suite passed fully and the fault suite confirmed structured
  error handling.
handoff_automated_limit: >
  Mock-first means exactly that — no plant equipment in the evaluation. 870 runs against mocks
  is a software result, not a deployment result, and the row must not be read as one.
integration_labour_detail: >
  The only row in three batches classified standards_layer on its own evidence rather than on
  its group's reputation: the adapters wrap open protocols, so the claim to carry across
  vendors is structural rather than aspirational.
bottleneck_named: "AI assistants do not natively speak industrial protocols."
coupling_door: supports_broken
coupling_door_detail: "The paper exists because the coupling is absent. Its premise IS link 1."
ownership_door: supports_layer
ownership_door_detail: >
  **The batch's sharpest challenge to link 2.** If MCP adapters over Modbus and OPC UA work on
  real plant, a company can reach the machines without owning them — which is the belief's
  first accepted threat, arriving three months old and from a working prototype. Its limit is
  that it has not met plant equipment. Ask about that directly.
outreach_status: pending
outreach_note: "Highest-priority target in batch 3 and arguably the whole sweep — a university address AND a company address, on the founder's exact stated theme. Midhun Xavier at IndustriAgents is commercialising it, which makes him the one who knows what breaks on real plant."
published_emails: [melwin.xavier@ltu.se, midhun@industriagents.com]
source_url: https://arxiv.org/abs/2603.24703

## 2608.24918 — Semantic graph unification across 11 manufacturing systems

canonical_name: "Grama Chethan (solo author, no affiliation stated)"
paper_date: 2026-08-11
site_control: simulation_only
handoff_automated: none
integration_labour: standards_layer
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  An ontology-driven RDF knowledge graph unifying **11 simulated sources across nine domains**
  through a five-stage ETL pipeline with automated entity resolution over 97 owl:sameAs links;
  the ontology carries 78 RDFS classes, 108 object properties and 243 data properties, drawing
  on ISA-95, OPC UA, eClass, the Asset Administration Shell and RAMI 4.0.
handoff_automated_limit: "Eleven SIMULATED sources. No real ERP, MES or SCADA instance was connected."
bottleneck_named: >
  "ERP, MES, PLM, SCADA, QMS, SCM — each with its own data model and API. Point-to-point
  integration scales as O(n²) and accumulates brittle dependencies."
coupling_door: supports_broken
coupling_door_detail: >
  **The most precise statement of link 1 found anywhere in this sweep**, and it names the
  mechanism the founder's own experience only described: the cost is not that any one pair
  won't talk, it is that point-to-point integration is O(n²). That is why a person retypes
  things — it is cheaper than the nth adapter.
ownership_door: supports_layer
outreach_status: off_scope
outreach_note: >
  **UNREACHABLE — and this is the batch's real loss.** No address in the source package; arXiv
  redacts the submitter address ("view email" is gated). Solo author, no affiliation stated, so
  no institutional page to fall back on. **The O(n²) finding above belongs in
  `03-validation/evidence.md` and is NOT there yet** — it was left out deliberately because
  another session was mid-edit in that ledger on 2026-09-02 and allocating an E-id against a
  moving file is the exact collision CLAUDE.md's push discipline exists to prevent. Promote it
  once the ledger is settled.
published_emails: []
source_url: https://arxiv.org/abs/2608.24918

## 2608.21418 — Composable trust infrastructure for manufacturing knowledge graphs

canonical_name: "Grama Chethan (solo author, no affiliation stated)"
paper_date: 2026-08-13
site_control: simulation_only
handoff_automated: none
integration_labour: standards_layer
variability_handled: open_set
real_data_cost: none
handoff_automated_detail: >
  Four trust capabilities — SHACL validation, PROV-O provenance, bi-temporal versioning and
  graph-native decision objects — composed through shared correlation identifiers. The ablation
  is the useful part: removing any single capability breaks exactly three of six composition
  queries.
bottleneck_named: >
  "Consumers cannot determine whether queried data is valid, whether it was valid when a
  decision was made, where it originated, or how it was acted upon."
coupling_door: supports_broken
coupling_door_detail: >
  Relevant to H2 in a way the author did not intend: that quoted sentence is the reason a
  buyer will not accept a non-OEM part (H2A2). The barrier is provenance, not machining.
ownership_door: supports_layer
outreach_status: off_scope
outreach_note: "Same author, same unreachability as 2608.24918. Companion paper — read both or neither."
published_emails: []
source_url: https://arxiv.org/abs/2608.21418

## 2608.29379 — Constrained LLMs bridging semantics and physics

canonical_name: Imperial College London
paper_date: 2026-08-29
site_control: lab_cell
handoff_automated: intent_to_program
integration_labour: not_reported
variability_handled: task_family
real_data_cost: none
bottleneck_named: "Language-level plans are not physically grounded, so a semantically correct instruction can be an unsafe motion."
coupling_door: supports_broken
ownership_door: supports_layer
outreach_status: pending
outreach_note: "London-based and reachable, on the constraint problem the Chalmers and KTH rows also hit. No draft written — send only if the Tier A wave underperforms."
published_emails: [d.zhang17@imperial.ac.uk]
source_url: https://arxiv.org/abs/2608.29379
