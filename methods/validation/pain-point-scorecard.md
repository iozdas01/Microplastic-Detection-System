---
name: Pain Point Scorecard
category: first-principles
excluded_because: "ranks a slate of mined candidates — runs *after* a shotgun, on its output"
applicable_at: [validation]
assumption_categories_it_helps: [pain, buyer, market]
source:
  title: "Pain Point Analysis for Startups: How to Find Problems Worth Building Around"
  author: Miner
  url: ""
  date: "2026-04-15"
  note: "Framework for triaging between multiple pain candidates surfaced from public conversation mining before committing interview cycles."
---

## Core Insight

Public mining (Reddit, LinkedIn, job postings, review sites, community threads) reliably produces more clustered pain candidates than a founder can validate. The failure mode is not that pain is invisible — it's that founders can't tell which of the 5–15 recurring pains they've surfaced deserves the next interview cycle. Loudness, recency, and confirmation bias then decide, and the wrong pain gets the outreach budget.

The mechanism of the scorecard is compound scoring across dimensions that fail independently. A viral thread can be Severe and show Buyer Intent (reposts, "I'd pay for this") while having no Workaround Intensity — nobody built a spreadsheet, so the pain isn't costing anyone enough to reorganize behavior around. A quiet job posting can show high Cost of Inaction and Workaround Intensity (the company is hiring specifically to duct-tape a process) while nobody vents about it publicly. Any one dimension can be faked by a single loud post; six dimensions grounded in different evidence types cannot. The 1–5 score forces the founder to name the *specific evidence* per dimension per candidate — which is where hidden weak points surface.

The second mechanism is comparative discipline. A single pain scored in isolation always looks worthy — founders find reasons to keep any hypothesis alive. Scoring 3–4 adjacent candidates side-by-side against the same rubric collapses this bias: relative ranking beats absolute conviction, and the loudest candidate is often not the highest scorer once workaround intensity and buyer reachability are weighed.

The band interpretation (24–30 / 18–23 / 12–17 / <12) is a decision gate, not a truth claim — it tells you whether to spend interview budget, not whether to build. The gate exists so that a candidate must clear a bar across *all* dimensions, not just excel on one.

## Process

1. **Assemble a slate of 3–4 candidates, not one.** Pull the top clustered pain categories from Public Signal Reconnaissance. Never score a single candidate — comparative ranking is the point.
2. **Apply the workflow-pain filter before scoring.** For each candidate, ask: "If this problem disappeared tomorrow, would the user get back time, money, risk-reduction, or revenue?" If the answer is no, it's a feature opinion or aesthetic complaint — drop it from the slate before scoring. This kills 30–50% of surface-level candidates cheaply.
3. **Score each candidate 1–5 on all six dimensions, and cite the specific evidence per score.** A score without a verbatim quote or a named workaround behind it is a guess.
   - **Repetition** — how many independent sources and users mention this same pain? 5 = shows up across Reddit + LinkedIn + Jobs + reviews. 1 = one thread, one poster.
   - **Severity** — when the pain hits, how disruptive is it to the workflow? 5 = blocks a revenue-linked outcome (client delivery, compliance, safety). 1 = mild annoyance.
   - **Frequency** — how often does the user actually face it in normal work? 5 = daily or per-transaction. 1 = quarterly or rare.
   - **Cost of Inaction** — what does leaving it unsolved cost in money, time, risk, or missed outcomes? 5 = named dollar figures, lost accounts, compliance exposure. 1 = intangible discomfort.
   - **Workaround Intensity** — what have users already built to patch the problem? 5 = internal tools, Zapier chains, dedicated headcount, multi-tool duct tape. 1 = no visible workaround (either they live with it, or the pain isn't real).
   - **Buyer Intent** — do users ask for solutions, compare tools, mention budgets, or switch products? 5 = named-product comparisons + budget language. 1 = venting only.
4. **Sum and interpret against the bands.** 24–30 = strong pain, spend interview budget. 18–23 = promising, needs more segmentation or a second mining pass. 12–17 = real but weak — hard to monetize even if solved. <12 = noise, drop from consideration.
5. **Investigate any single 1 or 2 score before trusting the total.** A candidate with three 5s and a 1 on Workaround Intensity is not actually a 22 — the low score is a red flag that the pain doesn't cost enough for users to reorganize around it, which usually kills willingness to pay. Compound scoring is honest only when no dimension is fatally weak.
6. **Rank the slate and pick one winner.** If two candidates tie within 2 points, break the tie with a "budget-worthy" screen: which one has a reachable buyer (person suffering pain = person with budget authority), which one has visibly poor existing solutions, which one has evidence of switching behavior. High-pain and high-value are different — the scorecard finds high-pain; the tiebreaker enforces high-value.
7. **Feed the winner into the interview pipeline, not into a build decision.** The scorecard's output is which pain earns Mom Test interviews and outreach, not which pain becomes the product thesis.

## Example

An agency-operations founder surfaces four candidates from Reddit + review sites + X:

| Candidate | Rep | Sev | Freq | Cost | Workaround | Intent | Total |
|---|---|---|---|---|---|---|---|
| Manual monthly client reporting | 4 | 4 | 5 | 4 | 5 | 4 | **26** |
| Scattered client comms across channels | 3 | 3 | 4 | 3 | 3 | 3 | 19 |
| Proposal→project handoff friction | 3 | 3 | 3 | 3 | 3 | 2 | 17 |
| Analytics dashboards ugly on mobile | 2 | 2 | 3 | 1 | 1 | 2 | 11 |

Reporting scores 26/30 — Workaround Intensity 5 because agencies are duct-taping Airtable + Looker Studio + Google Slides + manual QA every month; Buyer Intent 4 because named-tool comparisons appear in threads. Strong band → merits interviews, pre-sell tests, and tighter segmentation on agency size and vertical.

Mobile-dashboard aesthetics scores 11 — annoying, high engagement online, but no workaround behavior and no cost of inaction. Drop it despite surface-level virality.

Comms-fragmentation at 19 is the interesting middle case: promising but not strong. Instead of running interviews now, do a second mining pass focused on this pain specifically, or segment further (small agencies vs. mid-size) before scoring again.

## Limitations

- **Scores are subjective.** Two founders will score the same candidate differently, and a founder who wants a pain to win will find reasons to inflate its scores. Have a second reader score independently and reconcile disagreements before trusting the total.
- **Dimensions compound bias if the source pool is narrow.** If all six scores are grounded in Reddit posts alone, you're not measuring six independent signals — you're measuring one biased source six times. Use the cross-source evidence matrix from Public Signal Reconnaissance so scores draw from genuinely different sources.
- **Buyer Intent is the hardest dimension to score honestly.** "I'd pay for this" in a Reddit thread is not the same as opening a wallet. Weight only concrete behavior — named-product switching, procurement mentions, RFP language, budget cycles — over stated intent. When in doubt, score Buyer Intent one point lower than your first instinct.
- **Bands are heuristic, not statistical.** A 23 and a 24 are not meaningfully different. Treat scores within 2 points of each other as ties and use the budget-worthy tiebreaker, not the total.
- **Low Workaround Intensity is almost always disqualifying.** If nobody has built a spreadsheet, hired someone, or duct-taped tools around the pain, either the pain isn't costing enough to reorganize around, or the solvers are invisible to your search. Investigate before trusting a high total that includes a low Workaround score.
- **Passes the gate ≠ builds the product.** A 26/30 pain earns interviews and outreach. It does not validate willingness to pay, solution shape, or founder-market fit. All of those still need their own tests downstream.
- **Does not adjust for market size.** A perfect 30/30 pain that only 200 companies globally have is not a fundable market. Pair with market-sizing evidence before committing beyond interviews.

## Connection to the Loop

Sits as the triage gate between public-signal reconnaissance and customer contact. Upstream: Public Signal Reconnaissance produces a clustered list of candidate pains with a cross-source evidence matrix — the scorecard picks which one earns the next interview budget. Also upstream: Hair-on-Fire Problem Classification is the market-type sanity check on the winning candidate — if the scorecard's winner falls in the Vitamin or Dead Zone on the magnitude × frequency 2×2, the total was misleading and the candidate is a false positive. Downstream: the winning candidate becomes the pain-of-record for Mom Test interviews, the language for Smoke Test Landing Pages, and the testable pain assumption in the Kill Criteria Contract.

Use it whenever multiple pain candidates have survived mining and you need to pick one to invest interview cycles in. Do not use it as a build gate, do not use it on a single candidate in isolation, and do not use it before running at least one cross-source triangulation.

See also: `ideation/public-signal-reconnaissance.md`, `validation/hair-on-fire-classification.md`, `ideation/jtbd-substitute-map.md`, `practices/mom-test-interview-script.md`, `validation/kill-criteria-contract.md`, `validation/idea-quality-score.md`
