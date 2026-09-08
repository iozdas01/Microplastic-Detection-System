---
purpose: The evidence ledger for this idea — every graded claim, linked to the assumption it moves and the direction it moves it.
idea: high-mix-manufacturing
last_updated: 2026-09-07
---

# Evidence ledger — high-mix-manufacturing

Restarted 2026-09-02 with the lineage. The previous ledger (E1-E6) belonged to the retired
cabinet hunch and its archived assumption graph; it is preserved in git history and must not
be cited against H1, whose IDs are different.

**E1 is the first entry in this repo that came from a human being rather than a search.**

```yaml
entries:
  - id: E1
    date: 2026-09-02
    hunch: H1
    assumption_linked: unassigned
    verdict: supports
    confidence: 3
    source_type: founder_interview
    source: Phone call with a home moving company (SF). Founder-conducted, first call.
    claim: >-
      Furniture customers leave behind goes one of two ways: donated, or to the junkyard.
      1-800-GOT-JUNK-type services pick up a lot of it.
    why_it_matters: >-
      Confirms the disposal path exists and names who touches the material, which narrows the
      supply-side segment from five candidates to two: donation channels and junk removal
      operators. Movers are a referrer, not a holder of supply.
    limits: >-
      n=1. No volumes, no fees, no split between donation and junk. Founder notes did not
      capture what the mover charges to haul, which is the number that decides whether
      feedstock cost is negative.
    next: >-
      Ask the next three movers for the donate/junk split and the haul fee. Then call junk
      removal operators directly, since they hold the material.

  - id: E2
    date: 2026-09-03
    hunch: H2
    assumption_linked: H2A4
    verdict: contradicts
    confidence: 3
    source_type: commercial_data
    source: >-
      Google Trends, United States, five years, collected 2026-09-03 by
      scripts/research/t1_demand_sweep.py. Forty-three terms across every machinable
      material, each batch anchored on "custom furniture" so all terms are comparable.
      Scored by scripts/research/analyse_demand_sweep.py.
    claim: >-
      The blocked-part vocabulary has no measurable inbound search demand in the US. All
      four terms swept for it — "obsolete parts", "custom replacement part", "part no
      longer available", "reverse engineering parts" — sat at or below a Trends index of 1
      for more than half the weeks of five years, which is the resolution floor of the
      instrument rather than a small number. "obsolete parts" returned zero related
      queries at all, meaning the term is below the volume at which Google can compute
      co-occurring searches.
    why_it_matters: >-
      The founder's stated model is a website people arrive at to have something made
      ("vibe manufacturing"). For H2's segment that channel does not exist: the buyers are
      not searching. It does not touch whether the pain is real — H2A1 is untouched by this
      — but it means H2 has to be sold outbound, and the 17 first-degree contacts already
      in the ledger are the channel, not a warm-up for one.
    limits: >-
      Measures arrival-by-search only. A maintenance engineer with a stopped line phones a
      shop they already use or emails the OEM; none of that appears in Trends. Absence here
      is evidence about channel, never about pain. US-only. The four terms are the founder's
      and the model's vocabulary for the problem, not necessarily the buyer's — a buyer who
      searches "machine shop that can copy a part" would not be caught.
    next: >-
      Do not spend anything on a website or on search acquisition for the blocked-part lane.
      In the H2A1 conversations already queued, add one question that tests the channel
      rather than the pain: "when that happened, how did you go looking for someone to make
      it?" Their answer names the real channel.

  - id: E3
    date: 2026-09-03
    hunch: H2
    assumption_linked: H2A4
    verdict: supports
    confidence: 3
    source_type: commercial_data
    source: Same sweep and scoring as E2.
    claim: >-
      Buying intent runs inverse to search volume across the whole sweep. The trade terms
      sit below the resolution floor but nearly every related query they do generate is
      transactional — "waterjet cutting service" 100%, "laser cutting service" 86%,
      "metal fabrication near me" 75%, "cnc machining service" 70%. The largest measured
      term on the page, "custom signs", carries 21% buying intent, and "custom acrylic"
      and "custom neon sign" carry 0%.
    why_it_matters: >-
      Names the trade-off the website question actually faces, which is not "where is the
      demand" but "which kind of demand". Volume and intent are not available in the same
      place. A consumer-facing configurator buys traffic that mostly browses; a trade-facing
      one catches almost nobody but converts what it catches. This is the choice the founder
      is really making, and it was invisible while the question was framed as a single
      ranking.
    limits: >-
      Intent is inferred from the vocabulary of related queries against a declared marker
      list ("near me", "cost", "quote", "service", "supplier"…), not from observed
      conversion. It is a proxy. The high-intent terms are also the unmeasured ones, so
      their intent share is computed over a small related-query list and is noisier than
      the measured rows.
    next: >-
      Settle it by asking the founder which they are building for, rather than by more desk
      work — the measurement has taken this as far as it goes.

  - id: E4
    date: 2026-09-03
    hunch: H2
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 3
    source_type: commercial_data
    source: Same sweep and scoring as E2.
    claim: >-
      Signs and display is the largest measurable family of made-to-order demand across
      every machinable material — 2.43x the "custom furniture" anchor, and the only family
      where all four swept terms resolved. "custom signs" alone is 1.73x the anchor and up
      41% year on year, ahead of "custom t shirts" (1.16x), which was included only as a
      calibration category known to sustain real made-to-order web businesses.
    why_it_matters: >-
      It is the honest answer to the founder's question as asked — if the criterion is
      "most people arriving at a website wanting something made", this is where they are,
      and it beats every wood, metal and machining category measured. Logged as ambiguous
      rather than supporting because it belongs to no hunch on file: nothing here says the
      founder should enter it, and signage is a printing business as much as a fabrication
      one.
    limits: >-
      Search volume is not revenue and not margin. The family is heavily served already —
      Signs.com, VistaPrint, BuildASign and a large Etsy neon trade — and no competitive
      check has been run. The term mixes printed yard signs (not machining) with fabricated
      metal, acrylic and LED work (machining); the sweep does not separate them, and the
      split matters more than the total.
    next: >-
      DONE — the counter-query is E6, run the same day, and it substantially weakens this
      entry. The demand sits on the printed side of the family, which no CNC shop serves.
      Read E4 and E6 together; E4 alone overstates the opportunity.

  - id: E5
    date: 2026-09-03
    hunch: none
    assumption_linked: unassigned
    verdict: supports
    confidence: 3
    source_type: commercial_data
    source: Same sweep and scoring as E2.
    claim: >-
      "custom cabinets" survives a cross-material sweep — 1.06x the anchor, 29% buying
      intent, up 45% year on year, and one of only two wood-and-panel terms in four to
      resolve at all. It ranks above every metal, machining, plastics and cutting term
      measured. "custom closet" resolves at 0.59x; "custom built ins" and "custom wood
      furniture" do not resolve.
    why_it_matters: >-
      The cabinet hunch — archived, its IDs burned, NOT the current H1 — was retired on
      2026-09-02 without a customer conversation, and the
      2026-08-31 wedge map ranked freestanding furniture last on measured demand. This says
      the demand reading that made cabinets attractive was not an artifact of only looking
      at furniture: widen the field to every machinable material and cabinets still place
      second. It is a reason not to treat the retired lane as disproven.
    limits: >-
      Reconfirms demand only. It says nothing about the reason cabinets were retired, which
      was that the founder has CNC capacity now and cabinets need a panel line first. Demand
      was never the weak link in that decision.
    next: >-
      None. Recorded so the retired lane is not later remembered as demand-falsified, which
      it is not.

  - id: E6
    date: 2026-09-03
    hunch: none
    assumption_linked: unassigned
    verdict: contradicts
    confidence: 3
    source_type: commercial_data
    source: >-
      Google Trends, United States, five years, collected 2026-09-03 by
      scripts/research/t1_sign_split.py. Twenty sign sub-terms split into printed
      (ink on a flat substrate) and fabricated (cut, bent, routed, engraved, assembled),
      anchored on "custom neon sign" because the parent term "custom signs" is 7x the
      largest sub-term and quantised every fabricated term to zero.
    claim: >-
      The signs family is mostly a printing market, and the fabricated part that people
      do search for is small decorative goods rather than architectural sign fabrication.
      "custom decals" alone (2.55x the anchor) exceeds every resolved fabricated term
      combined (1.52x). Seven of ten fabricated terms did not resolve at all, and they are
      precisely the architectural ones — "channel letter sign" 0.034, "dimensional letters"
      0.039, "custom lobby sign" 0.002, "custom monument sign" 0.001. The three fabricated
      terms that did resolve — "custom metal signs" 0.68, "custom led signs" 0.49,
      "custom wood signs" 0.34 — are personalised decor, which is Etsy's market.
    why_it_matters: >-
      This is the counter-query on E4 and it substantially weakens it. Signs topped the
      cross-material sweep, but the demand sits on the side of the family a CNC shop cannot
      serve and does not want: wide-format printing on vinyl and corrugated plastic. The
      architectural fabrication work a router and a brake could do is not searched for,
      because it is specified by sign companies and general contractors rather than bought
      online. Signs should not be treated as an available wedge on the strength of E4.
    limits: >-
      INCOMPLETE — one batch of four terms ("custom signs", "custom yard signs",
      "custom banners", "custom stickers") failed with HTTP 429 across three attempts over
      fifteen minutes and is missing from the data. Three of those four are printed terms
      and are among the highest-volume in the family, so completing the batch would widen
      the printed-versus-fabricated gap, not close it: the missing data works against the
      fabricated side, which is why the direction is reported despite the gap. The side
      totals themselves are therefore floors, not measurements, and should not be quoted as
      ratios until the batch is re-run.
    next: >-
      Re-run `python scripts/research/t1_sign_split.py` from a different network or after a
      cooling-off period to recover the missing batch, then restate the split as a ratio.
      Nothing about the conclusion needs to wait for it.

  # ─── First buyer conversations for H3. Founder-conducted by phone, 2026-09-03. ───
  # Five calls into San Francisco / US window covering dealers and workrooms. These are the
  # first entries in this repo from people who sell the thing being studied.

  - id: E7
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A3
    verdict: contradicts
    confidence: 4
    source_type: customer_interview
    source: Phone call with Stoneside Blinds and Shades (San Francisco). Founder-conducted.
    claim: >-
      Stoneside sends someone out to measure free of charge. If the customer supplies their
      own dimensions and those dimensions are wrong, the CUSTOMER is liable for the reorder.
      They cited a specific case: a customer supplied their own measurements for 23 windows,
      the measurements were wrong, and the customer had to reorder the lot.
    why_it_matters: >-
      This cuts against H3A3 as written. The remake cost is not sitting on the manufacturer
      waiting to be removed — the dealer has already engineered it off their own books by
      making the free measure visit the default and pushing liability onto anyone who opts
      out. The party bearing the misfit cost here is the CONSUMER, who is a one-time buyer
      with no budget line and no ability to compare vendors on remake rate.
    limits: >-
      n=1 on the liability policy. The 23-window case is one incident, and the founder did not
      capture what the reorder cost or how often self-measurement happens as a share of orders.
    next: >-
      Ask the next dealers what share of orders come in on customer-supplied dimensions. If it
      is small, the consumer-liability path is a rounding error and the real cost is the free
      visit, not the remake.

  - id: E8
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A4
    verdict: supports
    confidence: 4
    source_type: customer_interview
    source: >-
      Phone call with a blinds retailer. Founder-conducted. Company name recorded by the
      founder as "the national blinds guys"; the exact legal entity is not pinned down.
      CORRECTED 2026-09-03: asked to confirm, the founder said the person "seemed like she
      owned it". So "national" was the founder's own uncertain shorthand, not something the
      contact said. Treat the firm size as UNKNOWN — the original wording implied a large
      chain, and E12 makes firm size the difference between a buyer and a non-buyer.
    claim: >-
      They charge $225 to send someone out to measure. They said it is "not accurate enough",
      and they decline jobs outright when sending someone out is too far.
    relink_note: >-
      Re-linked from H3A1 to H3A4 on 2026-09-03 when H3 was re-rooted. The entry reports a $225 measuring-visit fee and jobs declined on travel distance. That is H3A4's claim exactly. It never mentions a remake rate, which is what H3A1 asks for, so the original link overstated H3A1's support.
    why_it_matters: >-
      The strongest entry in this batch and it reframes the pain. This is a cash cost of $225
      per job paid on EVERY order, not a probabilistic remake cost paid occasionally. It is
      also a revealed constraint on the business: they turn away revenue when the drive is too
      long, which means the measurement visit bounds their serviceable radius. A cost that is
      both certain and territory-limiting is a better thing to attack than a remake rate
      nobody publishes.
      The size correction cuts the other way, though: declining jobs on drive distance is
      owner-operator behaviour, not national-chain behaviour, and an owner-operator is the
      firm E12 says cannot buy anything. The $225 stays the sharpest costed number in the
      ledger; who carries it is now less certain, not more.
    limits: >-
      "Not accurate enough" was said about their own paid visit, and the founder did not
      capture what inaccuracy rate they meant or what it costs them downstream. No figure for
      how many jobs they decline.
    next: >-
      Get the decline rate and the radius. "How many jobs a month do you turn down because of
      the drive, and how far is too far?" That converts a complaint into a lost-revenue number.

  - id: E9
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A2
    verdict: supports
    confidence: 4
    source_type: customer_interview
    source: >-
      Four calls, aggregated: Stoneside, the national blinds retailer, Art Shade Shop, and
      Susan Lind Chastain Inc. Founder-conducted.
    claim: >-
      Every dealer contacted measures by sending a human to the window. None uses software to
      capture or verify the dimension. Stoneside works through designers, architects and
      contractors and runs its own factories with a current lead time of four to five weeks.
    why_it_matters: >-
      Confirms the mechanism half of H3A2: the dimension is captured manually at the window in
      every case, so that is where the number enters the chain. It does NOT confirm that the
      error originates there — these dealers send trained people precisely because they have
      already decided customer measurement is the risk. The remaining question is whether the
      trained visit is accurate, and the national retailer volunteering "not accurate enough"
      about their own paid visit is the thread to pull.
    limits: >-
      Four dealers in one metro plus one national. "No software exists" is what dealers
      believe, not a market scan — measurement apps and laser tools do exist, so this reads as
      "nothing we would rely on", which is a different and more useful claim.
    next: >-
      Ask specifically what they use today at the window: laser distance meter, tape, or a
      phone. Then ask what they do when the opening is out of square.

  - id: E10
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A3
    verdict: contradicts
    confidence: 3
    source_type: customer_interview
    source: >-
      Several calls with owners of family-run window covering businesses. Founder-conducted.
      Individual businesses not separately named in the founder's notes.
    claim: >-
      The family-business owners were not enthusiastic about a software solution to the
      measuring problem.
    why_it_matters: >-
      Recorded deliberately as a contradiction rather than left out. This is the segment that
      would have to buy, and their unprompted lack of interest is worth more than the one
      positive reaction in E11. It suggests either that the cost does not hurt them enough to
      act on, or that software is the wrong shape of answer for an owner-operator who already
      does the visit themselves.
    limits: >-
      "Not super excited" is the founder's paraphrase of tone, not a recorded objection. No
      reason was captured for why they were unenthusiastic, which is the thing that matters.
    next: >-
      Go back to one of them and ask the question that gets the reason: "what would have to be
      true for you to stop sending someone out?" A no with a reason is more valuable than the
      yes in E11.

  - id: E11
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A6
    verdict: ambiguous
    confidence: 2
    source_type: customer_interview
    source: Phone call with Stoneside Blinds and Shades (San Francisco). Founder-conducted.
    claim: >-
      The Stoneside contact said, in the founder's transcription: "Yeah if there was such
      software that would be good but there isn't."
    relink_note: >-
      Re-linked from H3A1 to H3A6 on 2026-09-03 when H3 was re-rooted. "If there was such software that would be good but there isn't" is a statement about whether a seller would adopt a remote measurement, which is H3A6. It says nothing about a remake rate. It stays graded 2: prompted, hypothetical, and a Mom Test false positive.
    why_it_matters: >-
      Logged as AMBIGUOUS and graded 2 on purpose, because it is a textbook Mom Test false
      positive: a compliment about a hypothetical product, offered by someone who has spent
      nothing and changed no behaviour. It is recorded only so it cannot later be mistaken for
      demand. The behavioural evidence in E7 and E8 is worth more than this sentence, and the
      unenthusiastic owners in E10 are worth more still.
    limits: >-
      No past behaviour, no cost, no attempt to find a solution, and it followed the founder
      raising the topic rather than being volunteered.
    next: >-
      Do not count this toward H3A1. If Stoneside is worth pursuing, the real test is the
      premises visit and whether they will show their actual remake log.

  - id: E12
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A3
    verdict: contradicts
    confidence: 4
    source_type: commercial_data
    source: >-
      US Census SUSB 2022, "Number of Firms and Establishments, Employment, Annual Payroll and
      Receipts by Industry and Enterprise Receipts Size" — the keyless bulk workbook, since the
      Economic Census ecnbasic API returns HTTP 302 without a key. Collected by
      scripts/research/t2_susb_market_ladder.py, laddered by
      scripts/research/analyse_market_ladder.py.
    claim: >-
      The remake pain is concentrated precisely where there are almost no buyers, and the
      buyers are concentrated precisely where the pain per firm is trivial. In blind and shade
      manufacturing (NAICS 337920, $2.48bn, 302 firms) the largest TEN firms hold 62.5% of all
      revenue, and each carries $4.6m-$15.5m of remade order value a year at a 3%-10% rate. At
      the bottom of the same ladder, 27 firms under $100k of receipts carry $1,747-$5,825 each.
      Window treatment retail (442291, $2.77bn, 1,901 firms) is flatter but the same shape:
      4 firms hold 19%, while 801 firms under $500k carry under $29k each.
    why_it_matters: >-
      Answers the founder's question — is even enterprise affected, or do they not care — with
      a structural yes, and kills the obvious go-to-market in the same breath. A firm losing
      $5,000 a year cannot buy anything; a firm losing $15m a year can buy almost anything. So
      this is an ENTERPRISE sale to roughly ten manufacturers, not a product-led motion across
      two thousand small dealers.
    limits: >-
      NAICS undercounts this trade. Budget Blinds has 1,100+ US franchise locations whose
      franchisees may classify under contractors rather than 442291; Home Depot, Lowe's and
      Costco sell made-to-measure blinds and appear in neither code. The remake rate is
      UNMEASURED — 3%-10% is assumed, which is the entire reason H3A1 exists, and every dollar
      figure moves linearly with it. The $100,000+ band is open-ended, so its per-firm figures
      are floors.
    next: >-
      Reweight outreach toward the ten large manufacturers, and identify which firms occupy
      that band before spending the batch on micro-dealers who structurally cannot buy.

  - id: E13
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: contradicts
    confidence: 4
    source_type: commercial_data
    source: Same SUSB ladder as E12.
    claim: >-
      A blinds-only software business cannot reach venture scale in the US. Pricing every firm
      in both industries at an affordability-anchored seat price — nothing under $500k of
      receipts, $3k to $2.5m, $12k to $10m, $40k to $30m, $150k above — returns a ceiling of
      $9.3m ARR with 100% of the market bought, no competitor and no churn. The same ladder
      puts the wider made-to-measure pool at $108.5bn across five adjacent industries that all
      cut to a site-taken dimension: finish carpentry $42.97bn, wood kitchen cabinets and
      countertops $20.32bn, wood windows and doors $19.13bn, glass and glazing $18.08bn, cut
      stone $8.00bn. Blinds is 4.6% of that pool.
    why_it_matters: >-
      Directly answers "I am not convinced this is a VC-grade opportunity", and the arithmetic
      says the instinct is right for the narrow version. Three routes remain and they are
      different companies: take manufacturing revenue rather than a tool fee ($2.48bn TAM,
      1% = $25m), generalise the measure-to-machine path across made-to-measure generally
      ($113.75bn pool), or go global. Blinds survives as a BEACHHEAD — 302 manufacturers is a
      countable market to learn in — but not as the destination.
    limits: >-
      The seat prices are modelled, not observed, and no comparable vendor's pricing was
      checked. A per-order, per-remake-avoided or share-of-savings model against $158m-$525m of
      remade value is a different calculation and could land materially higher. The adjacency
      pool is measured, but nothing here establishes that one product serves a stonemason and a
      blind maker — that is an untested assumption.
    next: >-
      Put the wedge-versus-destination question to the founder rather than researching further.

  - id: E14
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 4
    source_type: commercial_data
    source: >-
      US Census Annual Retail Trade Survey 2022, "Estimated Annual U.S. Retail Trade Sales -
      Total and E-commerce", keyless bulk table. Collected by
      scripts/research/t2_census_arts_ecommerce.py.
    claim: >-
      US retail e-commerce was 14.4% of all retail trade in 2022 ($1,013bn of $7,041bn), and
      furniture and home furnishings STORES sold 3.3% of their own sales online ($4.8bn of
      $143.6bn) while nonstore retailers sold 70.7% online. There is no measured figure, keyless
      or otherwise, for the online share of window coverings specifically.
    why_it_matters: >-
      Corrects a number that was about to sit at the centre of the H3 statement. A "16% of
      window covering sales happen online" figure was recalled as prior research. It is not in
      this repo. The nearest thing is `online_addressable_share` base 0.15 in
      cabinet_tam_model.json, which REPORT.md itself labels an ASSUMPTION ("Census e-commerce
      share by merchandise line would measure it"), which concerns custom CABINETS, and whose
      own code comment calls it "the assumption that most needs testing". The remembered 16%
      is almost certainly the all-retail e-commerce headline — 14.4% here, around 16% by 2024
      — which says nothing about window coverings. The H3 statement was therefore written to
      claim that the measuring step CAPS the online share without asserting what the share is.
    limits: >-
      ARTS reports e-commerce by the SELLER's kind of business, not by merchandise line: a
      sofa bought on Wayfair counts under nonstore retailers, not under furniture stores. So
      3.3% is not "3.3% of furniture is bought online" and must never be quoted that way.
      Merchandise-line detail lives in the Economic Census, whose API returns HTTP 302 without
      a CENSUS_API_KEY.
    next: >-
      Treat the online share of window coverings as an OPEN QUESTION, not a known number. It is
      measurable with a free Census API key via merchandise-line detail, or approximately from
      the revenue split between 442291 window treatment stores and the online-only sellers.
      Until then no percentage belongs in the hunch statement.

  # ─── Blinds.com in-home measure appointment, 2026-09-03. Founder-conducted, in person. ───
  # An installer/technician working the SF and Oakland service area. First look inside the
  # operating model of the largest made-to-measure retailer in the category.

  - id: E15
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A2
    verdict: contradicts
    confidence: 4
    source_type: customer_interview
    source: >-
      In-person conversation with a Blinds.com measure technician during a booked in-home
      appointment for six windows (San Francisco). Founder-conducted.
    claim: >-
      When an order comes back with the wrong measurements, the technician described the cause
      as roughly a 50/50 split: half the time it is the technician who made the error, half the
      time it is the factory that made a manufacturing error.
    why_it_matters: >-
      This is the most important entry so far and it directly contradicts H3A2 as written.
      H3A2 claims the error originates at measurement capture RATHER than in manufacturing
      tolerance. A 50/50 split means the mechanism is at best half right, and a product that
      only fixes the measurement addresses only half the failures. It does not kill the lane,
      but it halves the value of any measurement-only answer and forces the question of what
      the factory-side half actually is.
    limits: >-
      "50/50" is one technician's impression, not a logged rate, and he is describing his own
      error class alongside the factory's, which invites self-serving rounding in either
      direction. n=1 and no absolute frequency was given: this is a split of errors, not a rate
      of errors.
    next: >-
      Get the denominator. "Out of how many jobs?" Then ask what the factory-side failures
      actually are: wrong fabric, wrong cut, wrong hardware, or the factory building correctly
      to a number that was already wrong when it arrived.

  - id: E16
    date: 2026-09-03
    hunch: H3
    assumption_linked: H3A3
    verdict: supports
    confidence: 4
    source_type: customer_interview
    source: Same Blinds.com in-home appointment as E15.
    claim: >-
      Blinds.com provides complimentary measure visits and covers all rework costs when their
      own technician took the measurement. It sits in the company's liability and P&L. If the
      CUSTOMER places the order on their own measurements, Blinds.com absorbs none of it.
    why_it_matters: >-
      This is the H3A3 answer, and it is a named, concentrated cost owner. The retailer pays
      for both the visit and the rework, on their own P&L, whenever they touch the measurement.
      That is a party with a direct financial incentive to make the measurement cheaper or more
      reliable, which is exactly what H3A3 asked for. It also corroborates E7 independently:
      Stoneside pushes liability to the customer on self-measurement in the same way. Two
      unrelated companies, same rule.
    limits: >-
      No figures. Not the cost of a visit, not the rework rate, not what either line is worth
      annually. The technician described the policy, not the P&L.
    next: >-
      This question now belongs to someone above the technician. C-level and merchandising
      contacts at Global Custom Commerce / Blinds.com are already in the ledger; the ask is the
      rework line as a share of category revenue.

  - id: E17
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 4
    source_type: customer_interview
    source: Same Blinds.com in-home appointment as E15.
    claim: >-
      Blinds.com performs the measure and fit service itself, then disperses orders to a range
      of different manufacturing vendors. It services San Francisco and Oakland directly; orders
      outside that area are moved to franchises.
    why_it_matters: >-
      Recorded as AMBIGUOUS because it cuts both ways and the founder should see both. It
      confirms the routing structure the founder identified: measurement is captured centrally
      and production is fanned out to many factories. But it also means the largest player in
      the category ALREADY OPERATES that router, including the franchise overflow for
      out-of-area demand. An "open router for window coverings" is therefore not an unoccupied
      gap; it is the incumbent's core model. The unoccupied part, if there is one, is the
      accuracy of the measurement that enters the router, not the routing.
    limits: >-
      One technician's account of his employer's operating model. Vendor count, how routing
      decisions are made, and whether franchises use the same factories are all unknown.
    next: >-
      Before treating routing as the product, establish what Blinds.com cannot do that a
      neutral router could. If the answer is nothing, the wedge is the measurement layer they
      would buy, not the router they already run.


  # ─── Economic Census merchandise line, collected 2026-09-03 once CENSUS_API_KEY existed. ───
  # E14 left the online share of window coverings as an OPEN QUESTION and named the exact
  # source that would close it. E18 closes it. E19 carries the size numbers that came with it.

  - id: E18
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: contradicts
    confidence: 4
    source_type: commercial_data
    source: >-
      2017 Economic Census, dataset `ecnnapcsprd`, product line NAPCS 5000625000 "Retail sales
      of window treatments, including rods, poles, and fixtures", split across the industries
      that sold it. Benchmarked against Census ARTS all-retail e-commerce for the same year.
      Collected by scripts/research/t2_census_merchline_window.py.
    claim: >-
      In 2017, electronic shopping and mail-order houses (NAICS 454110) booked $3.76bn of the
      $11.80bn US retail window-treatment line — 31.9%, a figure Census publishes directly as
      NAICSALL_PCT rather than one derived here. All US retail was 8.8% e-commerce that year
      (ARTS), so the category ran roughly 3.6x the all-retail rate. The
      visit-based channels were the minority: in-home direct selling 12.2% and window treatment
      stores 11.9%, 24.1% together. The largest single channel was home centers at 33.7%.
    why_it_matters: >-
      The H3 statement says the measuring step "caps the category's online share". A category
      selling at 3.6x the all-retail online rate is not behaving like one with a cap, and 31.9%
      is roughly double the 16% that was recalled from memory and corrected in E14. If a cap
      exists it sits far above where the hunch implied, and above the point at which "you must
      send someone to the window" can be the binding constraint on the whole category. What
      survives is the narrower claim: the visit binds the MADE-TO-MEASURE part, which this line
      cannot isolate.
    limits: >-
      Three limits, and the first is the one that matters. (1) The line bundles a $12 curtain
      rod with a motorised made-to-measure shade — nothing in the Economic Census isolates
      made-to-measure, so this is the online share of the CATEGORY, never of the part H3 is
      about. (2) 2017, not 2022: the 2022 NAICS revision dissolved subsector 454 and moved the
      online-only sellers into the storefront industries, so 2022 publishes a line total
      ($9.63bn) with no online row at all — see E19. (3) 31.9% is a floor for online, not a
      ceiling: 454110 includes mail order, but home centers' and specialists' own websites are
      counted inside their store industries, so the true online figure is higher.
      (4) The 3.6x is a comparison across two different measurement bases and is directional,
      not like-for-like. 454110 classifies the SELLER (and includes catalogue mail-order, which
      2017 NAICS collapsed into the same code and which cannot be split out); ARTS classifies
      the TRANSACTION across all sellers including store-based ones selling online. The two
      errors run in opposite directions and partly cancel. The claim that needs no adjustment
      is the within-table one: the visit-heavy channels — in-home direct selling 12.2% and
      window treatment stores 11.9% — total 24.1%, less than the remote channel alone.
      Prefer "bought from a nonstore seller" to "e-commerce" when quoting this; the latter is
      an inference about the transaction, the former is what the row actually says.
      (5) US ONLY, and not by omission — `ecnnapcsprd` publishes no geography below the
      nation (its only geo variables are GEO_ID and NATION; a state query returns HTTP 400).
      The sister dataset `ecnnapcsind` does carry state, but returns the line for California
      only through the two channels with physical presence — window treatment stores $221.1m
      (91.1% of those stores' revenue) and other direct selling $222.7m (83.2%) — and zero
      for electronic shopping, home centers and department stores, which is non-publication
      rather than absence. A state-level online share would be meaningless anyway: an
      establishment is located where the seller is, not where the customer is, so a nonstore
      retailer's sales all land in one state regardless of where the blinds went. The 31.9%
      works nationally and nowhere else. Do not attempt a California version.
      Graded 4 rather than the default 5 for commercial_data because of limit (1) — the
      measurement is exact, the fit to the question is not.
    next: >-
      Two things settle whether the cap claim survives. Ask sellers directly what share of
      their own MADE-TO-MEASURE orders ship without a visit — that is the number this line
      cannot give and a dealer can. And decide whether H3's statement should be narrowed from
      "the category's online share" to "the made-to-measure share", because as written this
      entry contradicts it.

  - id: E19
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 5
    source_type: commercial_data
    source: >-
      2022 Economic Census, datasets `ecnbasic` (NAICS 337920, 449122) and `ecnnapcsprd`
      (NAPCS 5000625000). Collected by scripts/research/t2_census_merchline_window.py and
      scripts/research/t2_census_econ.py.
    claim: >-
      Measured 2022 sizes for the trade. Blind and shade MANUFACTURING (337920): 320
      establishments and $2.59bn of shipments nationally, 53 establishments and $389m in
      California. Window Treatment RETAILERS (449122): 3,276 establishments, 2,988 firms,
      $4.78bn of sales, 14,199 employees. The whole retail window-treatment merchandise line
      across every industry that sells it: $9.63bn over 65,753 establishments, of which 449122
      booked $4.60bn (47.7%) and home centers $2.82bn (29.2%).
    why_it_matters: >-
      Replaces an unsourced pair of numbers and explains a jump that would otherwise read as
      growth. The recon asserted "484 establishments, ~$2.4-2.5bn, NAICS 337920" with no URL;
      the revenue was close to right ($2.59bn) and the establishment count was not (320). More
      importantly, 449122 in 2022 is 3.1x the revenue of its 2017 predecessor 442291 ($1.52bn,
      1,816 establishments) — not because window treatment retail tripled, but because the 2022
      NAICS revision moved the online-only sellers into it. Blinds.com and its peers now sit in
      the same industry code as the storefronts they compete with, which is precisely why the
      online share is only measurable for 2017 (E18) and why any post-2022 "window treatment
      retail" figure quietly includes the online channel.
    limits: >-
      Manufacturing shipments and retail sales are different denominators and must not be added
      or compared: the $2.59bn made and the $9.63bn sold are the same product at two points in
      the chain, with imports and margin between them. The 2022 line total is not comparable to
      2017's $11.80bn either — the establishment universe was reclassified between the two.
    next: >-
      Use $9.63bn as the retail denominator and $2.59bn as the manufacturing one, and say which
      is which every time. Where a per-seller figure is needed, 449122's $4.78bn over 2,988
      firms is the measured average for a window treatment retailer.

  # ─── Anthropic Model Hardware Standard, previewed 2026-08-27. Desk research 2026-09-03. ───
  # The mechanics live in pages/system-architecture.html, which already carries the machine
  # inventory and the phase-4 plan. This entry records only what MHS does to the BELIEF.

  - id: E20
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 2
    source_type: company_statement
    source: >-
      Anthropic, "Previewing the Model Hardware Standard", research preview announcement,
      2026-08-27. https://www.anthropic.com/news/model-hardware-standard-research-preview
    claim: >-
      MHS is an open specification giving AI agents a standardised driver — read/write
      primitives, standard-format device discovery, and natural-language tags documenting each
      device's capabilities and safety limits. Anthropic's stated effect is that hardware
      integration drops from "weeks, if not months" to "hours or minutes"; launch partners
      report Carnegie Mellon at about eight hours against several weeks for a vendor build, and
      University of Washington connecting six instruments in under a week. Model-agnostic,
      reachable over MCP, research preview with stated intent to open-source. Named vendors are
      lab automation and cobots — Tecan, QIAGEN, Danaher, MBF Bioscience, Automata, Universal
      Robots, Doosan, AWS Strands Robots, Hugging Face LeRobot, Raspberry Pi. Stated limits:
      it needs a programmable interface and does not work with hardware lacking one, and Claude
      "did not yet understand the underlying physics" in liquid handling, with spatial and
      physical reasoning still requiring expert oversight.
    why_it_matters: >-
      Logged as AMBIGUOUS because it does two opposite things to the belief on the same day.
      It CONFIRMS the prediction half — Anthropic is building for exactly "manufacturing done
      through an app", and it is the founder's why-now with a date on it, six days before this
      entry. It ERODES the precondition half as a source of advantage: belief.md v3 names
      "interoperability stops being the bottleneck" as the primary threat to the belief, and
      MHS is that threat arriving, from a company that intends to open-source it. The company
      therefore cannot be the interoperability layer. What survives is the layer above it —
      knowing what to send the machines, which is precisely the gap Anthropic names in its own
      limitations, and which a mechanical engineer who ran a high-mix shop and measured the
      CAD-to-machine handoff is unusually placed to fill. Note also that this partially
      vindicates the `mess_is_the_market` thesis the founder reversed on 2026-08-31: MHS
      commoditises the programmable greenfield fastest, leaving the un-programmable installed
      base as the durable part.
    limits: >-
      A company's own announcement about its own unreleased product — graded 2, the
      company_statement floor, and the mechanism is what to grade, never the "hours or minutes"
      superlative. Research preview, not shipped or open-sourced yet. The integration-time
      figures come from launch partners Anthropic selected. Every named vendor is lab
      automation or cobots: no CNC, panel-saw, or woodworking controls vendor — no Homag,
      Biesse, SCM, Fanuc or Siemens — is on the list, so nothing here has reached the machines
      this wedge needs. pages/system-architecture.html already found only one genuinely
      MHS-ready machine on a blind fabricator's floor.
      Checked 2026-09-03: there is NO paper, NO published specification, NO GitHub repository
      and NO public documentation. The announcement and modelhardwarestandard.com carry prose
      plus an application form (https://forms.gle/UdQ8JubjMN1R5CJt8) and nothing else. The
      annotation layer is described only in words — no tag syntax, no schema, no field names,
      no sample reference file. So nothing can be built against MHS today, and no claim of MHS
      compatibility is checkable by anyone, us included. Do not cite a paper; there isn't one.
    next: >-
      The event to watch for is a woodworking or CNC controls vendor adopting MHS; that is what
      would move it from lab automation into this trade, and it is checkable monthly for free.
      Until then the un-programmable installed base is the moat rather than the standard, and
      the pitch should say the edge is the judgement above the interface, not the interface.

  # ─── Paper-mine batch 4, 2026-09-03. Two rows with no author-published address, kept here ───
  # because the finding outlives the contact. Rows dropped from research-map.md; ids in the
  # shortlist CSV. Both are technical claims — they may kill a technical premise, never a hunch.

  - id: E21
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 3
    source_type: article
    source: >-
      "LAP: An Agent-to-Instrument Protocol for Autonomous Science", arXiv 2606.03755,
      2026-06-03. https://arxiv.org/abs/2606.03755
    claim: >-
      An independent group specified the same edge MHS is standardising, three months earlier
      and in public. LAP names the gap precisely: MCP standardises agent-to-tool and Google's
      A2A standardises agent-to-agent, but neither models the agent-to-instrument edge, where
      operations are stateful, safety-critical, exclusively owned, physically embodied, and
      produce measurements carrying units, calibration and uncertainty. It adds four
      primitives: the InstrumentCard, a signed capability and physical-limit description; a
      first-class reservation for exclusive instrument locking; a safety-fence handshake with
      operator-confirmation tokens cryptographically bound to a task and its parameters; and a
      MeasurementResult schema that is physically typed (QUDT/UCUM), calibration-anchored and
      uncertainty-bearing. It encapsulates rather than replaces SiLA 2 and OPC-UA.
    why_it_matters: >-
      Two things, and they pull in opposite directions, which is why this is ambiguous.
      First, it answers a question MHS cannot: the founder asked for a concrete example of the
      semantic layer, and Anthropic has published none — no spec, no syntax, no sample file
      (E20). LAP's InstrumentCard is the public, specified analogue of exactly that object,
      and it is readable today. Second, it is independent convergence on the architecture in
      pages/system-architecture.html: LAP's MeasurementResult is required to carry its own
      uncertainty, which is the trust envelope — "a measurement system that cannot report its
      own uncertainty converts a known cost into an unknown one" — arrived at by a different
      group for a different domain with no knowledge of this repo. A load-bearing design
      decision getting independent support is worth more than another market number.
      The cost side: the agent-to-instrument edge now has at least two candidate standards and
      neither is ours. Whatever the company is, it is not that layer.
    limits: >-
      A protocol DESIGN paper. Roles, a six-layer architecture, a JSON-RPC method set and state
      machines are specified, and a closed-loop campaign is walked through the protocol — on
      paper. No deployment, no instruments, no measured integration cost. Scoped to autonomous
      science, not manufacturing, so the InstrumentCard is shaped for lab instruments rather
      than for machine tools. No author-published address in the source package, so the row was
      dropped from the research map and the team is not currently reachable.
    next: >-
      Read the InstrumentCard and MeasurementResult schemas properly before designing the
      MachineProfile — this is free prior art for the object Agent B has to emit. And watch
      whether LAP and MHS converge or fork; two competing agent-to-instrument standards would
      delay the whole premise by years, which is the risk to track rather than to assume away.

  - id: E22
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: supports
    confidence: 2
    source_type: article
    source: >-
      "Semantic Graph Unification for Industrial Digital Threads: Bridging 11 Heterogeneous
      Manufacturing Systems Through Ontology-Driven Knowledge Graphs", arXiv 2608.24918,
      2026-08-24. https://arxiv.org/abs/2608.24918
    claim: >-
      Unifying ERP, MES, PLM, SCADA, QMS and SCM into one RDF knowledge graph, the authors
      measure what the silos cost: blocking the 24 cross-system tools drops recall from 1.00 to
      0.31 and F1 from 1.00 to 0.48, so 69% of discoverable signals require joins that cross a
      system boundary. They also state the structural reason point-to-point integration fails —
      it scales as O(n squared) and accumulates brittle dependencies.
    why_it_matters: >-
      A number for the belief's link 1. The claim that software and machines do not talk is
      usually argued anecdotally; this puts 69% on how much is invisible without crossing the
      boundary, and the O(n squared) point is the same fixed-cost argument the pitch makes,
      arrived at from graph theory rather than from unit economics.
    limits: >-
      Eleven SIMULATED sources, not eleven real installations, and the verification manifest
      was author-constructed — the authors say plainly this is verification, not independent
      validation. So 69% is a property of their synthetic estate and must never be quoted as an
      industry figure. No author-published address; row dropped from the map.
    next: >-
      If a number like this is ever needed for the pitch it has to come from a real estate, not
      this one. Useful as a framing for why point-to-point integration is not the answer;
      useless as a measurement.

  - id: E23
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: supports
    confidence: 2
    source_type: article
    source: >-
      "Previewing the Model Hardware Standard", Anthropic, 2026-08-27.
      https://www.anthropic.com/news/model-hardware-standard-research-preview
      Origin detail from HHMI: https://www.hhmi.org/news/how-one-postdocs-problem-solving-changing-way-scientists-work
    claim: >-
      Anthropic opened a gated research preview of the Model Hardware Standard: a driver
      specification exposing any programmable device through read/write primitives, with a
      natural-language annotation layer that compiles into a machine-readable reference file
      naming what a device measures, what is adjustable and what safety limits are enforced.
      Reported partner results include a laser relock at QuEra going from 58% at ~150s per
      attempt to 99.3% at 0.9-5.4s, hardware integration at HHMI Janelia falling from multi-day
      to minutes, and a dose-response setup at Carnegie Mellon integrated in eight hours against
      the several weeks a vendor build takes. It originated with one Janelia postdoc's shared
      memory dictionary for a mixed-vendor microscopy rig.
    why_it_matters: >-
      Direct evidence for the belief's precondition clause - interoperability is being paid for
      by someone with the balance sheet to make it stick, which is what "the precondition is
      arriving" looks like. Two structural details transfer regardless of whether MHS itself
      ever reaches this trade. First, the annotation layer is a format for writing down tacit
      operator knowledge that appears nowhere in any API, which is the same artifact a
      deduction table is. Second, the QuEra result is an agent searching a physical system
      overnight and emitting a DETERMINISTIC script - the agent leaves before runtime. That is
      the pattern to copy, and it works there because a relock attempt consumes nothing and
      resets itself, which is not true of anything that cuts material.
    limits: >-
      An announcement, not a paper. No specification, no driver implementation, no repository is
      public; access is application-only. Every figure is Anthropic's, unverified. Anthropic's
      own stated limitation is decisive here: it requires hardware with a programmable
      interface, and the blind fabrication floor is almost entirely below that line - the only
      MHS-ready machine found there is the shutter router. Under the repo rule an announcement
      may not move a thesis, hunch or lane, and this one does not.
    next: >-
      The leading indicator is not more lab partners; it is a machine-tool builder shipping
      native write access, which cannot even begin before the spec is public. One open question
      would change the machine inventory materially: whether a PLC over Modbus TCP counts as a
      programmable interface. Worth asking if preview access is ever granted.

  - id: E24
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 3
    source_type: article
    source: >-
      BlindMatrix manufacturer ERP product page, swept 2026-09-03.
      https://blindmatrix.com/erp-for-manufacturers/ Corroborated by BlinQ
      (https://www.blinq.com.au/) and Quoterite (https://quoterite.com/).
    claim: >-
      BlindMatrix states its software will "generate the cut sheets, allowances, and
      manufacturing calculations" and "send the information about the cut lengths after adding
      or deducting the allowances" to integrated cutting tables via XML or CSV, plus barcode
      work orders. It claims 1,000+ businesses across the UK, US, Australia, Canada, New Zealand
      and South Africa. BlinQ ships order deductions and labels; Quoterite ships linked quoting
      and ordering. Aggregator revenue estimates: BlindMatrix ~$22m, Windowmaker ~$21.8m,
      Cyncly ~$420m.
    why_it_matters: >-
      Deduction-to-cut-list is a commodity feature of this trade's ERP, not an opening. Any
      product plan that entered by automating the office arithmetic is entering against
      twenty-year incumbents who already ship it to a thousand shops. It also cuts the other
      way and that is the more useful half: if the office side is already automated at this
      density, the remaining remake cost is pushed toward the window, which is where H3 says it
      is. And an order-to-cutting-table pipeline already installed in a thousand fabricators is
      the precondition for routing across them, not a competitor to it.
    limits: >-
      Company-authored marketing copy, not a demonstration or a customer account. "Integrated
      cutting tables" is unquantified - which machines, how many customers actually use it, and
      whether the integration is live or a professional-services project are all unknown.
      Revenue figures are aggregator estimates with no filing behind them and should be read as
      bands. Penetration among the SMALL fabricators that make up most of the trade is not
      established; the market-ladder page already found the bottom of the ladder cannot afford
      software.
    next: >-
      Ask any fabricator two things: which system they run, and whether their cut lengths are
      calculated by the software or by a person. The answer decides whether the office half of
      rework is already solved in the field or only on a website.

  - id: E25
    date: 2026-09-03
    hunch: H3
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 3
    source_type: article
    source: >-
      Capability sweep of nine software companies selling into window coverings and the
      adjacent window/door trade, 2026-09-03. Rendered at pages/capability-matrix.html;
      per-company sources on entries CO166-CO178 in outreach/companies.md.
    claim: >-
      Across every software product found in this trade - BlindMatrix, BlinQ, Quoterite,
      Cyncly, Windowmaker, Measure Square - not one captures a measurement without a person on
      site. Windowmaker, established 1983, sells an on-site measuring app that pairs with a
      laser, cross-validates readings against each other and derives frame sizes from
      clearances; every one of those features assumes a surveyor is standing at the opening.
      The comparable job HAS been removed in six other made-to-measure trades: roofing
      (EagleView), house exteriors (Hover, $60m Series D at $490m post led by three insurance
      carriers), optical (SiVIEW), footwear (Volumental), apparel (3DLOOK) and dental (Dandy).
    why_it_matters: >-
      The lane H3 is entering is empty of the thing H3 claims, and full of tools that stop one
      step short of it. Six other trades prove the job is removable and fundable, and that the
      party paying for measurement errors will fund its removal - the Hover round was led by
      Travelers, State Farm Ventures and Nationwide. Also relevant to how far any of it travels:
      all six are vertical-locked, and the only one that generalised (Hover) did so across
      products on ONE capture surface, never across domains.
    limits: >-
      Genuinely ambiguous and must not be read as confirmation. Forty-three years of an
      incumbent stopping at assisted recording is equally consistent with two opposite readings:
      that the visit cannot be removed at the accuracy this trade needs, or that nobody holding
      that distribution ever tried. Nothing on a website distinguishes them. Absence of a
      product is also not absence of an attempt - failed attempts do not publish.
    next: >-
      Ask someone who has been in the trade twenty years whether anyone ever tried to let the
      customer measure, and what happened. A single answer separates "untried" from "tried and
      failed", and it is the cheapest question on the list.
  - id: E26
    date: 2026-09-05
    hunch: belief
    assumption_linked: unassigned
    verdict: supports
    confidence: 4
    source_type: founder_interview
    source: >-
      C122 Leonard, Sanyo - 27 years in the role, manages the design team whose output feeds
      manufacture. Async text reply, founder-conducted, 2026-09-05. Full notes at
      03-validation/belief-2026-09-05/interviews/leonard-sanyo-2026-09-05-notes.md
    claim: >-
      Design errors reaching manufacture run at roughly one per 50 manufactured details in
      machine building - a 200-detail project sees four, and most machines carry at least 50
      manufactured components. The rate is not random: it trades directly against designer
      speed. Designers who produce almost no errors across 200 details habitually run at
      110-125% of budgeted hours, and designers who finish under budget make errors at roughly
      double the rate.
    why_it_matters: >-
      The first quantified rate this idea has for link 1 of the belief, from the segment the
      belief was drawn from, given without being pushed for it. It also converts the pain from
      a defect rate into a PRICE: accuracy is currently bought with hours, and the exchange
      rate is 10-25% of a program's budget. That is the number any software claiming to close
      the handoff has to beat, and it exists whether or not anyone counts the errors.
    limits: >-
      n=1, and every figure is a recalled estimate rather than a query against a system -
      nothing in the message says Sanyo tracks these. The speed/accuracy correlation may be
      Leonard's model of his own team rather than a property of the work. "Detail" is his unit
      and is not defined; it is assumed to mean an individually manufactured component. Machine
      building, not window coverings: this may not be cited against any H3 node.
    next: >-
      Ask a second machine builder for the same two numbers before treating either as a base
      rate. Then ask Leonard whether 1-in-50 is felt or tracked.

  - id: E27
    date: 2026-09-05
    hunch: belief
    assumption_linked: unassigned
    verdict: contradicts
    confidence: 4
    source_type: founder_interview
    source: >-
      Same message and same contact as E26. Split into its own entry because it grades a
      different claim in the opposite direction.
    claim: >-
      The party carrying this cost has consciously priced it and declines to remove it. Sanyo's
      standing policy is to get machines to manufacturing as fast as possible and repair on the
      floor. The known remedy - dedicated checkers verifying all dimensional information before
      release - is named unprompted and rejected as "hard to justify the cost". The deployed
      control is not process but hiring: designers falling outside the speed/accuracy band are
      replaced. In his words, "I accept the small mistakes and the time required to take care
      of those small mistakes."
    why_it_matters: >-
      A quantified pain that its owner refuses to pay to remove is the harder case, not the
      encouraging one, and it lands on the same nerve as H3A3 in a different industry: the cost
      is real, measured, and absorbed. It also names the substitute and its failure mode -
      verification priced as a full-time person never clears the bar, which is the fixed-cost
      argument in belief.md arriving from the buyer's own mouth rather than from a paper.
    limits: >-
      What is refused is a HUMAN checker at human cost; nothing here prices a cheap one, and he
      was never asked. His acceptance is also load-bearing for a 27-year professional identity,
      which is the kind of position that moves when the price does and not before. Read as
      revealed behaviour it is still a no: what he does is accept the errors. Whether the
      refusal survives a cheaper remedy is untested and is the next question, not this entry's.
    next: >-
      Sent 2026-09-05: whether checkers were ever actually run or only ever costed, and what
      the last non-small error cost. Tried-and-failed and never-attempted point at opposite
      conclusions, and this message cannot tell them apart.

  - id: E28
    date: 2026-09-05
    hunch: belief
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 2
    source_type: founder_interview
    source: >-
      Joseph Garza (C123), owner, Advanced Machine Program & Design MFG., Santa Clara. LinkedIn
      reply on 2026-08-31 to a Msg 1 sent 2026-08-25.
    claim: >-
      Asked where the margin on a new job goes between the quote and the first good part, a job
      shop owner answers entirely in estimating terms: "speed, complexity of the part and
      features, outside processes like Plating or Anodizing. All these have to come into factor
      before sending out a quote." He names the differentiators as experience, being a high
      performing shop, quality, and solving customers' problems. No number, no specific job, and
      no mention of drawings, models, files or anything arriving from the customer.
    why_it_matters: >-
      The first answer this idea has from someone who sets the price and then has to hit it. It
      puts the risk at estimating time and on work that leaves the building, which is a
      competing explanation for where a job's margin goes and one the belief has to beat rather
      than assume away. Outside processes are also the one item on his list that is a handoff to
      another party, which is the shape link 1 predicts, arriving without the vocabulary.
    limits: >-
      Generic DM commentary, not a recalled job, and every clause of it would survive being
      written by any shop owner in the country, which is why this is a 2. He was never asked
      about what the customer sends or what is missing from it, so the absence of the
      information handoff from his answer is not evidence that it costs him nothing. n=1, and
      the question itself was framed in margin terms, which invites an estimating answer.
    next: >-
      The same question, now asked on a call rather than in a DM: the last job whose margin came
      out worse than quoted, and what he found out about the part after the price had gone out. A
      specific job is the only thing that turns this from commentary into evidence. Read anything
      he says after 2026-09-05 with the reveal in mind, since the Msg 2 the founder chose to send
      states what is being built before he has named a job.

  - id: E29
    date: 2026-09-05
    hunch: belief
    assumption_linked: unassigned
    verdict: ambiguous
    confidence: 4
    source_type: founder_interview
    source: >-
      Shane Duncan (C125), CNC Programming Supervisor, B&B Manufacturing. LinkedIn reply
      2026-08-26, answering which step between the print landing and a good first part backs up
      most often for his group.
    claim: >-
      "I would say most jobs get held up the most in the quality department." Asked to name the
      bottleneck between a print arriving and a good first part coming off the machine, the man
      who supervises the programmers puts it after the machining, in inspection, and says it is
      most jobs rather than the difficult ones.
    why_it_matters: >-
      The first answer this idea has to the prove-out question from someone who can see every job
      his group runs. It puts the constraint on the CHECK rather than on the cutting or the
      program, which is the half of the belief that says a person has to stand there and verify
      what the software produced. It also relocates where the money would be: if the queue is in
      inspection, then anything that makes a part self-evidently right pays out in the quality
      department's calendar, not in cycle time.
    limits: >-
      Ambiguous because two very different mechanisms produce the same sentence and this one
      sentence cannot separate them. Reading A, the one the belief predicts: jobs sit because
      verifying a new part against what the customer specified is slow and manual. Reading B, the
      ordinary operations answer: the quality department is understaffed or the CMM is a shared
      bottleneck, which would be true whatever the software did. No mechanism, no duration, no
      cost, and no job named. "Most jobs" is his quantifier, not a measurement.
    next: >-
      Drafted 2026-09-05, unsent: on the last new part that sat in quality, what it was actually
      waiting on and roughly how long it sat. The answer separates reading A from reading B, and
      until it does this entry cannot move any node.


  - id: E30
    date: 2026-09-07
    hunch: H3
    assumption_linked: H3A5
    verdict: contradicts
    confidence: 4
    source_type: founder_interview
    source: >-
      Richard Jones (C43), Installations Manager, Specialist Blinds (London/Essex, UK).
      LinkedIn reply 2026-09-07 13:21, answering whether blinds ever arrive not fitting the
      customer's measurements. Volunteered BEFORE the founder disclosed what she is building
      at 13:23-13:24, so this half of the thread is uncontaminated.
    claim: >-
      "We don't rely on customers measurements, we Survey ourselves. Reason being customers
      don't always know to look out for obstructions or understand how some blinds need to
      operate or fit. Different blinds require more space for example. This catches customers
      out." The question presupposed a customer-supplied number; he rejected the premise and
      named what the survey is actually for.
    why_it_matters: >-
      The first source in this ledger that says what the home visit DOES, and it is not
      measurement verification. Three things he names - obstructions, how a given blind has to
      operate, and per-product clearance - are product knowledge applied to an opening, not
      dimensions read off it. H3's mechanism clause says "nothing can verify a measurement
      except a person standing at the window". A tool that returns a perfect, verified
      dimension does not know a handle is in the way, that a vertical needs stack space, or
      that this recess will not let the blind operate. On his account the visit survives that
      tool intact, and the online-share cap survives with it. Directly against H3A5, which
      asks whether measurement is the BINDING constraint on selling online.
    limits: >-
      n=1, one market (UK), one company that surveys as standing policy. He is describing why
      his employer does not accept customer numbers, which is not the same as saying no seller
      could. He was never asked to RANK measurement against fabric, colour and installation,
      which is what H3A5's next_action actually requires, so this narrows the mechanism without
      completing the ranking. He also has an interest here: surveying is his department.
    next: >-
      Ask him the same-or-different fork (LR-M5): whether the list of things that catch
      customers out is the same list at every window or a different one every time. Same means
      the survey encodes a rule set; different means it is irreducibly a person's judgement,
      and the hunch has to say which it is betting against. Then ask the H3A5 ranking of two
      more sellers who run both channels, without naming measurement first.

  - id: E31
    date: 2026-09-07
    hunch: H3
    assumption_linked: H3A1
    verdict: contradicts
    confidence: 2
    source_type: founder_interview
    source: >-
      Richard Jones (C43), Installations Manager, Specialist Blinds. LinkedIn reply
      2026-09-07 13:29, immediately after the founder disclosed at 13:24 that she is
      "looking into the re-work rates right now and if it contributes to margin".
    claim: >-
      "We manufacture our own blinds and the process we use works very well, our remedial
      rate is very very low." No figure, no period, no denominator. "Remedial" is his own
      word for it.
    why_it_matters: >-
      The first practitioner answer on the remake rate and it is a denial. H3A1 has no
      supporting entry either, so the rate this hunch was built to price against remains
      unmeasured after the first person asked about it said there is not much of one. His
      firm also manufactures and installs under one roof, which removes the handoff H3 is
      about - that makes it a boundary case for the hunch rather than a counterexample to it,
      and worth saying so explicitly.
    limits: >-
      Graded 2, not 4, for three reasons and any one of them would be enough. It is
      unquantified - "very very low" is a posture, not a rate. It arrived AFTER the founder
      named rework and margin as what she was looking for, so he knew which answer was
      interesting before he gave it. And training is his job function (profile: "Recruitment,
      Training, Managing/driving the business needs. Maintaining KPI's"), so a low remedial
      rate is his own performance number. Do not let this entry stand as the category's rate;
      it is one vertically integrated UK firm's self-report under a revealed hypothesis.
    next: >-
      Do not re-ask the rate on this thread - he has committed to a position and will defend
      it. If a number is ever wanted from him it comes as variance around his own claim
      (LR-M6), on a call, framed as what the low ones have in common. The rate has to come
      from sellers who do NOT own their factory.

  - id: E32
    date: 2026-09-07
    hunch: belief
    assumption_linked: H3A5
    verdict: contradicts
    confidence: 3
    source_type: founder_interview
    source: >-
      Richard Jones (C43), Installations Manager, Specialist Blinds. LinkedIn reply
      2026-09-07 13:29, same message as E31.
    claim: >-
      Asked nothing about solutions, he named one and dosed it: "heavily investing in
      training our field team + the factory technicians makes a huge difference... other
      companies within the uk give 1 months training, we allow a minimum of 6 months. It
      costs more in the short term but pays off in the long term." Plus a second mechanism:
      "we also expose them to working in the factory so they understand the bigger picture."
    why_it_matters: >-
      This is the counter-query answer - who tried and SUCCEEDED - arriving unprompted, and
      it is the most consequential thing in the thread. The belief says machines do not
      register manufacturing intent and that interoperability is the fix. He says the intent
      gap is real and that his firm closed it by putting the field team physically inside the
      factory until they carry the intent in their heads. That is the same problem solved by
      people rather than by a digital thread, at a stated price of five extra months of
      salary per technician - which is the first cost number anyone has put on the incumbent
      alternative. It also tells us what the software would have to beat: not nothing, and
      not a spreadsheet, but a six-month apprenticeship that his employer believes pays for
      itself.
    limits: >-
      Same contamination as E31 - it follows the reveal, and it is a training manager
      describing the value of training. "Huge difference" is uncounted. He gives no evidence
      that the 1-month firms actually have worse outcomes, only that they train less. And a
      six-month ramp is itself an argument the other way: it is a large, recurring, per-head
      cost that only works if you retain people, which is why it may be exactly the thing a
      shop with turnover cannot copy. Graded 3 rather than 2 because the dosage is specific
      and checkable against the UK trade, unlike the rate claim.
    next: >-
      Drill the cause, do not accept it (LR-M4). Ask what specifically a technician can do at
      month six that they could not at month one - the answer is a list of failure modes, and
      that list is either the same at every window (a rule set, therefore encodable) or
      different every time (judgement, therefore not). Separately, check the six-month figure
      against UK window-covering trade training norms before treating it as the industry
      baseline.
```
