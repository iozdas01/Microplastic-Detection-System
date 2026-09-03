---
purpose: What consumer-marketplace demand for machine-made goods actually looks like on Etsy, priced and volume-calibrated, and which of it a single self-contained machine cell could make end to end.
idea: high-mix-manufacturing
collected: 2026-09-02
method: logged-out browser pass over etsy.com (no ETSY_API_KEY); 14 search queries x 60 listings, page 1, "Most relevant", US default locale, plus 7 shop pages for lifetime-sales calibration
data: data/processed/etsy_categories.csv, data/processed/etsy_shops.csv, data/raw/etsy/2026-09-02-search-summaries.json
status: desk research — grades no assumption and creates no hunch
---

# Reverse-engineering Etsy demand against a one-cell factory

Founder question, 2026-09-02: reverse-engineer what actually sells on a consumer marketplace,
so a self-contained machine cell ("a box") can be pointed at it and the demand tested cheaply.

Read the limits section before quoting any number. This is one snapshot of one page per query
on one day, not a census.

## The finding in one line

**Price rises with the number of processes, and Etsy volume falls with price. Everything a
single box can make end to end sells for $13–65; everything that clears $100+ needs a second
pair of hands for joinery, welding, hardware or finishing.** Two independent filters — "one
cell, no assembly" and "worth the freight from Türkiye" — select the same narrow slice: small,
dense, single-process metal goods. That slice is real but small.

This independently confirms what `pages/hmlv-map.html` already concluded from the company
landscape — that on the consumer side "only surface personalisation and fitted-installed goods
survive." That map reached it from who lived and died; this reaches it from unit prices. Same
answer from two directions is worth more than either alone.

## What each category sells for

60 listings per query, lowest-variant price shown on the card, USD. `ads` counts paid slots out
of those 60; `BS` counts Bestseller badges. Full table: `data/processed/etsy_categories.csv`.

| Category | p25 | **median** | p75 | max | ads/60 | BS/60 | Biggest shop on page (reviews) |
|---|---:|---:|---:|---:|---:|---:|---|
| custom cnc machined part | $15 | **$26** | $52 | $500 | 24 | 13 | BrandIronCraftShop (6.8k) |
| personalized cutting board | $20 | **$21** | $41 | $190 | 24 | 30 | MiraGiftsWorld (55.9k) |
| custom metal business sign | $22 | **$31** | $85 | $400 | 24 | 10 | Crossmetalworks (38.4k) |
| custom wood sign | $20 | **$34** | $61 | $200 | 24 | 23 | WoodByStu (128.3k) |
| modern house numbers | $14 | **$38** | $50 | $176 | 24 | 24 | Makertable (27.5k) |
| wooden puzzle | $15 | **$30** | $48 | $6,995 | 24 | 8 | BusyPuzzle (107.3k) |
| metal wall art | $32 | **$57** | $90 | $495 | 24 | 12 | Crossmetalworks (38.4k) |
| floating shelf | $31 | **$59** | $97 | $310 | 24 | 27 | URBANDIstore (10.4k) |
| wood desk organizer | $40 | **$59** | $109 | $505 | 24 | 4 | GretaOtoDesign (20.1k) |
| **machined titanium EDC** | $35 | **$65** | $95 | $825 | 24 | **2** | PacificSons (10.7k) |
| wall mounted coat rack | $51 | **$66** | $94 | $438 | 24 | 10 | DistressedMeNot (10.9k) |
| wooden jewelry box | $65 | **$109** | $162 | $1,049 | 23 | 10 | SeptemberAndGraceINC (21.1k) |
| wood monitor stand | $89 | **$114** | $153 | $383 | 23 | **1** | Oakywood (8.5k) |
| steel table legs | $84 | **$118** | $279 | $2,643 | 24 | 15 | RustyDesignCanada (7.5k) |

Three things fall straight out of this table:

1. **~40% of every results page is a paid slot** — 23 or 24 of 60, on every single query without
   exception. A new shop is not competing for attention, it is buying it. Any test of this
   channel has to be a paid-traffic test; an organic test of a zero-review shop measures Etsy's
   new-seller suppression, not demand.
2. **Bestseller-badge density is an inverse competition signal.** Cutting boards 30/60 and
   house numbers 24/60 are saturated commodity fights. Monitor stands (1/60), titanium EDC
   (2/60) and desk organizers (4/60) are not — few sellers there have the sustained volume the
   badge requires.
3. **The two lowest-competition categories are also the two highest-priced single-process ones.**
   That is not a coincidence; it is the same fact seen twice.

## What a good shop in each category actually earns

Read from seven shop pages on 2026-09-02. Lifetime sales are Etsy's own counter; the review
count is what the search card shows. Full table: `data/processed/etsy_shops.csv`.

| Shop | Category | Lifetime sales | Since | Sales/review | Sales/yr | Card price | Est. GMV/yr |
|---|---|---:|---:|---:|---:|---:|---:|
| GiftsToEngrave | cutting boards | 159,512 | 2022 | 3.8 | 37,979 | $12.99 | ~$493k |
| Crossmetalworks | metal art / signs | 143,494 | 2014 | 3.7 | 11,762 | $15.00 | ~$176k |
| Makertable | house numbers | 112,876 | 2017 | 4.1 | 12,269 | $16.57 | ~$203k |
| SHANIKStore | organizers / boxes | 75,491 | 2020 | 4.9 | 12,176 | $79.99 | ~$974k |
| RustyDesignCanada | steel table legs | 47,358 | 2016 | 6.3 | 4,643 | $110.23 | ~$512k |
| Oakywood | monitor stands / desk | 46,376 | 2016 | 5.5 | 4,547 | $126.33 | ~$574k |
| KeelanScott | monitor stands / legs | 27,308 | 2019 | 3.7 | 3,793 | $119.99 | ~$455k |

**Calibration worth keeping: shop review count x ~4 ≈ lifetime sales** (range 3.7–6.3, median
4.1 across these seven). That converts every review number on every search card into an order
estimate without opening a single shop page.

**The ceiling is roughly $0.2–1.0m GMV/yr per shop.** Not one of the largest shops in any
category read here is a large business. GiftsToEngrave moves 38,000 orders a year to make
~$493k of it; SHANIKStore makes about twice that on a third of the orders. Volume is not what
pays on this platform — price is.

## Which of it fits in one box

The founder's filter is a self-contained cell: load a blank, machine it, unload a finished
saleable good, no human between operations.

**Tier 1 — genuinely one cell, one pass**
- Engraving bought blanks (cutting boards, coasters, tags): laser only. **$13–21.** This is
  decorating a purchased good, not manufacturing it.
- Laser-cut flat goods (puzzles, flat house numbers, flat signs): cut only. **$16–38.**
- Small machined metal (titanium/brass EDC), accepting an as-machined finish: mill or lathe
  only. **$65.**

**Tier 2 — cell plus one secondary step**
- Metal wall art, metal business signs: cut, then powdercoat. **$31–57.**
- Floating shelves, monitor stands: cut, then sand and oil. **$59–114.**

**Tier 3 — assembly-bound, not a box at all**
- Jewelry boxes (joinery + hinges), coat racks (hardware), desk organizers (glue-up), steel
  table legs (welding). **$66–118.**

Only one category sits at the top of Tier 1 rather than the bottom: **machined metal EDC at $65
median, $95 p75, with 2 Bestseller badges out of 60.** One machine, one material, one
operation, a part that fits in a padded envelope, and it is the process IMTEK already runs. Its
weakness is honest: the market is small (top shop ~10.7k reviews ≈ ~44k lifetime sales against
GiftsToEngrave's 159k), and it is taste-led — buyers are choosing a design, and machining it
well is table stakes rather than the product.

## What Etsy does not contain

The query `custom cnc machined part` returns branding irons, rubber stamps and bead supplies.
Its top shops are BrandIronCraftShop, LittleCircleBeads, DIYStampDesign. **There is no
industrial replacement-part demand on Etsy.** Whatever this channel can test, it cannot test
H2 — buyers of blocked industrial parts are not here. If a listing-based test of H2 is wanted,
the marketplaces are Xometry / Protolabs / Fictiv / eBay Industrial, not Etsy.

## Why value density decides this, not demand

Every price above is what a US buyer pays. Against it (fee figures read from
`etsy.com/legal/fees` on 2026-09-02, freight and duty marked as assumptions):

- Listing $0.20 · transaction **6.5%** of price + shipping · payment processing ~3–4.5% + a
  fixed cent charge **(assumption — country-dependent, not verified this session)**.
- **Offsite Ads 15%** on attributed orders. Below $10k of sales in the prior 365 days a shop
  may opt out; at or above $10k it drops to 12% and **cannot be opted out of**. So the
  platform take rises exactly when the shop starts working.
- On-site Etsy Ads are discretionary but, given 24 of 60 slots are paid, are the only way a
  new shop is seen at all.

Run it on two of the categories above, at a Türkiye→US-consumer freight assumption:

| | Titanium EDC | Cutting board |
|---|---:|---:|
| Price | $65.00 | $21.00 |
| Etsy transaction 6.5% | −$4.23 | −$1.37 |
| Payment processing ~4% *(assumption)* | −$2.90 | −$1.14 |
| Offsite Ads, ~30% of orders attributed at 15% *(assumption)* | −$2.93 | −$0.95 |
| Freight, parcel, TR→US *(assumption: $10 / $12)* | −$10.00 | −$12.00 |
| **Left for material, machine time, duty and margin** | **$44.94** | **$5.54** |

A 60 g titanium blank is roughly $2 of metal. A bamboo board plus its packaging is more than
$5.54. **The cheap high-volume categories are not killed by competition, they are killed by the
freight leg** — which is a fact about where the box sits, not about what it can make.

**Flag before any of this is costed properly:** the US $800 de minimis exemption is believed to
have been withdrawn for all origin countries during 2025, meaning every direct-to-consumer
parcel now owes duty regardless of value. This has not been verified this session and it moves
every row in that table. Verify it first — it is the cheapest thing on this page to check and
the most expensive to get wrong.

## The decision this actually forces

The box's value is not that it manufactures. It is that it lets you manufacture **next to the
customer**. Two forks, and the Etsy data prices both:

- **Box in Türkiye, ship to US.** Only the $65+ single-process dense categories survive. That
  is machined metal EDC and little else — a ~$0.2–0.5m/yr shop, one machine, one operation.
- **Box in the US, near demand.** The freight leg collapses and the whole $13–38 volume tier
  reopens — the tier where the 100k+ lifetime-sales shops actually live. This is the only
  version where the box is worth building rather than renting time on IMTEK.

The Etsy data cannot choose between these. It does say that choosing the first one caps the
business at roughly one good Etsy shop.

## The cheapest test, and its kill condition

The instinct is to list something and see. That test is weaker than it looks: a zero-review
shop is suppressed in search, so an organic listing measures Etsy's cold-start penalty, not
demand. Two tests, in this order, because the second is only worth running if the first passes.

**Test 1 — cost, not demand. Free, one day, no listing.** Take the three highest-review SKUs in
machined metal EDC and in house numbers. Quote each through IMTEK as if it were a customer
order: material, setup, cycle time, finish, pack. Add the fee stack and freight above. Compare
against the observed median price. *Kill condition: if landed cost + fees exceeds ~55% of the
observed median price, the category is closed regardless of what any listing does — no volume
of demand fixes a cost stack.*

**Test 2 — paid-traffic demand. ~$60, two weeks.** Only if Test 1 passes. List 6 SKUs in the
surviving category ($0.20 each = $1.20) and put $50 behind Etsy Ads. Measure cost per order and
views-to-favourite rate, not gross sales. *Kill condition: customer acquisition cost above 30%
of price after the $50 is spent.* Read it against the 24-of-60 paid-slot density: that number
is the price of the channel, and it does not fall for a new entrant.

Both tests are cheaper than one week of building, and Test 1 needs no Etsy account at all.

## Limits

- **One page, one day.** 60 listings per query, "Most relevant", logged out, US default locale,
  2026-09-02. Etsy personalises results and injects ads; a second pass would not reproduce this
  exactly.
- **The card price is the lowest variant**, not the average order value. Every GMV estimate
  here is therefore a lower bound if buyers upgrade sizes or options, which in these categories
  they usually do.
- **Lifetime sales ÷ years understates the current run rate** of a growing shop, and every shop
  in that table is growing. Read the per-year column as a floor.
- **The review→sales ratio is calibrated on seven shops** spanning 3.7–6.3. It is good enough
  to rank categories and not good enough to size one.
- **Supply density was not measured.** Etsy did not render a result count in the DOM on these
  pages, so "how many sellers are in this category" is unanswered.
- **No search-volume data.** What people search for, as opposed to what is listed, is a
  separate source (Google Trends is keyless and already wired in `scripts/data/`); it was not
  run here.
- **The API path stays closed.** `scripts/research/t1_etsy_supply.py` would give this
  quantitatively and repeatably — hundreds of listings, exact lifetime sales per shop — but it
  needs a free `ETSY_API_KEY` that is not in `.env`, and its queries are still hardcoded to the
  retired cabinet hunch.

## What this does not change

Nothing here is buyer or site evidence, so per `CLAUDE.md` it grades no assumption and creates
no hunch. H2 and its assumption graph are untouched. If the founder wants this to become a
lane, the route is a real conversation or a real listing test — not this page.
