---
purpose: The send-ready researcher email drafts for batch 1, each with the claim-by-claim grounding that makes it defensible.
idea: high-mix-manufacturing
campaign: researchers-2026-09
created: 2026-09-02
channel: email
from_address: "TBC — founder to confirm the Cambridge alumni address; founders/izgin-ozdas.md has reply_email empty"
status: drafted_not_sent
---

# Researcher emails — batch 1

**The founder sends every one of these by hand.** Nothing here has been sent.

Grounding source for every row: `../../research-map.md`. Every factual claim about a paper
below is traceable to a row there; every claim about the founder to `founders/izgin-ozdas.md`.

## Before the first send

1. **Set the from address.** These are written to be read as coming from a Cambridge
   address — that is the whole reason the opener works on academics. Confirm it and I will
   write it into `founders/izgin-ozdas.md → outreach_identity.reply_email`, which is the
   single author for that fact.
2. **Do not paste a scheduling link.** `schemas/copy-rules.md` bans them from outreach copy.
   Offer times; send the link only if they ask.
3. **Send in waves of 5-6**, not all at once. If the first wave gets no reply the problem is
   the opener, and you want to find that out on six emails rather than seventeen.
4. **Send Tier A on a weekday morning in the recipient's timezone.** CET for KTH, Chalmers,
   DFKI; SGT for NTU; ET for Sewbo and Cornell.

## Ordering

Tier A first — these nine are the ones whose method sits directly on the belief. Tier B is
real but secondary. Send Tier A, wait 48h, then Tier B regardless of replies.

Batch 2 (A7, A8, B7-B9) came from the CAD-and-drawings scan and is, if anything, closer to the
founder's own research than batch 1. A7 in particular: a solo author at a small company working
on verified G-code generation is the single most likely reply in the whole campaign.

---

# TIER A

## A1 · Jonathan Zornow — Sewbo · `jon@sewbo.com`

Paper: [2606.16078](https://arxiv.org/abs/2606.16078) — robotic apparel automation, DXF digital thread.
Why first: he is a founder who has spent a decade on robotic sewing, and his paper automates
the exact link the founder measured at Cambridge. Lowest formality barrier in the batch.

**Subject:** DXF to robot trajectories — I measured the same gap at Cambridge

> Hi Jon,
>
> I read the denim deployment paper — specifically the digital thread module that parses DXF
> production drawings into process parameters and executable trajectories.
>
> I spent last year at Cambridge's Institute for Manufacturing measuring that same handoff.
> I got 100% F1 annotating DXF metadata and 74% on STEP, and came away thinking the geometry
> was the easy half. Yours is the first work I've read where someone put the DXF half on an
> actual factory floor.
>
> Two things the paper left me wondering. How much of that parser survived the move from the
> first staged deployment to the second? And was the re-targeting cost dominated by the
> drawings or by the fixtures?
>
> I ran a high-mix CNC shop for two years before Cambridge and I'm building in San Francisco
> now, trying to work out whether this handoff can be sold as a layer over machines you don't
> own, or whether you have to own them. Ten years of Sewbo probably gives you a view.
>
> Any chance of 25 minutes in the next couple of weeks?
>
> Izgin

Grounding: DXF module and staged deployments → research-map 2606.16078. 100%/74% F1 →
founders/izgin-ozdas.md selected_projects_and_outputs. Two years CNC → IMTEK 2022-2024, same file.

---

## A2 · Omkar Salunkhe / Siyuan Chen — Chalmers · `omkar.salunkhe@chalmers.se`, `siyuan.chen@chalmers.se`
cc or separate: `johan.stahre@chalmers.se`, `anders.skoogh@chalmers.se`

Paper: [2608.21417](https://arxiv.org/abs/2608.21417) — MCP server between an LLM and ABB RobotStudio.
Why: the only MCP-for-manufacturing paper in the batch, and the one row that supports the
"layer, not ownership" side of the belief. Write to the hands first, the PIs second.

**Subject:** The expert setup your MCP loop didn't eliminate

> Hi Omkar,
>
> Your RAPID generation paper is the first thing I've seen that puts MCP between a model and
> a real robot controller, so I read it closely.
>
> The line I keep coming back to is your own: the loop reduces "but does not eliminate expert
> setup and final supervision." That residue is the thing I care about. What is actually left
> in it — is it the RobotStudio cell model, the fixture and tooling assumptions, or the
> judgement about whether a generated motion is safe to run?
>
> I ask because I measured the upstream half of this at Cambridge's IfM last year (DXF and
> STEP metadata annotation, 100% and 74% F1) and I'm now building on the assumption that the
> residue is where the real cost sits. I'd rather hear from someone who has measured it than
> keep assuming.
>
> Also curious whether anything in the MCP server would survive pointing it at a Fanuc.
>
> Would you have 25 minutes? I'm in San Francisco but will work to CET.
>
> Izgin

Grounding: the quoted limit and the simulated pick-and-place cell → research-map 2608.21417.
Fanuc question → the row's `vendor_stack` classification.

---

## A3 · Muhammad Tayyab Khan / Seung Ki Moon — NTU · `khan0022@e.ntu.edu.sg`, `skmoon@ntu.edu.sg`

Papers: [2608.24039](https://arxiv.org/abs/2608.24039) — Design-to-Plan, CAD + 2D drawings → process plan.
And [2602.18296](https://arxiv.org/abs/2602.18296) — binding GD&T callouts and datums to 3D CAD features.

Why: **Khan has published twice this year on the exact seam the founder measured at Cambridge.**
Citing both is what separates this email from a template — nobody who skimmed one paper knows
there is a second. Send ONE email covering both, not two emails.

**Subject:** Two papers on the same seam I spent a year measuring

> Hi Tayyab,
>
> I've now read both Design-to-Plan and the earlier paper on mapping drawing annotations to 3D
> CAD features, and I wanted to write because you are working on the thing I spent last year
> measuring.
>
> I did an MPhil at Cambridge's Institute for Manufacturing on CAD-CAM interoperability —
> annotating DXF metadata at 100% F1 and STEP at 74% — and came away convinced the geometry
> was the tractable half and the *intent* was not. Your line that 2D drawings remain the
> primary carrier of manufacturing intent in automotive, aerospace, shipbuilding and heavy
> machinery, twenty years after MBD, is the cleanest statement of that I have read anywhere.
>
> Two questions.
>
> On Design-to-Plan: across the 300 benchmark cases, when the framework got it wrong, was the
> failure in reading the drawing or in the manufacturing rules it retrieved? I spent two years
> quoting and running one-off precision work in a CNC shop and my instinct is that the drawing
> is the easy part and the rules are tacit — but that's an instinct and you have the data.
>
> On the annotation mapping: how far does it survive a drawing that is a scan rather than a
> clean vector file? That is the case I keep hitting in practice.
>
> I'm building in this space in San Francisco. Would 30 minutes be possible?
>
> Izgin

Grounding: 300 benchmark cases and the agents-over-deterministic-modules architecture →
research-map 2608.24039. The MBD / drawing-as-carrier line and GD&T binding → research-map
2602.18296. Note the map's stated limit on 2608.24039: process planning is NOT quoting, and
the email asks about planning failures without claiming otherwise.

---

## A4 · Martin Ruskowski — DFKI Innovative Factory Systems · `martin.ruskowski@dfki.de`
also: `achim.wagner@dfki.de`

Paper: [2604.06949](https://arxiv.org/abs/2604.06949) — composite skills + residual RL for peg-in-hole.
Why: **highest-leverage contact in the batch for the belief itself.** SmartFactory-KL exists to
answer whether a vendor-neutral production layer can work, which is the founder's link 2.
Write to him about that, not about peg-in-hole.

**Subject:** Does the vendor-neutral layer hold, or do you end up owning the machines?

> Dear Professor Ruskowski,
>
> I read your group's composite-skill paper — the pre/post/invariant condition encapsulation
> with residual RL restricted to refinements inside each skill. The formalism is what
> prompted me to write, but my question is really about SmartFactory-KL.
>
> I did an MPhil at Cambridge's IfM last year measuring the CAD-to-machine handoff — 100% F1
> annotating DXF metadata, 74% on STEP — after two years running production in a high-mix
> cryogenics shop where that handoff was done by a person retyping things. I came out
> convinced the coupling is genuinely broken. Where I'm stuck is what follows from that.
>
> The advice I keep getting is that you have to own both the software and the machines to fix
> it. SmartFactory-KL is the most serious attempt I know of at the opposite answer — a
> vendor-neutral layer over equipment nobody owns end to end. After years of running it, do
> you think that layer holds commercially, or does each new participant still cost bespoke
> integration?
>
> I'm building in San Francisco and would value 30 minutes, at whatever time suits.
>
> Izgin Ozdas

Grounding: composite skills / residual RL / MuJoCo-only evaluation → research-map 2604.06949.
SmartFactory-KL and AAS → the row's `integration_labour_detail`, which flags that the
standards_layer classification rests on the group's programme, not on this paper. The email is
written to match: it asks about the programme and does not claim the paper proved the layer.

---

## A5 · Lihui Wang / Xi Vincent Wang — KTH · `lihuiw@kth.se`, `wangxi@kth.se`
technical follow-up: `tianyuwa@kth.se`

Paper: [2606.08214](https://arxiv.org/abs/2606.08214) — agentic neuro-symbolic planning and commissioning.
Why: senior, formal-verification-adjacent, and the ablation result is genuinely load-bearing
for anyone planning to build this.

**Subject:** Your ablation is the most useful negative result I've read this year

> Dear Professor Wang,
>
> I read your Specifier-Designer-Inspector paper. The part I found most valuable was the
> ablation: that structured command expansion, symbolic verification, selective LLM routing
> and recovery skills are each individually necessary. In a literature full of papers claiming
> the LLM is enough, a clean demonstration that it isn't is worth more than the framework.
>
> My question is about the digital twin. Verifying against a Unity3D model before physical
> execution presupposes you know the cell precisely — which is affordable if you built the
> cell and expensive if you didn't. In your experience, how much of the commissioning effort
> is building that model, and does any of it carry to the next cell?
>
> I measured the upstream half of this problem at Cambridge's IfM last year — DXF and STEP
> metadata annotation, 100% and 74% F1 — and spent two years before that running high-mix
> production where nothing passed cleanly between CAD, the machines and the ERP. I'm building
> on that in San Francisco now and trying hard to find out where the real cost sits before I
> commit to an architecture.
>
> Would 30 minutes be possible in the next few weeks?
>
> Izgin Ozdas

Grounding: SDI architecture, LangGraph routing, Unity3D twin, ablation → research-map 2606.08214.
The digital-twin question is the row's `ownership_door_detail` turned into a question.

---

## A6 · Yunho Kim — Neuromeka · `yunho.kim@neuromeka.com`

Paper: [2604.22235](https://arxiv.org/abs/2604.22235) — learning-augmented automation on a live line.
Why: the batch's hardest numbers. **Screen note: Neuromeka builds cobots and validated on its
own process — treat what he says as vendor-side, not buyer-side, evidence.**

**Subject:** The 20 minutes per task — what did the 5 hours cost to set up?

> Hi Yunho,
>
> Under 20 minutes of real data per task, 5 hours 10 minutes continuous, 108 motors, 99.4%
> pass rate, no fencing. That is the most concrete deployment result I've read all year and
> I've been arguing with it for a week.
>
> What the paper doesn't say is what came before the 20 minutes. How long did the cell take
> to set up, who did it, and how much of that would repeat on the next line? I'm trying to
> work out whether the 20 minutes is the real cost or the visible one.
>
> The reason I care: I ran production for two years at a high-mix cryogenics manufacturer
> where every job needed its own setup, then spent a year at Cambridge measuring why CAD,
> CAM and ERP don't pass data cleanly. I'm now building in San Francisco on the bet that
> per-job setup is the thing worth automating, and your numbers are the closest thing to a
> reality check I've found.
>
> Would you have 25 minutes? Happy to work to KST.
>
> Izgin

Grounding: every number → research-map 2604.22235 `real_data_cost_detail`. The email deliberately
asks the question the row flags as unanswered ("no carry to another site is claimed or tested").

---

## A7 · Yeonseok Lee — Sling AI · `ylee@sling.ai.kr`

Paper: [2605.10568](https://arxiv.org/abs/2605.10568) — correct-by-construction G-code via separation logic.
Why: solo author, small company, and the topic is CAD-to-cut with a correctness guarantee.
Highest reply probability in the campaign.

**Subject:** Spatial data races — has the SL prover met a real machine yet?

> Hi Yeonseok,
>
> Treating a physical collision as a Spatial Data Race, and a separation-logic proof failure
> as a bounding box the model can correct against, is the most elegant framing of G-code
> verification I've come across. I read the paper twice.
>
> What I want to know is what happened when it met a machine. The framework extracts B-Rep
> from STEP through OpenCASCADE, which is the right foundation — but the gap between a proof
> of non-collision and a part that actually comes off the machine to tolerance is where I've
> lost money personally. Have you run any of the generated G-code on real hardware, and if so
> what broke first?
>
> My background: two years running a high-mix CNC shop doing sub-micron cryogenics work, then
> an MPhil at Cambridge measuring the CAD-to-machine handoff — 100% F1 annotating DXF metadata,
> 74% on STEP. I'm building on that in San Francisco. Verified toolpath generation is close to
> the centre of what I think has to exist.
>
> Would you have 25 minutes? Happy to work to KST.
>
> Izgin

Grounding: Spatial Data Race framing, OpenCASCADE B-Rep extraction, bounding-box feedback →
research-map 2605.10568. The map flags that no machine ran this G-code, which is exactly what
the email asks — do not send a version that assumes it did.

---

## A8 · Amir Barati Farimani — Carnegie Mellon · `barati@cmu.edu`

Paper: [2607.02448](https://arxiv.org/abs/2607.02448) — AgentsCAD, automated DFM for FDM parts.

**Subject:** Does the 59,665-part feature model carry to subtractive DFM?

> Dear Professor Barati Farimani,
>
> I read AgentsCAD — parsing STEP, building the face-adjacency topology graph, injecting
> semantic feature labels from a GraphSAGE model trained on MFCAD++'s 59,665 parts, and only
> then letting a reasoning agent recommend modifications.
>
> The sequencing is what I want to ask about. You do deterministic geometry first and the
> model second, and I've now read four unrelated 2026 papers that independently land on the
> same constraint — nobody who evaluated carefully let the model read the STEP file directly.
> Was that a considered design decision from the start, or did you try the direct version and
> watch it fail?
>
> Second question: how much of the feature recognition would survive a move from additive to
> subtractive DFM? Overhang rules don't transfer, but the face-adjacency representation might.
>
> I ran high-mix precision manufacturing for two years and then measured the CAD-to-machine
> handoff at Cambridge's IfM (DXF metadata annotation 100% F1, STEP 74%). I'm building on it in
> San Francisco and would value 25 minutes.
>
> Izgin Ozdas

Grounding: GraphSAGE / MFCAD++ / 59,665 parts / face-adjacency graph → research-map 2607.02448,
which also records the additive-to-subtractive limit the second question asks about.

---

## A9 · Midhun Xavier — IndustriAgents · `midhun@industriagents.com`
also (academic side): Melwin Xavier, Luleå — `melwin.xavier@ltu.se`

Paper: [2603.24703](https://arxiv.org/abs/2603.24703) — IndustriConnect, MCP adapters for
Modbus / MQTT Sparkplug B / OPC UA.

Why: **the closest paper in the whole sweep to what the founder said he wanted to talk about**,
and the sharpest live challenge to the belief's link 2 — if MCP adapters reach real plant, you
do not need to own the machines. Write to the company address first: he is the one who will
know what breaks outside the mocks.

**Subject:** Has IndustriConnect met real plant equipment yet?

> Hi Midhun,
>
> "AI assistants can decompose multi-step workflows, but they do not natively speak Modbus,
> MQTT/Sparkplug B or OPC UA" is the sentence I've been trying to write for a year, and you
> opened a paper with it.
>
> The benchmark is serious — 870 runs, 2,820 tool calls, fault and stress and recovery
> scenarios — but it is mock-first by design. So the question I actually want to ask is what
> happened the first time an adapter met real plant equipment. What broke that the mocks
> didn't predict?
>
> I ask because I'm making an architectural bet in the opposite direction and would rather be
> talked out of it early. I ran production for two years at a high-mix precision manufacturer
> where ERP, CAM and the machines never passed data cleanly, then measured that handoff at
> Cambridge's IfM — 100% F1 annotating DXF metadata, 74% on STEP. The advice I keep getting is
> that you have to own the machines to fix any of this. IndustriConnect is the best argument
> I've seen that you might not.
>
> Would you have 25 minutes? I'm building in San Francisco and will work to any timezone.
>
> Izgin

Grounding: the opening quote, the 870/2,820 benchmark and the mock-first design →
research-map 2603.24703, which also records the limit the second paragraph asks about — no
plant equipment appears in the evaluation.

---

# TIER B

Same structure, shorter. Send 48h after Tier A.

## B1 · Florian Töper — Mercedes-Benz · `florian.toeper@mercedes-benz.com`

Paper: [2608.28175](https://arxiv.org/abs/2608.28175) — bin picking to empty in production.

**Subject:** "Labour-intensive fine-tuning of grasp points for new parts"

> Hi Florian,
>
> Your bin-picking paper names something I've been trying to get people to say out loud:
> that labour-intensive fine-tuning of grasp points is commonly required **for new parts**.
> Per-new-part engineering labour is the thing that decides whether high-mix automation pays,
> and it's usually left out of the write-up.
>
> Two questions. Roughly how many hours went into a new part before the exploration agent, and
> how many after? And is that cost mostly perception, or mostly fixturing?
>
> I ran production at a high-mix precision manufacturer for two years and then measured the
> CAD-to-machine handoff at Cambridge (DXF metadata annotation, 100% F1; STEP, 74%). I'm
> building on that in San Francisco. Your paper is one of the few from inside an OEM that is
> honest about setup cost, which is why I'm writing to you rather than to a lab.
>
> Any chance of 25 minutes?
>
> Izgin

## B2 · Hanxiao Liu / Tengbo Yu — Peking University · `hx.liu@pku.edu.cn`

Paper: [2608.17962](https://arxiv.org/abs/2608.17962) — PRISM industrial contact-rich dataset.

**Subject:** 45 hours in PRISM vs 20 minutes per task on a live line

> Hi,
>
> I've been reading PRISM alongside a deployment paper from Neuromeka, and the pair of numbers
> is stark: you collected 5,000+ trajectories and 45 hours across 25 tasks, while they
> fine-tuned a live production task on under 20 minutes of real data.
>
> My question is what the 45 hours buys that the 20 minutes doesn't. Concretely: has anything
> trained on PRISM transferred to a task that wasn't in the set, and if so how much of the
> gap closed?
>
> I'm a manufacturing engineer by background — two years running high-mix precision
> production, then a Cambridge MPhil measuring why CAD and machine data don't connect — and
> I'm building in San Francisco. Whether industrial skill data is a moat or a commissioning
> line item is a decision I have to make soon, and your dataset is the best evidence either way.
>
> 25 minutes if you can spare it?
>
> Izgin

## B3 · Huan Zhao / Han Ding — HUST · `huanzhao@hust.edu.cn`, `dinghan@hust.edu.cn`

Paper: [2606.25754](https://arxiv.org/abs/2606.25754) — stage-aware roughness-constrained polishing.

**Subject:** Roughness-constrained polishing — does it hold on a variable workpiece?

> Dear Professor Zhao,
>
> I read your SRDP paper — inferring the process-stage posterior from observation history
> without external stage labels at execution, and constraining sampling on surface roughness.
> Conditioning on a measured process outcome rather than on a trajectory is the part I think
> generalises furthest.
>
> My question is about variability. Your evaluation holds the workpiece family roughly fixed.
> If the incoming geometry varied significantly piece to piece — as it does in one-off and
> small-batch work — does the stage posterior still resolve, or does it need re-fitting?
>
> I spent two years in high-mix precision manufacturing where finishing was the operation
> nobody could automate, and then a year at Cambridge measuring the CAD-to-machine handoff.
> I'm building in San Francisco now. Finishing is the step I keep being told to avoid, and
> I'd like to understand properly whether that advice is still current.
>
> Would 25 minutes be possible?
>
> Izgin Ozdas

## B4 · Ziwei Wang — NTU · `ziwei.wang@ntu.edu.sg`

Paper: [2609.01596](https://arxiv.org/abs/2609.01596) — Facet-0, contact-rich precise manipulation.

**Subject:** Facet-0's wrench prediction and per-part dynamics

> Hi Ziwei,
>
> I read Facet-0 the week it went up. Generating each action chunk together with the wrist
> wrench it expects to induce, then training a critic to separate motions with similar task
> progress but different contact outcomes, is a cleaner statement of the problem than most
> assembly work manages.
>
> The question I have is about the lightweight per-part adaptation. In small-batch
> manufacturing the part changes constantly. How much data does a new part need before the
> action-wrench critic is useful again, and does that cost scale with tolerance?
>
> Background: two years running high-mix precision production, then an MPhil at Cambridge
> measuring why CAD, CAM and machine data don't connect. Building in San Francisco now.
>
> 25 minutes if you have it?
>
> Izgin

## B5 · Aditya Chetan — Cornell · `achetan@cs.cornell.edu`

Paper: [2605.21625](https://arxiv.org/abs/2605.21625) — Flat-Pack Bench.

**Subject:** Where do the models actually fail on Flat-Pack Bench?

> Hi Aditya,
>
> I read Flat-Pack Bench — fine-grained temporal ordering and localisation on furniture
> assembly video, built because existing benchmarks only test coarse tasks on verbally obvious
> objects.
>
> The benchmark result I'd most like to understand is the failure structure. When the best
> models get temporal ordering wrong, is it because they can't tell two similar parts apart,
> or because they don't represent the constraint that step N has to precede step N+1?
>
> I'm a manufacturing engineer building in San Francisco — two years in high-mix production,
> then a Cambridge MPhil on the CAD-to-machine handoff. I'm interested in whether a model can
> read an assembly the way a person does, and your failure cases are more informative to me
> than the headline scores.
>
> Any chance of 25 minutes?
>
> Izgin

## B6 · Markus Knauer — `m.knauer@tum.de`

Paper: [2604.20468](https://arxiv.org/abs/2604.20468) — MOMO, multimodal skill adaptation.

**Subject:** LLM parameterising predefined functions — did you try code generation first?

> Hi Markus,
>
> I read MOMO — kinesthetic correction, natural language, and drag-and-drop via-point editing
> as three routes to the same adaptation.
>
> The choice I want to ask about is the tool-based LLM architecture: selecting and
> parameterising predefined functions rather than generating code. I've now read three
> unrelated 2026 papers that land on that same constraint, which makes me think it's a real
> finding rather than a preference. Did you try code generation first and back away from it,
> or start there?
>
> The reason it matters to me: I ran high-mix production for two years where the operators,
> not the engineers, were the ones who needed to change things — and then measured the
> CAD-to-machine gap at Cambridge. Whether a non-expert can safely adapt a cell decides
> whether small-batch automation is viable at all.
>
> 25 minutes?
>
> Izgin

## B7 · Hyungki Kim — Chungnam National University · `hk.kim@cnu.ac.kr`

Paper: [2607.27558](https://arxiv.org/abs/2607.27558) — Drawing-Recode, raster drawings → parametric CAD.

**Subject:** Raster drawings are the case I actually hit

> Hi Hyungki,
>
> Drawing-Recode works on the case almost nobody else does: raster drawings, the scanned and
> printed stock accumulated before digital transformation. Everyone else assumes a vector file
> exists. In my experience the ones that matter are the ones that don't.
>
> The Annotation Grounding Loss is the part I want to understand. Explicitly binding dimensional
> annotations to geometry through cross-attention, rather than hoping the model associates them,
> seems like the load-bearing idea. How much does accuracy fall off with scan quality — a clean
> 300dpi scan versus a photographed print?
>
> I ran a high-mix CNC shop for two years and then measured the CAD-to-machine handoff at
> Cambridge. The single most common reason a one-off part is hard to make is that the only
> drawing is a picture of a drawing. I'm building in San Francisco on that problem.
>
> 25 minutes if you can spare them?
>
> Izgin

## B8 · Hanjie Chen — Rice University · `hanjie@rice.edu`

Paper: [2605.10865](https://arxiv.org/abs/2605.10865) — BenchCAD.

**Subject:** What is the ceiling on the 106 industrial part families?

> Hi Hanjie,
>
> BenchCAD is the first CAD benchmark I've read that uses parts I recognise — bevel gears,
> compression springs, twist drills — rather than synthetic sequences, and 17,900
> execution-verified programs is a serious amount of work.
>
> The question I care about is the ceiling. Across the 106 industrial families, where does the
> best model actually top out on image-to-code, and is the residual failure geometric
> understanding or engineering-parameter inference? The distinction matters a lot to me: the
> first gets solved by scale and the second probably doesn't.
>
> I'm a manufacturing engineer — two years running high-mix precision production, then a
> Cambridge MPhil measuring why CAD and machine data don't connect — now building in San
> Francisco. Your benchmark is the closest thing to an honest answer about whether this is
> ready, which is why I'd rather ask you than infer it.
>
> Any chance of 25 minutes?
>
> Izgin

## B9 · Xiaoli Zhang — Colorado School of Mines · `xlzhang@mines.edu`

Paper: [2608.22128](https://arxiv.org/abs/2608.22128) — task-driven printability assistance.

**Subject:** Judging suitability before the part exists

> Dear Professor Zhang,
>
> Your framing stayed with me: printability is assessed before printing, task suitability only
> after — so a non-expert learns the material was wrong by holding the wrong part.
>
> That gap is not specific to additive. It is the same gap a buyer faces asking a machine shop
> whether a part can be made the way they need: nobody can tell them until it exists. Your
> framework grounds the answer in geometry evidence plus structured material and process
> knowledge, which is the shape I think the answer has to take.
>
> My question: how much of the reliability comes from the structured knowledge base versus the
> geometry grounding? If it is mostly the knowledge base, the approach transfers to machining
> by swapping the base. If it is mostly geometry, it doesn't.
>
> Background: two years in high-mix precision manufacturing, then a Cambridge MPhil on the
> CAD-to-machine handoff. Building in San Francisco now.
>
> Would 25 minutes be possible?
>
> Izgin

---

# The closing line — use it in every email that gets a reply

Not in the first email. Once someone answers, before the call ends:

> Who else should I be reading on this? I'd rather find the person who thinks I'm wrong.

That is the intro ask, and it converts far better after a conversation than inside a cold email.

# Advisor and recruiting — the timing rule

Do NOT raise it in email 1. Every draft above is a genuine technical question, which is why
they will get answered. Raise collaboration only when they have already spent 25 minutes
being interested — the natural moment is the end of the call:

> I'm going to be building this for the next couple of years. If it stays interesting to you,
> I'd like to keep you in the loop and come back with harder questions.

That is an advisor conversation starting, without asking anyone for anything they'd have to
decline.
