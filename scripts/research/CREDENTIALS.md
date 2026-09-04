# Credentials — what each one unlocks, what it costs, how long it takes

The pipeline runs with **no credentials at all**. Everything in this table is about
replacing an estimate with a measurement. They are listed in the order worth doing.

| # | Key | Unlocks | Cost | Time | Replaces |
|---|---|---|---|---|---|
| 1 | ~~`CENSUS_API_KEY`~~ **held since 2026-09-03** | Economic Census `ecnbasic` receipts, `ecnnapcsprd`/`ecnlines` **merchandise-line sales**; ACS households/income/movers | free | ~2 min | Done — the online share of window coverings is now measured (E18) and the trade's size with it (E19) |
| 2 | `GOOGLE_ADS_*` (5 vars) | Keyword Planner volume **and CPC** | free | ~1–2 days | The placeholder $2.50 CPC — the only unmeasured number left in the model |
| 3 | `ETSY_API_KEY` | Listing prices and lifetime shop sales | free | ~1 day | Nothing yet — this is net-new unit-level evidence |
| 4 | `SEMRUSH_API_KEY` | Competitor organic keywords | ~$130/mo | instant | Nothing yet — net-new competitive detail |
| 5 | `BLS_API_KEY` | Higher BLS rate limits (50 series, 20 years) | free | ~2 min | Nothing — the unregistered tier already covers what we pull |

Put them in `.env` in this folder (it is read before the sibling `Assumption-Lab/.env`).

---

## 1. Census API key — do this one first

<https://api.census.gov/data/key_signup.html> — name, email, organisation. The key arrives
by email within a minute or two; click the activation link.

```
CENSUS_API_KEY=...
```

Paste it into the repo-root `.env`, where a commented placeholder is already waiting:

```
CENSUS_API_KEY=...
```

**Held since 2026-09-03, and what it produced.** The Economic Census returns HTTP 302 without
a key. With one, `t2_census_merchline_window.py` measured the online share of the US retail
window-treatment line — 31.9% through electronic shopping and mail-order houses in 2017, 3.6x
the all-retail e-commerce rate that year (E18) — which closed the open question E14 had left
open, and `t2_census_econ.py` and `t2_census_acs.py` both went from `blocked_no_credential` to
running.

**The dataset is `ecnnapcsprd`, not `ecnprdlines`.** This table named `ecnprdlines` before the
key existed; no such dataset is published. Merchandise lines are `ecnnapcsprd` (product by
industry) and `ecnnapcsind` (industry by product) for 2017 and 2022, and `ecnlines` for 2012.
Only 2017 answers the channel question: the 2022 NAICS revision dissolved subsector 454 and
folded the online-only sellers into the storefront industries, so 2022 publishes the line
total with no online row (E19).

**If the key ever has to be replaced**, the activation email ends the key with a full stop.
Pasting the sentence rather than the token gives a 41-character value and every call returns
302 `Invalid Key` — the same symptom as having no key at all. The token is 40 hex characters.

Everything else Census in this repo is keyless: CBP (establishment counts), SUSB (receipts by
firm size — the market ladder) and ARTS (retail e-commerce by kind of business, which also
owns the all-retail benchmark series E18 is read against). The key adds measurement; it never
unblocked the pipeline.

Still outstanding on this key: the measured revenue-to-payroll ratio for the Bay Area
supply-side cross-check (currently a 3.3x assumption). ACS now runs, so the household count
is no longer estimated from population share.

## 2. Google Ads / Keyword Planner

Keyword Planner needs an Ads account but **no ad spend**. Three separate things:

1. **Ads account** — <https://ads.google.com>. Create a campaign to finish signup, then
   pause it immediately. Switch to Expert Mode to avoid being forced into a live campaign.
2. **Developer token** — API Center in the Ads UI. A *test* token cannot query real
   volume; you need at least Basic Access, which is a short application form and usually
   turns around in a day or two.
3. **OAuth refresh token** — create OAuth client credentials in a Google Cloud project,
   then run Google's `generate_user_credentials.py` from the `google-ads-python` repo.

```
GOOGLE_ADS_DEVELOPER_TOKEN=...
GOOGLE_ADS_CLIENT_ID=...
GOOGLE_ADS_CLIENT_SECRET=...
GOOGLE_ADS_REFRESH_TOKEN=...
GOOGLE_ADS_CUSTOMER_ID=1234567890
```

The collector already targets both California (`geoTargetConstants/21137`) and the
San Francisco–Oakland–San Jose DMA (`geoTargetConstants/200807`).

## 3. Etsy

<https://www.etsy.com/developers/register> — register a personal app, take the
"keystring". Read-only listing and shop endpoints need only the key, not OAuth.

```
ETSY_API_KEY=...
```

Worth doing because it is the only public source of **unit-level** data: what a custom
table actually sold for, and how many a given maker has sold in their lifetime. Etsy's
public HTML is behind a bot wall (a plain fetch returns 403), so the API is the route
that works. eRank and Alura resell a view of the same underlying data for $10–30/month;
the API gives it directly and free.

## 4. Semrush

<https://www.semrush.com/api-analytics/> — the API is a paid add-on on top of a Guru
subscription. The brief's own plan (one month, then cancel) is the right way to buy it.
The collector pulls the top 100 organic keywords for nine competitor domains; each row
costs 10 API units.

```
SEMRUSH_API_KEY=...
```

---

## Sources that stay manual

| Source | Why | What to do |
|---|---|---|
| **IBISWorld** | Library-card SSO, no API | San José Public Library card → <https://www.sjpl.org> databases → IBISWorld → reports **33712** (Wood Household Furniture Manufacturing) and **42321** (Furniture Wholesaling). Pull the five-year outlook and the cost-structure page. |
| **Houzz & Home survey** | Published as a PDF | <https://www.houzz.com/research> — annual, large-sample renovation and furnishing spend. The regional cut is the useful part. |
| **Pinterest Trends** | Public endpoint returns 404 to scripted requests | <https://trends.pinterest.com> in a browser. Home furnishings is Pinterest's core category and leads purchase by weeks. |
| **Furniture Today / AHFA** | Trade press, paywalled | Worth one month around the High Point Market cycle if the wholesale channel is in scope. |
| **NKBA** | Membership | Only relevant if the island/countertop B2B channel gets pursued. |
