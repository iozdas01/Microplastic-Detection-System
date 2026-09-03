---
purpose: What was invited on the H3 window-coverings LinkedIn track, when, in which market-size band, and what came back.
idea: high-mix-manufacturing
hunch: H3
assumptions: [H3A1, H3A2, H3A3]
campaign: h3-window-coverings-2026-09
opened: 2026-09-03
status: invites_sent_awaiting_acceptance
---

# H3 window coverings — LinkedIn invite track

Bare connection requests only. No copy has been sent to anyone on this list (LR-B29): the
first words any of them receive is Msg 1, drafted after they accept.

## Why this batch was banded

The pool that existed before this run sat almost entirely at the bottom of the market. The
receipts ladder in `research/data/processed/market_ladder_ranked.csv` says that is not a
sample of the industry, it is a sample of its tail:

| Layer | Firms in the $100m+ receipts band | Share of that layer's receipts |
|---|---:|---:|
| Manufacturers (NAICS 337920) | 10 | 62.5% of $2.48bn |
| Specialty retail dealers (NAICS 442291) | 4 | 19.0% of $2.77bn |

Fourteen firms hold most of the money, and none of them was represented. Worse, the ICP had
no tier those firms could occupy — `national_retail_channel` did not exist until this run, so
Home Depot and Wayfair were not excluded by the ICP, they were unrepresentable in it.

Banding exists so "we tested the whole market" is checkable rather than asserted. Bands are
declared in `02-assumptions/graph.md` frontmatter and recorded per contact as `size_band`.

## What was sent, 2026-09-03

**74 invites, every one bare, every one name-verified before the click.**

| Band | Sent | Who |
|---|---:|---|
| micro (<10 staff) | 17 | independent installers, one-van fitters, Budget Blinds franchise units |
| unbanded | 28 | regional dealers and small manufacturers; headcount not yet read, so not banded |
| enterprise | 29 | see below |
| **total** | **74** | |

Enterprise breakdown — the layer that did not exist in the pool before today:

| Company | Sent | Why they are in the top band |
|---|---:|---|
| The Home Depot | 2 | window-covering merchants; owns Blinds.com |
| Global Custom Commerce / Blinds.com | 3 | Home Depot's made-to-measure arm; publishes the SureFit remake cap |
| SelectBlinds | 3 | publishes FIT Protection, the strongest behavioural signal in the recon |
| Wayfair / Birch Lane | 2 | sells cut-to-size custom window treatments |
| Hunter Douglas | 2 | largest custom window-fashions maker in North America |
| Springs Window Fashions | 4 | Levolor/Bali; all major residential and commercial channels |
| Norman Window Fashions | 4 | among the world's largest custom makers |
| Blinds To Go | 4 | vertically integrated maker-retailer |
| 3 Day Blinds | 2 | seller owns the measurement — the structural control case |
| Hillarys | 3 | UK's largest made-to-measure operation |

The two **BlindMatrix** invites (`industry_software_vendor`) sit in the unbanded row above,
not in this table: they carry no band on purpose, being expert-side and nowhere on the
receipts ladder. The recon named it the highest-leverage target in the lane because an ERP
vendor sees remake rates ACROSS its customers rather than at one firm. Both the founder and
the technical lead were invited; the technical lead is 2nd-degree.

## Order, and why

The founder's standing rule puts 2nd-degree contacts first. Four qualified and went first:
SelectBlinds' COO and its pricing analyst, the BlindMatrix technical lead, and one Budget
Blinds installer. Everything after that ran bottom-to-top by band.

## How the sends were made safe

Two independent name checks per invite, because the obvious approach is unsafe here:
LinkedIn renders Connect buttons for OTHER people inside the profile body — the
"People similar to…" strip — and those are **not** inside an `<aside>`, so any selector based
on position or class can land on a stranger. Every click was gated on the control's
`aria-label` naming the intended contact, and again on the name printed in the invitation
modal before confirming.

Route used: `linkedin.com/preload/custom-invite/?vanityName={slug}`, which opens the
invitation modal directly. On 3rd-degree profiles the Connect control is otherwise hidden
behind the "More" menu, and on some profiles it is an `<a>` rather than a `<button>`.

Pacing: 20-30s between sends, per the founder's instruction on the day. No captcha, no
"unusual activity" interstitial, and no silent Connect failure at any point. LinkedIn's own
sent counter read 391 pending afterwards, consistent with the 74.

## Standing risk, not created by this batch

The account carries ~391 pending invitations. `private/linkedin-export/Invitations.csv`
(snapshot 2026-08-16) records 550 outgoing since February: 50 at 2-4 weeks, 391 at 1-3
months, 109 over 3 months. Essentially the whole pre-existing backlog is older than the
founder's two-week staleness bar and would qualify for withdrawal.

**It could not be actioned.** The invitation manager renders only the 10 most recent sent
invitations and exposes no pagination, so 300+ of them are unreachable from that page. The 10
that ARE visible top out at one week old and therefore do not qualify. Clearing the backlog
needs a different route and is logged here as open work, not done.

## Next

Nothing to draft until someone accepts. On acceptance, `/startup-outreach-draft` writes Msg 1
against the accepting contact's own band and tier — a plant manager at Springs and a
one-van fitter are not asked the same question. Reply-rate comparison BY BAND is the point of
the exercise: if the enterprise band ignores this and the micro band answers, that is a
finding about who owns the pain, not a disappointing response rate.
