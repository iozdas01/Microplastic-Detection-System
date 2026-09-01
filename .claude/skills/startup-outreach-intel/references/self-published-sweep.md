# Self-published source sweep — mechanics

Phase 0.6. Fetch what a company says about itself, in its own words, and fold it into
`companies.md`. No API key, no spend, no rate limit. The counterpart to Phase 0: Phase 0
finds companies from the network, this one finds *facts* the API sweep structurally cannot.

## Why the API sweep misses this

Procurement, filings and grants attest to transactions. They say nothing about how a company
positions itself, who it says it sells to, what it raised, who it partners with, or what market
claim it is built on. That material is published, dated, and authored by the company — and it is
usually the only place the business model is stated plainly. A registry built only from
transactional APIs plus one interview will confidently describe the wrong company.

Worked incident — MicroAGI, `physical-ai-deployment`, 2026-08-09. The entry was built from a
first-hand call and read them as a data-capture operation whose "vertical coverage stops at
manufacturing, which is the gap this campaign occupies." Four announcements on their own site,
all published *before* that call, describe a robotics **deployment** company for European
manufacturing running the founder's wedge nearly move-for-move. The entry had no `source_url`
at all, so nothing in the pipeline had ever looked. The closest funded competitor in the file
was mapped as an adjacent supplier for two days.

## Which companies to sweep

Priority order. Do not sweep the whole registry on every run.

1. **Any company with no `source_url`.** This is the gap that produced the incident. Fix these first.
2. **`relationship: competitor` and any company on the same `stack_layer` the idea is entering.** Their positioning IS the competitive landscape.
3. **Any company whose entry rests on a single informant.** One person describes the slice of the company they sit in. Check it against the public record.
4. **`deployment_maturity: retreat` candidates.** Companies rarely announce a retreat, but the gap between an old announcement and current silence is where you find one.

Skip: `role: analogue` entries kept as proof-of-category, and anything already swept inside 90 days
(positioning changes slower than contracts — a longer TTL than Phase 2's 30 days).

## What to fetch

The homepage alone is close to worthless — it is the most abstracted page a company owns. Fetch,
in this order, whichever exist:

| Page | What it yields |
|---|---|
| `/articles`, `/blog`, `/news`, `/newsroom` | Dated announcements: funding, partnerships, launches, HQ moves. The single richest source. |
| Named product page (`/atlas`, `/platform`) | `value_prop`, `works_on`, and the actual delivery sequence |
| `/about`, `/company` | Founding date, founders' backgrounds, HQ + office footprint |
| `/careers` | What they are building next, and their real headcount trajectory |
| Boilerplate "About {company}" at the foot of any press release | The company's own one-paragraph self-definition — usually the best `value_prop` source in the whole set |

Read the individual articles, not just the index. The index gives titles; the articles give the
mechanism, the numbers, and the market claim.

## Fetch mechanics — WebFetch first, browser second

`WebFetch` is the default: cheap, no browser session, cached 15 minutes.

**It fails silently on JS-rendered marketing sites**, which is most of them. The failure signature
is a near-empty return — one word, the company name, a nav skeleton — rather than an error. When
that happens, do NOT conclude the page is empty. Fall back to the browser:

```
navigate → https://{host}/articles
javascript_tool → [...document.querySelectorAll('a')].map(a => a.getAttribute('href') + ' :: ' + a.innerText.replace(/\s+/g,' ').trim().slice(0,80)).join('\n')
browser_batch → [navigate, get_page_text] × each article URL
tabs_close_mcp → when done
```

The link dump is what makes this cheap: it gives every article URL in one call, so the reads batch
into a single round trip. Close the tab when finished.

## Grading — this is company-authored, and the entry must say so

Self-published material is **positioning, not verified demand**. It is the company's own claim
about itself, written to raise money and attract customers. Grade accordingly:

- Facts about the company that are cheap to falsify — founding date, HQ, named investors, named
  partners, disclosed round size, named executives — are **usable as fact**, because a competitor,
  investor, or journalist would correct them.
- Claims about their traction, their customers' outcomes, or their market position are **claims**.
  Write them as "their own market claim:" and quote rather than assert.
- **Always state what is absent.** No customer names, no deployment count, no pricing is itself a
  finding — especially from a company that just raised a large round. Record the absence explicitly
  in `evidence:` so a later reader knows it was checked and not merely unmentioned.

Never let a self-published claim set `deployment_maturity: production`. Announcements describe
intent and capability; only a customer, a site, or an attested contract confirms a robot is running.

## Reconciling against an interview — keep both, never overwrite

When a company's own record contradicts what an informant told us, **both stay in the entry, each
labelled with its source and date.** The interview is not deleted and not marked wrong.

1. **Compare publication dates against the interview date.** If the announcements predate the call,
   the informant was not contradicting them — they were describing a different slice of the company,
   or answering a narrower question than the entry writer recorded.
2. **Default reconciliation: scope, not error.** An informant in go-to-market describes go-to-market;
   a research partnerships lead describes research partnerships. Treat the interview as accurate
   about that person's own surface and NOT as evidence about the company's full coverage.
3. **Write the reconciliation into `entry_point`**, naming both sources and the reading you took,
   so the next reader inherits the conflict rather than rediscovering it.
4. **Report it to the founder in the run summary.** A registry field silently flipping from
   `seller_data` to `integrator_deployer` is a competitive-position change, not a data cleanup.

## Writing back to `companies.md`

- `source_url:` — the richest page found, normally the articles/newsroom index rather than the homepage.
- Add a frontmatter `sources:` line naming the host, the fetch date, the dated announcements read,
  and the grading caveat in one sentence.
- Update the mapping dimensions (`stack_layer`, `role`, `value_prop`, `works_on`, `buyer`,
  `business_model`, `industries`, `relationship`, `env_control`) to match the public record.
- `known_contacts:` — reconcile against `contacts.md` while you are in the entry; a company being
  re-read is the cheapest moment to catch a missing contact id.
- Leave `pain_score` alone. It is computed in Phase 3 from transactional signals; self-published
  material is not one of its inputs and must not be smuggled in.

## Handing to Phase 4

A competitor's own market claim that restates the idea's own "why now" is evidence about the
**space**, not about the company. Route it to `evidence.md` with `source_type: article` (the vocab:evidence_source_type value; this file previously said `news`, which the validator rejects), and default
`verdict: ambiguous` — a funded competitor asserting the pain is real is weak confirmation that the
pain exists and simultaneously a fact about how contested the lane is. Do not let it move a thesis
or a lane on its own: the repo rule is that only `[T]`/`[V]`-grade buyer or site evidence does that.
Surface it to the founder as a competitive finding and let them decide.
