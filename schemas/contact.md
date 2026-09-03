# Schema: Contact Card

One row per contact in `reports/{slug}/outreach/contacts.md`. Contacts are scoped per idea
but a single contact can be linked to multiple assumptions over time — relationships
compound.

## File layout

`outreach/contacts.md` is a single living markdown file with one YAML block per contact
under a `## <Contact Name>` heading. Frontmatter at the top of the file:

```yaml
---
idea: example-idea
last_updated: 2026-07-08
totals:                       # rolled up across all contacts
  targeted: 0
  invited: 0
  accepted: 0
  scheduled: 0
  done: 0
  no_reply: 0
---
```

## Contact block format

```yaml
## Sarah Chen

id: C1                                # C{N}, monotonic across the file
name: Sarah Chen
linkedin_url: https://www.linkedin.com/in/sarah-chen-example/
linkedin_account: Izgin              # which founder's LinkedIn account this contact lives on —
                                      # a name listed in founders/. Determines whose export/inbox/session
                                      # this contact is reachable through and who sends the message.
                                      # Set at contact creation; never inferred from degree alone,
                                      # since "1st degree" is meaningless without saying to whom.
company: Example Corp
role: Operations Manager

signal_type: post_engagement           # post_engagement | comment_signal | job_posting | profile_fit
signal_multiplier: 1.5                # derived from signal_type — see multipliers below
signal_source_url:                    # URL to the exact post / job / comment
signal_excerpt: >                     # verbatim quote from the source, if applicable
  "The existing tools just don't cut it for the part of the job that actually
  matters — we're still doing that step by hand."

contact_role: practitioner            # buyer | practitioner | expert | influencer
role_pts: 2                           # derived — see points below

tier: isp                             # MUST be one of the tier names this assumption declared in
                                      # its `icp_valid_tiers` (idea-defined — NOT a fixed enum).
                                      # Every tier belongs to a structural side (demand | supply |
                                      # competitor | expert); that side is the only thing the
                                      # pipeline routes on. `other` is the fallback for off-scope.
                                      # tier reflects where their COMPANY sits in the value chain being tested
                                      # (a Head of Operations at an asset owner → the demand-side tier;
                                      #  a Head of Service at an independent provider → a supply-side tier)
                                      # contact_role is about them as an individual signal source;
                                      # tier is about their org's position in the market

size_band: micro                      # OPTIONAL, and orthogonal to tier. tier says WHERE in the
                                      # value chain their company sits; size_band says HOW BIG it is.
                                      # Band names are idea-defined, declared in that idea's graph.md
                                      # frontmatter under `size_bands` (NOT a fixed enum here) — the
                                      # bands come from that idea's own market sizing.
                                      # Set it from an observable: the company's LinkedIn headcount
                                      # range. Leave EMPTY rather than guessing — an unbanded contact
                                      # is visible, a wrongly banded one silently corrupts any
                                      # per-band reply-rate comparison.
                                      # Why it exists: a contact list can pass every ICP check and
                                      # still sample only the bottom of a market. Banding is what
                                      # makes "we tested the whole market" checkable instead of
                                      # asserted.

assumptions_tested: [A2]              # list of assumption IDs from graph.md — the ONE author
                                      # for which assumptions this contact tests. There used to
                                      # be a second, `validates_assumption`, constrained to
                                      # "must match one entry in assumptions_tested"; it was
                                      # written on every contact, read by nothing, and had
                                      # already gone stale on four of them (dropped 2026-08-09).
                                      # A contact that should not count as demand is marked with
                                      # relationship_type, which the funnel actually reads.
validation_rationale: >               # WHY this specific person can validate those specific
                                      # assumptions. If empty or vague ("adjacent, might
                                      # help"), the contact SHOULD NOT have been added.
                                      # Example: "Head of Operations at a target operator — sees the
                                      # recurring cost on an operating budget she owns; can directly
                                      # confirm or contradict the $100-300k/site/year claim."

response_likelihood: 7                # 1-10 JUDGEMENT, higher = more likely to accept + reply.
                                      # Not computed: see "Response likelihood scoring" below.
likelihood_factors: >                 # the terms behind that judgement — REQUIRED whenever a score
                                      # is set, because the score is not reproducible without it
  post_engagement (+3) · 2nd degree (+2) · open_to_work (+2)
channel: linkedin                     # vocab:outreach_channel. How this contact was REACHED.
                                      # Defaults to `linkedin` when absent, so existing cards
                                      # need no backfill. The conversion funnel is computed
                                      # PER CHANNEL: a phone contact who answered the phone is
                                      # not a LinkedIn reply, and counting the two together
                                      # produced a 100% reply rate on 2026-09-03.
outreach_pattern:                     # optional cluster tag; currently unused post outreach-strategy retirement.
                                      # startup-outreach-check now buckets replies by signal_type + degree.
                                      # Left in schema for backwards-compat with existing rows; safe to leave empty.
degree:                               # 1st | 2nd | 3rd+ | inmail_only — relative to linkedin_account,
                                      # NOT a network-wide fact (from LinkedIn search result)
mutuals_count:                        # integer or empty (visible on search results / profile)
active_last_30d:                      # true / false / unknown (posted or reacted publicly in last 30 days)
open_to_work: false                   # true / false (visible on profile)

# A contact carries at most a `signal_excerpt` plus a `validation_rationale`.
# Hook material for copy lives on the company entry in `companies.md`, not here —
# a nested per-source hook block on the contact was tried and deleted: it was shaped
# around one vertical's data sources and shipped as empty strings on every contact.

close_variant:                        # direct_question | soft_ask  — set at DRAFT time by
                                      # startup-outreach-draft, never guessed later.
                                      # direct_question = the message ends on a concrete question about a
                                      #   specific past event ("on your last one, what ate the most time?")
                                      # soft_ask        = the message ends on a low-commitment permission ask
                                      #   ("would you be open to a few questions?")
                                      # startup-outreach-check buckets reply rates on this field.
                                      # WARNING: keep it crossed against seniority. If soft_ask only ever goes
                                      # to senior contacts and direct_question only to ICs, the two variables
                                      # are confounded and neither reply rate means anything on its own.

relationship_type:                    # optional routing/classification label, e.g.
                                      # operator_buyer | data_supplier_practitioner |
                                      # peer_founder_target | peer_founder_competitor |
                                      # peer_founder_integrator | peer_founder_expert
                                      # A peer founder can still be a target or expert, but a
                                      # peer_founder_competitor must be separated from buyer
                                      # evidence and customer conversion analysis.
outreach_status: pending              # pending | invited | accepted | replied | scheduled | done | no_reply | declined | off_scope | held
message_stage:                        # optional audit detail: msg1_sent | msg2_sent
call_stage:                           # none | offered_by_contact | asked_by_founder | scheduled | completed
                                      # Call progression is reported separately from confirmed
                                      # scheduling. `offered_by_contact` and `asked_by_founder`
                                      # must never silently promote outreach_status to scheduled.
found_date: 2026-07-08                # when the target row was created
invited_date:                         # when the invite was sent
accepted_date:                        # when they accepted the invite
scheduled_date:                       # when the interview was booked
interview_date:                       # when the call actually happened

interviews: []                        # relative paths to interview note files
                                      # e.g. ["03-validation/A2-2026-07-08/interviews/sarah-chen-2026-07-15-notes.md"]

evidence_score:                       # cumulative score contributed by this contact
outcome_modifier:                     # last classified outcome — strong_confirm | moderate_confirm | weak | contradiction
notes: ""
```

## Signal multipliers (derived from signal_type)

| signal_type       | multiplier | Meaning                                            |
|-------------------|------------|----------------------------------------------------|
| `post_engagement`  | 1.5        | Publicly posted about the exact pain               |
| `comment_signal`  | 1.25       | Commented on a relevant post or competitor thread  |
| `job_posting`     | 1.1        | Their org posted a role that reveals the pain      |
| `profile_fit`     | 1.0        | Right role / company / segment; no active signal   |

Multiplier is set at contact creation time by whichever `startup:outreach-targets` path
found them. Never edited manually.

## Contact role points (derived from contact_role)

| contact_role     | points | What they can validate                                  |
|------------------|--------|---------------------------------------------------------|
| `buyer`          | 3      | Budget, procurement path, willingness to pay            |
| `practitioner`   | 2      | Pain reality, frequency, workarounds                    |
| `expert`         | 2      | Market dynamics, timing, competitive landscape          |
| `influencer`     | 1      | Referrals to real buyers/practitioners; not primary     |

## Evidence score formula

Per interview:
```
score = (role_pts × signal_multiplier) + outcome_modifier
```

Outcome modifiers:
- `strong_confirm`: +1
- `moderate_confirm`: 0
- `weak`: −0.5
- `contradiction`: −1

`evidence_score` on the contact card is the cumulative sum across all interviews with that
contact (usually 1, occasionally 2+ if they were called back for a different assumption).

## Status lifecycle

```
pending → invited → accepted → replied → scheduled → done
   ↓             ↓            ↓
 off_scope    declined     no_reply
(our audit)   (their       (accepted
              LinkedIn      but silent)
              action)
```

- `pending` — target list row, invite not yet sent
- `invited` — invite dispatched by the founder
- `accepted` — connection accepted on LinkedIn
- `replied` — substantive reply received (set by `startup-outreach-check`)
- `declined` — the contact declined the invite ON LINKEDIN (their action; set only by
  `startup-outreach-check` on confirmed negative reply with founder confirmation)
- `held` — ICP-VALID but deliberately not contacted in this campaign (our action; set by
  LR-B30). Added 2026-09-02. It exists because `no_reply` was being used for this and
  `no_reply` counts as *contacted* in the funnel, so eleven people who were never messaged
  for the active assumption were reported as a 29% contact rate. `held` is NOT a contacted
  status and never enters a reply-rate denominator. Every `held` contact carries a reason
  and, where the block is temporal, the date it becomes eligible again.
- `off_scope` — OUR ICP audit rejected them (our action; set by `startup-outreach-targets`
  during audit, ONLY when a mandatory `notes:` rationale is written explaining which ICP
  field failed and what the profile visit revealed)
- `scheduled` — interview booked
- `done` — interview complete AND capture skill has run
- `no_reply` — accepted but never replied to interview ask

**`declined` vs `off_scope` — do not conflate:**
- `declined` = their action (invite refused / negative reply)
- `off_scope` = our action (audit says wrong fit)

Silent status flips are prohibited. Any change to `outreach_status` must either (a) come
from a documented skill flow or (b) leave a `notes:` audit trail entry describing the
reason.

Only contacts with `outreach_status: done` contribute to the assumption's cumulative
score.

## Tier definitions — idea-defined, not a fixed enum

`tier` reflects the contact's org position in the value chain. Distinct from `contact_role`
because a "buyer" at a demand-side org is fundamentally different from a "buyer" at a
supply-side org — different budget structures, different pain visibility, different sales cycle.

**The tier vocabulary is declared per idea, in each assumption's `icp_valid_tiers`.** The
framework hardcodes no industry-specific tier names. What *is* universal is the **structural
side** every tier belongs to — that is the only thing the pipeline routes on:

| side         | Meaning                                                        | Example tier names (idea-defined) |
|--------------|----------------------------------------------------------------|-----------------------------------|
| `demand`     | Owns the pain / holds the budget (operator, owner, end-buyer)  | `enterprise_buyer`, `smb_operator`, `procurement_lead` |
| `supply`     | Does the work / sells the service for hire                     | `service_provider`, `contractor`, `distributor` |
| `competitor` | Building the same thing — captured separately, not outreached  | `competitor` |
| `expert`     | Consultant / ex-operator / analyst / academic (not at a target org) | `expert` |
| —            | Fallback for off-scope companies                               | `other` |

`tier` is set at contact creation time by `startup:outreach-targets`, drawn from the company's
role in the ecosystem — mapped to whichever tier the *active assumption declared* on the
matching side. Not derived from title: the same person can be a demand-side tier at an operator
or a supply-side tier at a service provider, depending on where their org sits.

## Response likelihood scoring

Every contact gets a `response_likelihood` 1-10 score, set when the contact is added and
updated by any skill that enriches the profile.

**This is a judgement, not a computation — do not treat the terms below as a formula.**
They are the standard opening prior:

```
start at 3
  signal:      post_engagement +3 · comment_signal +2 · job_posting +1 · profile_fit 0
  degree:      1st +3 · 2nd +2 · 3rd+ 0 · inmail_only −2
  warmth:      open_to_work +2 · active_last_30d +1 · dormant −1
  mutuals:     5+ +2 · 1-4 +1 · 0 0
  affiliation: shared alumni / nationality / employer, per founders/*.md +1
```

Measured against the live ledger on 2026-08-09, those terms reproduce **66 of 125** scores
exactly; the rest carry judgements the terms have no slot for — buyer seniority, a signal
decayed by age, "senior and busy", or a contact who had already replied unprompted. That is
not drift to be corrected: it is the scorer knowing something the terms don't encode. The
schema previously presented this as a formula, which made every one of those 59 scores look
like an error and invited a future session to "fix" them by recomputing.

So: adjust freely, but **`likelihood_factors` must name every term you used, including the
ones invented for that contact** — it is the only author of why a score is what it is, and
without it the number cannot be defended or recalibrated. Record only what was actually
observed, never data not yet gathered; where enrichment hasn't run, leave the warmth and
mutuals fields `unknown` and say so in the factors. A stale score after enrichment is a bug.

| Score | Meaning |
|-------|---------|
| 8-10 | High priority — warm signal + strong degree + active |
| 5-7 | Mid — worth messaging, expect a normal cold rate |
| 3-4 | Low — include but deprioritize; likely cold `profile_fit` |
| 1-2 | Skip or defer — InMail-gated, no signal, dormant |

**How the founder uses it:**
- Sort tracker by likelihood descending
- Send invites to the top 5-10 first
- Compare reply-rate at 9/10 tier vs 5/10 tier to calibrate the formula for future runs

## Outreach pattern (legacy field)

`outreach_pattern` was written by a retired strategy skill to cluster contacts by angle.
That skill is gone; `startup-outreach-draft` now figures out the angle per-contact from
`signal_type` + `contact_role` + the strongest `profile_fit_signal`, so the field is no
longer written on new rows.

The field remains in the schema because ~220 legacy rows on the active idea still carry
values. `startup-outreach-check` now buckets replies by `signal_type` + `degree` (cold vs.
warm vs. hot-signal) rather than by pattern. Safe to leave empty on new contacts.

## Deduplication rules

Before adding a new contact row, `startup:outreach-targets` MUST check that
`linkedin_url` is not already present in this file. If it is, the existing row is
updated (append the new `assumption_id` to `assumptions_tested`) rather than duplicated.
