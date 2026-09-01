# Profile Enrichment Reference

Every contact needs enrichment before the strategy skill runs. The strategy skill decides
the outreach angle based on current title, whether they posted about the pain, whether
they're open-to-work, and mutual count. Without enrichment, strategy is guessing.

## JS extraction snippet — run on each profile page

`navigate` to `<contact.linkedin_url>`, wait ~3s for the lazy sections to render, then run
this through `javascript_tool`. Wait ~2s after each profile before the next one — bursts
are what trigger throttling.

```javascript
(() => {
  const nameEl = document.querySelector("h1");
  const headlineEl = document.querySelector("div.text-body-medium");
  const bannerText = document.body.innerText || "";
  const openToWork = /Open to work|#OpenToWork/i.test(bannerText);
  const mutualMatch = bannerText.match(/(\d+)\s+mutual connection/i);
  const mutuals = mutualMatch ? parseInt(mutualMatch[1]) : 0;
  const hasRecentPost = document.body.innerText.includes("posted this");
  const expSection = Array.from(document.querySelectorAll("section"))
    .find(s => s.innerText.startsWith("Experience"));
  const currentCompany = expSection
    ? (expSection.innerText.split("\n").find(l => l.length > 3 && l.length < 60) || "")
    : "";
  return JSON.stringify({
    name: nameEl ? nameEl.textContent.trim() : "",
    headline: headlineEl ? headlineEl.textContent.trim() : "",
    open_to_work: openToWork,
    mutuals_count: mutuals,
    has_recent_post: hasRecentPost,
    current_company_hint: currentCompany
  });
})()
```

## Fields to update in contacts.md after each visit

- `company` — from profile experience section (more accurate than search-result headline)
- `role` — clean current title from profile
- `open_to_work` — true/false
- `mutuals_count` — integer
- `active_last_30d` — true if a recent post was found; false otherwise

Then **revisit `response_likelihood`** with the new data and update `likelihood_factors` to
match — it must name every term behind the new score, including any not in the standard list
(`schemas/contact.md` → Response likelihood scoring).

## Signal upgrade rule

If a contact has a recent post about the pain, upgrade them:
- Change `signal_type` from `profile_fit` → `post_engagement`
- Boost `signal_multiplier` from 1.0 → 1.5
- Paste the excerpt into `signal_excerpt`

This is why enrichment matters — a cold profile_fit can turn into a hot post_engagement
once you actually look at their activity.

---

## Profile-fit lookup — mandatory for every `signal_type: profile_fit` contact

For `profile_fit` contacts, enrich the live LinkedIn profile before writing
`profile_fit_signals` to `contacts.md`. These fields support contact scoring,
prioritisation, and auditability; they are not message evidence. Company-level
API enrichment is optional and must never block direct outreach.

**If `companies.md` (targeting fields) exists, check it first.** A company-level hit from
intel can improve prioritisation without another API call. If it is absent,
skip this lookup and rely on the live profile. Steps 1-4 are optional enrichment
only when the founder explicitly asks for company-level signals; they are not a
prerequisite for finding or messaging a contact.

Write everything you find (even partial hits) so ranking decisions remain explainable. `startup-outreach-draft` independently reopens the live profile and verifies every Msg 1 claim.

### Step 0 — Optional lookup in `companies.md` (targeting fields)

If `reports/{slug}/outreach/companies.md` exists, locate the block for the
contact's employer. Match by:

1. Exact company name (case-insensitive, legal-suffix stripped: "Ltd", "A/S", "Inc", "PLC", "GmbH")
2. If no match, check `also_known_as` (subsidiary → parent mapping written by intel)
3. If still no match, the company is unknown to intel — use live LinkedIn
   evidence and stop unless the founder explicitly requested external
   enrichment.

If found, read the `assumptions.A{X}` block (where `A{X}` is the active assumption being targeted). Pull these fields directly into `profile_fit_signals`. **Every field on the intel block has a documented consumer strategy — do not silently drop any of them:**

```yaml
# --- 0. Pre-computed strongest company signal (short-circuits enrichment) ---
top_signal_for_copy:   "<assumptions.A{X}.top_signal_for_copy>"   # legacy field name; discovery priority only

# --- 1. EDGAR filings (HIGHEST STRENGTH — legally attested, not opinion) ---
edgar_hook:            "<assumptions.A{X}.edgar_filings[0].excerpt>"
edgar_hook_url:        "<assumptions.A{X}.edgar_filings[0].source_url>"
edgar_form_type:       "<assumptions.A{X}.edgar_filings[0].form_type>"   # 10-K / 10-Q / 8-K
edgar_filing_date:     "<assumptions.A{X}.edgar_filings[0].filing_date>"

# --- 2. Contracts (TED EU / UK Contracts Finder) — includes role + counterparty ---
contract_hook:         "<contracts[0].title> awarded <contracts[0].date> (<contracts[0].value> <contracts[0].currency>)"
contract_hook_url:     "<contracts[0].source_url>"
contract_role:         "<contracts[0].role>"           # "contracting_authority" (they bought) OR "supplier" (they won)
contract_counterparty: "<contracts[0].counterparty>"   # the other party in the deal

# --- 3. News (GDELT primary, Exa fallback) ---
company_news:          "<news[0].title>"
company_news_url:      "<news[0].url>"

# --- 5. Hiring (Adzuna) — pull top title, not just count ---
hiring_surge:          "<hiring.postings_count> open roles"
hiring_surge_url:      "<hiring.source_url>"
hiring_top_title:      "<hiring.top_titles[0]>"        # most on-ICP open role — priority context

# --- 6. Score (for within-cluster sort) ---
company_pain_score:    <assumptions.A{X}.pain_score>   # 1-10
```

**Field-by-field mapping to the intel-skill schema is enumerated in `startup-outreach-intel/references/output-format.md`. If you're unsure what a field maps from, check that file — do not guess.**

Rules:

- **Every field is optional.** If intel didn't fetch it (API not enabled, or empty response), leave the field empty. Never fill from model knowledge — the intel file's grounding rule extends here.
- **Employer-level signals may be attached to every contact at that company for prioritisation.** They do not prove that a particular contact owns, knows about, or experienced the event; never turn that association into a personal claim.
- **Keep `contract_role` and `contract_counterparty` paired.** They explain whether the company appeared as buyer or supplier and keep the evidence auditable. If either is empty when `contract_hook` is populated, flag the incomplete intel record in the enrichment log; do not infer the missing value.
- **If Step 0 populated any signal**, use it for prioritization and do not make
  external calls unless the founder explicitly requested them.

Log to `.enrichment_log.jsonl`:
```json
{"contact": "C{N}", "company": "...", "step_0_hit": true, "fields_populated_from_intel": ["top_signal_for_copy", "contract_hook", "contract_role", "contract_counterparty", ...], "steps_1_4_skipped": true}
```
so reruns are auditable and gaps are grep-able.

### Steps 1-4 — External APIs (explicit opt-in only)

### Grounding rule — no hallucinations, ever

Every field in `profile_fit_signals` must be grounded in something you directly observed this session:

| Source | Acceptable evidence |
|---|---|
| LinkedIn browser | Text extracted by JS snippet or read from a browser snapshot |
| GDELT REST API | Article title + URL returned by the API in this session |
| Exa AI | Search result title + URL returned by the API in this session |
| Adzuna API | Job title + redirect_url returned by the API in this session |
| Model knowledge | **Never.** If you haven't actually called an API or browser, write empty. |

If a step returns nothing, write the field empty — do not fill it with plausible-sounding guesses. Fabricated enrichment corrupts ranking and audit history even though the draft skill performs a separate live-profile verification.

For WebSearch results: always record the source URL alongside the summary. No URL = no write.

### Step 1 — Career change (same profile page, from JS snippet)

The extended snippet below captures `career_change_days_ago`. If < 60, they recently moved roles — a useful prioritisation signal.

```bash
"$B" js '(() => {
  const expSection = Array.from(document.querySelectorAll("section"))
    .find(s => /Experience/i.test(s.innerText));
  let careerChangeDays = null;
  if (expSection) {
    const tenureHint = expSection.innerText.match(/(\d+)\s*(mo|month|yr|year)/i);
    if (tenureHint) {
      const n = parseInt(tenureHint[1]);
      const unit = tenureHint[2].toLowerCase();
      careerChangeDays = unit.startsWith("mo") ? n * 30 : n * 365;
    }
  }
  const activitySection = document.body.innerText;
  const commentPattern = /commented on .{10,80}[''"]s post/i;
  const hasCommentActivity = commentPattern.test(activitySection);
  const commentMatch = activitySection.match(commentPattern);
  const groupSection = Array.from(document.querySelectorAll("section"))
    .find(s => /Groups/i.test(s.querySelector("h2, h3")?.innerText || ""));
  const groupNames = groupSection
    ? Array.from(groupSection.querySelectorAll("span, a"))
        .map(el => el.textContent.trim())
        .filter(t => t.length > 5 && t.length < 80)
        .slice(0, 5)
    : [];
  return JSON.stringify({
    career_change_days_ago: careerChangeDays,
    comment_activity: hasCommentActivity ? (commentMatch ? commentMatch[0] : "recent comment detected") : null,
    group_names: groupNames
  });
})()'
```

Write `career_change_days_ago`, `comment_activity`, and `group_names` to `profile_fit_signals` in contacts.md.

### Step 2 — Job postings at their company (Adzuna API — run once per company, cache results)

Adzuna has structured job data across its supported countries; route by the company's country per `api-catalog.md`. Run once per unique company per batch, cache in scratchpad, reuse for all contacts at the same company.

```python
import os, requests, json
APP_ID  = os.environ["ADZUNA_APP_ID"]
APP_KEY = os.environ["ADZUNA_APP_KEY"]

company = "<contact's employer>"
keywords = " OR ".join(domain_keywords)   # derived per assumption, see keyword-derivation.md

url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1"
params = {
    "app_id": APP_ID, "app_key": APP_KEY,
    "results_per_page": 5,
    "what": keywords,
    "company": company,
}
r = requests.get(url, params=params)
hits = r.json().get("results", [])
for h in hits:
    print(h["title"], "|", h["redirect_url"])
```

If Adzuna returns a relevant role, write `job_posting` (title) and `job_posting_url` to `profile_fit_signals`. If Adzuna returns nothing, fall back to LinkedIn Jobs via the browser for that company only.

### Step 3 — Tech stack / tooling signals (from Adzuna JD text)

The Adzuna response includes full `description` fields. While you already have the results from Step 2, scan the JD text for named tools — no extra API call needed:

```python
for h in hits:
    desc = h.get("description", "")
    tools = [w for w in desc.split()
             if any(t in w.lower() for t in ["scope", "sap", "maximo", "salesforce", "drone", "lidar", "platform"])]
    if tools:
        print("Tech signals:", tools)
```

Write any found tool names to `profile_fit_signals.tech_stack`. If no JD text is available, skip — do not infer from model knowledge.

### Step 4 — Company news (GDELT REST API — keyless, no cost)

GDELT indexes 100+ languages, updates every 15 minutes, and covers global press back to 2015. Run once per company.

```python
import requests, urllib.parse

company = "<contact's employer>"
query   = f'"{company}" ' + " OR ".join(domain_keywords)
url = "https://api.gdeltproject.org/api/v2/doc/doc"
params = {
    "query":    query,
    "mode":     "ArtList",
    "maxrecords": 5,
    "format":   "json",
    "timespan": "6M",   # last 6 months only — stale news is weak prioritisation evidence
    "sort":     "DateDesc",
}
r = requests.get(url, params=params)
articles = r.json().get("articles", [])
for a in articles:
    print(a["title"], "|", a["url"], "|", a["seendate"])
```

Write the most recent relevant article title + URL to `profile_fit_signals.company_news` and `profile_fit_signals.company_news_url`.

If GDELT returns nothing relevant, run Exa AI as a fallback — it does semantic search across the full web:

```python
import os, requests
EXA_KEY = os.environ["EXA_API_KEY"]

r = requests.post(
    "https://api.exa.ai/search",
    headers={"x-api-key": EXA_KEY, "Content-Type": "application/json"},
    json={
        "query": f"{company} " + " OR ".join(domain_keywords) + " OR contract OR expansion",
        "numResults": 3,
        "type": "neural",
        "startPublishedDate": "2025-01-01",
    }
)
for result in r.json().get("results", []):
    print(result["title"], "|", result["url"])
```

**If neither GDELT nor Exa returns a real result: leave `company_news` empty.** The hallucination rule applies here too — no URL = no write.

### Writing `profile_fit_signals` to contacts.md

After the lookup, append to the contact block:

```yaml
profile_fit_signals:
  job_posting: "<on-ICP role title> (2026-06-15)"            # title + approx date, or empty
  job_posting_url: "https://www.linkedin.com/jobs/view/..."  # or empty
  company_news: "{Operator Co} awarded {contract} Jun 2026"   # or empty
  tech_stack: "<tools named in the JD>"                      # tools found in JDs, or empty
  career_change_days_ago: 45                                  # integer, or null if not detectable
  comment_activity: "commented on a post about <the pain>"   # or null
  group_names: ["<industry group>", "<certification network>"] # or []
```

All fields are optional — write what you found and leave the rest empty. The targets skill uses the populated fields to score and order contacts; the draft skill does not reuse them as message claims.

## Throttling — 30 seconds minimum between profile visits

**One profile per 30 seconds. Never faster. Never bursts. Never below 30s.**

Historical:
- 2026-07-10 A2 run 1: 30 profile visits at 3-second spacing → LinkedIn served the "Join LinkedIn" wall on 27 of 30 profiles AND signed the session out.
- 2026-07-10 A2 run 2: 60-second spacing after re-login — SAME 28 URLs still returned the Join Wall. This says: once your session is flagged by a burst, the flag persists for hours regardless of subsequent pace. 60s isn't the right per-visit floor — 30s is, and the more important discipline is **never bursting in the first place.**

Rules:
- Insert `sleep 30` between every profile visit — no exceptions
- **If a burst mistake has already happened this session, session is likely flagged for 12–24h.** No amount of slowing down mid-session unflags it. Best move: stop, cool off 24h, resume with 30s pace from a fresh session.
- If LinkedIn shows a captcha, "unusual activity" prompt, or returns the "Join LinkedIn" wall on any profile: STOP the batch immediately, log which contacts are done, wait ≥ 12h before resuming.
- Never automate around a throttle signal.

Practical implication for batch enrichment:
- 30 contacts × 30s = **15 minutes per batch** — plan for this, run in background
- Any Claude session driving the browser should run enrichment as a background task
  (`run_in_background: true` on the Bash tool) and check back periodically, not tail
  the log tightly
- Never skip the sleep to "test faster" — that's how the 2026-07-10 burn happened
