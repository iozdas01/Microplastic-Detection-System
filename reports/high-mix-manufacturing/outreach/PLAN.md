---
purpose: The one plan for the belief-level outreach block — which channel does what, in what order, and what each is allowed to prove.
idea: high-mix-manufacturing
created: 2026-09-02
covers: [email/researchers-2026-09, linkedin/belief-experts-2026-09, email/cambridge-reconnect-2026-09]
status: ready_to_send
---

# Outreach plan — belief-level expert block

Two channels, one purpose. Neither of them tests H2.

## What this block is for, and what it is not for

The founder's belief has two links. Link 1 — *the coupling between software and machines is
broken* — is first-hand and well evidenced. Link 2 — *therefore you must own both ends* —
arrived as advice and has **no observation behind it**. This block exists to attack link 2
before the company is built on it.

**Nothing from this block may enter `03-validation/evidence.md` against H2A1, H2A2 or H2A3.**
Every person here is a researcher, a vendor or an intro source. Per the segment competence gate,
none of them has first-hand knowledge of whether a maintenance manager feels a blocked part.
An expert's confident answer to a question outside their competence enters the ledger as
durable wrong evidence and nothing downstream can tell it from a good one.

What this block MAY produce: technical findings that kill or confirm a technical claim, names,
and advisors. The H2 buyer conversations are a separate track and are running elsewhere in
`contacts.md`.

## The two channels

| | Email — `email/researchers-2026-09/` | LinkedIn — `linkedin/belief-experts-2026-09/` |
|---|---|---|
| Who | 38 paper authors, cold | 17 first-degree connections, warm |
| Volume | No rate limit | ~20 DMs/day platform envelope |
| Opener | Their paper's own finding, cited by number | Shared context or a live profile fact |
| Cap | None | 450 chars, `schemas/copy-rules.md` |
| Ready | 18 drafts | 6 drafts |
| Surface | `pages/outreach-send-sheet.html` | `linkedin/belief-experts-2026-09/drafts.md` |

Email is the volume channel and it is where the argument gets tested. LinkedIn is the warm
channel and it is where the introductions come from. Run both; they feed each other, and there
is one place below where they cross.

## Order of work

**1 · LinkedIn first, and it takes twenty minutes.** Six DMs, all first-degree, no invite
needed. Send L6 (Gokul Narayanan) before anything else — see the crossover note below. These
are short, they are warm, and replies land within a day, so getting them out first means
answers arrive while the email wave is still in flight.

**2 · Email Tier A next — nine messages, one wave, then stop.** Set the from address first;
the copy is written to read as coming from a Cambridge address and that is the whole reason
the opener works on academics. Send in the recipient's morning: CET for KTH, Chalmers, DFKI,
TUM; SGT for NTU; KST for Sling AI and Neuromeka; ET for Sewbo, Cornell, CMU, Rice.

Then **stop and wait 48 hours.** If nine grounded emails to nine well-chosen people produce
zero replies, the opener is wrong and Tier B would be thirteen more of the same mistake.

**3 · Email Tier B after 48 hours**, regardless of what came back. Nine more.

**4 · Second addresses at the same organisation are held a full week.** R2, R5, R6, R8, R10,
R12, R13, R17, R19, R30, R32, R38, L9, L10 all point at organisations already written to. Two
messages into one department in one week reads as a blast and burns both.

## The crossover — the one place the channels meet

The email campaign was built around
[2606.16078](https://arxiv.org/abs/2606.16078), whose digital thread module parses DXF
production drawings into robot trajectories. That paper's first author, **Gokul Narayanan**,
turned out to be a **first-degree LinkedIn connection in the same metro as the founder** — he
is simply absent from the 2026-08-20 export, which is stale.

So: **send L6 first. If he replies, hold email targets R1 (Zornow, Sewbo) and R2 (Calle,
Levi's) and ask him for the introduction instead.** A warm intro from a co-author converts
better than either cold email, and sending all three in parallel spends the warm path to save
a day.

The general lesson is worth more than the instance: **confirm degree live before deciding
someone is only reachable cold.** The export is thirteen days old and already wrong once.

## What each channel has to come back with

**Email — three questions, in priority order.**

1. *Does anyone close the design-to-machine handoff without owning the machines?* This is the
   direct test of link 2. IndustriConnect (R37) is the sharpest live challenge: MCP adapters
   over Modbus and OPC UA, benchmarked over 870 runs — but mock-first, never on plant. Ask what
   broke the first time it met real equipment.
2. *What does commissioning actually cost?* The research map has one hard number — under 20
   minutes of real data per task at Neuromeka — and no number at all for the engineering before
   that. Everyone with a deployment has it and nobody publishes it.
3. *Is process planning from a CAD model close to being a quote?* Design-to-Plan ran 300
   benchmark cases. Where it failed is the answer, and the paper does not print it.

**LinkedIn — two things, and neither is an opinion.**

1. Names. McNiven and Kimmig are asked for introductions and nothing else.
2. First-hand numbers from people who have shipped: how many weeks a cell took, what the
   biggest line item was, which research result died on contact with a product.

## The discipline that decides whether this was worth doing

Msg 1 asks permission and never carries the question (LR-B18). When they say yes, **do not
harvest opinions.** These are articulate senior people who will speculate generously, and
expert speculation is the most convincing useless evidence there is. Ask what they have done,
not what they think.

Closing line on every call that goes well:

> Who else should I be reading on this? I would rather find the person who thinks I am wrong.

## The warm thread — `email/cambridge-reconnect-2026-09/`

Separate from both channels above and higher expected value than either, because it is the one
relationship where a named person has already described a product he would buy.

The founder ran a CAD-CAM interoperability case study with **Universal Wolf** (complex sheet
metal, Blyth, formerly Tharsus Engineering) during the Cambridge ISMM course. The contact's name
is lost in an inaccessible Cambridge mailbox. One email to **Dr Sam Brooks** (IfM, DIAL) asks
for the reintroduction — not the name, so the contact arrives warm and Sam's goodwill is spent
with his consent rather than around it.

Send it in the same sitting as the LinkedIn wave. It is one email and it is the only line in
this whole block that leads to a named person with stated intent to buy.

**The LOI waits.** Introduction, then a call confirming the problem is still live and still
costs him money, then terms. And when it lands, it evidences that *he* would buy, not that a
market would — one contact's commitment, not validation of H2.

## Known gaps in this block

- **No furniture designers.** The network has none, and the question needs 2nd-degree search.
  Not attempted here.
- **The CNC and machining literature was never scanned.** arXiv rate-limited the query
  repeatedly, and that literature lives mostly in journals rather than on arXiv anyway.
  OpenAlex is the right source. See `research-map.md`'s `method_note`.
- **One finding is not in the ledger.** The O(n²) point-to-point integration result from
  arXiv 2608.24918 belongs in `03-validation/evidence.md` and was left out because another
  session was mid-edit in that file on 2026-09-02. Promote it once the ledger settles.
- **The from address is unset.** `founders/izgin-ozdas.md` has `reply_email` empty.
