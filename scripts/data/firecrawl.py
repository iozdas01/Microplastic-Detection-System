"""Self-hosted Firecrawl web search helpers.

The local endpoint is used for Reddit discovery without Reddit OAuth. Firecrawl
searches the public web with a Reddit domain restriction; this module then
normalizes its response for ``scripts.data.reddit``.
"""

from __future__ import annotations

import os
import re
import time
from typing import Any
from urllib.parse import quote_plus, urlparse

import requests

from scripts.data._common import is_enabled


DEFAULT_BASE_URL = "http://127.0.0.1:3002"

_web_search_reddit_empty_streak = 0


def base_url() -> str:
    return os.environ.get("FIRECRAWL_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def is_reddit_url(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host == "reddit.com" or host.endswith(".reddit.com")


def subreddit_from_url(url: str) -> str:
    parts = [part for part in urlparse(url).path.split("/") if part]
    if len(parts) >= 2 and parts[0].lower() == "r":
        return parts[1]
    return ""


def _result_rows(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict):
        return []
    data = payload.get("data")
    if isinstance(data, list):
        return [row for row in data if isinstance(row, dict)]
    if isinstance(data, dict):
        web = data.get("web")
        if isinstance(web, list):
            return [row for row in web if isinstance(row, dict)]
    return []


def search_reddit(
    query: str,
    subreddit: str | None = None,
    limit: int = 10,
    time_filter: str = "all",
    timeout: int = 90,
) -> list[dict[str, Any]]:
    """Return Reddit search results from local Firecrawl.

    Firecrawl also asks its local Playwright service for main-content markdown.
    When Reddit permits extraction, that captures the post and visible comments;
    when it does not, the search title and description remain usable fallbacks.
    """
    if not is_enabled("firecrawl"):
        return []

    # Firecrawl already applies includeDomains. Repeating ``site:reddit.com`` in
    # the query makes SearXNG return zero results on some engines. Treat the
    # planned community as a soft semantic hint and preserve the actual
    # subreddit parsed from every returned URL.
    base_query = query.strip()
    scoped_query = base_query
    if subreddit:
        scoped_query = f"{base_query} {subreddit.strip()}"

    request_body: dict[str, Any] = {
        "query": scoped_query,
        "limit": max(1, min(int(limit), 100)),
        "sources": ["web"],
        "includeDomains": ["reddit.com"],
        "timeout": timeout * 1000,
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
        },
    }
    time_map = {
        "day": "qdr:d",
        "week": "qdr:w",
        "month": "qdr:m",
        "year": "qdr:y",
    }
    if time_filter in time_map:
        request_body["tbs"] = time_map[time_filter]

    errors: list[str] = []
    attempted_queries = [scoped_query]
    if subreddit and scoped_query != base_query:
        attempted_queries.append(base_query)

    # After web-engine discovery has come back Reddit-empty twice in this
    # process, stop paying for it on every call and use the fallback directly.
    global _web_search_reddit_empty_streak
    if _web_search_reddit_empty_streak >= 2:
        attempted_queries = []

    for attempted_query in attempted_queries:
        attempted_body = {**request_body, "query": attempted_query}
        for version in ("v2", "v1"):
            endpoint = f"{base_url()}/{version}/search"
            try:
                response = requests.post(
                    endpoint,
                    json=attempted_body,
                    timeout=timeout,
                )
            except requests.RequestException as exc:
                errors.append(f"{version}: {exc}")
                continue
            if response.status_code in {404, 405}:
                errors.append(f"{version}: HTTP {response.status_code}")
                continue
            if response.status_code != 200:
                errors.append(
                    f"{version}: HTTP {response.status_code} {response.text[:200]}"
                )
                continue
            try:
                rows = _result_rows(response.json())
            except ValueError as exc:
                errors.append(f"{version}: invalid JSON: {exc}")
                continue

            normalized: list[dict[str, Any]] = []
            for row in rows:
                url = str(row.get("url", "")).strip()
                if not is_reddit_url(url):
                    continue
                metadata = row.get("metadata")
                if not isinstance(metadata, dict):
                    metadata = {}
                title = str(
                    row.get("title") or metadata.get("title") or ""
                ).strip()
                description = str(
                    row.get("description")
                    or metadata.get("description")
                    or ""
                ).strip()
                extracted_text = str(row.get("markdown") or "").strip()
                normalized.append({
                    "title": title,
                    "selftext": (
                        extracted_text[:12000]
                        if extracted_text
                        else description[:1200]
                    ),
                    "url": url,
                    "score": 0,
                    "num_comments": 0,
                    "created_utc": "",
                    "subreddit": subreddit_from_url(url) or subreddit or "",
                    "sort": "web_relevance",
                    "query": query,
                    "flair": "",
                    "comments": [],
                    "provider": "firecrawl",
                })
            if normalized:
                _web_search_reddit_empty_streak = 0
                return normalized

            # The endpoint worked but the community hint was too restrictive.
            # Retry the unscoped belief/hunch query before changing providers.
            _web_search_reddit_empty_streak += 1
            break

    # Web-engine discovery failed (engines throttled, or includeDomains
    # ignored by the self-hosted build). Old.reddit search pages render fine
    # through the local Playwright service even where Reddit's JSON API is
    # blocked, and they carry each post's selftext inline.
    fallback = search_reddit_oldsearch(
        query,
        subreddit=subreddit,
        limit=limit,
        time_filter=time_filter,
        timeout=timeout,
    )
    if fallback:
        return fallback

    return [{
        "error": "; ".join(errors) or "Firecrawl search returned no Reddit results",
        "subreddit": subreddit or "",
        "query": query,
        "provider": "firecrawl",
    }]


_OLDSEARCH_RESULT = re.compile(
    r"(?P<points>\d+)\s+points?\s+"
    r"\[(?P<comments>\d+)\s+comments?\]"
    r"\((?P<url>https://old\.reddit\.com/r/[^)]+/comments/[^)]+)\)"
    r"\s+submitted\s+(?P<age>[^b]+?)\s+by\s+\[(?P<author>[^\]]+)\]",
)


def search_reddit_oldsearch(
    query: str,
    subreddit: str | None = None,
    limit: int = 10,
    time_filter: str = "all",
    timeout: int = 90,
) -> list[dict[str, Any]]:
    """Discover Reddit threads by scraping old.reddit.com search result pages.

    Fallback for when no web search engine is usable. The search page itself
    includes each self post's full body, so one scrape per query covers both
    discovery and content; comments still require a per-thread scrape.
    """
    if not is_enabled("firecrawl"):
        return []

    if subreddit:
        page = (
            f"https://old.reddit.com/r/{subreddit.strip()}/search/"
            f"?q={quote_plus(query)}&restrict_sr=on&sort=relevance"
        )
    else:
        page = f"https://old.reddit.com/search/?q={quote_plus(query)}&sort=relevance"
    if time_filter in {"hour", "day", "week", "month", "year"}:
        page += f"&t={time_filter}"

    try:
        response = requests.post(
            f"{base_url()}/v2/scrape",
            json={
                "url": page,
                "formats": ["markdown"],
                "onlyMainContent": True,
                "timeout": timeout * 1000,
            },
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
    except (requests.RequestException, ValueError):
        return []

    markdown = ""
    if isinstance(payload, dict):
        data = payload.get("data")
        if isinstance(data, dict):
            markdown = str(data.get("markdown") or "")
    if not markdown:
        return []

    # Be polite to old.reddit: the caller loops over many queries.
    time.sleep(2)

    matches = list(_OLDSEARCH_RESULT.finditer(markdown))
    normalized: list[dict[str, Any]] = []
    for index, match in enumerate(matches[: max(1, int(limit))]):
        url = match.group("url").strip()
        block_end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        )
        block = markdown[match.end():block_end]
        # Selftext runs from after the "to [r/Sub](...)" line to the
        # "moreless" expander old.reddit appends to each expanded post.
        body = ""
        to_line = re.search(r"to \[r/[^\]]+\]\([^)]+\)\s*", block)
        if to_line:
            body = block[to_line.end():]
            cut = body.find("moreless")
            if cut != -1:
                body = body[:cut]
            body = body.strip()
        title_match = re.search(
            r"\[(?!\!)([^\]]+)\]\(" + re.escape(url) + r"\)", markdown
        )
        title = ""
        if title_match and not re.fullmatch(
            r"\d+\s+comments?", title_match.group(1).strip()
        ):
            title = title_match.group(1).strip()
        if not title:
            slug = [part for part in urlparse(url).path.split("/") if part]
            title = slug[-1].replace("_", " ") if slug else ""
        normalized.append({
            "title": title,
            "selftext": body[:12000],
            "url": url.replace("old.reddit.com", "www.reddit.com"),
            "score": int(match.group("points")),
            "num_comments": int(match.group("comments")),
            "created_utc": "",
            "created_relative": match.group("age").strip(),
            "subreddit": subreddit_from_url(url) or (subreddit or ""),
            "sort": "oldreddit_search_relevance",
            "query": query,
            "flair": "",
            "comments": [],
            "provider": "firecrawl_oldreddit",
        })
    return normalized
