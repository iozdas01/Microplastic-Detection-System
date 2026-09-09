# Search passes and run mechanics

Loaded per stage by `startup-outreach-targets`. The SKILL.md carries the decision procedure and the guardrails; everything here is the mechanics of executing a pass — the five passes in order, volume caps, title ranking, pagination, enrichment, scoring, setup, write format, and the failure catalogue.

## Search flow — 5 passes, in this exact order

**50 contacts total per batch, then rank and repeat.** Passes are ordered by expected reply rate, highest first. Every pass is filtered against the assumption's ICP so we never contaminate the pool with off-scope contacts (an adjacent-technology vendor is not a demand-side buyer).

**Passes 0 and 1 use the founder's LinkedIn data export — no browser at all.** Only Passes 2-4 need the browser. Do the file passes first; they're free, complete, and they tell you how much cold browsing is actually left to do.

### Pass 0 — Prior-contact backfill from the export (no browser)

**Why first:** `contacts.md` only knows about people *this repo* invited. The founder has years of LinkedIn history before that — people already messaged, already replied, already gone quiet. Writing to someone the founder messaged eight months ago as if they were cold is the worst failure mode in outreach, and it's entirely avoidable from a local file.

```bash
.venv/bin/python -m scripts.data.linkedin_export history
```

Returns every person the founder has ever messaged or invited, with `outbound_count`, `inbound_count`, `last_message`, and a `suggested_outreach_status`.

**How to use it:**
1. For anyone already in `contacts.md`, compare `suggested_outreach_status` against the stored `outreach_status`. Where they disagree, surface the conflict to the founder — do not silently overwrite. The stored status came from a tracked outreach cycle; the export is historical context.
2. For anyone NOT in `contacts.md`, hold the record in memory. If Pass 1 later surfaces them as an ICP match, attach the history to their contact row.
3. Never write a contact to `contacts.md` from Pass 0 alone. History is not ICP fit — plenty of people the founder has messaged are irrelevant to this assumption.

**The suggested statuses are conservative and mean exactly this:**

| Suggestion | Means | What to do |
|---|---|---|
| `replied` | they have sent the founder a message at some point | treat as a warm contact; note the date in `notes:` |
| `no_reply` | founder messaged, no reply in the archive | do NOT re-blast blind — flag to the founder first |
| `invited` | invite sent, never messaged | safe to treat as `pending` for this assumption |
| `pending` | no prior contact at all | normal cold path |

**A stale `no_reply` is not a permanent no.** A message sent two years ago about an unrelated topic doesn't disqualify someone from this assumption. Surface the date and last message direction and let the founder decide.

### Pass 1 — 1st-degree network from the LinkedIn export (no browser)

**Why:** existing 1st-degree contacts already know the founder and reply at 5-10x the cold rate. The export contains the founder's *entire* 1st-degree network with position and company already attached — so this pass is a local file filter, not a search sweep. It is complete by construction: LinkedIn search samples, the CSV doesn't.

**Derive the filter arguments from `graph.md`, not from a hardcoded list.** Use the "Dynamic title-ranking" section below to extract domain vocabulary from the assumption and score each `icp_valid_titles` entry into Tier A / B / C. Then pass them in:

```bash
.venv/bin/python -m scripts.data.linkedin_export connections \
  --title "<Tier A title>" --title "<Tier B title>" \
  --domain-noun <noun> --domain-noun <noun> \
  --exclude recruiter --exclude <adjacent-industry noun>
```

- `--title` — every Tier A and Tier B title from `icp_valid_titles`. Matched against the connection's `position`. Generic seniority words (`Head of`, `Director`, `Senior`) are stripped before matching, so one title phrase catches its variants.
- `--domain-noun` — every domain noun-phrase extracted from the assumption text. Matched against `position` OR `company`, which catches in-domain people whose title is generic.
- `--exclude` — every `icp_out_of_scope` pattern. Checked first and wins outright over any title or noun match.
- Tier C titles: pass them as `--title "<tier C title> <domain noun>"` so the domain token is required. Never pass a bare Tier C title.

**Pass every derived title in one command.** There's no rate limit and no cost per keyword — the whole list runs against the same in-memory CSV in well under a second. Nothing here can "bail early", which is why this pass no longer needs the `.pass1-manifest.jsonl` guard that the old browser sweep required.

**Tune the filter before accepting the output.** Run once with `--include-rejected` and read the rejects. If real ICP people are landing in `rejected`, the title/noun list is too narrow — widen it and rerun. This is free; do it until the keep/reject split looks right.

**Zero keeps is a real finding here, not a search artifact.** With the old browser sweep, zero hits could mean the keyword phrasing missed. Against the full CSV, zero ICP matches means the founder genuinely has no 1st-degree network in this domain. Record that and move to Pass 2 — don't retry with more phrasings beyond one honest widening.

**What the export does NOT give you:** `open_to_work`, `mutuals_count`, `active_last_30d`, and current-role accuracy (`position` is as of the export date). Contacts from this pass enter with `signal_type: profile_fit`, `signal_multiplier: 1.0`, `degree: 1st`, and still need the profile-visit enrichment step before scoring. Enrich only the ones that survive the ICP filter — that's the whole saving.

**If the export is missing or stale**, the command exits 2 with instructions. Tell the founder how to refresh it (LinkedIn → Settings → Data Privacy → Get a copy of your data → Connections + Messages + Invitations, unzip to `private/linkedin-export/`), then continue to Pass 2 for this session. Do NOT fall back to browser-sweeping the 1st-degree network — that's the expensive path this pass exists to replace.

### LinkedIn search is fuzzy — filter results CLIENT-SIDE, not via quotes

**Applies to every browser pass (2, 3b, 4). Not Pass 1, which reads a CSV.**

**LinkedIn's people search does NOT support quoted exact-phrase queries.** Wrapping a three-word title in double quotes does NOT return "titles matching exactly this phrase" — LinkedIn either strips the quotes (making the search identical to unquoted) or interprets them as literal characters (returning zero results).

**What actually happens:** LinkedIn people search fuzzy-matches on individual words. A title like `<Domain> Reliability Engineer` unquoted returns everyone with "Reliability" OR "Engineer" in their title — SREs, chemical engineers, satellite engineers — because the one word that carried the domain is the word it dropped.

**Correct approach — filter results in code, not in the query:**

1. Run the search **unquoted** (natural LinkedIn behavior).
2. After extracting results from the DOM, apply a **title-substring filter** in Python/JS: keep only results whose extracted title contains every content word of the keyword, case-insensitively — the domain noun AND the function noun. Allow the leading role word to vary ("Head of" / "Director of" / "Manager of").
3. The specificity discipline lives in the filter, not the query. This lets LinkedIn's fuzzy match surface adjacent titles (`Head of <Domain> O&M` for `Head of <Domain> Operations`) that a strict-phrase search would miss.

A big gap between raw hits and kept-after-ICP is expected and healthy — that's fuzzy-match noise being correctly rejected, not a bug. `scripts/data/linkedin_export.py` implements the same token-matching rule for Pass 1, so both paths filter consistently.

### Pass 2 — Content search for pain keywords (post_engagement signal)

**Why second:** people who publicly post about the topic reply at very high rates when you reference their own words. This is where hot signals come from.

**How:** Use LinkedIn content search — `linkedin.com/search/results/content/?keywords=<pain_term>&sortBy=%22date_posted%22`. Extract post authors + a compact excerpt of what they posted (`signal_excerpt`).

Keywords must be technical noun-phrases the target segment would actually use in a complaint — NOT sales speak. Shape: `"<work task> mobilisation"`, `"<pain outcome> <asset noun>"`, `"<domain> O&M cost"`, `"<inspection task> campaign"`. These come from the assumption's disconfirmation clause and its target segment's vocabulary.

Save each post author's URL + excerpt → hand to Pass 3 for profile verification before adding to contacts.md.

### Pass 3 — Profile verification (filter false positives from Pass 2)

**Why:** LinkedIn's content search fuzzy-matches on keywords and returns people from adjacent industries, recruiters posting about the topic, and vendors pitching into the space. Profile verification filters those out.

**How:** For each author from Pass 2, visit their profile once and verify:
1. Their current role (from Experience section) is in the assumption's ICP domain
2. Their company tier is in `icp_valid_tiers` (or, if the company is unknown, the role itself clearly places them in-domain)

If either check fails, drop the contact. The nature of the post — complaint, commentary, news-share, thought-leadership — is **not a filter**. Anyone posting about the topic has demonstrated genuine interest in the space and is worth talking to. The only gate is ICP membership.

If they pass both checks, add to `contacts.md` with `signal_type: post_engagement`, `signal_multiplier: 1.5`, and store the exact excerpt in `signal_excerpt`.

**Then preserve the exact excerpt and recency in `contacts.md`, and put the contact at the top of the handoff to `startup-outreach-draft`.** The signal is time-sensitive, but message preparation still belongs to the draft skill, which reopens the live profile before making any claim.

### Pass 3b — LinkedIn Groups (domain self-selection signal)

**Why:** Group membership is explicit domain self-selection — joining a named industry practitioners' group requires more intent than appearing in a keyword search. Active members (who posted or commented in the group recently) are among the highest-signal contacts you can find.

**Step 1 — Find and join all relevant groups.**

Search LinkedIn Groups: `linkedin.com/search/results/groups/?keywords=<domain_term>`. Use the domain noun-phrases from graph.md (same vocabulary as Pass 2). For every group with > 200 members that is clearly domain-relevant, log it to `groups.md` (name, URL, member count). Then present the list to the founder: "Found N relevant groups — [list]. Want me to request to join all?" Proceed once confirmed. Joining is a visible action on the account profile — batch the requests and confirm once rather than auto-clicking.

Log every requested group (name, URL, member count) to `reports/outreach/groups.md` so membership status can be tracked across sessions. Membership approval may take hours — continue to Pass 4 for this session and return to Pass 3b next session for any newly approved groups.

**Step 2 — Browse group members.**

For each group the sending founder is already a member of, navigate to the group page and click the member list. LinkedIn shows members ordered by recency of activity. Extract members who appear near the top (active recently).

```
https://www.linkedin.com/groups/<group_id>/members/
```

Paginate via Next. Cap at 50 members per group per batch — active members cluster near the top.

**Step 3 — ICP filter.**

Same two checks as Pass 3:
1. Current role is in the assumption's ICP domain
2. Company tier is in `icp_valid_tiers`

If either fails, drop.

**Step 4 — Signal tier.**

- **Active member** (posted or commented in the group in the last 30 days — visible in their recent activity or as a top post in the group): `signal_type: group_active`, `signal_multiplier: 1.5`. Store the group name plus the exact post/comment excerpt and URL, then prioritize the contact in the blast handoff.
- **Passive member** (joined but no visible recent activity): `signal_type: group_member`, `signal_multiplier: 1.0`. Store the group name and add the contact to the normal blast batch.

**If no memberships are approved yet:** don't skip to Pass 4 without logging. Write the join requests, record them in `groups.md`, then continue to Pass 4 for this session. Pass 3b runs properly next session once membership is approved. Tell the founder how many join requests were sent and which groups.

### Pass 4 — 2nd-degree by title × company (fallback for volume)

**Only run this if Passes 0-3 have not delivered enough contacts to reach the 50-per-batch target.**

**How:** If `companies.md` exists, search each matching company **sorted by
`pain_score` descending** (highest-pain companies first), using `<title>
<company>` or the direct company-people URL. If it does not exist, use the
same pass with `<title> <domain qualifier>` and the assumption's declared ICP
vocabulary. Then click the **"2nd"** connection filter chip, paginate, apply
the ICP filter, and add qualified results to `contacts.md`.

When `pain_score` exists, sort by it: company contracts, {operational-loss signal}, or
hiring can prioritize the batch. If it is missing, sort by declared ICP tier
and live profile fit; do not pause the outreach cycle to run enrichment.

Cap at whatever's needed to reach 50 — no need to grind out hundreds raw when a few dozen targeted results suffice.

## Priority handoff for time-sensitive signals

`post_engagement` and `group_active` evidence can decay quickly. Record the exact excerpt, source URL, and observed date in `contacts.md`, rank those contacts first in the handoff summary, and recommend running `/startup-outreach-draft A{X}` immediately after the target batch. Do not draft or send a message here. The draft skill owns Msg 1 preparation and must verify all wording against a fresh live-profile snapshot before the founder clicks Send.

## Minimum viable batch — 50 contacts, spread across tiers + companies

**A batch is not complete under 50 in-ICP contacts.** Stopping at 15 or 20 is
NEVER acceptable — the founder cannot run meaningful outreach on fewer than
50 conversations across the different tiers of the value chain.

### Target composition per batch

| Axis | Minimum |
|---|---|
| Total contacts | **≥ 50** |
| Per tier in `icp_valid_tiers` | **≥ 10** (goal: 15, cap the top-3 tiers at 15+ each) |
| Companies represented | **≥ 10** distinct employers |
| Per company | **≤ 5** (already documented) |
| Response-likelihood spread | Mix of 1st / 2nd / 3rd — 3rd-only is fine when 1st/2nd are exhausted |

The 10-per-tier floor means an assumption declaring five tiers in `icp_valid_tiers`
needs at least 40-50 across them (some tiers may be thin because the
value chain isn't symmetric — that's fine, but never leave a tier at 0
unless the ICP explicitly says the tier isn't real for this domain).

### Two-phase acquisition to hit the floor

**Phase A — Company-scoped scrape (when companies.md exists).**
When the registry exists, iterate every matching company sorted by `pain_score`
desc, then by tier priority. For each, run the company-people URL with the
assumption's top title-keyword and extract up to 5 keepers. This is a fan-out
across the registry, not a company-by-company decision.

**Phase B — Broader LinkedIn people search (default when no registry exists,
or whenever Phase A yields < 50).**
When Phase A is exhausted and total < 50, drop the company scoping and type
`<title> <domain>` into LinkedIn's top search bar (or navigate to
`linkedin.com/search/results/people/?keywords=<title>+<domain>`). Then click
the **"2nd"** connection filter chip on the results page. Do NOT stuff
`network=%5B%22S%22%5D` into the URL — the on-page chip is more reliable.

Iterate the domain-specific titles from Tier A of the title-ranking. Cap at 15
keepers per title. This is the normal direct-outreach path and also surfaces
contacts at companies not present in any registry.

If `companies.md` exists, append newly discovered companies with a
`linkedin_slug` and evidence-backed tier. Do not fabricate company-level API
signals merely because a profile revealed a new employer.

### Company diversification rule

Even before hitting 50, if a single company already has 5 contacts AND
another tier has 0 contacts, PRIORITIZE the empty tier over hitting 5 at
the next company. A batch with 5×5 at one tier and 0 at four other tiers
is worse than 3×5 balanced across 5 tiers.

## Volume caps and prioritization — apply to every contact write

**Max 5 contacts per company per assumption.** Once 5 contacts at the same
`company` are in `contacts.md` for this A_ID, stop adding more from that
company. Rationale: outreach is one-at-a-time — the founder messages contact A
today, waits ~24h for a reply, if no reply moves to B, and so on. Any more
than 5 per company is queue-clogging that never gets used. If contact 6+ at
the same company shows up during scraping, log it to `.overflow-{company}.jsonl`
for a possible future batch, don't add to contacts.md.

**Pick the highest-response-likelihood 5 per company** before writing:
- 1st-degree > 2nd-degree > 3rd+
- open_to_work > active_last_30d > dormant
- higher mutuals_count > lower
- higher role_pts (buyer > practitioner/expert > influencer)
- title contains a domain noun > generic title

If you scrape 20 candidates at {Operator Co}, sort by the composite above and take
top 5. Write those 5. Log 15 to overflow.

**Geographic prioritization based on the founder's travel plans.**
Read `memory/MEMORY.md` for `founder_travel_plans` entries (e.g.
"in SF next month", "in London Nov 15-22"). Contacts based in those
locations get a +1 prioritization boost — they're candidates for
in-person coffee, which converts 3-5x better than a call.

For A2 (2026-07 — founder in SF next month): SF Bay Area contacts get
priority in the top-5 pick. Look at the `location` field from LinkedIn
snippet — `San Francisco`, `SF Bay Area`, `Bay Area, California`,
`Palo Alto`, `Berkeley`, `Oakland` all count.

## Dynamic title-ranking — pick the RIGHT titles per assumption

**Do NOT iterate `icp_valid_titles` in list-order.** That produces massive waste
(searching "Head of O&M" returns aerospace / defense / telecom / manufacturing
heads because "O&M" is a domain-general term). Instead, rank titles by
domain-specificity and run the best ones first.

### Step A — extract domain vocabulary from the assumption

Read `graph.md` → `assumption` + `disconfirmation` + `icp_segment`. Extract
the domain noun-phrases the pain lives in:

- For a health-tech assumption: `patient`, `EHR`, `claims`, `RCM`, `RVU`
- For a logistics assumption: `TMS`, `linehaul`, `dwell time`, `yard`, `drayage`
- For a legal-tech assumption: `matter`, `docket`, `discovery`, `billable hour`

The domain vocabulary is EXTRACTED FROM THE ASSUMPTION at run time — never
hardcoded to any industry.

### Step B — score each title in `icp_valid_titles` by domain-specificity

For each title, compute a specificity tier:

- **Tier A** — title CONTAINS at least one domain noun from Step A: the noun sits
  inside the role name (`<domain noun> Portfolio Director`, `<domain noun>
  Reliability Engineer`, `Head of <domain noun> Services`, `<domain noun>
  Inspection Lead`, `Site Manager (<operating site>)`).
  **Search these AS-IS on LinkedIn** — every result is domain-relevant, high
  ICP-fit rate expected.

- **Tier B** — title is DOMAIN-ADJACENT (implies the domain via context) but
  doesn't contain the exact noun: `Head of <domain noun> Operations`,
  `Regional O&M Director`, `Head of Asset Management`, `Head of Service Operations`.
  **Search these AS-IS on LinkedIn** — usually yields a mix of domain + adjacent
  industries; ~40-60% ICP-fit rate.

- **Tier C** — title is GENERIC across industries: `Head of O&M`,
  `VP Operations`, `VP O&M`, `Operations Director`, `MD (at a service provider)`.
  **DO NOT search Tier C alone on LinkedIn** — the noise floor is prohibitive.
  Two options:
  1. Append a domain keyword to the search: `"head of o&m" <domain noun>`
  2. Use this title inside Pass 4 with a known company from `companies.md`, or
     append a mandatory domain qualifier when no registry exists.

### Step C — execution order

Run Tier A titles first (Pass 1 filter args + Pass 4 searches). Only move to Tier B
when Tier A's yield falls under the 20-per-pass threshold. Reserve Tier C
for Pass 4 (company-scoped when available) or with a mandatory domain qualifier
appended.

If Tier A titles pull thin (the founder has few domain-specific
first-degree connections), that's SIGNAL — jump to Pass 2 (content search),
per the auto-progression rule. Pass 4 (company-scoped 2nd-degree) follows if
Pass 2+3 still come up short.

### LinkedIn URL filters that force domain-fit

Beyond title keywords, LinkedIn's URL filters can pre-filter to the domain:

- `industry=[X,Y]` — LinkedIn assigns each user an industry code. Pick the codes
  for this idea's domain, not a stored list: run one title search, open two or
  three confirmed in-ICP profiles, and read the industry LinkedIn shows them
  under. Expect one code that is the domain's core and one or two adjacent ones
  worth including when yield is thin. Record the chosen codes in the run notes so
  the next pass reuses them.
- `currentCompany=[<id1>,<id2>,...]` — scope to specific companies from
  `companies.md`. LinkedIn company IDs can be extracted from `linkedin_slug`
  by visiting the company page.
- `geoUrn=["<region>"]` — geography filter. Combine with title for
  regional targeting (e.g. DE-only for German operators).

**When Tier C generic titles are unavoidable, LAYER an industry filter** —
`Head of O&M` + `industry=[29,59]` cuts noise 90%.

## Speed + accuracy levers (mandatory — apply on every run)

### 1. URL cache — never re-visit an already-known URL

Every LinkedIn profile / post URL the skill has ever seen is written to
`reports/outreach/.visited_urls.json`. Before opening any URL:

```python
import json
from pathlib import Path
cache_path = Path(f"reports/outreach/.visited_urls.json")
visited = json.loads(cache_path.read_text()) if cache_path.exists() else {}
# key = url, value = {"first_seen": iso_date, "last_action": "enriched"|"added"|"skipped", "notes": ""}
```

Rules:
- Search result extraction: dedup by URL against cache before writing to contacts.md
- Profile enrichment: skip if url is in cache with `last_action == "enriched"` and less than 30 days ago
- Post authors from content search: skip if url is in cache (they've been evaluated before)

Cache is per-idea because a person might be relevant for one assumption's ICP and not another's. Update after every write. Ship with `.gitignore`d so the cache doesn't bloat the repo.

### 2. Direct company-people URLs (skip top-level search)

For any company in `companies.md`, LinkedIn exposes a direct people-at-company URL. Faster and MORE accurate than keyword search (no fuzzy-matching noise):

```
https://www.linkedin.com/company/<slug>/people/?keywords=<title>
```

For every registry entry, `companies.md` should include the `linkedin_slug` (add as a field alongside `tier` and `rationale`). When you know a company you want to search, go directly:

```bash
"$B" goto "https://www.linkedin.com/company/{linkedin_slug}/people/?keywords=head%20of%20o%26m"
```

This is a company-page view (cheap, doesn't look like burst keyword-searching) rather than top-of-funnel search — LinkedIn treats them differently in its abuse detection. Prefer this over keyword search whenever you already know the company.

Whenever you land on a real in-domain company via any pass and it's not yet in `companies.md`, extract its `linkedin_slug` and append it to the registry with LLM-inferred tier + rationale.

### 3. Pipelined flow — search all pages first, enrich second

Do NOT interleave `search → extract → enrich → search → extract → enrich`. That leaks browser session time to profile visits during search bursts.

Correct order per pass:
1. Load first search page
2. Extract candidates from all pages via click-based Next pagination (search only — no profile visits)
3. Write raw candidates to `scratchpad/{pass_name}.json`
4. Apply ICP filter to the JSON offline (pure Python, no browser)
5. Enrich survivors as a batch — one profile visit per contact, 2-4s pace
6. Write enriched contacts to contacts.md

Search-only passes are 2-3x faster than mixed. Enrichment can then be batched or deferred (see #4).

### 4. Deferred enrichment (spread across sessions)

If a batch produces more contacts than LinkedIn's daily 100-profile cap allows, enrichment splits across sessions.

- Immediately after adding to contacts.md, enrich the top 40 by initial score.
- Leave the rest in contacts.md and pick them up next session, highest initial score first, until the daily cap is hit.
- The URL cache above is what makes this resumable: an enriched profile is recorded with `last_action: "enriched"`, so a later pass skips it and spends its budget on the backlog.

### 5. Keyword rotation — track what's been searched

Same keywords fish out the same contacts. Every batch should rotate 3 of 6 keywords to surface new candidates.

Track in `reports/outreach/keywords_used.md` — the ledger is per-idea state and
never lives in this definition:

```markdown

## Keywords used per batch
### Batch {N} ({date})
- {keyword} → {n} candidates

### Batch {N+1} (planned)
- Rotate OUT: {fished-out keywords}
- Rotate IN: {fresh keywords from the assumption's disconfirmation vocabulary}
- Keep: {still-yielding keywords}
```

Rule for rotation: a keyword is "fished out" when 2 consecutive batches return < 3 new candidates. Retire it and add a fresh one from the assumption's disconfirmation vocabulary.

### 6. Strengthen Pass 3 verification (accuracy lever)

After Pass 2 content search returns a post author, the profile visit in Pass 3 must verify:

1. **Current role is domain-relevant.** Read the top of the Experience section. If the current role isn't in the assumption's ICP domain, drop — no exceptions. This catches recruiters, journalists, and consultants who happen to post about the topic but aren't in the buyer/practitioner chain.
2. **Company tier is in `icp_valid_tiers`** — OR the classifier can confidently assign an in-scope tier from the role alone. If tier=other and the role is ambiguous, drop.

The post content itself is **not a filter**. Whether it's a complaint, commentary, news-share, or thought-leadership — anyone posting about the keywords has demonstrated genuine domain interest and is worth talking to. The ICP check (role + company) is the only gate. This is where robotics/adjacent people leak in — they fail the role check, not the post-type check.

## Pagination — mandatory for every search

LinkedIn shows ~10 results per page, so a first-page snapshot is a sample, not a sweep.
Paginate until results are exhausted, the ICP-fit target is hit, or the cap is reached.

**Never use `?start=N`.** LinkedIn's people search ignores it and re-serves page 1 on every
URL. Click the on-page "Next" button instead. Same for the degree filter: click the
"1st" / "2nd" / "3rd+" chip rather than URL-encoding `network=%5B%22F%22%5D`, which drifts
and returns false negatives.

```
navigate → https://www.linkedin.com/search/results/people/?keywords=<terms>

# Click the connection-degree chip ("1st" / "2nd" / "3rd+") before paginating,
# with javascript_tool:
(() => {
  const chip = Array.from(document.querySelectorAll("button, [role=\"button\"]"))
    .find(el => (el.textContent||"").trim() === "1st");
  chip && chip.click();
})()
sleep 3; "$B" scroll >/dev/null; sleep 2

while true; do
  "$B" js "<extraction JS>" > /tmp/page.json

  HAS_NEXT=$("$B" js '(() => {
    const btn = Array.from(document.querySelectorAll("button"))
      .find(b => (b.textContent||"").trim() === "Next");
    if (!btn) return "false";
    if (btn.disabled || btn.getAttribute("aria-disabled") === "true") return "false";
    return "true";
  })()')
  [ "$HAS_NEXT" != "true" ] && break

  "$B" js '(() => {
    const btn = Array.from(document.querySelectorAll("button"))
      .find(b => (b.textContent||"").trim() === "Next");
    btn && btn.click();
  })()' > /dev/null
  sleep 3; "$B" scroll >/dev/null 2>&1; sleep 2
done
```

Hard caps per pass, to stay under throttling:

| Pass | Cap |
|------|-----|
| 1st-degree sweep | 500 results (50 pages) per keyword |
| Profile-fit (2nd-degree) | 200 results (20 pages) per title query |
| Content search | 100 posts (10 pages) per keyword |

If a captcha or "unusual activity" notice appears before the cap, STOP, note which contacts
are written so far, and resume next session.

## Full profile enrichment (mandatory, not optional)

**Read `references/enrichment.md` for the full JS extraction snippet and throttling rules.**

Every contact must be enriched before strategy runs — enrichment reveals `open_to_work`, `mutuals_count`, `active_last_30d`, and current title. A cold `profile_fit` can upgrade to `post_engagement` (×1.5 multiplier) once you check their recent activity. Rate limit: ~100 profile views/day; split across sessions if needed.

## Response likelihood scoring

**The opening terms, the score bands, and the two fields to write live in `schemas/contact.md` → Response likelihood scoring.** That schema is the single definition; do not restate the weights here or they will drift.

In short: start at 3, adjust for signal, degree, warmth, mutuals and shared affiliation, clamp to 1–10, and write both `response_likelihood` and `likelihood_factors`. The score is a judgement, not an arithmetic result — you may add a term the list doesn't have, but whatever you use must appear in `likelihood_factors`, which is the only record of why the number is what it is. Revisit it in place after enrichment.

## Setup (run every session before browsing)

Browsing uses the **claude-in-chrome tools** against the founder's own Chrome. Load every
schema you expect to need in ONE `ToolSearch` call, then:

```
tabs_context_mcp  → always first; shows the founder's existing tabs
tabs_create_mcp   → work in a tab you created, never one of theirs
get_page_text     → the default read; a fraction of a screenshot's cost
read_page         → when you need structure the text extraction drops
javascript_tool   → for chip clicks and pagination
tabs_close_mcp    → close the tab you opened when the pass is done
```

The founder is already logged in on that profile. If LinkedIn shows a logged-out state,
stop and say so rather than touching any login form.

**Never handle credentials.** **Never trigger `alert`/`confirm`/`prompt`** — a modal dialog
blocks every subsequent browser call and the pass dies until the founder dismisses it.

## Inputs you need

1. **The target assumption** — from `reports/02-assumptions/graph.md`, find node `id: {A_ID}`. Read `assumption`, `category`, `disconfirmation`, and any ICP hints in `next_action`
2. **Existing contacts.md** — `reports/outreach/contacts.md`. Load for deduplication and to find the next available `C{N}` id
3. **`companies.md` (optional)** — `reports/outreach/companies.md`. If
   present, read `tier`, `linkedin_slug`, `pain_score`, and `also_known_as` to
   prioritize company-scoped searches. If absent, do not invent company-level
   signals; use profile-level ICP evidence instead.
4. **`companies.md` (targeting fields) (optional)** —
   `reports/outreach/companies.md`. If present, use its contracts,
   news, hiring, {operational-loss signal}, and fleet signals as prioritization context. If
   absent, live LinkedIn profile evidence remains sufficient for outreach.
5. **Signal keywords** — technical noun-phrases the target segment would use to describe the pain in a LinkedIn post. NOT conversational sentences. Derive them per-assumption from `graph.md` (`assumption` text + `disconfirmation`) — never hardcode to any single industry. See `.claude/skills/startup-outreach-intel/references/keyword-derivation.md` if in doubt.
6. **The LinkedIn data export (strongly recommended)** — `private/linkedin-export/`. Powers Passes 0 and 1. Check it first with:

   ```bash
   .venv/bin/python -m scripts.data.linkedin_export inspect
   ```

   Read `latest_activity` from the output. If the export is more than ~3 months
   old, or missing entirely, tell the founder how to refresh it BEFORE starting
   the browser passes — it's a 10-minute wait that removes most of the browsing:

   > LinkedIn → Settings → Data Privacy → Get a copy of your data → "Want something in particular" → tick **Connections**, **Messages**, **Invitations** → Request archive. LinkedIn emails a zip in ~10 min–24 h. Unzip it to `private/linkedin-export/` (already gitignored).

   The archive contains other people's names, employers, and private message
   content. It is gitignored deliberately — never commit it, never copy its
   contents into `reports/`, and put only ICP-relevant fields into `contacts.md`.

If input 1 or 2 is missing, ask before browsing — don't waste browser session
time. Missing company files are a normal direct-outreach path, not a blocker.
A missing export is not a blocker either, but it means Pass 1 falls through to
the browser passes, so flag the cost to the founder before proceeding.

## Notes on browsing

- Insert `sleep 2-3` between navigation calls. LinkedIn rate-limits bursts and will show captchas or throttle.
- Never run multiple `browse` commands in parallel — the browser is single-threaded.
- If a page shows a captcha or auth prompt, STOP and ask the founder to resolve it in the browser window before continuing.
- Use `"$B" snapshot | head -N` or pipe through grep — never dump raw snapshots into your context, they're huge.
- InMail-gated profiles (Connect button hidden even in More menu) → skip or note under `notes:` with "InMail required — Follow + engage instead".

## Contact role classification

For each candidate, determine `contact_role` from their current title (top line of profile snapshot):

- **`buyer`** — controls the budget. Titles: VP, Director, Head of, Chief, procurement lead in the domain. Signal words: "Director of X", "Head of X", "VP", "Chief".
- **`practitioner`** — feels the pain daily. Titles: Manager, Lead, Coordinator, Specialist, Engineer, Analyst in the domain.
- **`expert`** — knows the space, doesn't work in it directly. Consultants, ex-operators, analysts, academics, journalists, VCs. Signal words: "Consultant", "Advisor", "Researcher", "Analyst" (with independent framing), "Ex-{Company}".
- **`influencer`** — publishes / speaks / connects. Content creator, newsletter author, verified accounts, "Advisor" without domain expertise, "Board Member". Follower count above ~5k is a strong signal.

When ambiguous, favor the more specific role. When the top card doesn't make it obvious, don't guess — look at the last two roles in Experience. Put uncertainty in `notes:`.

## Writing to contacts.md

Follow `schemas/contact.md` exactly. Fields the skill sets when appending:

- `id` — next available `C{N}` (read the file first)
- `name`, `linkedin_url`, `company`, `role` — from profile snapshot
- `signal_type` — set by which pass found them
- `signal_multiplier` — derived (1.5 / 1.25 / 1.0)
- `signal_source_url` — post URL for Pass 2 content search; group URL for Pass 3b; search URL for Pass 1/4 (profile_fit contacts)
- `signal_excerpt` — verbatim (quoted) for `post_engagement` and `comment_signal`; empty for `profile_fit` and `group_member`
- `contact_role` — classified above (buyer / practitioner / expert / influencer)
- `role_pts` — derived (3 / 2 / 2 / 1)
- `tier` — set from the contact's org position in the value chain (see below)
- `assumptions_tested` — `[{A_ID}]`
- `outreach_status` — `pending`
- `found_date` — today's ISO date
- `notes` — any 2nd/3rd degree oddities, connectability issues, mutual connections spotted

Update the frontmatter `totals.targeted` counter and `last_updated`.

### Setting `tier` — company position, not job title

`tier` is a property of the **company**, not the person. A Head of O&M can be a `buyer`
`contact_role` at any of these tiers:

Take the tier name from the assumption's `icp_valid_tiers`; assign it by the
company's **side**, which is the only part of this vocabulary that is global
(`vocab:tier_side`).

| side          | Set when the contact's company…                                   |
|---------------|-------------------------------------------------------------------|
| `demand`      | Owns the pain and holds the budget for fixing it                  |
| `supply`      | Does the work or sells the service for hire                       |
| `competitor`  | Solves the same problem for the same buyer                        |
| `expert`      | Consultant / ex-operator / analyst / academic — not currently employed by any target org |
| `other`       | Last resort — surface to founder for classification               |

Which concrete companies fall under which tier is per-idea and belongs in that
idea's `companies.md`, never in this file. A roster here would be one idea's
target list read by every other idea.

Set tier from the company name FIRST, then verify by role. If the company is unfamiliar,
web-search "is {company} a {asset} operator or service provider" before guessing.

## Prior-project alignment — the Linkedin Outreach repo

A founder may keep a separate outreach system outside this repo for a different domain; its path belongs in machine-local session memory, not in a shared skill definition.
- Uses its own browser automation, separate from this repo's
- Uses `outreach_data.json` + `its own tracker script` as its tracker (different format from our `contacts.md`)
- Has locked message templates and a marketing-director voice
- Runs the "5-by-5" outreach loop

Our system is separate — a different idea, different thesis, different contacts.md format. But the browsing patterns and safety rules are identical. When in doubt about how to drive the browser, look at that project's CLAUDE.md — it's the reference implementation.

## Common failure modes to avoid

- **Stopping at page 1.** The first page shows ~10 results. the founder has thousands of connections and searches return hundreds of pages. Always paginate by clicking the on-page "Next" button until results are exhausted or the cap is hit. A first-page-only run is not a network sweep — it's a sample.
- **URL-stuffing the degree filter.** Don't put `network=%5B%22F%22%5D` (1st) or `network=%5B%22S%22%5D` (2nd) into the search URL — LinkedIn's URL-encoded network filter drifts and returns 0-hits when a real search would return dozens. Always click the "1st" / "2nd" / "3rd+" chip on the results page instead.
- **Skipping the login check.** If the founder isn't logged in, `snapshot` returns the LinkedIn front page and you'll write nonsense to contacts.md. Always confirm login before any browser pass.
- **Conversational search keywords.** "why can't we inspect at height" → junk. Use noun-phrases: "rope access cost", "tactile inspection gap".
- **Fabricating profile URLs.** Copy the exact URL from the snapshot. Don't construct from name + slug — LinkedIn slugs are unpredictable.
- **Trusting old post authors.** If a post is >30 days old, the author's role may have changed. Verify current job (top of Experience) before adding.
- **Missing InMail gating.** Check the profile's Connect button state. If gated (behind email or hidden even in More menu), note it — don't just skip silently.
- **Duplicating contacts across assumptions.** If C1 already exists testing A2 and you're now targeting them for A5, append A5 to `assumptions_tested`, don't create C99.

## Note on testing

This skill has no automated eval — it requires a live LinkedIn session that the user logs into manually. Test manually when first invoked: pick one low-stakes assumption, run Passes 0-1 only (export-based, no browser), verify contacts.md structure looks right, then proceed to the browser passes.

## Degree visibility is mandatory in the tracker

Every contact's `degree` field (`1st` / `2nd` / `3rd+` / `inmail_only`) must be **visually distinct** in the outreach tracker — not just a column, a first-class visual grouping.

**Why:** the outreach strategy differs completely by degree.
- 1st-degree = existing relationship, direct message, no invite needed. Highest reply rate.
- 2nd-degree = mutual visible on invite. Warm-cold hybrid. Medium reply rate.
- 3rd+ = fully cold. May need InMail. Lowest reply rate.

The founder should be able to filter the tracker by degree AND see the degree at a glance on every contact card. Any tracker HTML rebuild MUST preserve this.

## Regenerate the tracker after every write

**Every time you add or update rows in `contacts.md`, run:**

```bash
python3 scripts/build_control_room.py
```

This regenerates `reports/dashboard.html` — the founder's live
dashboard showing counts by tier / status / role, a filterable contact table, and
LinkedIn links. It's a pure projection of contacts.md; overwrite is safe.

Skip this only if you're mid-batch and about to write more rows in the same run — batch
the writes, then run the script once at the end. Never leave a session with contacts.md
newer than the tracker.

## LinkedIn account safety (respect these)

- **~100-150 connection invites per week max** across all activity. This skill doesn't send anything, but if the founder then uses the LinkupOAuth mode or manual clicking, that's the ceiling.
- **~20 invites per day is a safer daily cap.** LinkedIn flags bursts.
- Reading / browsing / snapshotting is fine — this is what the skill does. No mass scraping.
- **LinkedIn ToS.** Automated browsing technically violates LinkedIn's User Agreement regardless of pacing or browser type. The human-paced, headed-browser approach reduces detection risk — it does not make it permitted. the founder is making this trade-off knowingly.
- Never use headless mode or run in the background — always the visible Chromium window the founder can watch.
- If LinkedIn shows a captcha, throttle warning, or "unusual activity" prompt, STOP immediately and let the founder handle it in the browser. Don't automate around it.

## Mechanics

Every pass, table, cap and failure catalogue lives in `references/search-passes.md`. Read the section for the stage you are running; the decision procedure above is the whole of what is always-on.

## Batch flow — step-by-step summary

0. **Verify the assumption's ICP is declared in `graph.md`.** If any of
   `icp_segment`, `icp_valid_tiers`, or `icp_out_of_scope` are missing, STOP and
   ask the founder to fill them in first. `companies.md`
   are optional enrichment inputs, not prerequisites. If they exist, use their
   tier, pain-score, and company-level signals to prioritize searches. If they
   do not exist, run the broad LinkedIn passes using the assumption's declared
   titles, domain vocabulary, and live profile evidence. Do not block direct
   outreach on an API enrichment run.
1. **Run Pass 0** (`linkedin_export history`) — backfill prior contact, surface any status conflicts. No browser.
2. **Run Pass 1** (`linkedin_export connections`) — derive title/noun/exclude args from `graph.md`, tune with `--include-rejected`, keep the matches. No browser.
3. **Check total** — if the batch is already at 50 from Pass 1, skip straight to enrichment. Every browser pass below is optional volume.
4. **Run Pass 2** (content search) — collect post authors + excerpts, do NOT add yet
5. **Run Pass 3** (profile verify Pass 2's candidates) — only add those passing all three checks
6. **Check total** — if under 50, run Pass 3b (groups), then Pass 4 (2nd-degree by title × company)
7. **Enrich every candidate** — visit each profile to extract open_to_work, mutuals, active_last_30d, current company/title. Rescore. Pass 1 contacts need this too: the export's `position` is as of the export date, not today.
8. **Regenerate the tracker + run the audit** — `python3 scripts/build_control_room.py` and `python3 scripts/audit_target_list.py`.
9. **Present the top by score to the founder** for review.

**Rate limits:** LinkedIn tolerates ~100 profile views per day with normal browsing patterns. Split enrichment across sessions if needed. Never burst — 2-4 second delay between profile visits.

## The handoff summary

At the end of the run, produce a concise report:

```
Target list for A{X} — "<assumption text>"

Signal breakdown:
  profile_fit:      10 contacts (Pass 1+4 — queued for /startup-outreach-draft)
  post_engagement:   5 contacts (Pass 2+3 — time-sensitive, prioritize in blast)
  group_active:      3 contacts (Pass 3b — time-sensitive, prioritize in blast)
  group_member:      4 contacts (Pass 3b — queued for blast)

Role breakdown:
  buyer:            2 (Priya Shah, Anwar Butt)
  practitioner:    10 (list first 3)
  expert:           1 (Dr Whitmore)
  influencer:       1 (Tom Brady)

Priority handoff:
  8 time-sensitive contacts have exact excerpts + source URLs in contacts.md.
  No messages were drafted or sent by this skill.

Deduplicated:
  3 candidates already existed in this contacts.md → assumptions_tested extended
  1 candidate found in the founder's separate outreach tracker — flagged in notes

Skipped:
  2 InMail-gated (no free Connect button) — noted for Follow+engage
  2 posts > 30 days old — contacts written, message preparation deferred to /startup-outreach-draft

Next step:
  1. Run /startup-outreach-draft A{X}; process time-sensitive contacts first
  2. Review the generated clause table before any modal is prepared
  3. Founder verifies each target and clicks the final Send button
  4. Run /startup-outreach-check for inbox classification, then /startup-outreach-reply for approved follow-ups
```
