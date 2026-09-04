---
purpose: The contact ledger for this idea — one record per person approached, their signal, and where the conversation got to.
idea: high-mix-manufacturing
last_updated: 2026-09-04
totals:
  targeted: 94
  invited: 65
  accepted: 9
  scheduled: 0
  done: 0
  no_reply: 0
---

# Contacts — high-mix-manufacturing

> **2026-09-03 — H3 (made-to-measure window coverings) is the active hunch.** Every contact
> below was sourced against the H1 or H2 ICPs and none of them validates H3, so all are
> `held`. They are deliberately NOT deleted and NOT `off_scope`: C-ids are burned on deletion
> and never reused, and nothing about these people's fit for their own assumption failed.
> H1 and H2 are both `superseded`, which means un-falsified and revivable, so reviving either
> lane restores its contacts, its live-verified snapshots and its drafts by flipping `held`
> back to `pending`. One contact stays live: C20 Viliam Kacerik, sent 2026-09-02, because a
> thread in flight is never retroactively closed.
>
> **H3 contacts do not exist yet.** Run `/startup-outreach-targets` against H3A1.

Batch 1 for **H2A1**, written 2026-09-02 from the LinkedIn export (Passes 0 and 1 — no
browser). All 17 are **1st-degree**, so none of them needs an invite: the founder can message
each one directly, which is why this batch skips the connect-and-wait latency entirely.

**Correction, 2026-09-02.** An earlier note here claimed the network held "0 furniture
manufacturers and 1 machinist" and concluded the founder's industrial access was not on
LinkedIn. That framing was wrong and it under-counted this batch by more than half. It came
from a grep for the SUPPLY side (people who operate CNCs), which is the opposite of this
ICP: H2A1 is about people who NEED a part, not people who make one.

Recounted company-first, which is what the ICP actually says ("inside manufacturers and
asset-heavy operators"): **242 connections are at a manufacturer or asset-heavy operator,
and 53 of those hold a role that would personally feel a blocked part.** The first pass
found 17 because it filtered on title nouns (supply chain, maintenance, procurement) and
missed engineers at manufacturers whose titles carry none of those words — supplier
quality, fleet engineering, avionics, industrial engineering, F1 aero.

Wave 1 (C1-C17) is live-snapshot verified. **Wave 2 (C18-C38) is not**: it is drawn from
the export only, so prior-contact state is unchecked and no profile has been re-read. Both
are required by LR-B25 and LR-B6 before any of those is drafted.

**Four have replied to the founder before** (Cliffe, Satish, Tahir, Kumar — all within the
last 7 months) and should be opened as continuations, not cold intros. **Two were messaged
in the last three weeks and did not reply** (Thoresson, Macron); both are flagged
`no_reply` and must not be re-blasted without a founder decision.

Excluded from the batch but useful, and deliberately NOT written as contacts because they
fail `icp_out_of_scope` for H2A1 (they describe the problem at one remove):

- **Intro multipliers** — Vanessa McNiven and Aamir Patel (Cambridge IfM), Tim Kimmig and
  Ozan Kaya (ETH-HSG Manufacturing Alliance). Each knows dozens of manufacturers. Worth a
  call for introductions, never as evidence of pain.
- **Expert/supply-side** — James Byrnes (VP Ops, LaserCraft Technologies) and Jadon Pauling
  (Factory Automation Systems) can speak to how variable one-offs get quoted today (H2A3),
  but no competitor or expert tier is declared on H2A3, so they are not demand evidence.
- **Internal** — Rumeysa Çınar (IMTEK) is the cost-model conversation, not a buyer.

C-ids are allocated monotonically and never reused.

## Charles Evans

id: C1
name: Charles Evans
linkedin_url: https://www.linkedin.com/in/charles-evans-198564158/
linkedin_account: Izgin
company: Boeing
role: Liaison Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Liaison engineering IS the unavailable-or-nonconforming-part function on an aircraft build — when a part is missing, late, or out of spec, he is the person who decides what happens next. He can describe blocked-part events from direct daily experience (H2A1), name who signs off a non-OEM substitution in the most compliance-heavy environment there is (H2A2), and say whether anyone ever went out to a machine shop (H2A3).

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · role sits exactly on the assumption (+4) · no prior contact (0) · large-employer response drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot: Boeing since Jan 2026 (9 mos), prior Pratt & Whitney 2y8m, Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Matthew Cliffe

id: C2
name: Matthew Cliffe
linkedin_url: https://www.linkedin.com/in/matthew-cliffe-126589144/
linkedin_account: Izgin
company: Ørsted
role: WTG Reliability Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Offshore wind turbine reliability — an asset class where a blocked part means a vessel mobilisation and six figures of lost generation, so the cost of the wait is measured rather than estimated. Directly answers H2A1's cost question and H2A3's 'did you ask a shop' question.

response_likelihood: 9
likelihood_factors: >
  1st degree (+2) · replied to founder 2026-07-15, 7 weeks ago (+3) · pain is quantified in his job (+3) · no active public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "Prior exchange in the archive: he replied 2026-07-15. Open with continuity, not a cold intro. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-07-15). Msg 1 is the wrong shape — route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Can Tafulcan

id: C3
name: Can Tafulcan
linkedin_url: https://www.linkedin.com/in/can-tafulcan-460324134/
linkedin_account: Izgin
company: LyondellBasell
role: Maintenance Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Petrochemical plant maintenance — the sector with the deepest obsolescence problem, where equipment outlives its OEM by decades and a blocked part can idle a unit. Turkish-speaking, which the founder shares. First-hand on H2A1 and H2A2.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · Turkish shared-language affinity (+1) · pain central to the role (+3) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[msg1 drafted 2026-09-02] soft_ask, written in Turkish (informal, LR-6). LIVE CORRECTION: LyondellBasell role ENDED Jul 2026, export had it as current. Drafted from the prior in-ICP role (LR-B8), past tense. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Margaux Ratcliff

id: C4
name: Margaux Ratcliff
linkedin_url: https://www.linkedin.com/in/margaux-ratcliff/
linkedin_account: Izgin
company: Viasat Inc.
role: Reliability Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Reliability engineering at a satellite-communications manufacturer — sees part failures and the sourcing scramble that follows, in a sector where qualification requirements are strict enough to make H2A2 a sharp test rather than a soft one.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · role-fit (+3) · no prior contact (0) · no public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot confirms Viasat current (4y4m); anchor is her own wording on antenna operating data and return rates. Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Heath Holtz

id: C5
name: Heath Holtz
linkedin_url: https://www.linkedin.com/in/heath-holtz-b57535/
linkedin_account: Izgin
company: Kohler Co.
role: Chief Operations, Supply Chain & Sustainability

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: supply_chain_procurement
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  C-level owner of supply chain at a major manufacturer — the person who would actually authorise a new source of supply, not merely report the pain. Highest-authority contact in the batch; can settle H2A2's sign-off question definitively.

response_likelihood: 5
likelihood_factors: >
  1st degree (+2) · buyer authority (+3) · C-level reply drag (-3) · stale 2019 outbound with no reply (-1) · no public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: no_reply
notes: "Founder messaged 2019-10-03, no reply. Seven years stale and about something unrelated — effectively a fresh approach, but the founder should confirm before sending. [msg1 drafted 2026-09-02] soft_ask, senior register (LR-B5). Founder messaged 2019-10-03, no reply; ~7 years stale so LR-B25 treats this as fresh Msg 1, not a follow-up. FOUNDER TO CONFIRM before sending. Live: Kohler C-level since Feb 2024, 50 sites / 18 countries. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Akshaya Satish

id: C6
name: Akshaya Satish
linkedin_url: https://www.linkedin.com/in/akshaya19/
linkedin_account: Izgin
company: Tata Advanced Systems Limited
role: Executive Manufacturing Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Manufacturing engineering in aerospace and defence — high-mix, low-volume, long-lead, heavily qualified parts. Exactly the environment where the blocked-part event is frequent and the non-OEM answer is hardest, which makes her a strong test of H2A2 rather than a friendly one.

response_likelihood: 9
likelihood_factors: >
  1st degree (+2) · replied 2026-08-12, 3 weeks ago (+3) · segment-fit (+3) · no public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "Prior exchange in the archive: replied 2026-08-12. Warm and recent — continue the thread. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-08-12). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Haroon Tahir

id: C7
name: Haroon Tahir
linkedin_url: https://www.linkedin.com/in/haroontahir/
linkedin_account: Izgin
company: Tesla
role: Senior Manufacturing Controls Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Manufacturing controls at Tesla — sits where machines, line software and spares meet, which is the founder's belief stated as a job description. Can speak to H2A1 and H2A3 from the line side.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · replied 2026-08-11, 3 weeks ago (+3) · role sits on the belief (+3) · large-employer drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "Prior exchange in the archive: replied 2026-08-11. Warm and recent. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-08-11). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Clynton Thoresson

id: C8
name: Clynton Thoresson
linkedin_url: https://www.linkedin.com/in/clynton-thoresson-8433424/
linkedin_account: Izgin
company: Agratas
role: Vice President of IT Manufacturing

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  VP of IT Manufacturing at a battery gigafactory build — owns the seam between manufacturing systems and the machines, and at gigafactory scale a blocked part is a commissioning delay with a board-level number attached.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · VP authority (+2) · role-fit (+3) · messaged 2026-08-11 with no reply (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: no_reply
notes: "FLAG: founder messaged 2026-08-11 (3 weeks ago), no reply. Do NOT re-blast blind — founder decides whether to follow up or leave it. [not drafted 2026-09-02] LR-B25: founder messaged 2026-08-11 (3 weeks), ours last, silent. That is a FOLLOW-UP, not a Msg 1 — carries no research anchor and must not repeat the ignored ask. Needs founder decision before drafting. [LR-B30 hold 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Gate is closed under 3 months and VP seniority does not open it. Do not write. Eligible as a no-anchor follow-up from 2026-11-11."

## Peter Macron

id: C9
name: Peter Macron
linkedin_url: https://www.linkedin.com/in/pmacron/
linkedin_account: Izgin
company: Boeing
role: Manufacturing Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Manufacturing engineering at Boeing — same environment as Charles Evans, from the process side rather than the disposition side. A useful cross-check: if two people at the same manufacturer describe blocked parts differently, that difference is itself the finding.

response_likelihood: 5
likelihood_factors: >
  1st degree (+2) · role-fit (+3) · messaged 2026-08-10 with no reply (-2) · large-employer drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: no_reply
notes: "FLAG: founder messaged 2026-08-10 (3 weeks ago), no reply. Do NOT re-blast blind — founder decides. [not drafted 2026-09-02] LR-B25: founder messaged 2026-08-10 (3 weeks), ours last, silent. Follow-up shape, not Msg 1. Needs founder decision before drafting. [LR-B30 hold 2026-09-02] Messaged 2026-08-10, 23 days, no reply, no buyer authority. Do not write. Charles Evans (C1) covers Boeing for this assumption, so nothing is lost."

## Mia Huff

id: C10
name: Mia Huff
linkedin_url: https://www.linkedin.com/in/miahuff/
linkedin_account: Izgin
company: DePuy Synthes
role: Supply Chain Senior Launch Specialist

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: supply_chain_procurement
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Medical-device supply chain at J&J — the most qualification-bound manufacturing environment in the batch. If a non-OEM machined replacement is ever acceptable here it is acceptable anywhere; if it is categorically not, that bounds H2A2's addressable slice.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · segment-fit (+3) · regulated-sector test value (+2) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot upgraded her: 'LCM Supplier Change Project Lead' at J&J through 2025 makes her the sharpest test of H2A2 in the batch. Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Ruilong Ma, Ph.D.

id: C11
name: Ruilong Ma, Ph.D.
linkedin_url: https://www.linkedin.com/in/ruilongma/
linkedin_account: Izgin
company: Amgen
role: Global Category Strategy Lead

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: supply_chain_procurement
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Category strategy in pharma procurement — owns supplier selection for a category, so he can say what actually happens when a category has a single blocked source, and what a new supplier has to clear to be used.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · buyer authority (+3) · replied 2019, long stale (+1) · no public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "Prior exchange is from 2019-10-15 — treat as effectively cold but not a stranger. [not drafted 2026-09-02] LR-B25: thread exists and they replied, but in 2019. Route to /startup-outreach-reply, which decides continuation vs fresh. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Blossom Tariro Kafumbata

id: C12
name: Blossom Tariro Kafumbata
linkedin_url: https://www.linkedin.com/in/blossom-tariro-kafumbata/
linkedin_account: Izgin
company: JKH Ltd
role: Manufacturing Systems & Planning Coordinator

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Manufacturing planning — the planner is the person who personally chases a late part and reschedules around it, which is the single most direct first-hand view of H2A1's frequency and cost.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · planning role feels the pain daily (+3) · smaller employer, easier reply (+2) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## ADESH KUMAR

id: C13
name: ADESH KUMAR
linkedin_url: https://www.linkedin.com/in/adesh-k-3069b775/
linkedin_account: Izgin
company: RMG
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Production manager — owns line output, so the cost of a stopped line lands on him. Can price the wait in H2A1 and says whether he would authorise a machined substitute in H2A2.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · replied 2026-02-12 (+2) · owns the downtime (+3) · no public signal (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "Prior exchange in the archive: replied 2026-02-12. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-02-12). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Moussa Chidiac

id: C14
name: Moussa Chidiac
linkedin_url: https://www.linkedin.com/in/moussachidiac/
linkedin_account: Izgin
company: Creagh Concrete
role: Operations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Operations at a precast concrete manufacturer — heavy plant, custom moulds and formwork, and equipment that is repaired rather than replaced. A different industry from the aerospace-heavy rest of the batch, which is what stops the sample being one sector's opinion.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · asset-heavy operator (+3) · sector diversity value (+2) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Grace Reed

id: C15
name: Grace Reed
linkedin_url: https://www.linkedin.com/in/grace-reed/
linkedin_account: Izgin
company: Deeplocal
role: Director of Production

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Directs production at a studio that builds one-off custom robotic and interactive installations — genuinely high-mix, quantity-of-one work, which is the variability side of H2 rather than the obsolescence side. Best contact in the batch for H2A3's 'nobody would quote it' question.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · quantity-of-one work is the exact variability case (+4) · no prior contact (0) · small org, reachable (+1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot upgraded her materially: prior roles were cost estimating and quoting for one-off builds (KPMG take-offs, then costing/quotes at acrylicize). Best contact in the batch for H2A3. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Awase Mustafa

id: C16
name: Awase Mustafa
linkedin_url: https://www.linkedin.com/in/awase-mustafa-66b3984b/
linkedin_account: Izgin
company: Bayouni Trading Co.
role: Supply Chain Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: supply_chain_procurement
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Supply chain at an industrial trading company — a distributor sits on the sourcing side of blocked parts and sees the problem across many customers rather than one plant. Breadth rather than depth; useful for H2A1 frequency, weak on H2A2 sign-off since the decision is not his.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · sees many blocked-part events (+3) · one remove from the asset owner (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "Distributor, not an asset owner. Competence gate: ask about frequency and sourcing behaviour, NOT about who signs off a non-OEM part in a plant he does not run. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Priyadharshni Baskaran

id: C17
name: Priyadharshni Baskaran
linkedin_url: https://www.linkedin.com/in/priyadharshnibaskaran/
linkedin_account: Izgin
company: McLaren Automotive Ltd
role: Manufacturing Graduate

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1]
validation_rationale: >
  Manufacturing graduate at McLaren — low-volume, high-mix supercar production, which is the archetype for the variability side of H2. Junior, so scoped to H2A1 only.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · exemplar HMLV employer (+3) · junior, limited visibility (-2) · graduates reply readily (+2)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "Competence gate: junior. Ask only what she has seen on the line (H2A1). Do NOT ask about sign-off authority or procurement policy — an out-of-competence answer enters the ledger as durable wrong evidence. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Kwan Mok

id: C18
name: Kwan Mok
linkedin_url: https://www.linkedin.com/in/kwanmok
linkedin_account: Izgin
company: Honda
role: Senior Supplier Quality Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: supply_chain_procurement
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Supplier quality at Honda is the function that decides whether a part from a new or substitute source is allowed into a vehicle. That is H2A2 stated as a job title, and he can describe the qualification path rather than guess at it.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · role IS the H2A2 question (+4) · large-employer drag (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 2026-09-02] They REPLIED 2019-10-10. Continuation, not a Msg 1 - route to /startup-outreach-reply. Strongest wave-2 fit on paper (supplier quality IS the H2A2 question), so worth doing properly."

## Ken Lee

id: C19
name: Ken Lee
linkedin_url: https://www.linkedin.com/in/ken-lee-windprofessional
linkedin_account: Izgin
company: EDF power solutions North America
role: Associate Director - Fleet Engineering

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A2, H2A3]
validation_rationale: >
  Fleet engineering at a power operator owns a large installed base of ageing equipment where OEMs go end-of-life faster than the assets do. Directs rather than executes, so he sees the cost of a blocked part on a budget he holds.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · Associate Director authority (+2) · ageing installed base is the core case (+3) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 HOLD 2026-09-02] Messaged 2026-07-15, 49 days, no reply. Gate closed under 3 months. Eligible 2026-10-15."

## Viliam Kacerik

id: C20
name: Viliam Kacerik
linkedin_url: https://www.linkedin.com/in/viliam-kacerik
linkedin_account: Izgin
company: Aston Martin F1 Team
role: Aerodynamics Design Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  F1 is the most extreme high-mix low-volume manufacturing there is: nearly every part is a one-off, and the deadline is a race weekend that does not move. If quote speed on a variable part matters anywhere, it matters here.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · extreme HMLV, purest test of H2A3 (+4) · design rather than sourcing side (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg1_sent
call_stage: offered_by_contact
found_date: 2026-09-02
invited_date: 2026-09-02
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[reply 2026-09-02] Replied on LinkedIn: 'Hi Izgin! Yes sure that sounds good :) I'm happy to have a chat\' — read from the inbox list preview; the thread is still UNREAD and was not opened. He OFFERED the call, so call_stage is offered_by_contact. Next step is /startup-outreach-reply for Msg 2. [msg1 drafted 2026-09-02] Live-verified. Aston Martin F1 since Oct 2025; was at Cambridge IfM May-Aug 2024, which does NOT overlap the founder's Oct 2024 start - copy says 'just before I got there' for that reason. Copy in outreach/copy/H2A1-linkedin.md. [msg1 SENT 2026-09-02 by founder, by hand]"

## Samir Oliveira

id: C21
name: Samir Oliveira
linkedin_url: https://www.linkedin.com/in/samir--oliveira
linkedin_account: Izgin
company: GE Vernova
role: Site Pre-Assembly Package Manager | Offshore Wind | Project Management

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Runs pre-assembly packages for offshore wind, where a missing part does not delay a shift, it delays a vessel. The cost of waiting is unusually legible in this role.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · owns package delivery (+3) · offshore cost of delay is quantified (+3) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 HOLD 2026-09-02] Messaged 2026-07-14, 50 days, no reply. Eligible 2026-10-14."

## Efe BEK

id: C22
name: Efe BEK
linkedin_url: https://www.linkedin.com/in/efebek
linkedin_account: Izgin
company: Enercon Windtech
role: Head of Process Engineering

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Heads process engineering at a wind turbine manufacturer, so he owns how parts actually get made and what happens when one is not available. Turkish, which the founder shares.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · Head of, owns the process (+3) · Turkish affinity applied after ICP fit (+1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 2026-09-02] They REPLIED 2026-07-13. Continuation - route to /startup-outreach-reply."

## Lauren Gwin

id: C23
name: Lauren Gwin
linkedin_url: https://www.linkedin.com/in/lauren-gwin
linkedin_account: Izgin
company: Lockheed Martin
role: Avionics Engineering Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Avionics is the textbook obsolescence problem: electronic components go end-of-life on a far shorter cycle than the aircraft, and someone has to decide what replaces them. Manages the function that lives with that.

response_likelihood: 8
likelihood_factors: >
  1st degree (+2) · manager authority (+2) · obsolescence is structural to avionics (+3) · defence disclosure limits (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[msg1 drafted 2026-09-02] Live-verified. Prior outbound 2021-03-16 no reply; >12mo plus leadership token, so LR-B30 permits fresh Msg 1. Copy in outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Regu Nammalwar

id: C24
name: Regu Nammalwar
linkedin_url: https://www.linkedin.com/in/regu-nammalwar
linkedin_account: Izgin
company: Lockheed Martin
role: Systems Engineering Lead

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Systems engineering lead in defence, where programme lifetimes outrun supplier lifetimes and part substitution is a routine engineering event rather than an exception.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · lead role (+2) · long-life programmes (+2) · defence disclosure limits (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Enoch Koech

id: C25
name: Enoch Koech
linkedin_url: https://www.linkedin.com/in/enoch-koech-8662479a
linkedin_account: Izgin
company: Nissan Motor Corporation
role: Sr. Regional Quality Lead Engineer 

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Regional quality lead at an automaker sees nonconforming and substituted parts as a daily category, and can say what actually happens when the specified part is not the one available.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · quality sees substitutions first-hand (+3) · large-employer drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Howard Chu

id: C26
name: Howard Chu
linkedin_url: https://www.linkedin.com/in/howard-chu-a5888448
linkedin_account: Izgin
company: Nissan Motor Corporation
role: Engineering Manager - VQE

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Manages vehicle quality engineering at Nissan, so he sits where a part problem becomes a decision rather than an observation.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · manager authority (+2) · quality decision seat (+2) · large-employer drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Olgac Aker

id: C27
name: Olgac Aker
linkedin_url: https://www.linkedin.com/in/olgacaker
linkedin_account: Izgin
company: Tesla
role: Quality Lab Engineering

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Quality lab engineering at Tesla, where the manufacturing ramp makes part availability a constant live constraint. Turkish, which the founder shares.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · quality role (+2) · Turkish affinity applied after ICP fit (+1) · prior thread exists, check before drafting (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 HOLD 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Eligible 2026-11-11."

## Bonnie Yang

id: C28
name: Bonnie Yang
linkedin_url: https://www.linkedin.com/in/bonnie-yang-876007109
linkedin_account: Izgin
company: Boeing
role: Industrial Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Industrial engineering at Boeing works the line itself, so she sees where a missing part actually stops work rather than where the schedule says it should.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · line-side visibility (+3) · large-employer drag (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[msg1 drafted 2026-09-02] Live-verified. 7yrs at Boeing, Georgia Tech. Copy in outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Mostafa Elzamar

id: C29
name: Mostafa Elzamar
linkedin_url: https://www.linkedin.com/in/mostafa-elzamar
linkedin_account: Izgin
company: Schaeffler
role: PMT Process Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Process engineering at a bearings and precision components manufacturer, which is both a maker of the parts others wait for and a plant that waits for its own.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · sits on both sides of the question (+3) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 2026-09-02] They REPLIED 2026-08-12. Continuation - route to /startup-outreach-reply."

## Engin Sengezer

id: C30
name: Engin Sengezer
linkedin_url: https://www.linkedin.com/in/enginsengezer
linkedin_account: Izgin
company: Intel Corporation
role: Process TD Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Process technology development in a semiconductor fab, where tool spares are single-sourced and lead times are notorious. Turkish, which the founder shares.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · fab spares are an extreme case (+3) · Turkish affinity applied after ICP fit (+1) · confidentiality culture (-2)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 HOLD 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Eligible 2026-11-11."

## Bismenjeet Singh

id: C31
name: Bismenjeet Singh
linkedin_url: https://www.linkedin.com/in/bismenjeetsingh
linkedin_account: Izgin
company: Northrop Grumman
role: Electromechanical Engineer, T2

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1]
validation_rationale: >
  Electromechanical engineering in defence manufacturing, where builds run long and parts get discontinued mid-programme.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · in-domain role (+2) · junior grade (-1) · defence disclosure limits (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Matt Havard

id: C32
name: Matt Havard
linkedin_url: https://www.linkedin.com/in/matthew-havard
linkedin_account: Izgin
company: Rivian
role: Senior Technical Program Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Technical programme management at an EV manufacturer in ramp, where a blocked part is a programme date rather than a line stoppage. A different shape of the same cost.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · programme authority (+2) · ramp makes shortages constant (+2) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[msg1 drafted 2026-09-02] Live-verified. Ex-Tesla 4680 NPI across engineering and supply chain. Copy in outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Michael Wallis

id: C33
name: Michael Wallis
linkedin_url: https://www.linkedin.com/in/michael-wallis1
linkedin_account: Izgin
company: McLaren Automotive Ltd
role: Aerothermal Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Aerothermal engineering at McLaren, a genuinely low-volume high-mix manufacturer where parts are made in tens rather than thousands.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · HMLV exemplar (+3) · design rather than sourcing side (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 DROP 2026-09-02] Messaged 2024-11-05, no reply, no buyer-authority token. Stale-and-junior drops."

## Chris Tagnon

id: C34
name: Chris Tagnon
linkedin_url: https://www.linkedin.com/in/chris-tagnon
linkedin_account: Izgin
company: Aston Martin Performance Technologies
role: Engineering Associate to the Managing Director

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Sits alongside the managing director at an applied performance engineering business, which is close enough to the commercial decision to say what a delay actually costs.

response_likelihood: 7
likelihood_factors: >
  1st degree (+2) · proximity to leadership (+3) · indirect role (-1) · no prior contact (0)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Tom Cho

id: C35
name: Tom Cho
linkedin_url: https://www.linkedin.com/in/tom-cho-40a9432
linkedin_account: Izgin
company: Ford Motor Company
role: Exterior Lighting Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Component engineering at Ford means owning a part through supplier tooling and change, which is where a source substitution is felt first.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · component ownership (+2) · narrow component scope (-1) · large-employer drag (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 DROP 2026-09-02] Messaged 2019-10-02, no reply, no buyer-authority token. Drops."

## Jia Wei, Ph.D.

id: C36
name: Jia Wei, Ph.D.
linkedin_url: https://www.linkedin.com/in/jia-wei-profile
linkedin_account: Izgin
company: ABB
role: Senior R&D Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1]
validation_rationale: >
  R&D at an industrial automation manufacturer, so he sees both what a factory buys and what it cannot get.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · in-domain manufacturer (+2) · R&D is one remove from the line (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 HOLD 2026-09-02] Messaged 2026-08-06, 27 days, no reply. Eligible 2026-11-06."

## Oliver Junnila

id: C37
name: Oliver Junnila
linkedin_url: https://www.linkedin.com/in/junnila-oliver
linkedin_account: Izgin
company: Toyota Automated Logistics
role: Project Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: maintenance_reliability
size_band: 

assumptions_tested: [H2A1, H2A3]
validation_rationale: >
  Project engineering on automated material handling equipment, which is asset-heavy kit that customers must keep running long after installation.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · installed-base exposure (+2) · project rather than service side (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: unchecked
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

## Eric Yoshikawa, MBA, MAM

id: C38
name: Eric Yoshikawa, MBA, MAM
linkedin_url: https://www.linkedin.com/in/eric-yoshikawa-mba-mam-8ab97b25
linkedin_account: Izgin
company: Intelliswift/Honeywell
role: Senior Advanced Test Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H2A1, H2A2]
validation_rationale: >
  Advanced test engineering across industrial and aerospace product lines, a role that meets parts which fail qualification or are no longer available.

response_likelihood: 6
likelihood_factors: >
  1st degree (+2) · test and qualification exposure (+2) · contractor position, may shift (-1)
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: held
message_stage:
call_stage: none
found_date: 2026-09-02
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[LR-B30 2026-09-02] They REPLIED 2021-02-17. Continuation - route to /startup-outreach-reply."

## Suhey Perez

id: C39
name: Suhey Perez
linkedin_url: https://www.linkedin.com/in/suhey-perez-68aa7b11b/
linkedin_account: Izgin
company: Budget Blinds
role: Measure and install pro

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Only 2nd-degree contact in the H3 batch and the only one whose job is taking the measurement itself. Primary value is H3A2, not H3A1: he cannot give a company remake rate, but he can say whether the number he takes at the window is what the factory cuts to. That is the causal split the hunch calls its sharpest unknown.

response_likelihood: 6
likelihood_factors: >
  2nd degree with a shared connection (+2) · MEASURES and installs, so sees where the error enters (+4) · franchise employee, cannot give a company-wide rate (-1)
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Paul Stuart

id: C40
name: Paul Stuart
linkedin_url: https://www.linkedin.com/in/paulstuart341/
linkedin_account: Izgin
company: Specialist Blinds
role: Designer, Surveyor and Installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  His title carries 'Surveyor', which in UK made-to-measure is the formal name for the person who takes the measurement the whole order depends on. He designs, measures and fits the same job, so he can say whether a misfit traces to his own number, the factory's tolerance, or an out-of-square opening — the causal split H3 names as unknown.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · SURVEYOR — literally the measuring role the hunch is about (+4) · small firm, reachable (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: London, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Zac Dellicompagni

id: C41
name: Zac Dellicompagni
linkedin_url: https://www.linkedin.com/in/zac-dellicompagni-02692aa9/
linkedin_account: Izgin
company: The Blinds & Shutter Company / Moonie Co
role: Installation/Project Manager (6+ yrs at The Blinds & Shutter Company)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Six years as installation manager means he has seen enough jobs to state a misfit rate rather than recall one incident, which is precisely the number H3A1 says no published source gives.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · six years running installations, long enough to know the rate not just an anecdote (+3) · now also a founder, likelier to answer a founder (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Stafford, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Andrii Bondar

id: C42
name: Andrii Bondar
linkedin_url: https://www.linkedin.com/in/bondarandrii/
linkedin_account: Izgin
company: NY City Blinds & Window Treatments (past)
role: Regional Installation Manager, 10+ yrs luxury window treatments

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  A regional installation manager aggregates across crews and jobs, so he is one of the few contacts who can give a frequency rather than a story. Luxury/motorised work also has the highest unit value, which is where a remake hurts most.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · regional manager sees many crews, so reports a rate not an anecdote (+3) · luxury segment where a remake costs most (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Edgewater, New Jersey, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Richard Jones

id: C43
name: Richard Jones
linkedin_url: https://www.linkedin.com/in/richard-jones-a20400b3/
linkedin_account: Izgin
company: Specialist Blinds
role: Installations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Runs installations at the same firm as Paul Stuart, which makes the pair a useful cross-check: if the manager and the surveyor describe misfit frequency differently, that gap is itself the finding.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · manages installs, sees the return rate (+3) · small firm (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: London, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Andy Andre

id: C44
name: Andy Andre
linkedin_url: https://www.linkedin.com/in/andy-andre-76039343/
linkedin_account: Izgin
company: Blinds To Go
role: Installation Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  Blinds To Go manufactures and retails its own product, so a remake stays inside one company. He can say what happens when the maker and the seller are the same entity — the case where the 'who absorbs it' question has an unambiguous answer.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · installation manager at a large vertically integrated retailer (+3) · big employer reply drag (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Stafford, Virginia, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Levi Flaherty

id: C45
name: Levi Flaherty
linkedin_url: https://www.linkedin.com/in/levi-flaherty-b33a7010b/
linkedin_account: Izgin
company: Budget Blinds
role: Installed Sales Manager / Lead Installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Sits on the seam between the sale and the fit, so he sees what a misfit costs in customer trust and rebooking, not only in product.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · sales AND install, so sees the customer-facing cost of a remake (+3) · franchise (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greater Hartford, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Dave Yews

id: C46
name: Dave Yews
linkedin_url: https://www.linkedin.com/in/dave-yews-62b62091/
linkedin_account: Izgin
company: Hillarys
role: Specialist installer — shutters and conservatory roof blinds

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Conservatory roof blinds and shutters carry the tightest tolerance in the category and out-of-square openings are normal there. First-hand on H3A2's question of whether misfits trace to capture or to hard geometry.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · shutters and conservatory roofs, the least forgiving fits (+3) · Hillarys, the UK volume leader (+2) · installer, not a rate-holder (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Alun Harry

id: C47
name: Alun Harry
linkedin_url: https://www.linkedin.com/in/alun-harry-5b45a5230/
linkedin_account: Izgin
company: Hillarys
role: Blinds installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Hillarys fitters measure and install under a company guarantee, so he can say who bears the cost inside that model — retailer, factory, or the fitter via chargeback. That is H3A1's 'who absorbed it' half, answered from the position that gets charged.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · Hillarys measure-and-fit model (+3) · self-employed fitter under a company guarantee (+1) · no rate visibility (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Anthony Brooks

id: C48
name: Anthony Brooks
linkedin_url: https://www.linkedin.com/in/anthony-brooks-b9b82090/
linkedin_account: Izgin
company: Hillarys Blinds Limited
role: Blinds installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Cross-market check on the Hillarys measure-and-fit chargeback practice, UK against Ireland.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · same model as Alun Harry, different market (+2) · no rate (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Glenn Mcavoy

id: C49
name: Glenn Mcavoy
linkedin_url: https://www.linkedin.com/in/glenn-mcavoy-87637745/
linkedin_account: Izgin
company: Independent
role: Self-employed contract blind installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  A self-employed contract fitter absorbs the cost of a re-visit personally with no employer to socialise it. If anyone in the chain feels a misfit sharply, it is this position.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · self-employed, so a remake hits his own income directly (+4) · independents reply well (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Oldham, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Ben Simpson

id: C50
name: Ben Simpson
linkedin_url: https://www.linkedin.com/in/ben-simpson-975b90184/
linkedin_account: Izgin
company: Independent
role: Self-employed curtain and blinds installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Same structural position as Glenn Mcavoy — an independent whose unpaid re-visit is the cost. Two independents make the answer less anecdotal.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · self-employed, direct personal cost (+4) · independent (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Rochdale, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## MJ Khah

id: C51
name: MJ Khah
linkedin_url: https://www.linkedin.com/in/mj-khah-03b6953b4/
linkedin_account: Izgin
company: Independent
role: Curtain and blind installer — commercial fit-out and residential

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Commercial fit-out orders arrive in bulk to one building, so a systematic measurement error multiplies rather than affecting one window. Tests whether misfit cost scales differently in commercial work.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · covers commercial fit-out as well as residential (+3) · independent, reachable (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greater Manchester, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Chris Chase

id: C52
name: Chris Chase
linkedin_url: https://www.linkedin.com/in/chris-chase-9814b320/
linkedin_account: Izgin
company: Hunter Douglas dealer network
role: Hunter Douglas master blind and shutter installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Certified to Hunter Douglas standards and does repair work, so he sees both fresh misfits and the ones that get remediated rather than remade — a distinction that changes the true cost.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · certified against the largest global manufacturer's standard (+3) · does repairs too, sees failure modes (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Calgary, Canada. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Leanna Thompson

id: C53
name: Leanna Thompson
linkedin_url: https://www.linkedin.com/in/leanna-thompson-a1733533/
linkedin_account: Izgin
company: Leanna Thompson Installs
role: Blind and drapery installer/consultant (past: Custom Decorators Inc.)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Works across two separate Budget Blinds franchises, so he can say whether remake handling is franchisor policy or set territory by territory — a question no single-territory contact can answer.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · installs across TWO franchise territories (+3) · no rate (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Dustin Hayes

id: C54
name: Dustin Hayes
linkedin_url: https://www.linkedin.com/in/dustin-hayes-14724b69/
linkedin_account: Izgin
company: Budget Blinds (Pickerington / Upper Arlington)
role: Installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  His own profile describes loading the truck against the custom order at the start of each day — the exact checkpoint where a wrong-size unit is either caught in the warehouse or driven to a customer's house. Directly on H3A2.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · loads the truck against the custom order each morning (+3) · no rate (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Christopher Vermont

id: C55
name: Christopher Vermont
linkedin_url: https://www.linkedin.com/in/christopher-vermont-8a6204220/
linkedin_account: Izgin
company: Budget Blinds
role: Installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Franchise installer; volume check on whether the Budget Blinds remake experience is consistent across US territories.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · franchise installer (+2) · no rate (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location kept from the search result. REINSTATED 2026-09-03 after an incorrect off_scope: they were marked off for not matching icp_valid_titles, but that field is advisory and is not enforced by audit_target_list.py — they pass icp_valid_tiers (dealer_installer) and hit no icp_out_of_scope pattern. Tagged to H3A2 as well as H3A1: an installer answers WHERE THE ERROR ENTERS from first hand, which is H3A2, and should not be asked for a company-wide remake rate, which is H3A1 and belongs to the owners and production managers. Headline/company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile (LR-B6)."

## Nolan Smith

id: C56
name: Nolan Smith
linkedin_url: https://www.linkedin.com/in/smithnop/
linkedin_account: Izgin
company: Budget Blinds
role: Installer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Franchise installer; volume test of whether the Budget Blinds remake experience is consistent across US territories.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · franchise installer (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: field_practitioner
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greater Fort Wayne, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Paul Holden

id: C57
name: Paul Holden
linkedin_url: https://www.linkedin.com/in/paul-holden-41aa8a44/
linkedin_account: Izgin
company: EASi Blind Ltd (online D2C bespoke blinds)
role: Owner and Managing Director

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Sells bespoke made-to-measure blinds online direct to consumers, which means the CUSTOMER takes the measurement and his business absorbs whatever comes of that. This is exactly the model where SelectBlinds' free-remake guarantee (H3 evidence) implies a high rate. He is the sharpest test of who pays in the online channel.

response_likelihood: 6
likelihood_factors: >
  3rd degree, cold (0) · owner, holds the budget (+3) · ONLINE D2C, where the customer measures (+3)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Bolton, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Chris Dickens

id: C58
name: Chris Dickens
linkedin_url: https://www.linkedin.com/in/chris-dickens-founder-and-ceo-12418291/
linkedin_account: Izgin
company: Independent specialist
role: Founder and CEO — bespoke automated blinds and curtains

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Motorised and heavy-duty bespoke units are the highest-value made-to-measure product in this batch, so a remake destroys the most margin per event. Active public poster, which raises reply odds.

response_likelihood: 6
likelihood_factors: >
  3rd degree, cold (0) · founder/CEO, owns the P&L (+3) · 15+ yrs bespoke motorised work (+2) · 16K followers, active poster (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Boughton, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Dan Powell

id: C59
name: Dan Powell
linkedin_url: https://www.linkedin.com/in/dan-powell-76555a211/
linkedin_account: Izgin
company: DJP Blinds
role: Owner — supply and installation of made-to-measure shading

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Owner of a supply-and-fit business covering residential, commercial and marine. Because he both orders and fits, the remake cost lands entirely inside his own P&L — no one to charge it back to.

response_likelihood: 6
likelihood_factors: >
  3rd degree, cold (0) · owner (+3) · supplies AND installs, so absorbs the whole error (+3)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Powys, Wales, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Tim Pacholski

id: C60
name: Tim Pacholski
linkedin_url: https://www.linkedin.com/in/tim-pacholski-673887aa/
linkedin_account: Izgin
company: Bay View Shade & Blind, Inc.
role: Owner and Operations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Combines ownership with day-to-day operations, so he can give both the remake rate and its P&L consequence in one conversation — rare in this batch.

response_likelihood: 6
likelihood_factors: >
  3rd degree, cold (0) · owner AND ops manager, budget plus daily visibility (+4) · currently hiring, so growing (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: New Berlin, Wisconsin, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Greg Thompson

id: C61
name: Greg Thompson
linkedin_url: https://www.linkedin.com/in/gregorythompson/
linkedin_account: Izgin
company: 3 Blind Mice Window Coverings
role: Director of Operations

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Operations director at an established regional dealer — the level where a remake rate is tracked as a number rather than felt as an irritation.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · operations director, owns the process (+3) · established regional dealer (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: San Diego County, California, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Toby Dishmon

id: C62
name: Toby Dishmon
linkedin_url: https://www.linkedin.com/in/toby-dishmon-4166155/
linkedin_account: Izgin
company: CCWC Blinds and Shades
role: General/Operations Manager — commercial and multi-family

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Multi-family projects order hundreds of units to a schedule of openings, so a measurement error propagates across a whole building. Tests whether the bulk case has a different failure mode from one-off residential.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · runs ops and scheduling (+3) · commercial/multi-family, bulk orders (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greensboro–Winston-Salem, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Katie Judds

id: C63
name: Katie Judds
linkedin_url: https://www.linkedin.com/in/katie-judds/
linkedin_account: Izgin
company: Skyline Window Coverings
role: Operations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Operations manager at a metro dealer — sits where orders, measurements and installs are coordinated, which is the handoff H3 claims is unverified.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · operations manager (+3) · mid-size dealer (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Chicago, Illinois, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Melissa Whitley

id: C64
name: Melissa Whitley
linkedin_url: https://www.linkedin.com/in/melissawhitleymwmanagement/
linkedin_account: Izgin
company: Intelligent Window Coverings
role: Sales and Operations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Holds both sales and operations, so she sees the remake as a customer problem and a cost problem simultaneously.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · sales and ops in one role (+3) · small firm, reachable (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Brackendale, British Columbia, Canada. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Kevin Hogue

id: C65
name: Kevin Hogue
linkedin_url: https://www.linkedin.com/in/kevin-hogue-b7a841b9/
linkedin_account: Izgin
company: AZ Endless Sun / Hogue's Enterprise
role: Operational Manager, drapery installer, shutter specialist

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Runs the business and still fits personally, so his answer on cause is first-hand rather than reported up a chain.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner-operator who still installs (+3) · specialist in shutters, tight tolerance (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Mesa, Arizona, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Justin Munchinsky

id: C66
name: Justin Munchinsky
linkedin_url: https://www.linkedin.com/in/justin-munchinsky-5706213b/
linkedin_account: Izgin
company: Window Masters / Ascension Blinds
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Owns both a window business and a blinds business, so he can compare misfit economics between a window and the covering that goes on it.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owns multiple related businesses (+3) · smaller market (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Red Deer, Alberta, Canada. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Peter Nias

id: C67
name: Peter Nias
linkedin_url: https://www.linkedin.com/in/peter-nias-63223119/
linkedin_account: Izgin
company: Intelli-blinds
role: Electric blinds, solar shading and smart home

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  His stated differentiator is surveying at first-fix wiring stage — i.e. he already invests in measuring earlier than competitors. That is a workaround for exactly the problem H3 describes, and worth understanding whether it pays.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner-level (+3) · pre-sale technical survey at first-fix wiring stage (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Stockport, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Donald Marsh

id: C68
name: Donald Marsh
linkedin_url: https://www.linkedin.com/in/donald-marsh-082b5648/
linkedin_account: Izgin
company: D&HP Blinds
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Independent owner; the remake lands on his own margin with nowhere to pass it.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner (+3) · small independent (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Chelmsford, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## ray price

id: C69
name: ray price
linkedin_url: https://www.linkedin.com/in/ray-price-9827905b/
linkedin_account: Izgin
company: Independent
role: Owner — sales and fitting of blinds and awnings

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Sells and fits personally, so both the measurement and its consequence are his.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner who also fits (+3) · independent (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Milton Keynes, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Philip Robbins

id: C70
name: Philip Robbins
linkedin_url: https://www.linkedin.com/in/philip-robbins-b3888a277/
linkedin_account: Izgin
company: Montemblinds
role: Owner — supply and fit, and fit-only

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Offers fit-only service on goods measured by someone else, which is the natural experiment for H3: he can compare misfit rates between jobs he measured and jobs he did not.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner (+3) · offers FIT-ONLY as well as supply-and-fit (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Gina du Toit

id: C71
name: Gina du Toit
linkedin_url: https://www.linkedin.com/in/gina-du-toit-429b287a/
linkedin_account: Izgin
company: G-Blinds
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A1]
validation_rationale: >
  Non-US/UK market. If misfit economics look the same in South Africa, the problem is structural to made-to-measure rather than a feature of one market's trade practice.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · owner (+3) · outside US/UK, tests geography (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Durban, South Africa. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Adam Baratynski

id: C72
name: Adam Baratynski
linkedin_url: https://www.linkedin.com/in/adambaratynski/
linkedin_account: Izgin
company: Window treatments retailer
role: Sales — plantation shutters, blinds and window treatments

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Sells plantation shutters and blinds into residential and commercial; sales-side view of what a remake does to a booked order.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · sales-side, quotes and measures (+2) · distant timezone (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: New Zealand. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Jesse Evans

id: C73
name: Jesse Evans
linkedin_url: https://www.linkedin.com/in/jesse-evans-b2595848/
linkedin_account: Izgin
company: Next Day Blinds (Poulsen Finish and Decor)
role: Window covering specialist

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Next Day Blinds manufactures and retails, and competes explicitly on lead time — which is the thing a remake destroys. Tests whether speed promises change remake tolerance.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · works for a vertically integrated maker-retailer (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Logan, Utah, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Kenneth Brown

id: C74
name: Kenneth Brown
linkedin_url: https://www.linkedin.com/in/kenneth-brown-4129b5b5/
linkedin_account: Izgin
company: Blinds To Go
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  Blinds To Go manufactures to order at scale and his own headline is about production efficiency, so a remake rate is a number he manages against. Highest-value single contact for the rate H3A1 says no source publishes.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager at a large vertically integrated maker (+4) · his headline names production efficiency (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: United States. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## yana nickels

id: C75
name: yana nickels
linkedin_url: https://www.linkedin.com/in/yana-nickels-861985106/
linkedin_account: Izgin
company: Blinds To Go
role: Production Department Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  Second production manager at the same manufacturer — if two managers give different remake rates for one company, that inconsistency is itself informative about whether the number is really tracked.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · department-level production manager (+4) · same firm as Kenneth Brown, cross-check (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Eatontown, New Jersey, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Andres Leree

id: C76
name: Andres Leree
linkedin_url: https://www.linkedin.com/in/andres-leree-0a283297/
linkedin_account: Izgin
company: 3 Day Blinds
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  His own profile describes managing production problems and corrective/preventive actions — the vocabulary of someone who already measures defect and rework rates.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager at a major US maker-retailer (+4) · his profile names corrective/preventive action work (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Tijuana, Baja California, Mexico. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Neil Vickers

id: C77
name: Neil Vickers
linkedin_url: https://www.linkedin.com/in/neil-vickers-08820b64/
linkedin_account: Izgin
company: Waverley Blinds
role: Factory/Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Runs a UK trade factory that manufactures for dealers, so he sees remakes arriving from many different measurers — the best position to say whether cause is dealer error or factory tolerance.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · runs the factory (+4) · UK trade manufacturer supplying dealers (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Luton, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Gavin Barrow

id: C78
name: Gavin Barrow
linkedin_url: https://www.linkedin.com/in/gavin-barrow/
linkedin_account: Izgin
company: CBS Blinds
role: Production, Manufacturing and Operations Manager — lean

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  His headline is process optimisation and lean manufacturing, which means rework is a metric he already fights. Most likely contact in the entire batch to answer with a number rather than an impression.

response_likelihood: 6
likelihood_factors: >
  3rd degree, cold (0) · explicitly lean/process-optimisation focused (+4) · custom LinkedIn vanity URL, active user (+2)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Upwey, Victoria, Australia. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Jeremy Clarke

id: C79
name: Jeremy Clarke
linkedin_url: https://www.linkedin.com/in/jeremy-clarke-3149b392/
linkedin_account: Izgin
company: Prestigious Blinds Ltd.
role: Technical Services Manager to the production department

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Provides technical services to the production department, which in practice means diagnosing why things went wrong. Directly on H3's causal-split question.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · technical services INTO production, i.e. the fault-diagnosis role (+4)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Bradford, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Wayne Hayes

id: C80
name: Wayne Hayes
linkedin_url: https://www.linkedin.com/in/wayne-hayes-60196769/
linkedin_account: Izgin
company: TM Blinds Ltd
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Production manager at an Irish trade manufacturer; smaller operation where the manager knows the remake count directly rather than via a report.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager (+4) · smaller firm, easier to reach (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Ireland. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Troy Liddell

id: C81
name: Troy Liddell
linkedin_url: https://www.linkedin.com/in/troy-liddell-15a71b70/
linkedin_account: Izgin
company: Russell's Curtains and Blinds
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Manufactures and retails, so remakes stay internal — another instance of the case where 'who pays' is unambiguous.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager at a maker-retailer (+4)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Nelson, New Zealand. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Sajit Sharma

id: C82
name: Sajit Sharma
linkedin_url: https://www.linkedin.com/in/sajit-sharma-284b43272/
linkedin_account: Izgin
company: Apollo Blinds / Apollo Windows
role: Production and Factory Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Apollo supplies a franchise dealer network, so he sees remakes generated by franchisees' measurements — the cross-party case where blame and cost are contested.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · factory manager at a franchise-supplying maker (+4)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greystanes, New South Wales, Australia. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Losana Mata

id: C83
name: Losana Mata
linkedin_url: https://www.linkedin.com/in/losana-mata-961768122/
linkedin_account: Izgin
company: Blinds manufacturer
role: Production Manager, NSW

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  State-level production manager; company needs confirming on the profile visit before any message is written.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · state-level production manager (+3) · company not yet identified from search (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Greater Sydney, Australia. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Kendal Franklin

id: C84
name: Kendal Franklin
linkedin_url: https://www.linkedin.com/in/kendal-franklin-17aa53170/
linkedin_account: Izgin
company: Blinds By Noon and Shutters Real Soon
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  The company name is a speed promise, and a remake is the direct enemy of a speed promise. Tests whether fast-turnaround makers tolerate a higher error rate.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager (+4) · firm competes on speed, per its own name (+1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Atlanta, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Jason Webb

id: C85
name: Jason Webb
linkedin_url: https://www.linkedin.com/in/jason-webb-43168761/
linkedin_account: Izgin
company: Bay Way Blinds and Draperies
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Production manager at a regional maker covering both blinds and soft goods.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager (+4)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Tooele, Utah, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Arun V S

id: C86
name: Arun V S
linkedin_url: https://www.linkedin.com/in/arun-v-s-86a70251/
linkedin_account: Izgin
company: Callistus Window Blinds Middle East
role: Production Manager / Production In-charge / QC

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Holds production and quality control in one role, so the remake number is literally his metric. QC ownership makes him the most likely to quote a percentage.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · production manager who ALSO owns QC (+5)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Sharjah, UAE. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Saboor Ali

id: C87
name: Saboor Ali
linkedin_url: https://www.linkedin.com/in/saboor-ali-629046105/
linkedin_account: Izgin
company: Callistus Window Blinds Middle East
role: Production and Operations Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Second manager at the same UAE manufacturer, for internal consistency on the reported rate.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · production and ops manager (+4) · same firm as Arun V S, cross-check (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Sharjah, UAE. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## yadvinder singh

id: C88
name: yadvinder singh
linkedin_url: https://www.linkedin.com/in/yadvindersingh-deakin-university/
linkedin_account: Izgin
company: Majestic Curtains and Blinds, Plantation Shutters and Outdoor Blinds
role: Production Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1]
validation_rationale: >
  Manages production across curtains, shutters and outdoor blinds, so he can say whether misfit rate differs by product type — outdoor and shutters being the least forgiving.

response_likelihood: 4
likelihood_factors: >
  3rd degree, cold (0) · production manager across several product lines (+3)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: South Geelong, Victoria, Australia. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Glenn Burns

id: C89
name: Glenn Burns
linkedin_url: https://www.linkedin.com/in/glenn-burns-3a807bb6/
linkedin_account: Izgin
company: Blinds To Go
role: Production Call Center Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  Runs the call centre that feeds production, which is the exact point where a customer's measurement becomes a manufacturing instruction. That is the handoff H3 says is unverified, and he owns it.

response_likelihood: 5
likelihood_factors: >
  3rd degree, cold (0) · sits between customers and production (+4) · third Blinds To Go contact, within the 5-per-company cap (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: New York City Metro, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6)."

## Stoneside Blinds and Shades

id: C90
name: Stoneside Blinds and Shades
linkedin_url:
linkedin_account: Izgin
company: Stoneside Blinds and Shades
role: Sales / measure consultant (name not captured)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1, H3A2, H3A3]
validation_rationale: >
  Runs their own factories, sells through designers, architects and contractors, and offers a free measure visit with customer liability if the customer self-measures. Already produced the sharpest single data point in the batch: a 23-window reorder caused by customer-supplied measurements. Best candidate for a premises visit.

response_likelihood: 9
likelihood_factors: >
  already spoken by phone (+5) · in-segment (+3) · cold-called rather than introduced (0)
outreach_pattern:
degree: inmail_only
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
channel: phone
relationship_type: operator_buyer
outreach_status: replied
message_stage:
call_stage: completed
found_date: 2026-09-03
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-03

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: phone
notes: "[called 2026-09-03] Free measure visit; customer liable if they supply their own dimensions. 23-window reorder case. Own factories, 4-5 week lead time. Source for E7, E9, E11. E11 is a Mom Test false positive and must not be counted as demand."

## National blinds retailer

id: C91
name: National blinds retailer
linkedin_url:
linkedin_account: Izgin
company: (name not pinned down)
role: Phone / scheduling contact

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Charges $225 per measure visit, says it is not accurate enough, and declines jobs when the drive is too far. That is a certain per-job cash cost plus a hard bound on serviceable radius, which is a better-defined pain than the remake rate.

response_likelihood: 9
likelihood_factors: >
  already spoken by phone (+5) · in-segment (+3) · cold-called rather than introduced (0)
outreach_pattern:
degree: inmail_only
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
channel: phone
relationship_type: operator_buyer
outreach_status: replied
message_stage:
call_stage: completed
found_date: 2026-09-03
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-03

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: phone
notes: "[called 2026-09-03] $225 per measure visit, 'not accurate enough', declines distant jobs. Source for E8, E9. IDENTITY NOT CONFIRMED - founder's notes say 'the national blinds guys'; pin the legal entity before any follow-up."

## Art Shade Shop

id: C92
name: Art Shade Shop
linkedin_url:
linkedin_account: Izgin
company: Art Shade Shop
role: (owner / staff, name not captured)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: 

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  A workroom that measures, visits and does all measurement in person with no software in the loop. Confirms the manual-capture mechanism in a second independent shop.

response_likelihood: 9
likelihood_factors: >
  already spoken by phone (+5) · in-segment (+3) · cold-called rather than introduced (0)
outreach_pattern:
degree: inmail_only
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
channel: phone
relationship_type: operator_buyer
outreach_status: replied
message_stage:
call_stage: completed
found_date: 2026-09-03
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-03

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: phone
notes: "[called 2026-09-03] Must measure and visit in person; no software; sends people for visits. Source for E9."

## Susan Lind Chastain Inc

id: C93
name: Susan Lind Chastain Inc
linkedin_url:
linkedin_account: Izgin
company: Susan Lind Chastain Inc
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1, H3A2, H3A3]
validation_rationale: >
  Owner-level contact at a workroom, same manual-measure pattern. Asked for an email and a premises visit is being arranged, which makes this the first contact willing to let the founder see the actual process rather than describe it.

response_likelihood: 9
likelihood_factors: >
  already spoken by phone (+5) · in-segment (+3) · cold-called rather than introduced (0)
outreach_pattern:
degree: inmail_only
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
channel: phone
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg1_sent
call_stage: completed
found_date: 2026-09-03
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-03

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: phone
notes: "[called 2026-09-03] Same manual measure pattern. Asked founder to email; founder sending blinds photos. PREMISES VISIT being arranged - highest-value next step in the batch. Source for E9. [email SENT 2026-09-03 by founder, by hand] To Christopher Adams (VP). Asks for a workroom visit at 1330 Natoma St and flags the designer-channel question outright. Copy and reasoning in outreach/copy/H3A1-email.md. Awaiting reply."

## Family-run window covering owners (aggregate)

id: C94
name: Family-run window covering owners (aggregate)
linkedin_url:
linkedin_account: Izgin
company: (several, not individually named)
role: Owners

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: 

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  The segment that would actually have to buy. Recorded as one aggregate card because the founder's notes did not separate them. Their lack of enthusiasm is the most important negative signal in the batch and needs a named follow-up.

response_likelihood: 9
likelihood_factors: >
  already spoken by phone (+5) · in-segment (+3) · cold-called rather than introduced (0)
outreach_pattern:
degree: inmail_only
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
channel: phone
relationship_type: operator_buyer
outreach_status: replied
message_stage:
call_stage: completed
found_date: 2026-09-03
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-03

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: phone
notes: "[called 2026-09-03] Not enthusiastic about a software answer. Source for E10. AGGREGATE CARD - split into named contacts before any follow-up; the reason for the no was not captured and is the thing worth going back for."

## Marcelo Mazzafera

id: C95
name: Marcelo Mazzafera
linkedin_url: https://www.linkedin.com/in/mazzafera/
linkedin_account: Izgin
company: SelectBlinds
role: Chief Operating Officer & VP of Finance

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=SelectBlinds
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A2, H3A3]
validation_rationale: >
  SelectBlinds publishes FIT Protection - a free remake at corrected dimensions when the CUSTOMER measured wrong. The recon calls that the single strongest behavioural signal in the lane, because no one absorbs remakes on a made-to-order product unless they have measured the rate and decided eating it is cheaper than losing the sale. As COO and VP Finance he is the person that decision was costed by: he can state the rate (H3A1), say where the error is adjudicated (H3A2), and say what the guarantee costs the company against what it recovers in conversion (H3A3).

response_likelihood: 7
likelihood_factors: >
  profile_fit (0) · start 3 · 2nd degree (+2) · COO owns the guarantee P&L, so the question is in his competence (+3) · senior and busy (-1)
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Benjamin Grimes

id: C96
name: Benjamin Grimes
linkedin_url: https://www.linkedin.com/in/benjamin-grimes13/
linkedin_account: Izgin
company: SelectBlinds
role: Pricing Strategy Analyst

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=SelectBlinds
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  A pricing analyst at the company that gives away customer-error remakes has to carry the cost of that giveaway in the price. He is likely the person who knows the claim rate as a number rather than an impression (H3A1), and what share of order value it consumes (H3A3). Deliberately paired with C95 - the analyst usually answers where the COO delegates.

response_likelihood: 6
likelihood_factors: >
  profile_fit (0) · start 3 · 2nd degree (+2) · shared mutual connection (+1) · pricing analyst sees the remake as a line he models (+1) · junior, may defer upward (-1)
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Elizabeth Papagni

id: C97
name: Elizabeth Papagni
linkedin_url: https://www.linkedin.com/in/elizabethpapagni/
linkedin_account: Izgin
company: The Home Depot
role: Associate Product Development Merchant (Blinds/Window Coverings)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Home%20Depot%20window%20coverings%20merchant
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Her title names blinds and window coverings specifically at the largest home-improvement retailer in the US - the merchant role owns the category's returns and claims line, which is where a customer-mismeasure remake lands (H3A1). Home Depot both sells cut-to-size in store and owns Blinds.com, so she sees the cost across both channels and can say which party absorbs it (H3A3).

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · title names the exact category under test (+3) · large-employer response drag (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Nathaniel Erebia

id: C98
name: Nathaniel Erebia
linkedin_url: https://www.linkedin.com/in/nathanielerebia/
linkedin_account: Izgin
company: The Home Depot
role: Associate Merchant, Pro - Cabinets & Countertops, Closets, Window Coverings

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Home%20Depot%20window%20coverings%20merchant
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Carries window coverings on the Pro side, where the buyer is a contractor rather than a consumer and the measurement is taken by a trade professional. That makes him the control case for H3A2's question about who mis-measures: if the Pro channel's remake rate is materially lower than the consumer one, the error is the consumer's, and if it is not, the mechanism is elsewhere.

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · window coverings is one of three categories he carries, so attention is split (+2) · large-employer response drag (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Amber Hall

id: C99
name: Amber Hall
linkedin_url: https://www.linkedin.com/in/amber-hall-3629314/
linkedin_account: Izgin
company: Global Custom Commerce / Blinds.com (a Home Depot company)
role: Vice President Merchandising

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Blinds.com
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Blinds.com is Home Depot's made-to-measure arm and publishes SureFit, which caps free customer-error remakes at four windows per household. The recon reads that cap as evidence the claim volume was worth capping. As VP Merchandising she owns the category P&L that cap protects and can state the rate behind it (H3A1) and who the cost is charged to (H3A3).

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · VP owns the category P&L the remake hits (+2) · senior and busy (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Kris Decker

id: C100
name: Kris Decker
linkedin_url: https://www.linkedin.com/in/kris-decker/
linkedin_account: Izgin
company: Global Custom Commerce / Blinds.com (a Home Depot company)
role: VP Category Experience

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Blinds.com
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A2, H3A3]
validation_rationale: >
  Category Experience owns what happens after a wrong-size blind arrives - the claim, the adjudication and the remake wait that the recon found dominates the negative reviews. He is the person who can say how Blinds.com works out whose number was wrong (H3A2) and who ends up paying once it does (H3A3).

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · category experience owns the claim journey (+2) · senior and busy (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Bruno Campos

id: C101
name: Bruno Campos
linkedin_url: https://www.linkedin.com/in/camposbruno/
linkedin_account: Izgin
company: Select Blinds US
role: Chief Marketing Officer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=SelectBlinds
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A3]
validation_rationale: >
  H3A3 only, on the competence gate. A CMO can say why the fit guarantee exists commercially - what it buys in conversion and what the company decided it was worth paying for that - which is exactly the who-eats-the-cost question. He cannot speak to a remake rate or to error attribution, so he is not asked about either.

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · owns the conversion side of the guarantee (+2) · marketing seniority, may deflect operational detail (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Casey Ogden

id: C102
name: Casey Ogden
linkedin_url: https://www.linkedin.com/in/casey-ogden/
linkedin_account: Izgin
company: Wayfair
role: General Manager - Home Improvement Categories & Global Supplier Partnerships

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Wayfair%20window%20treatments
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Wayfair sells custom window treatments cut to the customer's own measurement, and home improvement is the category that contains them. As GM of that category and of supplier partnerships he sits on both sides of the remake: what it costs Wayfair in returns (H3A1) and what Wayfair charges back to the supplier who cut the fabric (H3A3). The chargeback direction is the part no other contact on this list can answer.

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · GM of the category that contains custom window treatments (+2) · large-employer response drag (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Rose Mauloni

id: C103
name: Rose Mauloni
linkedin_url: https://www.linkedin.com/in/rosemauloni/
linkedin_account: Izgin
company: Birch Lane (Wayfair)
role: Merchandise Manager - Textiles and Upholstery, incl. Window

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Wayfair%20window%20treatments
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Merchandises window alongside rugs, lighting, decor, bedding and bath for a Wayfair house brand. Window is the only made-to-measure line in that list, which makes her a useful comparison: she can say whether window returns behave differently from the stock-size categories she runs beside it. A difference is evidence the misfit is real (H3A1); no difference would be a contradiction worth having.

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · window is named in her category list (+2) · window is one line among many, so depth is uncertain (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Elizabeth B.

id: C104
name: Elizabeth B.
linkedin_url: https://www.linkedin.com/in/elizabeth-b-413235151/
linkedin_account: Izgin
company: Global Custom Commerce / Blinds.com (a Home Depot company)
role: Project Coordinator, Customer Experience

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Blinds.com
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A2, H3A3]
validation_rationale: >
  Sits on the customer experience desk at Blinds.com, which is where a wrong-size blind is first reported and where the argument about whose measurement was wrong actually happens (H3A2). Coordinator level is deliberate: the recon found the remake WAIT and the fault dispute are the pain, and that is visible from the desk handling it rather than from the VP above it.

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · coordinator level replies more readily than VP (+2) · no visible seniority to commit an answer (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Steven Chiang

id: C105
name: Steven Chiang
linkedin_url: https://www.linkedin.com/in/steven-chiang-9545b160/
linkedin_account: Izgin
company: Norman Window Fashions
role: VP of Operations

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Norman%20Window%20Fashions
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Norman is named in the recon as among the world's largest makers of custom window fashions. A VP of Operations tracks remakes monthly because they hit cost of goods twice - material and labour paid twice, collected once, per Sun Glow's dealer guide. He is one of the few people who can give the rate rather than estimate it (H3A1) and say how his plant attributes a returned unit between its own tolerance and the incoming measurement (H3A2).

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · VP Ops owns the remake as a cost-of-goods line (+3) · senior and busy (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Fernando Antonio Martinez Almaraz

id: C106
name: Fernando Antonio Martinez Almaraz
linkedin_url: https://www.linkedin.com/in/fernando-antonio-martinez-almaraz-32773b71/
linkedin_account: Izgin
company: Springs Window Fashions
role: Quality Engineering Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions%20quality%20manager
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Springs Window Fashions (Levolor, Bali) covers all major residential and commercial channels, so its quality data spans the industry rather than one niche. A Quality Engineering Manager owns the categorisation that H3A2 turns on - whether a returned unit is logged as a manufacturing defect or as a wrong incoming dimension - and that categorisation is the source of any rate he could quote for H3A1.

response_likelihood: 6
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · quality engineering owns the defect-vs-mismeasure split directly (+3) · engineer-level contacts answer technical questions readily (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Julio Tinajero

id: C107
name: Julio Tinajero
linkedin_url: https://www.linkedin.com/in/julio-tinajero-9b5a5332/
linkedin_account: Izgin
company: Springs Window Fashions
role: Plant Operations Manager (1,300 employees)

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions%20quality%20manager
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Runs a 1,300-employee Springs plant - his own headline states the size, which independently confirms the enterprise band rather than leaving it inferred. Remakes re-enter his production schedule as rush work, so he feels them as disruption as well as cost, and can say what share of the line's output they consume (H3A1) and whether the wrong number arrived or was created inside his plant (H3A2).

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · runs a 1,300-person plant making this exact product (+3) · plant managers are hard to reach on LinkedIn (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Javier Bustamante Martinez

id: C108
name: Javier Bustamante Martinez
linkedin_url: https://www.linkedin.com/in/javier-bustamante-mart%C3%ADnez-319b54115/
linkedin_account: Izgin
company: Springs Window Fashions
role: Corporate Supplier Quality Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions%20quality%20manager
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A2]
validation_rationale: >
  H3A2 only. Supplier quality sits upstream of the cut, so he can rule a component tolerance in or out as a cause of misfit - which is the alternative explanation H3A2 has to eliminate before a measurement product makes sense. He is not asked for a remake rate; that is not his line.

response_likelihood: 4
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · supplier quality is upstream of the measurement question (+1) · corporate role may be too far from the window (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Heather Barrows

id: C109
name: Heather Barrows
linkedin_url: https://www.linkedin.com/in/heather-barrows-270b5289/
linkedin_account: Izgin
company: Springs Window Fashions
role: Customer Service Supervisor

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A2, H3A3]
validation_rationale: >
  Every remake claim at Springs passes her desk before it reaches the plant. That makes her the best-placed person on this list for the adjudication question - how they establish whose number was wrong (H3A2) - and for who is told they are paying once the answer is reached (H3A3). The recon found the fault dispute is where the customer-facing pain concentrates, and that dispute is her job.

response_likelihood: 6
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · supervises the desk where remake claims arrive (+3) · supervisor level replies more readily than plant leadership (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Armando Pedraza

id: C110
name: Armando Pedraza
linkedin_url: https://www.linkedin.com/in/armando-pedraza-7280b228b/
linkedin_account: Izgin
company: Hunter Douglas, Inc.
role: Quality Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Hunter%20Douglas%20quality
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Hunter Douglas is the largest custom window-fashions maker in North America and the first name the recon lists under who actually knows the number. A quality engineer works the returned units themselves, so his answer to H3A2 comes from inspection rather than from a report, and any rate he gives for H3A1 is the one his own defect coding produces.

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · quality engineering at the largest NA maker (+2) · individual-contributor engineer, may not be cleared to share rates (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Abubakr Abushanab

id: C111
name: Abubakr Abushanab
linkedin_url: https://www.linkedin.com/in/abubakrabushanab/
linkedin_account: Izgin
company: Hunter Douglas, Inc.
role: Quality Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Hunter%20Douglas%20quality
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  Second Hunter Douglas quality engineer, at a different site from C110 (Dallas-Fort Worth against Monterrey). Deliberately paired: if two quality engineers at the same company on different sites give materially different remake rates, the rate is site-specific and the whole sizing question changes shape. Same competence, same two assumptions.

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · quality engineering at the largest NA maker (+2) · second contact at the same firm, so one may cover for the other (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## James McLaughlin

id: C112
name: James McLaughlin
linkedin_url: https://www.linkedin.com/in/james-mclaughlin-b9747051/
linkedin_account: Izgin
company: Norman USA
role: General Manager - Northeast Region

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Norman%20Window%20Fashions
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  A regional GM at Norman sits between the plant and the dealer network, which is exactly the handoff H3A3 is about: he sees remakes charged in both directions and can say which side absorbs them in practice rather than in policy. He can also give the regional rate (H3A1), which is a useful check on whatever the VP of Operations (C105) states nationally.

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · regional GM carries the remake on a P&L he owns (+2) · regional rather than plant, so the rate may be second-hand (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## William DeSemple

id: C113
name: William DeSemple
linkedin_url: https://www.linkedin.com/in/william-desemple-69253069/
linkedin_account: Izgin
company: Norman Window Fashions
role: General Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Norman%20Window%20Fashions
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1, H3A3]
validation_rationale: >
  Second Norman general manager, Greater Seattle against C112's Northeast. Same reasoning and the same pairing logic as C110/C111 - a rate that holds across two regions of one manufacturer is worth more than either region alone, and a rate that does not hold tells you the number is local.

response_likelihood: 5
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · GM carries the remake on a P&L he owns (+2) · third Norman contact, so redundancy is real (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Ranjan Mada

id: C114
name: Ranjan Mada
linkedin_url: https://www.linkedin.com/in/ranjan-mada-67900916/
linkedin_account: Izgin
company: Norman International Corp.
role: Chief Executive Officer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Norman%20Window%20Fashions
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A3]
validation_rationale: >
  H3A3 only. A CEO can say whether remake cost is material enough to reach him - which is itself the answer to whether the cost is concentrated or diffused - but he will not hold the rate, and asking him for it would be an out-of-competence question inviting a confident guess. Low expected reply; included because a top-band CEO saying the cost is beneath his attention would be a real contradiction.

response_likelihood: 3
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · CEO of a top-band maker (+1) · CEOs rarely answer cold and rarely hold the operational number (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Dan Williams

id: C115
name: Dan Williams
linkedin_url: https://www.linkedin.com/in/conversion/
linkedin_account: Izgin
company: 3 Day Blinds
role: Chief Revenue Officer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=3%20Day%20Blinds%20operations
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A3]
validation_rationale: >
  H3A3 only. 3 Day Blinds measures and installs with its own consultants rather than relying on the customer, which makes it the structural opposite of SelectBlinds. If the cost lands differently when the seller owns the measurement, that shows up on the revenue side first, and the CRO is who sees it. Not asked about rates or attribution.

response_likelihood: 3
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · owns the revenue side of a remake guarantee (+1) · CRO is a commercial not operational answer (-1)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Vivek Rao

id: C116
name: Vivek Rao
linkedin_url: https://www.linkedin.com/in/vivek-rao-0a217217/
linkedin_account: Izgin
company: BlindMatrix Ltd.
role: Founder

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=BlindMatrix
signal_excerpt:

contact_role: expert
role_pts: 2

tier: industry_software_vendor
size_band: 

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  The recon names BlindMatrix as the highest-leverage target in this lane and it did not arrive by design - it surfaced incidentally. A vendor whose ERP runs inside many window-covering manufacturers and dealers sees remake rates across the industry rather than at one firm, and has no competitive reason to hide the aggregate. That is a cross-firm answer to H3A1 that no single manufacturer can give. NOT tagged to H3A3: H3A3 declares no expert tier, and a vendor cannot say which party inside a customer's business absorbs the cost - he would be guessing, and a confident guess enters the ledger as durable wrong evidence. size_band left empty on purpose: he is expert-side and sits nowhere on the made-to-measure receipts ladder.

response_likelihood: 6
likelihood_factors: >
  profile_fit (0) · start 3 · 3rd+ (0) · founder of the one vendor that sees the rate ACROSS firms (+3) · founders answer cold outreach about their own market (0)
outreach_pattern:
degree: "3rd+"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: invited
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."

## Praveen Perfeito

id: C117
name: Praveen Perfeito
linkedin_url: https://www.linkedin.com/in/praveen-perfeito-75852a64/
linkedin_account: Izgin
company: BlindMatrix Ltd.
role: Technical Lead

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=BlindMatrix
signal_excerpt:

contact_role: expert
role_pts: 2

tier: industry_software_vendor
size_band: 

assumptions_tested: [H3A1, H3A2]
validation_rationale: >
  2nd degree, and the cheaper way into BlindMatrix than the founder. A technical lead knows whether remakes are a first-class tracked field in the product or something customers record in free text - which decides whether the industry rate H3A1 needs is recoverable from software at all, and whether the system captures error attribution (H3A2). size_band left empty for the same reason as C116.

response_likelihood: 6
likelihood_factors: >
  profile_fit (0) · start 3 · 2nd degree (+2) · technical lead knows what the system records (+2) · not the person who reads the aggregate (-1)
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: accepted
message_stage:
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25)."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.
