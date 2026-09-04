---
purpose: The evidence ledger for this idea — every graded claim, linked to the assumption it moves and the direction it moves it.
idea: high-mix-manufacturing
last_updated: 2026-09-03
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
      $11.80bn US retail window-treatment line — 31.9%. All US retail was 8.8% e-commerce that
      year, so the category was 3.6x more online-penetrated than retail as a whole. The
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
```
