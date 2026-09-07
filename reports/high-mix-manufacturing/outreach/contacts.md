---
purpose: The contact ledger for this idea — one record per person approached, their signal, and where the conversation got to.
idea: high-mix-manufacturing
last_updated: 2026-09-05
totals:
  targeted: 95
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

assumptions_tested: [H0A1]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[live snapshot 2026-09-05] VERIFIED: Liaison Engineer, Boeing, Everett WA, since Jan 2026 (9 mos). Prior Pratt & Whitney 2y8m - Structures Engineer, Design Engineer, Project Engineer. Georgia Tech. 26 mutual connections. No recent posts, so no post_engagement hook exists. Card was already accurate. [audit H0A1 keep 2026-09-05] Liaison engineering IS per-instance disposition - when a part reaches the floor wrong, he engineers the fix. That is H0A1's failure event seen from the point where it costs hours. Aerospace build rates are low, so the high-volume exclusion does not apply. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [msg1 drafted 2026-09-02] soft_ask. Live snapshot: Boeing since Jan 2026 (9 mos), prior Pratt & Whitney 2y8m, Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [msg1 sent 2026-09-05 18:44] Sent by the founder by hand, and REWORDED: he replaced the frame with his own, "I am currently researching the real2sim gap in CNC's", which names the gap concretely instead of pointing at it. That rewrite is what exposed the dangling-referent defect in the drafted version. No reply yet."
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
notes: "Prior exchange in the archive: he replied 2026-07-15. Open with continuity, not a cold intro. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-07-15). Msg 1 is the wrong shape — route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [founder decision 2026-09-05] DO NOT MESSAGE AGAIN. The founder's instruction, and the inbox supports it: a thread exists from 2026-07-15 and it ended with the founder's own "Ah okay, thanks for the response! Enjoy the rest of your day", which is how a no gets closed politely. He REPLIED, so this is not an LR-B30 time gate and never ages back in. Held, not off_scope: his ICP fit did not fail, the answer did. The drafted Msg 1 stays in the archive unsent as the record of what was nearly sent to someone who had already declined. THIS IS THE MISS THAT MATTERS: LR-B25 was never run on this batch of fourteen before drafting, which is exactly the silent failure that rule exists to prevent."
## Can Tafulcan

id: C3
name: Can Tafulcan
linkedin_url: https://www.linkedin.com/in/can-tafulcan-460324134/
linkedin_account: Izgin
company: LyondellBasell (role ended Jul 2026)
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[msg1 drafted 2026-09-02] soft_ask, written in Turkish (informal, LR-6). LIVE CORRECTION: LyondellBasell role ENDED Jul 2026, export had it as current. Drafted from the prior in-ICP role (LR-B8), past tense. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. CORRECTED: the LyondellBasell role reads Jul 2023 to Jul 2026 and has ENDED. The card said current. Copy is written so it is true either way. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [msg1 sent 2026-09-05 18:46] Sent by the founder by hand and REWRITTEN COMPLETELY, in Turkish and in a personal register: "Can selam - nasilsin?? I am doing some research for my startup and my agents gave me your name to contact haha. numaran ayni mi?" The drafted cold message was not used. He is a personal contact, which the ledger did not know; treat the relationship as warm."
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot confirms Viasat current (4y4m); anchor is her own wording on antenna operating data and return rates. Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 6:49 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
## Heath Holtz

id: C5
name: Heath Holtz
linkedin_url: https://www.linkedin.com/in/heath-holtz-b57535/
linkedin_account: Izgin
company: Kohler Co.
role: Chief Operations, Supply Chain and Sustainability Officer

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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "Founder messaged 2019-10-03, no reply. Seven years stale and about something unrelated — effectively a fresh approach, but the founder should confirm before sending. [msg1 drafted 2026-09-02] soft_ask, senior register (LR-B5). Founder messaged 2019-10-03, no reply; ~7 years stale so LR-B25 treats this as fresh Msg 1, not a follow-up. FOUNDER TO CONFIRM before sending. Live: Kohler C-level since Feb 2024, 50 sites / 18 countries. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. CORRECTED: promoted Apr 2026, Sustainability added to the remit. Kohler is 18,000 associates across 50 plants in 18 countries; he came from Nissan and Target. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] A thread exists from 2019-10-03: a student connection note, ours last, no reply. Nearly seven years and he now holds buyer authority, so LR-B30 puts this well above the twelve-month line and a fresh Msg 1 is correct. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:12 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
## Akshaya Satish

id: C6
name: Akshaya Satish
linkedin_url: https://www.linkedin.com/in/akshaya19/
linkedin_account: Izgin
company: Tata Advanced Systems Limited (role ended Jul 2026)
role: Executive Manufacturing Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: 

assumptions_tested: [H0A1]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg1_drafted
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
notes: "[live snapshot 2026-09-05] VERIFIED WITH A CORRECTION: the Tata role ENDED Jul 2026 and no current role is listed, so `company` is now stale and she may be between roles. Executive Manufacturing Engineer Aug 2023-Jul 2026 on the C295 military aircraft Final Assembly Line at Vadodara, Graduate Manufacturing Engineer before that on the C295 greenfield programme, plus 6 mos at Airbus Defence and Space in Seville on the San Pablo FAL. Industrialisation and APQP. Low-rate aerospace with a real per-order industrialisation step. Copy MUST use past tense about Tata. [audit H0A1 keep 2026-09-05] Aerospace at Tata Advanced Systems is low-rate with per-order engineering. Executive Manufacturing Engineer sits on the handoff. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. Prior exchange in the archive: replied 2026-08-12. Warm and recent — continue the thread. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-08-12). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. CORRECTED: the Tata role reads Aug 2023 to Jul 2026 and has ENDED. Work was the C295 military aircraft final assembly line. [LR-B25 2026-09-05] NOT A COLD CONTACT. A thread exists and SHE REPLIED: on 2026-08-24 the founder wrote "Akshaya thank you - I have sent Cristina a connection request", so she had answered and referred someone on. Routing corrected from Msg 1 to the reply arc; the drafted cold message must not be sent. Find out who Cristina is and whether that referral was ever followed up."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Tesla - high-volume repeat manufacturing. Controls engineering on a line that runs the same part thousands of times. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. Prior exchange in the archive: replied 2026-08-11. Warm and recent. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-08-11). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Agratas is a gigafactory: high-volume repeat. Noted for later as a possible EXPERT-tier contact - a VP of IT Manufacturing owns the MES integration layer first-hand - but he is not demand for H0A1 and must not be counted as such. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. FLAG: founder messaged 2026-08-11 (3 weeks ago), no reply. Do NOT re-blast blind — founder decides whether to follow up or leave it. [not drafted 2026-09-02] LR-B25: founder messaged 2026-08-11 (3 weeks), ours last, silent. That is a FOLLOW-UP, not a Msg 1 — carries no research anchor and must not repeat the ignored ask. Needs founder decision before drafting. [LR-B30 hold 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Gate is closed under 3 months and VP seniority does not open it. Do not write. Eligible as a no-anchor follow-up from 2026-11-11."

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

assumptions_tested: [H0A1]
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
outreach_status: pending
message_stage: msg1_drafted
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
notes: "[live snapshot 2026-09-05] VERIFIED: Manufacturing Engineer, Boeing, North Charleston SC, since Jun 2023 (3y4m). Internships at FN America, Timken (applications engineering and manufacturing R&D) and JELD-WEN. Georgia Tech. Mid-level, so he can describe the failure well and cannot price it - H0A1 only. [audit H0A1 keep 2026-09-05] Boeing manufacturing engineering at aircraft build rates - low volume, per-order work packages. Same tier logic as C1. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. FLAG: founder messaged 2026-08-10 (3 weeks ago), no reply. Do NOT re-blast blind — founder decides. [not drafted 2026-09-02] LR-B25: founder messaged 2026-08-10 (3 weeks), ours last, silent. Follow-up shape, not Msg 1. Needs founder decision before drafting. [LR-B30 hold 2026-09-02] Messaged 2026-08-10, 23 days, no reply, no buyer authority. Do not write. Charles Evans (C1) covers Boeing for this assumption, so nothing is lost."

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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[msg1 drafted 2026-09-02] soft_ask. Live snapshot upgraded her: 'LCM Supplier Change Project Lead' at J&J through 2025 makes her the sharpest test of H2A2 in the batch. Georgia Tech. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified: in post since Jan 2026 after the J&J rotational programme. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:13 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "Prior exchange is from 2019-10-15 — treat as effectively cold but not a stranger. [not drafted 2026-09-02] LR-B25: thread exists and they replied, but in 2019. Route to /startup-outreach-reply, which decides continuation vs fresh. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] A thread exists from 2019-10-14 and it is personal rather than commercial: the founder rescheduling a call because a friend was in hospital. Ours last, no reply, seven years. Fresh Msg 1 stands, but the history is warmer than the ledger implied. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:14 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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

assumptions_tested: [H0A1]
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05 - live read] Live read 2026-09-05: TWO MONTHS into the JKH role (started Aug 2026), and she founds Finlay Systems, which sells AI and enterprise systems into operations-heavy industries. That makes her landscape and possibly competitor-adjacent, never demand. Prior roles are Luminance solutions engineering and fintech product. Cambridge IfM placement 2023-24 is a genuine shared-institution link and the reason to keep the card rather than delete it. [audit H0A1 keep 2026-09-05] Manufacturing Systems and Planning is the handoff function by name. JKH Ltd is unidentified in this repo - verify the company on the profile visit before sending anything. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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

assumptions_tested: [H0A1]
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
notes: "[audit 2026-09-05] UNVERIFIED - the experience page returned 'Something went wrong' on 2026-09-05 and the company 'RMG' is unidentified in this repo. Do not draft or send until the profile loads and the company is established. Held out of the H0A1 draft batch for that reason. [audit H0A1 keep 2026-09-05] Production Manager, but RMG is unidentified and the abbreviation is ambiguous. Verify the company before sending; drop if it is volume apparel. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. Prior exchange in the archive: replied 2026-02-12. [not drafted 2026-09-02] LR-B25: thread exists and THEY REPLIED (2026-02-12). Route to /startup-outreach-reply. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. PROFILE WOULD NOT LOAD 2026-09-05 (LinkedIn returned 'Something went wrong'). No draft written: LR-B6 needs a live snapshot and there is none. Retry before writing to him."
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

assumptions_tested: [H0A1, H0A2]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[live snapshot 2026-09-05] VERIFIED and STRONGER than the card said: 9y8m at Creagh Concrete, and he came up through the drawing office - Structural Engineer Feb 2017, Senior Structural Engineer Aug 2019, Operations Manager since Jan 2021 (5y9m). Also 2 yrs self-employed as a CAD designer. He has been on BOTH ends of the same drawing, which is rare and is exactly what H0A1 needs. Also holds budget, so he reaches H0A2. NOTE for the call, deliberately NOT in the copy: a 1-month Operations Consultant contract at Tharsus in Jan 2022 - Tharsus is Universal Wolf's former name, the founder's own Cambridge case-study company. Too thin a link to open with; a strong thing to have in hand. [audit H0A1 keep 2026-09-05] Precast concrete is made-to-order: every element is drawn for one building. Operations Manager holds budget, so this contact reaches H0A2 as well as H0A1. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:15 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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

assumptions_tested: [H0A1, H0A2]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: pending
message_stage: msg1_drafted
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
notes: "[live snapshot 2026-09-05] VERIFIED, and the headline is misleading - it reads 'Experiential Design Leader' but the experience is Director of Production at Deeplocal since Jul 2022 (4y3m), New York. Before that acrylicize Head of Projects: experiential builds with budgets up to $4m, and she wrote the costing documents - estimates, quotes, SOWs, fee agreements - and oversaw production partners 'to ensure projects adhered to design intent, timeline and budget'. That sentence is H0A1. Before that KPMG construction cost analysis and an architecture background. Pronouns She/Her per her profile. Strongest contact in this tier. [audit H0A1 keep 2026-09-05] Deeplocal builds one-off experiential installations - every job is designed once and made once, which is the scope statement almost word for word. Director of Production owns the handoff and the hours lost to fixing it. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [msg1 drafted 2026-09-02] soft_ask. Live snapshot upgraded her materially: prior roles were cost estimating and quoting for one-off builds (KPMG take-offs, then costing/quotes at acrylicize). Best contact in the batch for H2A3. Copy at outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [LR-B25 2026-09-05] Inbox check clean; the Grace search returned Grace Ling, a different person."
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
notes: "Distributor, not an asset owner. Competence gate: ask about frequency and sourcing behaviour, NOT about who signs off a non-OEM part in a plant he does not run. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. NOT DRAFTED 2026-09-05. Live profile confirms Bayouni Trading is a distributor in Saudi Arabia, not a manufacturer, so an MCP-layer-for-machines message has no purchase. Not off_scope, just wrong frame."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Manufacturing Graduate - fails the students/graduates exclusion. No budget, no history, no rate to state. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. Competence gate: junior. Ask only what she has seen on the line (H2A1). Do NOT ask about sign-off authority or procurement policy — an out-of-competence answer enters the ledger as durable wrong evidence. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
message_stage: msg2_sent
call_stage: asked_by_founder
found_date: 2026-09-02
invited_date: 2026-09-02
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[reply 2026-09-02] Replied on LinkedIn: 'Hi Izgin! Yes sure that sounds good :) I'm happy to have a chat\' — read from the inbox list preview; the thread is still UNREAD and was not opened. He OFFERED the call, so call_stage is offered_by_contact. Next step is /startup-outreach-reply for Msg 2. [msg1 drafted 2026-09-02] Live-verified. Aston Martin F1 since Oct 2025; was at Cambridge IfM May-Aug 2024, which does NOT overlap the founder's Oct 2024 start - copy says 'just before I got there' for that reason. Copy in outreach/copy/H2A1-linkedin.md. [msg1 SENT 2026-09-02 by founder, by hand] [msg2 sent 2026-09-03] Thread read live 2026-09-05. Viliam replied and the founder answered the same day: "Sounds great thank you! What times next week would you be available? I am in SF right now so will be in PDT time I am usually free 9-9". The ball is HIS. He was appearing in the control room's reply-waiting list only because no msg2 marker had been logged; the marker is now here and the panel drops him."
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

assumptions_tested: [H0A1]
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05 - live read] Live read 2026-09-05: offshore wind CONSTRUCTION and O&M, not manufacturing engineering - Dogger Bank tower pre-assembly at GE Vernova, before that site O&M at Invenergy and Goldwind and blade services at LM Wind Power. His one manufacturing stint (Nordex, 395 hubs and 325 nacelles) is series production. No per-order design step anywhere. Fails H0A1 ICP. [audit H0A1 keep 2026-09-05] Site pre-assembly on GE Vernova energy projects is one-off by definition: every site package is engineered for that site. Package Manager owns schedule and rework. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [LR-B30 HOLD 2026-09-02] Messaged 2026-07-14, 50 days, no reply. Eligible 2026-10-14."

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

assumptions_tested: [H0A1]
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05 - live read] Live read 2026-09-05: wind BLADE manufacturing, which is moulded series production - 14y7m at TPI Composites through production management, continuous improvement and blade process engineering, now Head of Process Engineering at Enercon Windtech. Serious operations leader, wrong mix/volume point. Fails the same icp_out_of_scope line as Tesla. Turkish and senior: worth keeping as network, not as H0A1 demand. [audit H0A1 keep 2026-09-05] Head of Process Engineering at a wind turbine builder. Verify on the visit whether Enercon Windtech runs series or project work; if series, this goes off_scope on the same line as Tesla. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [LR-B30 2026-09-02] They REPLIED 2026-07-13. Continuation - route to /startup-outreach-reply."

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

assumptions_tested: [H0A1]
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05 - live read] Live read 2026-09-05: Systems Engineering Lead on RADAR subsystems at Lockheed Moorestown, 6y1m - requirements, integration and test across software/network/hardware teams. He never sees a drawing reach a shop floor. Role-title screen said low-rate defence; the profile says systems engineering. Fails icp_valid_titles for H0A1. [audit H0A1 keep 2026-09-05] Low-rate defence - programme volumes in the tens, heavy per-order engineering. A Systems Engineering Lead carries the consequence when the design reaching manufacture is wrong. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Nissan - high-volume automotive. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Nissan - high-volume automotive. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Tesla - high-volume repeat manufacturing. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 HOLD 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Eligible 2026-11-11."

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

assumptions_tested: [H0A1]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[audit 2026-09-05] NOT YET VERIFIED - no live read taken this session. Boeing industrial engineering is borderline on FUNCTION rather than on volume, and the borderline is what the profile visit was supposed to settle. Held out of the H0A1 draft batch until verified. [audit H0A1 keep 2026-09-05] Boeing industrial engineering - borderline on function rather than on volume; keep at lower priority than C1 and C9, and verify on the profile visit that the role touches the drawing-to-floor path. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [msg1 drafted 2026-09-02] Live-verified. 7yrs at Boeing, Georgia Tech. Copy in outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:15 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Schaeffler - bearings, among the highest-volume repeat manufacturing there is. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 2026-09-02] They REPLIED 2026-08-12. Continuation - route to /startup-outreach-reply."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Intel - semiconductor process, the opposite end of the mix/volume axis. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 HOLD 2026-09-02] Messaged 2026-08-11, 22 days, no reply. Eligible 2026-11-11."

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

assumptions_tested: [H0A1]
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[audit 2026-09-05] NOT YET VERIFIED - no live read taken this session. Junior (Electromechanical Engineer T2), so H0A1 only and never H0A2 even if verified. Held out of the H0A1 draft batch. [audit H0A1 keep 2026-09-05] Low-rate defence electromechanical work. Junior (T2), so he can describe the failure but not price it - H0A1 only, never H0A2. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified. His own entry says he sends drawing packages to vendors for quotes and lead times, which is the handoff this idea is about. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:16 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Rivian - volume EV manufacturing. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [msg1 drafted 2026-09-02] Live-verified. Ex-Tesla 4680 NPI across engineering and supply chain. Copy in outreach/copy/H2A1-linkedin.md. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: McLaren Aerothermal Engineer - a design-analysis function. He does not see the drawing reach the floor. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 DROP 2026-09-02] Messaged 2024-11-05, no reply, no buyer-authority token. Stale-and-junior drops."

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

contact_role: influencer
role_pts: 1

tier: manufacturing_operations
size_band: 

assumptions_tested: []
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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: pending
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
notes: "[audit downgrade 2026-09-05] Live read: 'Engineering Associate to the Managing Director - Special Projects, developing Value Creation thesis' at Aston Martin Performance Technologies, 1 yr, plus Founder & CEO of CAST Energy and a King's Cambridge E-Lab residency. That is a strategy role held by a founder, not an operator who owns a drawing reaching the floor. F1 was the right instinct about the COMPANY and the wrong one about the PERSON. Reclassified contact_role buyer -> influencer: high-value intro multiplier into low-volume motorsport manufacturing and Cambridge, never counted as demand for H0A1. [audit H0A1 keep 2026-09-05] Aston Martin Performance Technologies is F1: nothing is made twice, and per-order engineering is the entire operating model. Engineering Associate to the MD sees both the drawing and the cost of it being wrong. Re-screened against the H0A1 ICP declared 2026-09-05; status held -> pending so copy can be drafted. Prior H2 assumption links replaced. [wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified. Also Founder and CEO of CAST Energy and a resident at the King's entrepreneurship lab in Cambridge, which overlaps the founder's own Cambridge year. That overlap is the opener. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean; the Chris search returned only unrelated threads."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Ford - high-volume automotive, and exterior lighting is a component design role rather than the handoff. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 DROP 2026-09-02] Messaged 2019-10-02, no reply, no buyer-authority token. Drops."

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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: ABB Senior R&D Engineer - research, not operations. Possible expert-tier value, never demand. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 HOLD 2026-09-02] Messaged 2026-08-06, 27 days, no reply. Eligible 2026-11-06."

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

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[wave 2, 2026-09-02] Added on the company-first recount. NOT yet live-snapshot verified and prior-contact state NOT checked (LR-B25) - both required before drafting. [H3 hold 2026-09-03] Sourced against H1/H2 ICPs. H3 (made-to-measure window coverings) is the active hunch and this contact does not validate it. NOT off_scope: their ICP fit for their own assumption is intact, and H1/H2 are superseded un-falsified, so this reverses in one pass if either lane is revived. [msg1 drafted 2026-09-05, MCP framing] Founder-set anchor: what he is building, with the Cambridge work as provenance rather than as the subject. Live profile re-read 2026-09-05 (LR-B6). Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. Live-verified 2026-09-05, card already correct. [unheld 2026-09-05] Founder decision: the MCP framing is written for this lane, so this contact leaves `held` and re-enters the campaign as `pending`. The H3 hold that put them here is lifted for them, not for the lane. [LR-B25 2026-09-05] Inbox check clean, no thread. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:16 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
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
outreach_status: off_scope
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
notes: "[audit off_scope 2026-09-05] Fails icp_out_of_scope on H0A1: Honeywell via Intelliswift, advanced test engineering. Volume electronics and a test function, not the design-to-manufacture handoff. Sourced against H2 from the founder 1st-degree network; H2 is superseded and this contact does not reach the belief-level nodes either. [LR-B30 2026-09-02] They REPLIED 2021-02-17. Continuation - route to /startup-outreach-reply."

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
company: Blinds To Go
role: Installation Manager, Manhattan area

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: dealer_installer
size_band: 

assumptions_tested: [H3A4]
validation_rationale: >
  He leads the Manhattan install crews at Blinds To Go and spent seven months as a design
  consultant taking the measurements himself, so he has stood on both ends of H3A4: what a visit
  costs to make in Manhattan, and which ones are worth making. His own posts describe protective
  shoe covers and laser measuring as core practice, so the visit economics are not abstract to
  him.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · leads a multi-crew install team so reports a rate not an anecdote
  (+3) · posts about measurement and installation practice, active in the last 30 days (+1) ·
  profile_fit signal (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: replied
message_stage: msg3_sent
call_stage: asked_by_founder
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Edgewater, New Jersey, US. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A4, soft_ask, standard register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED from the search-result cache: he is at Blinds To Go leading the Manhattan team, not at NY City Blinds, which he left in 2018. Copy at outreach/copy/H3-linkedin.md. [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads 'Connected on September 3, 2026'. No message from them. [msg1 sent] 2026-09-04 by the founder, by hand, in his own rewording of the draft: the opening names interoperability as the research subject and reaches it through measurement mis-matches, with the window-to-factory trip second, in a warmer register. 476 chars, 26 over the ~450 DM cap. The as-sent text is in outreach/copy/H3-linkedin.md; the eight other H3 drafts there still carry the drafted opening, so the two openings can be compared on reply rate. Awaiting reply. [replied 2026-09-04] Thread read live 2026-09-05. Full arc: founder's Msg 1 at 12:18, Andrii "Absolutely" at 12:50, founder asked for a call next week at 13:31, Andrii "Sure / I will" at 13:41 then "Let's chat Tuesday about my availability for next week" at 13:43. [msg3 sent 2026-09-05] Founder replied 09:34 "Sounds great - I will message you Tuesday!". FIRST CALL AGREEMENT SOURCED FROM LINKEDIN in this campaign. NEXT ACTION IS THE FOUNDER'S AND IT IS DATED: message him Tuesday 2026-09-08 to fix a time. He has agreed to talk, not yet to a slot, so this is call_stage asked_by_founder rather than scheduled. Nothing he has said is evidence yet: no question was asked and no claim was made."
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

assumptions_tested: [H3A4]
validation_rationale: >
  Installations manager at a UK dealer since Jan 2024 and a self-employed installation specialist
  across Essex and London since 2022. He is the H3A4 unit of analysis twice over: he carries the
  visit cost as an employer and as a sole trader, and his Appeal Home Shading entry uses 'Survey /
  Installation' as his own term for the trip.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · runs installs for a dealer and separately trades as a self-employed
  installation specialist, so he sees both cost structures (+2) · used 'survey' as his own word
  for the measuring visit on a prior role (+1) · profile_fit (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: London, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A4, soft_ask, standard register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05] Sent by the founder by hand. NOTE: this one went out carrying the SUPERSEDED anchor, which described the Cambridge year as research into how a window measurement reaches the factory. The founder corrected that on 2026-09-05: the MPhil was on the broken digital thread between CAD-CAM systems, not on window measurement. Every remaining draft was rewritten to the true claim; this one cannot be recalled. If he asks what the Cambridge work was, answer with the interoperability version, which is what the profile supports."
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
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Rochdale, UK. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6). [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 6:14 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing. Invite had been accepted; the ledger still said invited."
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
company: C & S Blind Installations Inc.
role: Independent business owner, blind and drapery installation

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A4]
validation_rationale: >
  He OWNS the installation company rather than working inside a dealer network, which the cached
  entry missed. That makes him the cleanest H3A4 respondent on the list: the cost of driving
  across Calgary to a window comes out of his own margin, and after thirteen years he can say
  which jobs he declines on distance without consulting anyone.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · owns the business so carries the visit cost himself, which is the
  H3A4 unit of analysis (+2) · thirteen years in one metro, so distance and drive time are a lived
  constraint (+1) · profile_fit (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. Location: Calgary, Canada. Found via LinkedIn people search 2026-09-03 (Pass 4, Phase B — no companies.md registry exists yet). Headline and company are from the SEARCH RESULT only; /startup-outreach-draft must re-open the live profile before any claim is written (LR-B6). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A4, soft_ask, senior register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED from the search-result cache: he is the independent owner of C & S Blind Installations Inc. in Calgary, not a contractor inside the Hunter Douglas dealer network. contact_role raised to buyer accordingly. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05 10:53] Sent by the founder by hand, found by an inbox check the same day rather than reported. Sent verbatim from the draft, the only one of the five that was. The as-sent text is in outreach/copy/H3-linkedin.md; it is NOT the drafted text and it is not the later two-frame rewrite either, so treat this send as its own copy variant. No reply as of 2026-09-05."
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

assumptions_tested: [H3A5]
validation_rationale: >
  REROUTED from H3A1/H3A3 to H3A5 on 2026-09-04. Blinds.com sends nobody to measure, so she cannot
  name a visit fee and asking her H3A4 would collect a courteous opinion outside her competence.
  What she owns is the mirror question and H3A5's disconfirmation test: her own profile says she
  drives online sales for every window treatment category, so she is the one person on this list
  who can rank why the category still sells offline, and say whether measurement leads that
  ranking or fabric and colour do.

response_likelihood: 7
likelihood_factors: >
  1st degree, accepted (+3) · owns the category P&L at the largest online-only made-to-measure
  seller in the US (+2) · no posts or visible activity to read (0) · profile_fit (0), start 3,
  capped at 7 for seniority and inbox volume
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A5, soft_ask, senior register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. Live snapshot confirms the cached title and company unchanged. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05 10:55] Sent by the founder by hand, found by an inbox check the same day rather than reported. "Thanks for connecting." added after the greeting. The as-sent text is in outreach/copy/H3-linkedin.md; it is NOT the drafted text and it is not the later two-frame rewrite either, so treat this send as its own copy variant. No reply as of 2026-09-05."
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
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 10:53 AM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing. Invite had been accepted; the ledger still said invited."
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
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 6:15 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing. Invite had been accepted; the ledger still said invited."
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
role: Quality Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions%20quality%20manager
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  REROUTED from H3A2 to H3A1 alone on 2026-09-04. A plant quality manager books no measuring
  visits, so H3A4 is outside his competence, but the remake rate is exactly what his function
  measures. His thirteen years in automotive quality before Springs is the useful asymmetry: he
  knows what a normal external-defect rate looks like in an industry that tracks it obsessively,
  so a window-covering figure will read as high or low to him rather than just as a number.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · quality owner at a manufacturer, so remakes land on his desk as data
  rather than as a story (+2) · thirteen years of automotive quality gives him a defect-rate
  baseline outside this industry to compare against (+1) · profile_fit (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A1, soft_ask, standard register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED: his title reads Quality Manager, not Quality Engineering Manager. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05 10:56] Sent by the founder by hand, found by an inbox check the same day rather than reported. The founder fixed the clause himself: "a wrong measurement rather than a bad manufactured part", replacing the drafted "a wrong number rather than a bad part" that he had flagged as not making sense. The as-sent text is in outreach/copy/H3-linkedin.md; it is NOT the drafted text and it is not the later two-frame rewrite either, so treat this send as its own copy variant. No reply as of 2026-09-05."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

## Julio Tinajero

id: C107
name: Julio Tinajero
linkedin_url: https://www.linkedin.com/in/julio-tinajero-9b5a5332/
linkedin_account: Izgin
company: Springs Window Fashions (Reynosa; role ended Oct 2025)
role: Plant Operations Manager, Reynosa

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Springs%20Window%20Fashions%20quality%20manager
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A1]
validation_rationale: >
  REROUTED from H3A2 to H3A1 alone on 2026-09-04, and drafted from the PRIOR role per LR-B8. His
  own entry says he cut external defects by half in eighteen months across three shifts and 1,300
  people at Springs Reynosa. A person who moved that number knows what was driving it, which is
  the causal split H3A1 needs and that no published source provides. He cannot speak to the
  measuring visit, which happens at the dealer, so H3A4 is not asked.

response_likelihood: 7
likelihood_factors: >
  1st degree, accepted (+3) · ran a $67m P&L at the plant, so he saw the remake cost as money
  rather than as a defect count (+2) · left the role in Oct 2025, so recall is recent but he no
  longer has the reports in front of him (-1) · profile_fit (0), start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A1, soft_ask, senior register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED, and this is the reason LR-B6 exists: the Springs role ENDED Oct 2025. His headline still reads as current, so the two disagree; the message is written so it is true either way. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05 10:58] Sent by the founder by hand, found by an inbox check the same day rather than reported. Frame replaced with the founder's own, plainer version: whether the software gap "traces all the way down to quality issues". Shorter and in plant language. The as-sent text is in outreach/copy/H3-linkedin.md; it is NOT the drafted text and it is not the later two-frame rewrite either, so treat this send as its own copy variant. No reply as of 2026-09-05."
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
outreach_status: msg1_sent
message_stage: msg1_sent
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
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 6:14 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing. Invite had been accepted; the ledger still said invited."
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
company: Norman International Inc.
role: General Manager, Western US and Canada

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=Norman%20Window%20Fashions
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A4]
validation_rationale: >
  REROUTED from H3A3 to H3A4 on 2026-09-04. Sixteen years running Norman's western US and Canada
  region puts him above the individual dealer, so he can say whether a visit cost is one company's
  problem or the category's, which is precisely what H3A4's disconfirmation test needs and what E8
  alone cannot settle. His six years selling for a shutter dealer before that means he has also
  carried the cost personally, so he is a route into H3A6 later without a second sourcing pass.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · sixteen years running a manufacturer's western region, so he sees
  visit economics across many dealers rather than one (+2) · six prior years selling inside a
  shutter dealer, so he has carried the visit himself (+1) · profile_fit (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A4, soft_ask, senior register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED: the company is Norman International Inc. and his remit is Western US and Canada, not Norman Window Fashions unqualified. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 14:02] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. Sent on the PREVIOUS framing ("I spent a year at Cambridge on why the machines and the software that drives them never share one thread"), four hours before the MCP rewrite. He is the only one of the six not on the MCP anchor. No reply yet."
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

assumptions_tested: [H3A4]
validation_rationale: >
  REROUTED from H3A3 to H3A4 on 2026-09-04, and he is now the strongest H3A4 contact on the list.
  3 Day Blinds sends its own consultants to measure, and his own role description carries the
  company line 'We Design, we Measure, we Install, you Relax', so the visit is not a cost centre
  he has to look up. He also came to it from running online retail, which means he has personally
  made the trade H3A4 asks about, in both directions.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted (+3) · owns the revenue line at the company whose model IS the assumption,
  and his own profile names the measuring step (+3) · one mutual connection, Bruno (+1) · comments
  on other people's posts within the last week, so the account is live (+1) · start 3, capped at 8
  for seniority
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg2_sent
call_stage: asked_by_founder
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A4, soft_ask, senior register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. The linkedin_url /in/conversion/ is CORRECT and not broken: it is his own vanity slug. A prior session flagged it as invalid; it resolves to his live profile. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 18:12] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. MCP framing, sent verbatim from the draft. No reply yet. [replied 2026-09-05] HE ANSWERED. Reported by the founder, not read by Claude: the founder instructed that the thread NOT be opened in the browser, so his exact wording is not in this ledger and the reply excerpt is second-hand. What he asked was what the end goal of the research is. He is Chief Revenue Officer of a company whose whole model is measure and install, which makes this the most valuable reply the campaign has produced. [msg2 drafted 2026-09-05] Answers the question in one line and asks for a call this week. The end goal is stated as the founder states it: an intent layer for MCP machine orchestration. NO COST QUESTION: H3A4's next_action wants the per-visit fee, but LR-B11 puts money at Msg 4 and its own note says an assumption's next_action describes the interview rather than the message. Asking a CRO for a per-visit cost in message two reads as qualifying a lead. Availability offered as a range per the founder, not a booking link (LR-M9). Copy at outreach/copy/H3-linkedin.md. UNSENT. [msg2 sent 2026-09-05 by founder, by hand] Observed in the founder's inbox on 2026-09-05, timestamp 7:08 PM. Answers his question and asks for a call, offering 9am to 9pm PDT. The message states the end goal as an intent layer for MCP machine orchestration, which is a product reveal made by founder decision."
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
company: BlindMatrix Ltd. (role ended Jun 2026)
role: Tech lead, e-commerce

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/search/results/people/?keywords=BlindMatrix
signal_excerpt:

contact_role: expert
role_pts: 2

tier: industry_software_vendor
size_band: 

assumptions_tested: [H3A5]
validation_rationale: >
  REROUTED from H3A1/H3A2 to H3A5 on 2026-09-04, expert side. He spent nearly six years building
  the e-commerce module of the industry's own software, which is the online ordering path H3A5 is
  about, seen across every customer that deployed it. He is not a buyer and never carried a
  remake, so nothing he says can be logged as pain evidence; his competence is the failure
  mechanism, not the economics.

response_likelihood: 7
likelihood_factors: >
  1st degree, accepted (+3) · built the online ordering path for the industry's own software, so
  he has seen what breaks across many blind companies rather than one (+2) · one mutual
  connection, Anto (+1) · the role ended Jun 2026 and his headline has not caught up, so currency
  is uncertain (-1) · start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-03
invited_date: 2026-09-03
accepted_date: unknown  # observed 1st-degree 2026-09-04; LinkedIn does not show the date
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[invited 2026-09-03] Bare connection request, no note (LR-B29), sent by Claude with per-invite name verification against the invitation modal. Campaign: outreach/linkedin/h3-window-coverings-2026-09/. [sourced 2026-09-03] Enterprise/top-band pass against the H3 ICP after the market ladder showed the existing pool sat almost entirely in the micro band. Headline and company read from LinkedIn people search on 2026-09-03; profile NOT yet opened, so degree and title are search-result facts and must be re-verified live before any draft (LR-B6, LR-B25). [msg1 drafted 2026-09-04] Post-acceptance Msg 1 for H3A5, soft_ask, standard register. Live profile re-read 2026-09-04 (LR-B6); LR-B25 first-name inbox check clean, positive control (Viliam) returned its thread in the same batch. CORRECTED: his title is Tech Lead e-Commerce and the BlindMatrix entry ends Jun 2026 while his headline still reads as current. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 18:13] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. MCP framing, sent verbatim from the draft. No reply yet. [copy defect, sent 2026-09-05] This message went out with a DANGLING REFERENT: it asked whether "that gap" shows up in rework rates, and no gap had been named anywhere in it. The MCP anchor replaced an earlier one that had named the gap, and the frame was left pointing at nothing. Founder-caught after sending. Not recallable. If they reply asking what gap, the answer is the one the corrected drafts now state: design software and the machines never share one thread. Every unsent draft was rewritten the same day."
  [accepted 2026-09-04] Connection accepted; LinkedIn connections list reads "Connected on September 3, 2026". No message from them. Awaiting Msg 1.

---

### Batch 2026-09-05 — accepted connections found in the network sweep

Four contacts who accepted between 2026-09-04 and 2026-09-05 and were found by reading the
recently-added connections list rather than by a sourcing pass. Three more accepted in the
same window and are NOT recorded here because they fail the H3 ICP: a robot-kit manufacturer,
a robotics engineer and an aerospace entrepreneur. They belong to the H1 and H2 lanes and
nothing about them changed.

## Bruno Campos

id: C118
name: Bruno Campos
linkedin_url: https://www.linkedin.com/in/camposbruno/
linkedin_account: Izgin
company: SelectBlinds
role: Vice President of Marketing

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: window_covering_manufacturer
size_band: enterprise

assumptions_tested: [H3A5]
validation_rationale: >
  The highest-value contact in this ledger. SelectBlinds is the company whose FIT Protection
  free-remake guarantee sits in the H3 hunch statement and in the pitch, and he runs the marketing
  function that offers it at checkout. He also spent a career selling boxed goods online at Nike
  and AB InBev before selling made-to-measure, so he can rank why this category behaves
  differently rather than guessing. On the call, do NOT open on FIT Protection: the discovery
  pitch's own trap list says naming it makes the conversation about their policy instead of their
  losses.

response_likelihood: 9
likelihood_factors: >
  1st degree, accepted 2026-09-04 (+3) · his employer is the source of the single most cited piece
  of evidence in this ledger, so the fit is not incidental (+2) · a career in digital commerce at
  Nike and AB InBev before this, which is exactly the comparison H3A5 needs (+1) · already a
  mutual connection on C115's profile (0), start 3, capped at 9
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date: unknown  # accepted before this session saw them; LinkedIn shows the day, not the invite
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 in the recently-added connections list; he accepted an invite on 2026-09-04. Live profile read 2026-09-05: the headline says CMO at Select Blinds US, the experience entry says Vice-president of marketing, Jul 2024 to present, Phoenix. The copy says 'run marketing', which is true of both. LR-B25 first-name inbox check clean 2026-09-05. [msg1 drafted 2026-09-05] Post-acceptance Msg 1 for H3A5, soft_ask. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1 sent 2026-09-05 10:53] Sent by the founder by hand, found by an inbox check the same day rather than reported. Opening changed to "Bruno hi! Thanks for connecting." in place of "How are you?". The as-sent text is in outreach/copy/H3-linkedin.md; it is NOT the drafted text and it is not the later two-frame rewrite either, so treat this send as its own copy variant. No reply as of 2026-09-05."
## Armando Pedraza

id: C119
name: Armando Pedraza
linkedin_url: https://www.linkedin.com/in/armando-pedraza-7280b228b/
linkedin_account: Izgin
company: Hunter Douglas, Inc.
role: Quality Engineer

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
  He updates the rework and customer-complaint numbers across three production lines at a
  window-covering manufacturer, which is H3A1 stated as a job rather than as a question. His six
  years as a dimensional and tooling specialist at an automotive supplier before this means he can
  also speak to the factory-tolerance half that E15 opened up, which no other contact on the list
  can.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted 2026-09-05 (+3) · his own role description names the rework KPI as
  something he personally updates, so the H3A1 number is on his desk (+2) · six prior years on
  dimensional and tooling work, so he reads a tolerance the way the assumption needs (+1) ·
  profile_fit signal (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date: unknown  # accepted before this session saw them; LinkedIn shows the day, not the invite
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 in the recently-added connections list; accepted 2026-09-05. Live profile read the same day. Apodaca, Nuevo Leon, Mexico. LR-B25 first-name inbox check clean 2026-09-05. [msg1 drafted 2026-09-05] Post-acceptance Msg 1 for H3A1, soft_ask. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 18:14] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. MCP framing, sent verbatim from the draft. No reply yet. [copy defect, sent 2026-09-05] This message went out with a DANGLING REFERENT: it asked whether "that gap" shows up in rework rates, and no gap had been named anywhere in it. The MCP anchor replaced an earlier one that had named the gap, and the frame was left pointing at nothing. Founder-caught after sending. Not recallable. If they reply asking what gap, the answer is the one the corrected drafts now state: design software and the machines never share one thread. Every unsent draft was rewritten the same day."
## Ben Simpson

id: C120
name: Ben Simpson
linkedin_url: https://www.linkedin.com/in/ben-simpson-975b90184/
linkedin_account: Izgin
company: Self-employed
role: Curtain and blinds installer, self-employed

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: dealer_installer
size_band: micro

assumptions_tested: [H3A4]
validation_rationale: >
  Nine years fitting curtains and blinds on his own books around Manchester. Like C52 he is both
  the person who drives to the window and the person who decides the drive is worth making, so the
  H3A4 pair can be asked of one person without an approval chain. His profile carries one line and
  no description, so the grounded clause rests on tenure and trading status rather than on his own
  words; expect a lower reply rate than the richer profiles.

response_likelihood: 7
likelihood_factors: >
  1st degree, accepted 2026-09-04 (+3) · self-employed, so he both makes the visit and decides
  whether it is worth making, which is the H3A4 unit of analysis (+2) · nine years in one city
  (+1) · profile is a single line with no description, so there is less to ground a message in
  (-2), start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date: unknown  # accepted before this session saw them; LinkedIn shows the day, not the invite
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 in the recently-added connections list; accepted 2026-09-04. Live profile read 2026-09-05 and it is SPARSE: one experience entry, no description, no posts. Copy drafted from the headline and tenure, per the skill's sparse-profile rule. LR-B25 first-name inbox check clean 2026-09-05. [msg1 drafted 2026-09-05] Post-acceptance Msg 1 for H3A4, soft_ask. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 18:14] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. MCP framing, sent verbatim from the draft. No reply yet."
## Rose Mauloni

id: C121
name: Rose Mauloni
linkedin_url: https://www.linkedin.com/in/rosemauloni/
linkedin_account: Izgin
company: Wayfair
role: Merchandise Manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: national_retail_channel
size_band: enterprise

assumptions_tested: [H3A5]
validation_rationale: >
  CORRECTS the assumption that she is a furniture contact. She has owned the WINDOW category at
  Birch Lane and now Wayfair for three years, alongside rugs, bedding and bath. That mix is the
  natural experiment H3A5 needs: the same merchant, the same customers, the same site, and one
  category that will not move online the way the others did. She can rank the reasons from sales
  data rather than from opinion, and if she ranks fabric or colour above measurement, that counts
  fully against the hunch.

response_likelihood: 8
likelihood_factors: >
  1st degree, accepted 2026-09-04 (+3) · has owned the Window category at the largest online home
  retailer for three years, so the offline-versus-online question is her P&L (+2) · carries boxed
  categories alongside window, which gives her the controlled comparison H3A5 wants (+1) ·
  profile_fit signal (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date: unknown  # accepted before this session saw them; LinkedIn shows the day, not the invite
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 in the recently-added connections list; accepted 2026-09-04. Live profile read 2026-09-05: she moved from Senior Merchant at Birch Lane to Merchandise Manager at Wayfair in Mar 2026 and again in Jun 2026, so the Birch Lane headline seen in the connections list is one role behind. Boston, Massachusetts. LR-B25 first-name inbox check clean 2026-09-05. [msg1 drafted 2026-09-05] Post-acceptance Msg 1 for H3A5, soft_ask. Copy at outreach/copy/H3-linkedin.md. UNSENT: the founder sends by hand. [msg1_sent 2026-09-05 18:15] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. MCP framing, sent verbatim from the draft. No reply yet."
## Leonard

id: C122
name: Leonard
linkedin_url:
linkedin_account: Izgin
company: Sanyo
role:

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt: >
  "I would say on average, we see one of these errors every 50 manufactured details. So if a
  project has 200 details on it, we'll see this 4 times."

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: 

assumptions_tested: []
validation_rationale: >
  BELIEF-LEVEL, not H3. Sanyo builds machines; the active graph is window coverings, so
  `assumptions_tested` is deliberately empty and nothing he said may be scored against an H3
  node. He tests link 1 of belief.md directly and better than anyone contacted so far: he
  manages the designers whose output feeds manufacture, owns the process, decides whether
  verification headcount is justified, and replaces people who fall outside the speed/accuracy
  band. He gave an error rate (1 in 50 manufactured details), a cost-of-accuracy figure
  (110-125% of budgeted hours), the standing remedy (checkers) and the reason it is refused
  (cost justification) — the whole economics of the handoff, unprompted, in one message.

response_likelihood: 9
likelihood_factors: >
  already in an active exchange and writing long-form unprompted (+4) · 27 years in role with
  direct process ownership (+2) · profile_fit (0) · start 3 · capped at 9
outreach_pattern:
degree:
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg2_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date: 2026-09-05

interviews:
  - date: 2026-09-05
    path: reports/high-mix-manufacturing/03-validation/belief-2026-09-05/interviews/leonard-sanyo-2026-09-05-notes.md
    stage: problem_discovery
    medium: linkedin_text

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[captured 2026-09-05] Existed nowhere in this repo until now — the exchange ran entirely outside the outreach machinery and the 1-in-50 rate lived only in chat. Card created from the message itself. FIELDS UNVERIFIED and left blank rather than guessed: surname, LinkedIn URL, exact job title, degree, which Sanyo entity, and headcount band. `contact_role: buyer` is inferred from him managing designers, owning process stoutness and deciding checker headcount — confirm it. `medium: linkedin_text` assumes LinkedIn DM; correct it if the channel was email or WhatsApp. Evidence E26 (supports, the rate) and E27 (contradicts, willingness to pay) are logged. `outcome_modifier` and `evidence_score` deliberately BLANK: proposed moderate_confirm, awaiting founder confirmation per the capture contract. [msg2 sent 2026-09-05] Two questions: whether checkers were ever actually run or only ever costed, and what the last non-small error cost."

## Joseph Garza

id: C123
name: Joseph Garza
linkedin_url: https://www.linkedin.com/in/joseph-garza-a4561784/
linkedin_account: Izgin
company: Advanced Machine Program & Design MFG.
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/joseph-garza-a4561784/
signal_excerpt: >
  "the margin for between the quote and the 1st good part depends on speed, complexity of the
  part and features, outside processes like Plating or Anodizing. All these have to come into
  factor before sending out a quote... It all comes down to Experience and being very high
  performing shop... The Key Driver in all of it is quality and Solving customers problems."

contact_role: buyer
role_pts: 3

tier: manufacturing_operations
size_band: micro

assumptions_tested: []
validation_rationale: >
  BELIEF-LEVEL, not H3. He runs a job shop, not a window-covering business, so
  `assumptions_tested` is empty and nothing he says may be scored against an H3 node. What he
  can testify to is the quote side of link 1: he prices work off whatever a customer sends him
  and then has to make the first good part for that price, and he owns the consequence when the
  two disagree. He is also 45 minutes from the founder while the founder is in San Francisco,
  which makes him the cheapest shop visit on the list.

response_likelihood: 8
likelihood_factors: >
  1st degree and already replied at length (+4) · owner, so no approval chain (+2) ·
  wrote "this is Worth a Conversation" and invited more questions (+2) · comments rather than
  posts, so low platform activity (-1) · start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count: 2
active_last_30d: true
open_to_work: false

close_variant: soft_ask
relationship_type: operator_buyer
outreach_status: replied
message_stage: msg2_sent
call_stage: offered_by_contact
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[captured 2026-09-05] Existed nowhere in this repo until now: Msg 1 went out 2026-08-25, before this outreach machinery existed, and the thread lived only in LinkedIn. Card created from the thread the founder pasted plus a live profile read on 2026-09-05 (LR-B6): headline reads OWNER, Santa Clara California, Advanced Machine Program & Design MFG., De Anza College, 218 connections, 2 mutuals (Maximilian, Nathan), no posts in the last year and three comments, the most recent on cnc machining as an owner. Shop address from public listings is 451 Aldo Ave, Santa Clara. A web search attributed a second company, Primex Precision of Farmington Missouri, to a Joseph Garza; the Primex site names no founder and nothing on this profile mentions it, so it is a DIFFERENT PERSON until proven otherwise and must not enter any message. FIELDS UNVERIFIED and left blank rather than guessed: headcount, what the shop actually machines, and who its customers are. `size_band: micro` is inferred from a single Santa Clara address and 218 connections, not from a headcount source. [msg1 sent 2026-08-25 by founder, by hand] H2-era framing, before the repo tracked copy: asked where the margin on a new job goes between the quote and the first good part, off the Cambridge research, closing on a permission ask. [reply 2026-08-31] Substantive and warm, apologised for the delay, answered in estimating terms, said 'Sure, this is Worth a Conversation' and 'Any more questions, please feel free'. Logged as E28 (ambiguous). [msg2 drafted 2026-09-05] Settled on the third pass. Founder instruction: ask for a call and nothing else, agree with what he said rather than pivot off it, and name the work as capturing intent. The message opens by agreeing that the money is at quoting and at whether the quote survives prove out, gives the direction in one clause, and asks for half an hour Tuesday or Wednesday. Deliberately absent: the Turkiye capacity, which to a shop owner reads as a competitor announcement, the shop visit, which was pulled as the larger ask, and the acronyms. An alternate carries the why-now (E20, the Model Hardware Standard) in plain words. The cost is recorded rather than argued: per copy/H3-discovery-pitch.md a contact who has heard the thesis reacts to it instead of reporting, and Joseph has named no job or number yet, so grade anything after this as a reaction. Both drafts, the two superseded passes and the call question order are in outreach/linkedin/belief-experts-2026-09/replies.md. UNSENT: the founder sends by hand. [msg2 sent 2026-09-05 by founder, by hand] Observed in the founder's inbox on 2026-09-05, timestamp 6:09 PM. The Msg 2 drafted this session went out, in the settled third-pass version that opens by agreeing with him about quoting and prove out. Awaiting his reply."
---

## Nathan Meyer

id: C124
name: Nathan Meyer
linkedin_url: https://www.linkedin.com/in/nathan-meyer-joby/
linkedin_account: Izgin
company: Joby Aviation
role: Advanced manufacturing and R&D prototyping

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: 
size_band: enterprise

assumptions_tested: []
validation_rationale: >
  Backfilled 2026-09-05 after an inbox check found the whole thread absent from this ledger.
  He is the warmest relationship the campaign has produced and none of it was recorded: he
  answered a cold message inside a day, offered either written answers or a call, took a call
  on 2026-08-27, and then volunteered two referrals and an offer of introductions at IMTS. He
  sits in the first-article and prove-out lane, which belongs to H1 and H2, so he cannot carry
  H3 evidence and no H3 question should be put to him. He is recorded because a person this
  generous going unlogged is how a relationship gets dropped, which is what nearly happened.

response_likelihood: 9
likelihood_factors: >
  1st degree and already replying (+3) · answered a cold message within a day and offered a
  call unprompted (+3) · volunteered two named referrals and an introduction offer without
  being asked (+2) · eight days of silence from our side is a real debt against the next
  message (-1), start 3, capped at 9
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg5_sent
message_stage: msg5_sent
call_stage: completed
found_date: 2026-08-25
invited_date:
accepted_date: unknown
scheduled_date: 2026-08-27
interview_date: 2026-08-27

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: replied
notes: "[id C124, not C122 — allocated 2026-09-05 against a stale next-free number while another session was writing C122 Leonard and C123 Joseph Garza into the same file. Theirs landed first and keeps the id; this one renumbered. C122 is NOT burned, it belongs to Leonard.] [backfilled 2026-09-05] Thread read live during an inbox check; it was never in this ledger. Arc: founder cold-messaged him about why a first article of a never-made part costs so much more than the ones after, citing the Cambridge work. He replied the same day: 'That's a problem I've spent most of my career inside of. Send the questions over whenever you're ready, glad to work through them in writing, or find 30 minutes if a call is easier on your end.' [call 2026-08-27] HAPPENED WITHOUT THE FOUNDER. Christian, the co-founder at the time, took it alone and the founder missed it. NOTHING FROM THAT CALL WAS EVER CAPTURED and the pairing ended 2026-08-31, so unless Christian's own notes surface it is lost. That is the single largest uncaptured item in this repo. [reply 2026-08-28] Volunteered two referrals unprompted: David Liu (linkedin.com/in/davidliuxyz, local, recently started his own venture) and Jim Belosic (linkedin.com/in/belosic, now in Reno). Asked 'Sounds like you and Christian already know Chris over at Hydrian?' and offered to network and make introductions at IMTS. [no reply from us, 8 days] The founder did not answer that message; the silence ran 2026-08-28 to 2026-09-05. [msg5 drafted 2026-09-05] Repair message only, no ask, per founder decision: it thanks the two referrals, offers to let him make the introductions himself, discloses that the co-founder pairing ended, answers that Chris at Hydrian was Christian's connection and not the founder's, and declines IMTS. His standing offer of written answers is deliberately NOT redeemed: his lane is H1/H2, superseded, so anything he says lands against a hunch nobody is testing. Redeem it later and against the belief, not against H3. Copy at outreach/copy/H1-H2-linkedin.md. UNSENT. [msg5_sent 2026-09-05 17:55] Sent by the founder by hand; confirmed by an inbox read 2026-09-05. Repair message sent with the founder's own additions: an opening thank-you, and a closing line naming the MCP layer for manufacturing machine control with an invitation to react. The drafted version deliberately asked for nothing; the sent version ends on a light ask. No reply yet."
## Shane Duncan

id: C125
name: Shane Duncan
linkedin_url: https://www.linkedin.com/in/shane-duncan-b7575a200/
linkedin_account: Izgin
company: B&B Manufacturing
role: CNC Programming Supervisor

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/shane-duncan-b7575a200/
signal_excerpt: >
  "I would say most jobs get held up the most in the quality department."

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: []
validation_rationale: >
  BELIEF-LEVEL, not H3. He supervises the programmers at a machining company, so nothing he says
  may be scored against an H3 node. He is the best-placed contact this idea has on the question
  the founder actually asked him: why a program that looks right still needs a person standing at
  the machine for the first part. He programmed 5 axis work himself and now runs the group that
  does, so where a new job stalls between the print landing and a good first part is his daily
  visibility, not an opinion.

response_likelihood: 8
likelihood_factors: >
  1st degree and replied twice within a day (+4) · supervises the group, so reports a pattern
  rather than one job (+2) · answered a call offer by continuing in text, so prefers DMs (-1) ·
  no public activity in the last year (-1), start 3, capped at 8

outreach_pattern:
degree: "1st"
mutuals_count: 4
active_last_30d: false
open_to_work: false

close_variant: direct_question
relationship_type: data_supplier_practitioner
outreach_status: replied
message_stage: msg2_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[captured 2026-09-05] Existed nowhere in this repo until now: the whole exchange ran on LinkedIn before this machinery covered it. Card created from the thread the founder pasted plus a live profile read on 2026-09-05 (LR-B6): CNC Programming Supervisor at B&B Manufacturing, 1st degree, United States, 500+ connections, 4 mutuals (Ian, Oswaldo and two more), 579 followers, one comment in the last year. FIELDS UNVERIFIED and left blank rather than guessed: which B&B Manufacturing this is, its location, sector and size. A search on 2026-09-05 could not settle whether they are an aerospace shop, so nothing about first article inspection or AS9102 may enter a message until he says it himself. The 5 axis history in Msg 1 came from an earlier reading of his experience section and is not re-verified here. [msg1 sent 2026-08-25 by founder, by hand] Date inferred from the thread sitting in the same afternoon batch as C123; correct it if wrong. Asked why a program that looks right still needs someone standing at the machine for the first part, permission close. [reply 2026-08-25] 'Sure, I'd be glad to answer some of your question.' [msg2 sent 2026-08-25 by founder, by hand] Which step between the print landing and a good first part backs up most often, with a call offered as an alternative. [reply 2026-08-26] 'I would say most jobs get held up the most in the quality department.' He answered in text rather than taking the call, so the call is NOT re-asked in Msg 3. Logged as E29. [msg3 drafted 2026-09-05] One drill on what quality was actually waiting on for the last new part, plus how long it sat. Copy in outreach/linkedin/belief-experts-2026-09/replies.md. UNSENT: the founder sends by hand."

---

### Batch 2026-09-05 — mined from the founder's own connections

Found by screening the LinkedIn export COMPANY-first against the H0A1 ICP rather than by a
browser sweep. The network is mostly robotics and software, and a title-first screen returned
almost nothing; screening on the employer being an organisation that makes things to order
surfaced a cryogenics cluster the campaign had never touched. That cluster is IMTEK's own
industry, which is why it was hiding in plain sight.

## Paul Rowe

id: C129
name: Paul Rowe
linkedin_url: https://www.linkedin.com/in/paul-rowe-21558718/
linkedin_account: Izgin
company: Wessington Cryogenics
role: Technical Director

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band: small

assumptions_tested: [H0A1]
validation_rationale: >
  The strongest H0A1 contact in the network and nobody had found him. Wessington builds coded
  cryogenic storage vessels, multi-coded liquid nitrogen, argon, oxygen and helium vessels, and
  intermodal ISO tank containers. Every one is certified and built to order, which is the
  definition of the lane. He ran the company from 1991 to 2022 and is now Technical Director, so
  he has both the drawing and thirty one years of what happens when it is wrong. It is also
  IMTEK's own industry, so the founder can hold the conversation.

response_likelihood: 9
likelihood_factors: >
  1st degree (+3) · thirty five years at one made-to-order vessel manufacturer, thirty one of them
  as the person who owned the drawing (+3) · the founder's own industry, so the vocabulary is
  shared (+1) · prior outbound 2020 with no reply, but nearly six years stale so LR-B30 treats
  this as a fresh Msg 1 (0), start 3, capped at 9
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: msg1_sent
message_stage: msg1_sent
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "[id C129, not C125 — allocated against a stale next-free number while another session wrote C125 Shane Duncan into the same file; theirs landed first and keeps the id.] Found 2026-09-05 by mining the LinkedIn export company-first against the H0A1 ICP. Live profile read the same day: Wessington 35 yrs 9 mos total, Managing Director 1991 to Apr 2022, Technical Director since Feb 2022. His own entry names dewars, multi-coded gas vessels and ISO tank containers. LR-B25: a thread EXISTS from 2020-10-07, the founder writing as a Georgia Tech student saying they were a fan of Wessington. Ours was last and there was no reply. At nearly six years LR-B30 puts this above the twelve-month line, so it is a fresh Msg 1 and the opener names the old message rather than pretending it did not happen. [msg1 drafted 2026-09-05, MCP framing] soft_ask. Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude. [msg1 sent 2026-09-05 by founder, by hand] Observed in the founder's own LinkedIn inbox on 2026-09-05 during a reconciliation pass, timestamp 7:16 PM. The thread shows the founder's message last and no reply yet. The copy sent is NOT the copy archived in this repo: the founder is now opening with "I am building the MCP layer for machines in manufacturing" and asking whether the gap shows up in rework rates. See outreach/linkedin/belief-experts-2026-09/drafts.md for the record of that framing."
## Sigal Lavenda

id: C130
name: Sigal Lavenda
linkedin_url: https://www.linkedin.com/in/sigal-lavenda-2b043ba3/
linkedin_account: Izgin
company: Ricor Cryogenic & Vacuum Systems
role: Vice President Research And Development

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band: mid

assumptions_tested: [H0A1]
validation_rationale: >
  Ricor builds cryocoolers, which are low-volume precision assemblies. As VP R&D she owns the
  design side of the handoff H0A1 is about, and her fourteen years at Rafael Advanced Defense
  Systems, latterly carrying a business unit P&L of roughly $300m, means she can speak to what the
  correction actually costs rather than only that it happens.

response_likelihood: 7
likelihood_factors: >
  1st degree (+3) · runs R&D at a cryocooler manufacturer, so the handoff is her function (+2) ·
  fourteen years at a defence prime including a business unit P&L, so she can price the answer as
  well as describe it (+1) · no prior contact and a senior inbox (0), start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 by mining the LinkedIn export. Live profile read the same day: Ricor since Oct 2021, prior Rafael Advanced Defense Systems 14 yrs 8 mos. LR-B25 inbox check clean. [msg1 drafted 2026-09-05, MCP framing] soft_ask. Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude."

## Jadon Pauling

id: C131
name: Jadon Pauling
linkedin_url: https://www.linkedin.com/in/jadonpauling/
linkedin_account: Izgin
company: Factory Automation Systems
role: Project Engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band: small

assumptions_tested: [H0A1]
validation_rationale: >
  An integrator sees the same handoff at every customer it builds for, which is the one vantage
  point a single manufacturer cannot give. Project Engineer sits in the H0A1 valid titles. He is
  two years in, so expect mechanism rather than economics, and treat anything he says about cost
  as second-hand.

response_likelihood: 7
likelihood_factors: >
  1st degree (+3) · project engineer at an integrator, so he sees the handoff across many
  customers rather than one (+2) · shared Georgia Tech affiliation on the founder's own profile
  (+1) · two years in role, so less history to draw on (-1), start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 by mining the LinkedIn export. Live profile read the same day: Factory Automation Systems, Atlanta, since Aug 2024; Georgia Tech graduate tutor before that. LR-B25 inbox check clean. [msg1 drafted 2026-09-05, MCP framing] soft_ask. Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude."

## Omnish Adroja

id: C132
name: Omnish Adroja
linkedin_url: https://www.linkedin.com/in/omnish-adroja-9ab329180/
linkedin_account: Izgin
company: Villonex Cryogenics
role: Founder & MD

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band: micro

assumptions_tested: [H0A1]
validation_rationale: >
  A one-year-old cryogenics manufacturer in Ahmedabad. Useful as the micro end of the H0A1 ladder:
  a founder building the process at the same time as the product notices the handoff in a way an
  established firm has already absorbed. His profile carries one line and no description, so
  expect a lower reply rate and treat any rate he gives as a founder's impression rather than a
  tracked number.

response_likelihood: 6
likelihood_factors: >
  1st degree (+3) · founder, so he carries the cost himself (+2) · the company is one year old and
  the profile is a single line, so there is little to ground a message in and little history to
  report (-2), start 3, capped at 6
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 by mining the LinkedIn export. Live profile read the same day: Villonex Cryogenics, Ahmedabad, since Oct 2025, one experience entry and no description. LR-B25 inbox check clean. [msg1 drafted 2026-09-05, MCP framing] soft_ask. Copy at outreach/copy/H1-H2-linkedin.md. UNSENT and NOT to be sent by Claude."

---

### Batch 2026-09-05 (c) — the rest of the export mine

## RP Singh

id: C133
name: RP Singh
linkedin_url: https://www.linkedin.com/in/rp-singh-b0428561/
linkedin_account: Izgin
company: Linoxy Cryogenic Solutions
role: Founder

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band: micro

assumptions_tested: [H0A1]
validation_rationale: >
  PARTIAL ICP match, recorded per LR-B12. Linoxy provides installation, commissioning, operation
  and maintenance plus project management for cryogenic equipment; it does not manufacture. So he
  can speak to the MECHANISM of a spec failing between design and the plant, and to what
  correcting it costs on site, but not to a manufacturer's rework rate. Four decades across
  National Dairy Development Board, Philips Cryogenics and Stirling Cryogenics, commissioning for
  BHEL, IGCAR and the Institute of Plasma Research, is unusually deep recall. Do not log anything
  he says as a manufacturer's base rate.

response_likelihood: 7
likelihood_factors: >
  1st degree (+3) · four decades in cryogenics and fourteen years running his own firm, so he has
  seen the handoff across employers rather than at one (+2) · commissioned bespoke plants for
  national research and power clients, which is one-off engineering by definition (+1) · Linoxy
  sells services and consultancy rather than manufacturing, so he is adjacent to the ICP rather
  than inside it (-1), start 3, capped at 7
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: target_customer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 by mining the LinkedIn export company-first against the H0A1 ICP. Live profile read the same day: Linoxy since Oct 2012 (14 yrs), Stirling Cryogenics 2002-2012, Philips 1989-2002, National Dairy Development Board 1979-1989. His own entry states more than four decades in cryogenics. LR-B25 inbox check clean (searched Singh; the Jagjit Singh and Jai Singhal threads are different people). Cryogenics is IMTEK's own industry, which is why this cluster went unnoticed for so long."

## Micah Zinnerman

id: C134
name: Micah Zinnerman
linkedin_url: https://www.linkedin.com/in/zinnerman/
linkedin_account: Izgin
company: Nordstern Automation
role: Managing Director

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: expert
role_pts: 2

tier: industry_software_vendor
size_band: micro

assumptions_tested: [H0A1]
validation_rationale: >
  EXPERT side, not a buyer. Nordstern is a consultancy taking robot and control cells from design
  through virtual commissioning to site acceptance, so what he can testify to is the MECHANISM
  across many customers, and it is the widest such view in the ledger. He cannot speak to any one
  manufacturer's economics and nothing he says should be logged as buyer pain. His
  virtual-commissioning and digital-twin work is also the closest thing in the network to what an
  MCP layer would have to interoperate with.

response_likelihood: 9
likelihood_factors: >
  1st degree and HE HAS ALREADY SAID YES (+4) · runs an integrator taking cells from design to
  site acceptance, so he sees the handoff at every customer rather than one (+2) · Tesla, KUKA,
  Raytheon and Gestamp commissioning behind him (+1) · his yes has sat unanswered for three weeks,
  which costs something (-1), start 3, capped at 9
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: msg2_sent
message_stage: msg2_sent
call_stage: asked_by_founder
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Backfilled 2026-09-05 during an export mine; the thread was never in this ledger. HE REPLIED 2026-08-14 AND IT IS STILL UNREAD: 'Thanks for reaching out. What you guys are working on sounds very promising; and I might add that you have a very impressive profile! I would be happy to answer your questions to the best of my ability.' That is an explicit yes that has gone unanswered for three weeks. Read from the conversation-list preview only; the thread was NOT opened, per the no-opening-unread rule. Live profile read 2026-09-05: Nordstern since Jun 2022, prior Micropsi Industries, Raytheon SPY-6, teamtechnik, Tesla Model 3, KUKA, Gestamp. His own entry reports inheriting an EV battery friction-stir-welding line with deformation risk and bringing it to above 98% acceptance. [msg2 drafted 2026-09-05] Arc stage 1, frequency and context, anchored on the last cell he commissioned rather than the general case. [msg2 sent 2026-09-05 18:41] Sent by the founder, closing on availability: "I am available 9am-9pm PDT time!". The three-week-old yes has finally been answered and a call is on the table."
## Vanessa McNiven

id: C135
name: Vanessa McNiven
linkedin_url: https://www.linkedin.com/in/vanessa-mcniven-54944941/
linkedin_account: Izgin
company: Institute for Manufacturing, University of Cambridge
role: Executive Course Director

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: influencer
role_pts: 1

tier: 
size_band: 

assumptions_tested: []
validation_rationale: >
  NOT A CUSTOMER and must never be logged as evidence. She is Executive Course Director of the
  MPhil the founder took, and was an Industrial Tutor on it for ten years before that. Her value
  is the ISMM industrial network, which places students inside UK manufacturers every year, and
  that is the population H0A1 needs. Her own background is Senior Body Engineer at Ford and
  Production Manager at Marconi Data Systems, so she can judge whether the problem is real before
  deciding who to point at. relationship_type is set to a non-customer value so she cannot enter a
  reply-rate denominator.

response_likelihood: 8
likelihood_factors: >
  1st degree and she ran the founder's own MPhil, which is the strongest shared context available
  (+4) · Ford body engineering and production management before academia, so she understands the
  problem rather than only the network (+1) · not a buyer and never will be, so the ceiling is
  referrals (0), start 3, capped at 8
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: peer_founder_competitor
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Found 2026-09-05 by mining the LinkedIn export. Live profile read the same day: Executive Course Director of MPhil ISMM since Nov 2022, Industrial Tutor on the same course 2012-2022, IfM Industrial Research Fellow 2001-2009, Ford Senior Body Engineer 1996-2000. LR-B25 inbox check clean. [msg1 drafted 2026-09-05] LR-B26 shape: the shared context REPLACES the research anchor, so the message does not name Cambridge at its own course director; it names ISMM, the research project and the DIAL group, which only someone who was there would produce. It volunteers the E26 finding rather than requesting one, and the ask is for names, not for her own answers."

## Mustafa Akin

id: C136
name: Mustafa Akin
linkedin_url: https://www.linkedin.com/in/mustafa-akin58/
linkedin_account: Izgin
company: Keystone Tile
role: Team Lead / Coordinator

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url:
signal_excerpt:

contact_role: practitioner
role_pts: 1

tier: 
size_band: 

assumptions_tested: []
validation_rationale: >
  OFF SCOPE, and recorded rather than dropped so a later sourcing pass does not rediscover him.
  The export made him look like a made-to-measure contact because Keystone Tile reads as a maker.
  The live profile says otherwise: his role description is a product and design team lead's, and
  his background is user-experience design at PepsiCo and DevMountain. The nearest manufacturing
  work is a four-month aircraft-equipment design contract in 2018. He fails the H0A1 icp_segment
  on both halves, company and role.

response_likelihood: 2
likelihood_factors: >
  Not scored for outreach; off_scope.
outreach_pattern:
degree: "1st"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant: soft_ask
relationship_type: field_practitioner
outreach_status: off_scope
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: checked
notes: "Screened 2026-09-05 from the export mine. Live profile read the same day. NOT drafted and NOT messaged. The failing evidence: Keystone Tile is a tile distributor, and his own role description names product managers, developers, user feedback and end-user experience, not manufacture."

## Glenn Charest

id: C137
name: Glenn Charest
linkedin_url: https://www.linkedin.com/in/glenncharest/
linkedin_account: Izgin
company: United CNC Machining
role: CEO and owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/glenncharest/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owns the shop and its P&L. Headline names aerospace, space, defence and naval work, which is low-rate per-order machining where every job is quoted, programmed and proved out on its own.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; recipient name "Glenn Charest" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Detroit Metropolitan Area. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Gabrielle Devroy

id: C138
name: Gabrielle Devroy
linkedin_url: https://www.linkedin.com/in/gabrielle-devroy-3332b444/
linkedin_account: Izgin
company: (AS9100 machine shop, name not in the search result)
role: Second-generation machine shop owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/gabrielle-devroy-3332b444/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Second-generation owner of an AS9100 shop. AS9100 means first article inspection on every new part number, which is the prove-out step H0A1 is about, and she carries the cost of it.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; recipient name "Gabrielle Devroy" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: St Clair, Michigan, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Stanley Evans

id: C139
name: Stanley Evans
linkedin_url: https://www.linkedin.com/in/stanley-evans-093367110/
linkedin_account: Izgin
company: SJS Machine
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/stanley-evans-093367110/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a shop doing CNC machining, fabrication, production parts and tooling and fixtures. A vendor to Toyota running fixtures and one-offs sees both ends of the handoff, and the headline mentions engineering change.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; recipient name "Stanley Evans" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Fayetteville, Tennessee, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Rick Rasmussen

id: C140
name: Rick Rasmussen
linkedin_url: https://www.linkedin.com/in/rick-rasmussen-6392941a/
linkedin_account: Izgin
company: (precision CNC shop, name not in the search result)
role: President

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/rick-rasmussen-6392941a/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs a precision CNC shop whose stated work is prototypes, components, devices and equipment. Prototype work is per-order by definition, so his shop has no repeat-run engineering to amortise.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Rick Rasmussen" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Brian Kippen

id: C141
name: Brian Kippen
linkedin_url: https://www.linkedin.com/in/brian-kippen-76037332/
linkedin_account: Izgin
company: KAD Models & Prototypes
role: CEO

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/brian-kippen-76037332/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs a model and prototype shop in Berkeley, 30 minutes from the founder. Every job is a one-off from a customer's file, which is the purest form of the per-order handoff, and he is close enough to visit.

response_likelihood: 7
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0) · Bay Area while the founder is in San Francisco (+1), start 3, capped at 7
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Brian Kippen" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Berkeley, California, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Everett Sharp

id: C142
name: Everett Sharp
linkedin_url: https://www.linkedin.com/in/everett-sharp-46b335142/
linkedin_account: Izgin
company: AusTex Machine & Design
role: Shop manager and co-owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/everett-sharp-46b335142/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Co-owner and shop manager at a machine and design shop, so he sits on both the design side and the floor side of the same handoff and can say where a job stops moving.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Everett Sharp" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Buda, Texas, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Scott Williams

id: C143
name: Scott Williams
linkedin_url: https://www.linkedin.com/in/scott-williams-75547230/
linkedin_account: Izgin
company: Velocity Custom Fabrication
role: Owner and VP of operations and engineering

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/scott-williams-75547230/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a custom fabrication shop holding both the operations and the engineering title. Custom fabrication is per-order work and he is the person who decides whether checking before release is worth paying for.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Scott Williams" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Tulsa, Oklahoma, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Chase Hettinger

id: C144
name: Chase Hettinger
linkedin_url: https://www.linkedin.com/in/chase-hettinger-13606a159/
linkedin_account: Izgin
company: Consolidated Precision Manufacturing
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/chase-hettinger-13606a159/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a precision manufacturing shop. Owner-operators are the only tier in this ICP who can answer both halves of the belief, what the errors cost and whether they would pay to remove them.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Chase Hettinger" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Chandler, Arizona, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Chelsea Sutton

id: C145
name: Chelsea Sutton
linkedin_url: https://www.linkedin.com/in/chelsea-sutton-8378943a/
linkedin_account: Izgin
company: Smith Metal LLC
role: Vice president and co-owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/chelsea-sutton-8378943a/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Co-owner of a CNC machining business. Carries the cost of a bad job directly, and the VP title means she is inside the quoting decision rather than downstream of it.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Chelsea Sutton" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Augusta, Michigan, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## John Shaw

id: C146
name: John Shaw
linkedin_url: https://www.linkedin.com/in/john-shaw-907670ba/
linkedin_account: Izgin
company: Progressive Machining & Fabrication
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/john-shaw-907670ba/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a shop that both machines and fabricates, so a single job can cross two processes inside his building before it is right, which is where per-order information gets lost.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "John Shaw" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Anderson, South Carolina, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Dave Ellis

id: C147
name: Dave Ellis
linkedin_url: https://www.linkedin.com/in/dave-ellis-5ab80950/
linkedin_account: Izgin
company: Ellis Design and Fabrication
role: Business owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/dave-ellis-5ab80950/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  The company name is design AND fabrication, so the design-to-machine handoff happens inside one small business he owns. That makes the cost of it visible to one person rather than split across departments.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Dave Ellis" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: San Tan Valley, Arizona, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Brian Bixler

id: C148
name: Brian Bixler
linkedin_url: https://www.linkedin.com/in/brian-bixler-7785b7a2/
linkedin_account: Izgin
company: Brandt Tool & Die Co., Inc.
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/brian-bixler-7785b7a2/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owns a tool and die shop. Tool and die is the extreme of one-off engineering: every die is designed, cut and tried out once, and the try-out is the prove-out step this assumption is about.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Brian Bixler" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Littlestown, Pennsylvania, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Zoltan Voros

id: C149
name: Zoltan Voros
linkedin_url: https://www.linkedin.com/in/zoltan-voros-06064327/
linkedin_account: Izgin
company: Vortool Manufacturing Ltd.
role: Owner and tool and diemaker

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/zoltan-voros-06064327/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner who still makes the tools himself. Someone who both quotes the job and cuts it can say what he found out about a part after the price had already gone out, without translating it through anyone.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Zoltan Voros" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Surrey, British Columbia, Canada. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Andrew Kurzrok

id: C150
name: Andrew Kurzrok
linkedin_url: https://www.linkedin.com/in/akurzrok/
linkedin_account: Izgin
company: Hopewell Sheet Metal Mfg.
role: President

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/akurzrok/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  President of a sheet metal manufacturer. Sheet metal jobs are cut from customer-supplied flat patterns, so a wrong or ambiguous file becomes scrap material rather than a rework, which sharpens the cost question.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Andrew Kurzrok" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Washington, DC, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Christopher Carlson

id: C151
name: Christopher Carlson
linkedin_url: https://www.linkedin.com/in/christopher-carlson-3665b2159/
linkedin_account: Izgin
company: Carlson Brothers Machining and Excavating LLC
role: Co-owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/christopher-carlson-3665b2159/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Co-owner of a small machining business. The smallest shops are where the per-order handoff is most obviously manual, because there is no ERP layer between the drawing and the machine.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Christopher Carlson" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Sharon, Wisconsin, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## WOJCIECH CWYNAR

id: C152
name: WOJCIECH CWYNAR
linkedin_url: https://www.linkedin.com/in/wojciech-cwynar-272aa658/
linkedin_account: Izgin
company: Hyde CNC Services Ltd
role: Business owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/wojciech-cwynar-272aa658/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner who was a CNC machinist-programmer before that, per his own past-role line. He has personally done the step the assumption is about and now carries its cost as the owner.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "WOJCIECH CWYNAR" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Hyde, England, UK. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Greg Ellis

id: C153
name: Greg Ellis
linkedin_url: https://www.linkedin.com/in/greg-ellis-127b7a183/
linkedin_account: Izgin
company: (own business, name not in the search result)
role: Business owner, mechanical engineer and machinist

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/greg-ellis-127b7a183/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Describes himself as owner, mechanical engineer and machinist in one line, which is the whole handoff inside one person. He can say which part of it actually takes the time.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Greg Ellis" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Youngstown-Warren area, Ohio, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Rick Hafner

id: C154
name: Rick Hafner
linkedin_url: https://www.linkedin.com/in/rickhafner/
linkedin_account: Izgin
company: CNC Machined Parts Depot
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/rickhafner/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a machined-parts business selling direct. Selling parts online means quoting from whatever a customer sends, which is the belief's link one arriving as a daily commercial problem.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Rick Hafner" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Travis Kemp

id: C155
name: Travis Kemp
linkedin_url: https://www.linkedin.com/in/travis-kemp-6a837b13b/
linkedin_account: Izgin
company: (own business, name not in the search result)
role: President and founder

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/travis-kemp-6a837b13b/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Founder-president whose listed skills are machining and 3D printing, so he runs per-order production across two processes. Company unidentified in the search result and must be established on the profile before any message.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Travis Kemp" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: South Lebanon, Ohio, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Li Hsu

id: C156
name: Li Hsu
linkedin_url: https://www.linkedin.com/in/li-hsu-95004636/
linkedin_account: Izgin
company: Custom Industrial Manufacturing Inc
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/li-hsu-95004636/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a company whose name is custom industrial manufacturing. Custom is the whole ICP in one word, and an owner can answer the willingness-to-pay half that H0A2 needs.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Li Hsu" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## EMRE YURTEMRE

id: C157
name: EMRE YURTEMRE
linkedin_url: https://www.linkedin.com/in/emryrtemr/
linkedin_account: Izgin
company: SELSA Makina
role: General manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/emryrtemr/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  General manager of a special machine design and CNC manufacturing firm. Special machine building is the segment E26 came from, and this is the second machine builder available to test whether the one-in-fifty rate is a property of the work or one manager's model.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "EMRE YURTEMRE" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Özgür DURSUN

id: C158
name: Özgür DURSUN
linkedin_url: https://www.linkedin.com/in/%C3%B6zg%C3%BCr-dursun-msc-b980bb72/
linkedin_account: Izgin
company: Poykal
role: General manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/%C3%B6zg%C3%BCr-dursun-msc-b980bb72/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  General manager of a precision machining firm serving aerospace and defence. Low-rate aerospace work is per-order with formal first article inspection, and the GM owns the schedule that inspection sits in.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Özgür DURSUN" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Istanbul, Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Tacettin ŞAL

id: C159
name: Tacettin ŞAL
linkedin_url: https://www.linkedin.com/in/tacettinsal/
linkedin_account: Izgin
company: ŞAL Makina
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/tacettinsal/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a precision CNC machining and engineering business. Turkish-speaking owner, which lets the conversation run in the founder's own language once ICP fit is already established.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Tacettin ŞAL" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Ahmet Çakın

id: C160
name: Ahmet Çakın
linkedin_url: https://www.linkedin.com/in/ahmet-%C3%A7ak%C4%B1n-71832352/
linkedin_account: Izgin
company: Phoenix Tooling Limited
role: Company owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/ahmet-%C3%A7ak%C4%B1n-71832352/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owns a tooling company. Tooling is engineered once per job and proved out once, so the error and the hours land on the same person who quoted it.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Ahmet Çakın" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Ankara, Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Serdar Alper

id: C161
name: Serdar Alper
linkedin_url: https://www.linkedin.com/in/serdar-alper-78031728/
linkedin_account: Izgin
company: Damen Shipyards, Workboats Division
role: Manufacturing engineering manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/serdar-alper-78031728/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: machine_builder
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Manufacturing engineering manager at a shipyard workboats division. Ships are project-based one-offs and the ICP note explicitly keeps project-based plant and one-off build shops in scope.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Serdar Alper" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## İbrahim Alper Ozan

id: C162
name: İbrahim Alper Ozan
linkedin_url: https://www.linkedin.com/in/ibrahim-alper-ozan-b695a03b/
linkedin_account: Izgin
company: (not in the search result)
role: Manufacturing engineering manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/ibrahim-alper-ozan-b695a03b/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Manufacturing engineering manager, the role that owns the drawing when it reaches the floor. Employer is not visible in the search result and has to be established on the profile before any message.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Ankara, Türkiye. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Simon (Xiao Long) Jiang

id: C163
name: Simon (Xiao Long) Jiang
linkedin_url: https://www.linkedin.com/in/xiaolongjiang/
linkedin_account: Izgin
company: (not in the search result)
role: CNC programming manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/xiaolongjiang/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs the programming group, which is the exact seat Shane Duncan (C125) sits in and the one that can say whether a program that looks right still needs a person at the machine.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Elgin, Illinois, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Adriaan Te Brugge

id: C164
name: Adriaan Te Brugge
linkedin_url: https://www.linkedin.com/in/adriaantebrugge/
linkedin_account: Izgin
company: (not in the search result)
role: Machine shop manager and senior CNC programmer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/adriaantebrugge/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Both shop manager and senior programmer, so he sees a new part from the file arriving to the first good one coming off, without handing it to anyone else.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Canada. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Daniel Schimke

id: C165
name: Daniel Schimke
linkedin_url: https://www.linkedin.com/in/daniel-schimke-6494aa97/
linkedin_account: Izgin
company: Specialized Bicycle Components
role: R&D machine shop manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/daniel-schimke-6494aa97/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs an R&D machine shop, where every part is a one-off from a designer's model and nothing is ever re-run. Ninety minutes from the founder while he is in San Francisco.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0) · Bay Area while the founder is in San Francisco (+1), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Santa Cruz, California, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Emily Coker

id: C166
name: Emily Coker
linkedin_url: https://www.linkedin.com/in/emily-coker/
linkedin_account: Izgin
company: Axon
role: Senior machinist and shop manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/emily-coker/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Manages an in-house shop making one-offs for a product company, and is local to the founder. In-house shops carry the handoff cost internally, which is a different accounting from a job shop and worth contrasting.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0) · Bay Area while the founder is in San Francisco (+1), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Oakland, California, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Kassandra Nguyen

id: C167
name: Kassandra Nguyen
linkedin_url: https://www.linkedin.com/in/knguyen91939/
linkedin_account: Izgin
company: Simbe Robotics
role: Mechanical engineer and shop manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/knguyen91939/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Designs the part AND runs the shop that makes it, at one company, in the founder's own city. She is the single clearest test of whether the handoff still costs anything when both ends are the same person.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0) · Bay Area while the founder is in San Francisco (+1), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: San Francisco Bay Area, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## March Tighe

id: C168
name: March Tighe
linkedin_url: https://www.linkedin.com/in/marchtighe/
linkedin_account: Izgin
company: (not in the search result)
role: Operations manager, trades shops and facilities

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/marchtighe/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Operations manager over machining, prototyping and lab fit-out work. Employer not visible in the search result; the role sits across several one-off shops at once, which is where the same-or-different question gets a real answer.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Shawn N.

id: C169
name: Shawn N.
linkedin_url: https://www.linkedin.com/in/shawn-n-a7b367103/
linkedin_account: Izgin
company: (not in the search result)
role: Engineering manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/shawn-n-a7b367103/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Engineering manager whose listed skills are computer numerical control. Employer is not visible in the search result and must be established before any message is written.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: North Hartland, Vermont, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Rajveer Yadav

id: C170
name: Rajveer Yadav
linkedin_url: https://www.linkedin.com/in/rajveer-yadav-a977b1148/
linkedin_account: Izgin
company: (not in the search result)
role: Production manager, machine shop operations

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/rajveer-yadav-a977b1148/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Production manager over machine shop operations, so the queue between a job arriving and a good part existing is his to explain.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: India. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Rob Russell

id: C171
name: Rob Russell
linkedin_url: https://www.linkedin.com/in/rob-russell-008565a2/
linkedin_account: Izgin
company: PGI Steel
role: Machine shop manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/rob-russell-008565a2/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs the machine shop inside a steel business, where jobs arrive per order from other departments and customers rather than from a repeat production schedule.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Odenville, Alabama, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Jeremy Bellanti

id: C172
name: Jeremy Bellanti
linkedin_url: https://www.linkedin.com/in/jeremy-bellanti-9a429768/
linkedin_account: Izgin
company: American Axle
role: Manager of manufacturing prototype operations

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/jeremy-bellanti-9a429768/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs prototype operations inside a large automotive supplier. Prototypes are the per-order island inside a high-volume company, which makes him the one person there who is in scope while the rest of the plant is explicitly out.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Brighton, Michigan, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Oliver Smith

id: C173
name: Oliver Smith
linkedin_url: https://www.linkedin.com/in/oliver-j-smith/
linkedin_account: Izgin
company: (not in the search result)
role: NPI and manufacturing engineer, CNC programmer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/oliver-j-smith/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Holds all three roles the handoff passes through, new product introduction, manufacturing engineering and programming, so nothing about the handoff is second-hand to him.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: UK. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Jagannath Rao

id: C174
name: Jagannath Rao
linkedin_url: https://www.linkedin.com/in/jagannath-rao-091b53a1/
linkedin_account: Izgin
company: (not in the search result)
role: Senior production engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/jagannath-rao-091b53a1/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Fifteen years of CNC programming across mill-turn, VMC and HMC by his own headline. Long tenure at the machine is what makes a rate answer recall rather than estimate.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: India. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Jeff Brackus

id: C175
name: Jeff Brackus
linkedin_url: https://www.linkedin.com/in/brackusj/
linkedin_account: Izgin
company: Advanced Precision Machining, Inc.
role: General manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/brackusj/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  General manager of a precision machining company, so he owns the schedule and the labour cost of a job that has to be fixed on the floor.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Jeff Brackus" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Meridian, Idaho, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## William Ellison

id: C176
name: William Ellison
linkedin_url: https://www.linkedin.com/in/william-ellison-6998174b/
linkedin_account: Izgin
company: Precision Grinding Industries, Inc
role: General manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/william-ellison-6998174b/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  General manager of a precision grinding business. Grinding is the last operation before a part is accepted, so a mistake found there has already had every earlier operation paid for.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "William Ellison" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Piedmont, South Carolina, US. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Fatih Bıyıklı

id: C177
name: Fatih Bıyıklı
linkedin_url: https://www.linkedin.com/in/fatihbiyikli/
linkedin_account: Izgin
company: Impro Industries Mexico
role: General manager

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/fatihbiyikli/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  General manager of a precision machining plant. Higher volume than most of this batch, which is useful as the boundary case: the ICP excludes repeat production, so his answer says where the line actually falls.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Fatih Bıyıklı" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: San Luis Potosí, Mexico. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Mike Zhang

id: C178
name: Mike Zhang
linkedin_url: https://www.linkedin.com/in/mike-zhang-355688210/
linkedin_account: Izgin
company: HuanYi Precision
role: Founder and owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/mike-zhang-355688210/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Founder-owner of a CNC machining business quoting international customers from their files, which is the handoff at its most remote and least forgiving.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
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
found_date: 2026-09-05
invited_date: 2026-09-05
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite sent 2026-09-05] Bare connection request, no note (LR-B29). Sent by Claude via linkedin.com/preload/custom-invite; name "Mike Zhang" verified in the invitation modal against the ledger before clicking. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: China. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Linda S

id: C179
name: Linda S
linkedin_url: https://www.linkedin.com/in/lindashan/
linkedin_account: Izgin
company: Dongguan Sibai Metal Works Ltd.
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/lindashan/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a customised precision CNC machining works. Customised is the qualifier that keeps her in scope where a volume contract manufacturer would not be.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [invite UNCERTAIN 2026-09-05] The browser extension disconnected on the batch that would have sent this invite. The modal for "Linda (单艳娇) S" was confirmed open and named correctly, but the send click and the disconnect cannot be ordered from here. Status left `pending`. CHECK LinkedIn sent-invitations before re-sending - a duplicate invite is visible to the recipient. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Dongguan, China. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Howard Chen

id: C180
name: Howard Chen
linkedin_url: https://www.linkedin.com/in/founfacthoward/
linkedin_account: Izgin
company: FounFact INC.
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/founfacthoward/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner whose About text is about production processes. Asia-based owners quote almost entirely from files with no site visit, which is the strongest form of the remote handoff.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Taipei, Taiwan. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Aakash Vekariya

id: C181
name: Aakash Vekariya
linkedin_url: https://www.linkedin.com/in/aakash-vekariya-16992b15b/
linkedin_account: Izgin
company: CNC Works
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/aakash-vekariya-16992b15b/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Company owner in CNC machining. Included to keep the batch from being entirely North American and European, since the belief claims the economics are structural rather than regional.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Surat, Gujarat, India. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Candy Jin

id: C182
name: Candy Jin
linkedin_url: https://www.linkedin.com/in/candy-jin-%F0%9F%87%BA%F0%9F%87%B8-6a6b421a4/
linkedin_account: Izgin
company: InnoX Tech
role: Founder and CEO

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/candy-jin-%F0%9F%87%BA%F0%9F%87%B8-6a6b421a4/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: job_shop_fabricator
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Runs a rapid prototype business spanning CNC, 3D printing and sheet metal. Rapid quoting from customer files is her core operation, though the sales-facing headline means the profile needs a careful read before any claim.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: US and China. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Thilina Bowatta

id: C183
name: Thilina Bowatta
linkedin_url: https://www.linkedin.com/in/thilinabowatta/
linkedin_account: Izgin
company: (not in the search result)
role: New product development engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/thilinabowatta/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  New product development engineer, the person who hands the design over. He can say what he sends the shop and what comes back as a question, which is the customer side of the same handoff.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: West Gosford, New South Wales, Australia. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Yassine Saidat

id: C184
name: Yassine Saidat
linkedin_url: https://www.linkedin.com/in/yassine-saidat-33165b7a/
linkedin_account: Izgin
company: (not in the search result)
role: Supplier quality and NPI engineer

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/yassine-saidat-33165b7a/
signal_excerpt:

contact_role: practitioner
role_pts: 2

tier: manufacturing_operations
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Supplier quality and new product introduction across aerospace and automotive, so he sees first article failures across many suppliers rather than one shop. Weakest fit in the batch: he audits the handoff rather than carrying its cost.

response_likelihood: 5
likelihood_factors: >
  2nd degree, invite needed (0) · inside the handoff daily so reports what happens rather than what is decided (+2) · profile_fit signal (0), start 3, capped at 5
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: UK. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."

## Charles Khairallah

id: C185
name: Charles Khairallah
linkedin_url: https://www.linkedin.com/in/charles-khairallah-9936704/
linkedin_account: Izgin
company: Robotics Design Inc
role: Owner

signal_type: profile_fit
signal_multiplier: 1.0
signal_source_url: https://www.linkedin.com/in/charles-khairallah-9936704/
signal_excerpt:

contact_role: buyer
role_pts: 3

tier: machine_builder
size_band:

assumptions_tested: [H0A1]
validation_rationale: >
  Owner of a custom robotics design and build house, which is design-to-order machine building rather than a product line. Borderline against the ICP's exclusion of robotics startup founders: this is an established design firm, not a startup, and that has to be confirmed on the profile before any message.

response_likelihood: 6
likelihood_factors: >
  2nd degree, invite needed (0) · owner or general manager so can answer both the cost and the willingness to pay (+3) · profile_fit signal (0), start 3, capped at 6
outreach_pattern:
degree: "2nd"
mutuals_count:
active_last_30d: unknown
open_to_work: false

close_variant:
relationship_type: operator_buyer
outreach_status: pending
message_stage:
call_stage: none
found_date: 2026-09-05
invited_date:
accepted_date:
scheduled_date:
interview_date:

interviews: []

evidence_score:
outcome_modifier:
prior_contact_status: pending
notes: "[UNVERIFIED 2026-09-05] No live profile read exists for this contact. Screened on company and title only, which the H0A1 icp_verification_rule now says is not enough — the invite went out before that rule existed. DO NOT draft or send a DM off this card: read the profile first and confirm the vertical, the production shape, the function and the tenure, then record what it showed here. [sourced 2026-09-05] H0A1 batch, LinkedIn people search restricted to 2nd degree, Pass 4 Phase B. Name, headline and location are SEARCH RESULT facts only; the profile was NOT opened, so degree, current employer and title must be re-verified live before any message is written (LR-B6, LR-B25). Location as listed: Montreal, Quebec, Canada. Pass 1 against the founder's own export returned nothing for this ICP, so every contact in this batch is cold. NOT YET INVITED: the founder sends every invite by hand, bare, with no note (LR-B29)."
