# Per-contact drafting pipeline

The seven-step pipeline for `startup-outreach-draft`. SKILL.md carries the decision procedure
and guardrails; this file carries the mechanics. The copy rules it enforces — and the send
boundary — live in `schemas/copy-rules.md`.

## Per-contact pipeline

### Step 1 — Live snapshot, both pages

Navigate to the profile URL and call `get_page_text`. Then navigate to
`{profile_url}details/experience/` and call `get_page_text` again.

**The second page is not optional.** The main profile page lazy-loads; `get_page_text` on it
returns the top card and little else. The experience detail page returns every role with its
full verbatim description — and that description is where the reply-earning clause comes
from, because it is the contact describing their own work in their own words. Drafting from
the headline alone produces exactly the generic bridge that LR-B1 exists to prevent.

Extract and hold: display name, headline, current company, location, connection degree,
every Experience entry with its verbatim description, listed skills, education, mutual
connections, and any visible recent activity.

### Step 1b — Check the sending account's inbox (LR-B25, mandatory)

Connection degree tells you whether you *can* message someone. It does not tell you whether
you already have. Before drafting, search the sending account's inbox:

```
https://www.linkedin.com/messaging/?searchTerm={surname}
```

A hit means this is a follow-up or a reply, never a Msg 1. Last message ours and under a week
old means draft nothing at all and say so. `contacts.md` cannot answer this question — it
records when this repo found someone, not when the founder last wrote to them — and neither
can a fresh target sweep. Where no `private/linkedin-export/` exists, Pass 0 of
`/startup-outreach-targets` never ran, so prior contact is UNKNOWN rather than absent.

Founder-caught: three of six drafts in a batch were prepared as cold first contacts
for people who already had unanswered threads, one from two days earlier. See LR-B25 for the
follow-up shape and the full evidence.

### Step 2 — Read connection state, decide which message this is

The profile's connection state tells you what you are writing. Get this wrong and the
message is absurd — a "thanks for connecting" to a stranger, or a connection pitch to
someone the founder has been talking to for a month.

| Live signal | What it means | What to draft |
|---|---|---|
| `· 1st` degree, primary button is `Message` | Already connected | A DM. If no prior substantive exchange, this is Msg 2. |
| `· 2nd` / `· 3rd+`, an `Invite {Name} to connect` affordance exists anywhere on the page | Not yet connected | **Nothing (LR-B29).** First touch is a bare invite with no note — there is no copy to draft until they accept. |
| `Pending` visible | Invite already sent, not yet accepted | Nothing to draft. Update `outreach_status: invited` and tell the founder to wait. |
| `2nd`/`3rd+`, no visible invite affordance | **Assume connectable anyway** — Connect is almost certainly in the collapsed More menu | Nothing to draft (LR-B29 — bare invite). If a `/messaging/compose/` link is present they are Open Profile: a Msg 1 DM may be drafted as an alternative to waiting for an acceptance. |
| No invite affordance, no compose link, no Pending, no 1st-degree Message | Possibly restricted, but you cannot confirm this read-only | Nothing to draft — bare invite path. Do NOT mark `off_scope` on this basis alone. |
| 404 or redirect away from the profile | Dead or renamed URL | Skip. `outreach_status: url_broken`. |

Search the WHOLE page text for `Invite .* to connect`, not just the primary button.
LinkedIn puts Connect in at least three places: the top toolbar, inside the More menu, and
as a standalone link elsewhere on the page. A profile showing `Follow` as its primary CTA is
very often still connectable.

**Connect is almost always available, just often hidden.** LinkedIn moves it into the
collapsed More menu whenever the profile's primary CTA is Follow, which is common. Read-only
browsing cannot open that menu, so a missing Connect in the page text and in the
accessibility tree proves nothing at all. Treat every non-1st-degree contact as connectable
by default — the first touch is a bare invite (LR-B29), so connectability decides the
invite queue, not what gets drafted.

This is a regression the skill has already suffered once. Founder-caught: two
contacts were classified as unconnectable on exactly this evidence, and both were reachable
via More. Never state that a profile cannot be connected to — you cannot see the menu that
would tell you.

Running `read_page` with `filter: "interactive"` is still worth one call, but for a narrower
purpose than skip-or-not: a `/messaging/compose/?profileUrn=…` link means **Open Profile**,
so the contact can be DM'd immediately without waiting for an acceptance. That is the one
case where a not-yet-connected contact gets copy drafted (a Msg 1 DM); everyone else gets a
bare invite and waits for acceptance (LR-B29).

When the contact is already 1st degree, read the copy archive for what was already said to
them. Continue the frame that earned the connection rather than restating it — a second
introduction reads as a mail merge.

### Step 3 — ICP fit, three outcomes not two

Check the live profile against the active assumption's declared ICP fields. Never carry a
fixed industry list from another idea; the graph is the authority.

**FULL match** — company inside `icp_segment` and title inside `icp_valid_titles`. Draft
normally.

**PARTIAL match (per LR-B12)** — company inside `icp_segment`, no `icp_out_of_scope` hit,
but the title sits outside `icp_valid_titles`. This is common and often valuable, so do not
treat it as a failure. Most assumptions about cost or margin declare senior, P&L-visible
titles, while the people who can describe what actually happens on the ground are ICs.
An IC can confirm or contradict the **mechanism**; only the senior tier can speak to the
**economics**. Draft for the half they can answer, record the limit explicitly in
`validation_rationale`, and treat the contact as a warm route to the senior titles the
assumption's disconfirmation test actually needs.

**WRONG ASSUMPTION** — the profile is a real, valuable contact but for a different assumption
than the one being drafted for. Check `reports/{slug}/outreach/email/contact-routing.md →
Segment competence` before drafting: a contact may only be asked about assumptions their role
gives them first-hand knowledge of. Researchers testify to what data their own work needed;
they cannot testify to deployment labour, site access or integration economics. Integrators and
plant operators are the mirror image. Reroute to the assumption they can answer and draft that
message instead — do not ask the original question anyway. An out-of-competence answer is a
courteous opinion that enters the ledger as evidence and stays there.

**SKIP** — profile fails `icp_segment` or hits any `icp_out_of_scope` rule. Do not draft.
Update `contacts.md` with `outreach_status: off_scope` and a note naming the specific field
and evidence that failed. The note matters: a bare `off_scope` six weeks later is
indistinguishable from a mistake.

Say which outcome fired and why in one sentence when presenting the draft. A partial match
that looks full is worse than no contact, because it produces evidence filed under the wrong
claim.

### Step 4 — Draft

Msg 1 is **three beats, in this order** (LR-B19):

1. **The research anchor, chosen per sender (LR-B23).** Read `linkedin_account` for this
   contact/batch, take that founder's `outreach_identity.credibility_hook` from
   `founders/{name}.md`, and build the anchor from their own verified claims: either
   `{their hook} and researching the {domain} gap`, or the longer credential form
   `Hi {Name}, thanks for connecting! I want to build in {space} after {their background},
   your {specific work} excites me and I'm trying to understand it better.` (no trailing
   smiley, per LR-B3). Never invent a hook and never borrow another founder's — LR-B14
   requires every first-person claim to survive a profile click. Where the contact shares a school that appears on the SENDING
   founder's OWN profile, lead with the shared-affiliation line before the anchor. Never
   invent an overlap — if you cannot verify the school on the sending founder's side, omit it.
2. **The grounded clause** per LR-B1: `you + verb + concrete noun + at {company}`, drawn
   from the contact's own verbatim Experience description wherever possible. Their own words
   about their own work are the strongest available material and they are self-verifying.
   Never their title. Never certifications. It must anchor on something CENTRAL to their
   work, not merely something verbatim (LR-B16).
3. **The permission ask** per LR-B18: `Would you be open to a couple of questions for my
   research?` — **not the research question itself.**

**The close is a permission ask by default. This is the rule most often got wrong.**
Anyone who could plausibly buy from us later gets the permission ask: every
`physical_ai_lab`, `humanoid_developer`, `robot_foundation_model`,
`enterprise_physical_ai_lab`, `robotics_data_platform` and `synthetic_data_sim_vendor`
contact, at any seniority — a junior IC at a frontier lab is a future buyer's colleague.
The specific question moves to Msg 2, after they say yes. Record
`close_variant: soft_ask` for every one of these.

Only a contact with **no purchasing path at all** — a professor, a journalist — may take a
direct question. Investors are not a third option; they are never contacted at this stage
(LR-B20).

Choose the close from COMMERCIAL POTENTIAL first and seniority second. LR-B15's tier grid
still gets recorded, but it no longer selects the close on its own.

The puzzle framing (LR-B2) still does its work — it lives in the research anchor and the
grounded clause, which together say what the founder is curious about. What changes is that
the message stops before extracting an answer.

**Length.** Msg 1 is hard-capped at 250 characters including name and clause; LinkedIn will
truncate past that. Keep the fixed template under 170 so a long name and a 60-character
clause still fit. DMs have no hard cap, but stay under ~450 — a wall of text on a phone
screen gets read later, which means never.

**Never ask for money in Msg 1 or Msg 2 (LR-B11).** Time is the free proxy. People answer
"what took the longest" instantly and answer "what did it cost" almost never, and asking too
early reads as qualifying a lead. The escalation is documented in LR-B11; keep the early
messages on time, surprises, and unplanned work.

**Length.** Msg 1 is hard-capped at 250 characters including name and clause; LinkedIn will
truncate past that. Keep the fixed template under 170 so a long name and a 60-character
clause still fit. DMs have no hard cap, but stay under ~450 — a wall of text on a phone
screen gets read later, which means never.

**Never ask for money in Msg 1 or Msg 2 (LR-B11).** Time is the free proxy. People answer
"what took the longest" instantly and answer "what did it cost" almost never, and asking too
early reads as qualifying a lead. The escalation is documented in LR-B11; keep the early
messages on time, surprises, and unplanned work.

### Step 5 — Self-check before showing anything

Run the rejection rules from `schemas/copy-rules.md`. Cheapest as a script, since these are exact
string checks and eyeballing them is where errors survive:

```bash
python3 - <<'EOF'
msg  = """<the drafted message>"""
role = "<the contact's raw title>"
linkedin_account = "<sending founder's name>"  # whose account is sending this (LR-B23)
# True for every tier that could plausibly buy from us later (LR-B18)
future_buyer = True
msg_num = 1

cliches = ["hope this message finds you well", "came across your profile", "pick your brain",
    "picking your brain", "circle back", "touch base", "synergy", "synergies", "move the needle",
    "low-hanging fruit", "at the end of the day", "in this day and age", "game changer",
    "game-changer", "no brainer", "no-brainer", "thought leader", "deep dive", "double-click on",
    "let's connect", "quick question", "just following up", "reaching out because", "i'd love to"]

bans = ["—", "–", ":)", ":D", ";)", role] + cliches
hits = [b for b in bans if b and b.lower() in msg.lower()]
low  = msg.lower()

# LR-B18 — the close must be a permission ask, not the question itself
if future_buyer and msg_num == 1 and "would you be open to" not in low:
    hits.append("LR-B18: no permission ask in the close")
if future_buyer and msg_num == 1 and msg.rstrip().endswith("?") \
   and "would you be open to" not in low:
    hits.append("LR-B18: message ends on the research question")

# LR-B19 / LR-B23 — the research anchor must open the message, chosen per sender
# Msg 1 only: a follow-up into an existing thread carries no anchor at all (LR-B25).
# Hooks are read from founders/{name}.md -> outreach_identity.credibility_hook, never
# hardcoded: a shared definition that names one founder is wrong for the other.
ANCHORS = load_credibility_hooks()   # {founder_name: hook_substring}
if msg_num == 1:
    expected = ANCHORS.get(linkedin_account)
    if expected is None:
        hits.append(f"LR-B23: no anchor on file for linkedin_account={linkedin_account}")
    elif expected not in low:
        hits.append(f"LR-B23: missing {linkedin_account}'s anchor")
    for who, other in ANCHORS.items():          # never send one founder's claim as another
        if who != linkedin_account and other in low:
            hits.append(f"LR-B23: {who}'s anchor in a message sent as {linkedin_account}")

print(f"{len(msg)} chars | violations: {hits or 'none'}")
EOF
```

`future_buyer` is True for every `physical_ai_lab`, `humanoid_developer`,
`robot_foundation_model`, `enterprise_physical_ai_lab`, `robotics_data_platform` and
`synthetic_data_sim_vendor` contact. Set it False only for a contact with no purchasing
path whatsoever, and say in the presentation why that contact is exempt.

Then build the **traceability table** — every factual claim in the message beside the exact
live-snapshot line it rests on. This is not paperwork. It is how LR-B6 gets enforced instead
of merely intended: a claim with no row is a claim you invented, and the contact will spot
it immediately because it is about them. Any claim you cannot source, rewrite or drop.

| Claim in message | Live-snapshot source ({date}) |
|---|---|
| "{quoted fragment}" | {section} → "{verbatim line}" |

### Step 6 — Present

For a single contact, show: the ICP verdict in one sentence, the message, the character
count, the traceability table, and a short alternate if one is worth having. Say which
message number it is and why.

For a batch, show one row per contact and keep the full drafts below the table:

```
 ID   Name            Role @ Company           Msg  Chars  Fit      Draft opener
 C1   {Name}          {Role} @ {Company}       1    228    full     {first clause}
 C7   {Name}          {Role} @ {Company}       2    412    partial  {first clause}
 C9   {Name}          {Role} @ {Company}       —    —      skip     off_scope: {reason}
```

Founder commands: `<ID>` to revise one, `regen <ID>` to redraft with different emphasis
(rotation described below), `drop <ID>` to remove it from the batch.

### Step 7 — Log

Write the log when the draft is settled. Do not wait for the founder to send — an unsent
draft with its verification intact is worth keeping, and the founder may send hours later
from their phone.

**`reports/{slug}/outreach/contacts.md`** — one block per contact per `schemas/contact.md`.
New contact: create the block. Existing: update in place, never duplicate, and append the
new assumption id to `assumptions_tested` if it differs. Deduplicate on `linkedin_url`.

Set `outreach_status` from the live connection state, not from intent: `pending` for a
drafted but unsent Msg 1, `accepted` for a 1st-degree contact, `invited` where LinkedIn
shows Pending. Record what you could not determine as `unknown` rather than guessing — an
invented `invited_date` silently corrupts every reply-rate number computed later.

Set `close_variant` per LR-B15 — `direct_question` or `soft_ask` — while drafting, never
afterwards. Before finalising a batch, check which tier × close cells are thin and place the
batch's weakest-fit contact in the empty one, so the comparison stays interpretable without
spending a strong contact on it.

**`reports/{slug}/outreach/copy/{A_ID}-linkedin.md`** — the message, its traceability table,
the rule-compliance list, and the planned arc for the next two or three messages. Append,
never overwrite; the archive is how a later session knows what this person has already been
told.

**Put every sendable message in a blockquote or a fenced block, and nothing else in one.**
The tracker's copy modal pulls exactly those runs, so a message left as bare prose never
reaches the founder's send view, and a retrospective note that gets quoted shows up as
something to paste into LinkedIn. Head each one with a label naming it and its length —
`### Msg 2 — DRAFTED {date}`, `**Primary (439 chars):**`, `**Short alternate:**` — and when
quoting what the contact said back, use a possessive label (`**Their last reply:**`,
`**{Name}'s reply:**`) so it is filed as evidence rather than as copy to send.

Then regenerate the tracker:

```bash
python3 scripts/build_control_room.py {slug}
```

It is a pure projection of `contacts.md`, so it is always safe to overwrite.

When the founder later confirms a message went out, append to that contact's `notes:`:
`[msg{N} sent {date}] {one-line summary of the ask}` and update the status.
