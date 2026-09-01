---
name: startup-outreach-check
description: >-
  Checks the LinkedIn inbox for replies after outreach, classifies each confirmed response, updates contacts.md, and refreshes results-{A_ID}.md with reply rates and next-step routing. Use for "check who replied", "any replies?", "check inbox", "who responded", or an outreach check for a specific assumption. Reads unread conversations from list previews without opening them, asks the founder to confirm classifications, and never sends messages. Drives the founder's own Chrome via the claude-in-chrome tools and needs an already-authenticated LinkedIn session.
---

# Startup Outreach Check

Scan the LinkedIn inbox for replies from contacts in your target list. The browser does the tedious thread-by-thread checking; you confirm what it found and decide next steps.

## Prerequisites

- `reports/{slug}/outreach/contacts.md` must exist with at least one contact at `outreach_status: accepted`
- If no contacts are `accepted` yet, the invites haven't been accepted — nothing to check. Tell the founder.
- `reports/{slug}/outreach/results-{A_ID}.md` may or may not exist — if it does, read it for `last_checked` date; otherwise this is the first check run.

## Setup

Browsing is done with the **claude-in-chrome tools**, driving the founder's own Chrome —
same as `startup-outreach-targets`, whose "Setup" section is the single author of the
procedure. In short: load the tool schemas in one `ToolSearch` call, call
`tabs_context_mcp` first, then work in a tab you created with `tabs_create_mcp` and close
it when done.

The LinkedIn session is whichever founder account is already logged into that Chrome
profile. **Check it before reading anything**, because `contacts.md` is split across two
accounts via `linkedin_account:` and an inbox only holds one side's threads. Filter the
contact list to the logged-in account and say which one you filtered to; never report a
contact on the other account as `no_reply` — it is unchecked, which is a different thing.

## The check flow

### Step 1 — Load the contact list

Read `contacts.md`. Collect every contact where:
- `outreach_status: accepted` (connection accepted, message sent, awaiting reply)

Also note the `outreach_pattern` for each contact — you'll need this to compute per-strategy reply rates.

Read `results-{A_ID}.md` if it exists and note `last_checked`. If no results file, `last_checked` is null (check for any reply, regardless of date).

### Step 2 — Check the inbox for replies

Navigate to the LinkedIn messaging inbox and read the conversation list:

```
navigate      → https://www.linkedin.com/messaging/
get_page_text → the conversation list, name + preview + timestamp per row
```

`get_page_text` is the right tool here: the inbox list is text, and it costs a fraction of
a screenshot. Fall back to `read_page` when you need the unread badge state, which the
text extraction drops, and to `computer` screenshots only when both fail.

The list virtualizes — it renders roughly the first 20 threads and loads more on scroll.
Scroll the list and re-read until you either reach threads older than `last_checked` or
hit the bottom. **A name absent from the rows you actually read is not a `no_reply`** — it
is unread territory, so keep scrolling before concluding anything about it.

**HARD RULE — do NOT open unread messages.** Read reply content from the conversation list preview snippets only. Never click into a thread that has a "new notification" / unread badge — that marks it as read and interferes with the founder's inbox. Only navigate INTO a thread if it is already read (no unread badge) AND the preview snippet is truncated and you need the full text.

For each outreach contact in your list: scan the conversation list for their name. Extract the reply snippet verbatim from the preview. Note the unread/read state.

If `last_checked` is set, only count messages timestamped after that date — LinkedIn shows timestamps on each thread in the list.

**Rate-limit:** if navigating into already-read threads, 3–5 second sleep between contacts. Stop immediately if LinkedIn shows a captcha or throttle warning — alert the founder to resolve it.

### Step 3 — Classify each reply

For each contact, assign one of four statuses:

| Classification | Meaning | Next step |
|---|---|---|
| `substantive` | They answered the question you asked, gave real detail, or want to talk | → `startup-outreach-reply` for Msg 2; capture only after an interview |
| `soft` | Acknowledged it, interested but vague ("happy to chat sometime", "send me more") | → `startup-outreach-reply` for a light Msg 2 |
| `negative` | Not interested, wrong person, no time, bounced | → mark declined |
| `no_reply` | No message from them in the thread at all | → flag if > 14 days since message sent |

Extract a 1–3 sentence `reply_excerpt` for `substantive` and `soft` replies. Keep it verbatim — their actual words matter for the follow-up or interview.

### Step 4 — Present summary for confirmation

Once you've checked all contacts, present a summary before writing anything:

```
Inbox check for A{X} — "{assumption text}"
Checked {N} contacts. Last check: {last_checked or "first run"}.

Replies found:
  substantive (3):
    - {Name}: "We've been doing it by hand for the last two years — the existing tools just can't do the fine work..."
    - Marcus Bell: "Yes this is a real issue, happy to jump on a call."
    - Priya Shah: "Interesting — what kind of approach are you thinking about?"

  soft (1):
    - Anwar Butt: "Send me some info and I'll have a look."

  negative (0):

  no reply (4):
    - Tom L., Wei Z., Dr Whitmore, Jane K. (>14 days since message — flag for follow-up or retire)

Does this look right? Any corrections before I update the tracker?
```

Wait for confirmation. If the founder says something is wrong (e.g. "Wei actually replied last week, I just forgot to check"), update your classification before writing.

### Step 5 — Update contacts.md

For each contact, update their block:

**Substantive or soft reply:**
- Add reply_excerpt to `notes:` field (prefix with `[reply {date}]`)
- Do NOT change `outreach_status` — the founder decides when to move to `scheduled`

**Negative reply:**
- Set `outreach_status: declined`

**No reply (> 14 days):**
- Do NOT auto-change status — surface to founder in the summary. Only update to `no_reply` if the founder confirms.

Update the file `last_updated` frontmatter field.

### Step 6 — Write results-{A_ID}.md

Write to `reports/{slug}/outreach/results-{A_ID}.md`. If the file already exists, update in place.

```markdown
# Outreach Results: A{X}
# "{assumption text}"

last_checked: {today's date}
total_sent: {count of accepted contacts}
total_replied: {substantive + soft}
reply_rate: {%}

## Regenerate threshold

A strategy hits the regenerate threshold when 0/{N} contacts in that cluster have replied
after 14 days. At that point, flag to founder: the angle isn't working.

{list any strategies at threshold, or "None at threshold yet."}

## What this skill does NOT do

- **Doesn't send messages.** `startup-outreach-reply` may send Msg 2 only after the founder explicitly approves its displayed draft.
- **Doesn't schedule interviews.** Founder handles booking.
- **Doesn't write follow-up copy.** That's `/startup-outreach-reply`, which reads the confirmed reply excerpts to anchor Msg 2.
- **Doesn't run interview capture.** That's `/startup-interview-capture` after the call happens.

## Common failure modes

- **Classifying a LinkedIn notification as a reply.** LinkedIn sometimes shows "Your connection request was accepted" in the message thread. That's not a reply — it's a system message. Only count messages the contact actually wrote.
- **Missing a reply because the thread loaded partially.** If the snapshot shows "Show earlier messages" or similar, the thread may be truncated. Scroll or click to load more before concluding no_reply.
- **Checking contacts for the wrong assumption.** If contacts.md has contacts for multiple assumptions, filter to the target A{X} before checking. Don't mix reply data across assumptions.
- **Updating status without confirmation.** Never change `outreach_status` to `no_reply` or `declined` without surfacing to the founder first.

## Reference files

- `schemas/contact.md` — contact card format + status lifecycle
- `reports/{slug}/outreach/blast-sessions/*.md` — confirmed Msg 1 session records

## Mechanics

Step mechanics, output templates and taxonomies live in `references/check-outputs.md`.
