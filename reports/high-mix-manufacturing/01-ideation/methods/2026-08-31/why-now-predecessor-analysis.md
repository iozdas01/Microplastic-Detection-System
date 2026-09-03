---
method: why-now-predecessor-analysis
run_id: "2026-08-31"
mode: explore
card: methods/ideation/why-now-predecessor-analysis.md
status: founder_opted_conditional_lens
note: Not in explore_pool. Added on founder request 2026-08-31.
counter_query_run: yes - "who tried and SUCCEEDED" (omitted in the first pass; it changed the verdict)
---

# Why-now and predecessor analysis

## Predecessors

| Predecessor | Outcome | Failure cause | Class | Source |
|---|---|---|---|---|
| **Protolabs** (1999-) | **alive, profitable** — $533M rev, $1.45B cap, 44% GM | n/a — succeeded | **success** | [AMT](https://www.amtonline.org/article/protolabs-innovation-in-low-volume-manufacturing) |
| **Xometry** (2013-) | **alive, +41% YoY to $229M/qtr** | n/a — succeeded, asset-light | **success** | [3DPrint](https://3dprint.com/330078/3d-printing-financials-xometry-protolabs-and-lincoln-electric-post-strong-quarters/amp/) |
| **Cutwrights** (2009-) | alive, UK panel processing with instant online quotes | n/a | **success** | [cutwrights.com](https://www.cutwrights.com/) |
| **SendCutSend** | alive, instant-quote CNC routing incl. plywood/MDF | capped at 30x44in instant quote | **success, bounded** | [SendCutSend](https://sendcutsend.com/materials/baltic-birch-plywood/) |
| Fictiv | $200M raised, ~$300M post-money | flat-to-down valuation | unknown | search result |
| **Katerra** | bankrupt 2021, ~$3bn destroyed | full vertical integration = many simultaneous single points of failure; Greensill collapse removed the lender | **wrong-idea** | [Failory](https://www.failory.com/cemetery/katerra) |
| **Lustron** (1948-50) | dissolved | could not deliver on time, could not beat traditional housing on cost, misread family demand | **wrong-idea** | [Tomorrow.City](https://www.tomorrow.city/lustron-homes/) |
| Modular/prefab sector | no major exit, no category leader, no scalable model after a decade and billions | factory economics, builder adoption/risk, market realities, capital structure | **wrong-idea** | [OneBuild](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard) |
| **Fab.com / Hem** | sold ~$15M after $336M raised (96% loss) | serial pivots, $14M/mo burn; vertical integration was a **late rescue attempt on an already-broken model**, not the thesis | **unknown** — do not cite as anti-vertical-integration | [TechCrunch](https://techcrunch.com/2014/10/20/fab-hem/) |
| Interior Define | ABC 2022-23 | cash crunch when **contract factories** and shippers raised prices | wrong-idea (argues *for* ownership) | [BOH](https://businessofhome.com/articles/interior-define-bankruptcy-questions-answered) |
| Model No. | absorbed by its 3D-printing supplier | owned factory + configurator was not sufficient | wrong-idea (argues *against* ownership) | [BOH](https://businessofhome.com/articles/3d-printed-furniture-company-model-no-is-acquired) |

**Wrong-time count: zero.** Not one predecessor failed because the technology was not ready.
Every diagnosable failure was wrong-idea — demand, cost, delivery, or operating leverage.

Per the card: *"wrong-idea predecessors are counterevidence, not timing proof."* This graveyard
is counterevidence.

## Required conditions for the belief

| Condition | Status | Threshold / change | Date | Evidence | Remaining risk |
|---|---|---|---|---|---|
| Automated CAD → firm quote is possible | **already true** | full manufacturability analysis + price in minutes | **1999** | Protolabs | none — it is 25 years old |
| Automated quote → toolpath is possible | **already true** | machine-ready G-code from design | 1999 (metal), ~2010s (panels) | Protolabs; Mozaik at $125/mo | none |
| ...for **standard** panel goods | **already true** | design→cut list→nesting→G-code | current | Mozaik; dconti: *"does that very well"* | none |
| ...for **custom, non-standard** millwork | **STILL FALSE** | placing parts without typing x,y,z; material allocation across a multi-room job | — | cncpgmr: *"horrendous to custom build with"* | **this is the only open condition found** |
| Instant online quoting for panels at carcass scale in the US | **uncertain** | above SendCutSend's 30x44in ceiling | — | UK has Cutwrights since 2009; no US analogue found | may be demand, not capability |
| Buyers will buy this way | **uncertain** | — | — | untested in every vertical | the whole demand side |

## Why-now conclusion

**The belief's stated why-now does not survive.** "LLMs plus constraint solvers make this
newly possible" is false as written: the mechanism shipped in 1999 and is $125/month for
standard cabinet work today.

**A narrower why-now may survive.** Exactly one required condition is still false: the
design-to-machine handoff for **custom, non-standard** millwork, where the cheap tool is
described by a 30-year veteran as *"garbage"* and *"horrendous"*, and the work is done by
typing coordinates. That is a real unautomated step, in scope, described unprompted by
someone in the segment. Whether LLMs plus solvers cross *that* threshold is untested and is
the honest form of the why-now claim.

## Counterevidence

**The counter-query is the finding of the run.** Asking who *succeeded* rather than who died:

| | Xometry (asset-light) | Protolabs (asset-heavy) |
|---|---|---|
| Quarterly revenue | **$229M, +41% YoY** | $149.3M, +10.6% |
| Guidance | raised to 33-34% growth | 8-10% growth |
| Gross margin | 35.7% | **44%** |
| Factories | **none** | ~1M sq ft owned |

The company that does **not** own the machines is larger and growing roughly four times
faster. The company that owns them earns more per dollar. Both are alive.

That is direct evidence against *"you have to own both ends to fix it"* as a necessity claim —
and it partially satisfies the founder's own disconfirmer #1, which was written before this
was known.

Per card step 7 — do the same changes enable incumbents? **Yes.** Mozaik at $125/month is the
falling barrier arriving for everyone. A falling barrier is timing evidence, not a moat.

## Still-too-early trigger

The hunch is still too early if custom-millwork shops, asked directly, say their coordinate
entry and material allocation is an annoyance rather than a cost — or if they will not pay to
remove it. One conversation with cncpgmr's segment settles it.
