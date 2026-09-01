# Local Firecrawl

Self-hosted Firecrawl and SearXNG power keyless Reddit discovery for the
ideation shotgun. SearXNG aggregates public search engines; Firecrawl exposes
the search API, and its local Playwright service extracts the main post plus
visible comments when Reddit permits it. Results are restricted to Reddit,
then normalized into the same corpus as Hacker News. Search descriptions remain
the fallback when a page cannot be extracted.

The service binds only to `127.0.0.1:3002`. It does not use the Firecrawl cloud
API and does not require a Firecrawl or Reddit API key.

## Commands

```bash
scripts/firecrawl-service.sh up
scripts/firecrawl-service.sh status
scripts/firecrawl-service.sh smoke-test
scripts/firecrawl-service.sh logs
scripts/firecrawl-service.sh down
```

The runtime is Colima plus Docker Compose. Containers use
`restart: unless-stopped`, so they return when Colima starts. The stack is
intentionally limited to two concurrent jobs and one browser instance.

Firecrawl discovers Reddit URLs through web search. Its self-hosted edition
does not include Firecrawl's commercial anti-blocking engine, so extraction can
occasionally return only the search title and description. Those records remain
usable and visibly identify their provider; an extraction failure is not
treated as negative evidence. A subreddit is a search hint: if it produces no
results, the adapter retries the same belief/hunch query across Reddit before
changing providers.
