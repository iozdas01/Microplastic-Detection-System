---
name: startup-outreach-draft
description: >-
  Drafts one grounded LinkedIn DM per contact from a LIVE profile snapshot, then logs it. First invites NEVER carry copy (LR-B29): a 2nd/3rd-degree first touch is a bare connection request with no note, so this skill drafts only DMs — to 1st-degree contacts, to accepted connections (the post-acceptance Msg 1), and to Open Profiles. Give it a profile URL (or several, or point it at accepted/1st-degree contacts) and it pulls the real profile, checks ICP fit against the active assumption, writes the message, and records it in contacts.md plus the copy archive with a claim-by-claim traceability table. It never sends messages — the founder sends every message by hand. Use this whenever the user pastes a LinkedIn profile and wants a message, asks "what should I write to this person", "draft outreach", "message for A2", "someone accepted, what do I say", or wants existing draft copy checked against the copy rules. Also use it to prepare messages in bulk for manual sending.
---

# Startup Outreach Draft

Turn a LinkedIn profile into one message that proves a human read that profile, and leave
behind a record of why every claim in it is true.

The founder sends. This skill drafts and logs. That division is the whole design: a message
that leaves the account is irreversible and lands on a real person, so the human who owns
the relationship makes that call, every time, with the message in front of them.

## Load first

1. `schemas/copy-rules.md` — mandatory, read every `LR-*` rule before drafting. These
   are founder-taught and reply-backed; they outrank anything in this file. Highest
   authority: **LR-B1** (title → observable activity), **LR-B2** (research statement is a
   puzzle), **LR-B6** (claims must be live-snapshot verifiable), **LR-B7** (ICP fit before
   drafting), **LR-B11** (no money question early), **LR-B12** (partial ICP match),
   **LR-B18** (permission ask, not the question), **LR-B19** (the research
   anchor, per-sender via LR-B23), **LR-B20** (never contact investors), **LR-B23** (anchor
   is per-sender, not universal), **LR-B24** (no cliché phrases), **LR-B25** (check the
   sending account's inbox before drafting a Msg 1), **LR-B28** (the research frame is
   PER-SEGMENT — data post-processing for robot builders, what goes wrong on the line for
   manufacturing; never one house frame across a batch, and never the assumption restated).
   *Rule IDs keep the `LR-B*` prefix: they are cited across existing `contacts.md` notes
   and copy archives, so renumbering would orphan those references.*

   **Read it to the end, every run.** Skimming produces drafts that look rule-compliant
   and are not — the close rules and the anchor rules have both been missed that way.
2. `founder.md` **and every profile it points at** under `founders/` — the shared-affiliation
   opener (LR-B19) and `affiliation_boost` are driven by each founder's `affiliations` and
   `affiliation_scoring` blocks, and those live in `founders/{name}.md`, NOT in `founder.md`
   itself. `founder.md` is only an index of the two co-founders. Grepping it alone returns
   nothing and looks exactly like "no school recorded" — founder-caught, after a
   batch omitted a legitimate Georgia Tech opener on that false reading. the sending founder currently
   carries `cambridge_match: +1` and `georgia_tech_match: +1`.
   Per `founder.md`, write from whichever founder holds the genuine affinity, and never
   reference one founder's affiliation in a message sent as the other.
3. `reports/{slug}/02-assumptions/graph.md` — the active assumption, its `icp_segment`,
   `icp_valid_tiers`, `icp_valid_titles`, `icp_out_of_scope`, and domain vocabulary.
4. `reports/{slug}/outreach/contacts.md` — existing contacts, for dedup and history.
5. `reports/{slug}/outreach/copy/{A_ID}-linkedin.md` — prior messages to this person and
   the frame already established with them.
6. `reports/{slug}/outreach/blast-templates.md` — OPTIONAL. Per-idea locked templates if
   they exist. Absent is fine; draft from the rules and the assumption directly.

If `graph.md` is missing, stop and say so. Everything downstream depends on knowing which
assumption the message is trying to test, and guessing produces confident nonsense.

If `contacts.md` is missing, create it with the frontmatter from `schemas/contact.md`.
That is a first run, not an error.

## Identify the idea and assumption

Get the idea slug from the founder's message or the working context. Read `graph.md`
frontmatter for `active_assumption` — that is the assumption the message serves unless the
founder names a different one.

State both back in one line before drafting, so a wrong idea gets caught before ten
messages are written against it:

> Drafting for `{slug}` · assumption `{A_ID}` · ICP: {one-line icp_segment summary}

## Modes

**Single contact** — founder pastes one profile URL. Default. Highest quality per message.

**Batch** — founder pastes several URLs, or asks for draftable contacts from `contacts.md`.
Run the identical per-contact pipeline on each, then present one review table. Batch changes
the presentation, never the verification: every contact still gets its own live snapshot and
its own traceability check. Skipping that is how a message ends up claiming someone works
somewhere they left a year ago.

For batch from `contacts.md`, take contacts where `outreach_status: accepted`, plus
`pending` contacts at 1st degree (already connected, DM-able now), sorted by
`response_likelihood` descending. Pending 2nd/3rd-degree contacts are NOT draft targets —
they get a bare invite (LR-B29) and become draftable on acceptance. Default to 10 per run
unless the founder says otherwise — past that, quality drops and the review table stops
being readable.

## Browser pre-flight

Load the chrome tools in ONE `ToolSearch` call:

```
select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp
```

Then call `tabs_context_mcp` once to get a tab id.

If a profile redirects to `/login`, the founder's session has expired. Pause:

> LinkedIn is asking for a login. Log in in that tab and say 'ready' — I'll pick up where I left off.

Never handle credentials. Never attempt to log in.

## What this skill never does

**It never sends, and it never touches a send control.** No clicking Connect or Invite, no
opening the connection modal, no filling the note textbox, no clicking Send or Message. The
browser is used strictly read-only: navigate and read.

This is stricter than the old rule, which allowed preparing a modal for the founder to
confirm. That was still Claude clicking an affordance on a live social account, and the
failure mode was ugly — a loose selector hitting a "People also viewed" card and preparing
an invitation to the wrong person entirely. Reading only makes that class of error
impossible. The founder copies the message and sends it themselves.

If the founder asks this skill to send, say plainly that it drafts and logs only, and hand
them the message to send.

## Also not this skill

- Finding contacts → `/startup-outreach-targets`
- Checking who replied → `/startup-outreach-check`
- Drafting a reply to someone who has already responded → `/startup-outreach-reply`
- Turning a completed conversation into evidence → `/startup-interview-capture`

The boundary with `/startup-outreach-reply` is the reply itself: if the contact has sent a
substantive message, that skill owns the response because it grounds the draft in what they
actually said. This skill owns first contact and the follow-up to a silent acceptance.

## Failure states

- **Profile page returns only the top card** → fetch `details/experience/`. If that is also
  thin, the profile is genuinely sparse; draft from the headline and company, say so, and
  expect a lower reply rate.
- **Redirected to `/login`** → session expired. Pause and ask the founder to log in.
- **URL contains `/checkpoint/challenge`, or a captcha iframe is present** → stop the run
  immediately, capture the exact text, alert the founder, and append the verified signal to
  the LR-B10 journal at `reports/{slug}/outreach/copy-rules-log.md`. Do not navigate further.
- **Contact already has a `[msg{N} sent]` note for this stage** → do not redraft silently.
  Show the founder what was already sent and ask whether they want the next message instead.

## Mechanics

Step mechanics, templates and the failure catalogue live in `references/per-contact-pipeline.md`. Read the section for the step you are running.
