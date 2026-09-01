"""Reddit pain-signal query — Firecrawl with secondary fallbacks.

CLI:
    python -m scripts.data.reddit \
        --subs windpower,oilandgas \
        --queries "maintenance backlog workaround|CMMS nightmare" \
        [--limit-top 50] [--limit-controversial 25] [--time-filter all]

Emits JSON list on stdout.

Three paths:
  1. **Self-hosted Firecrawl** (primary) — searches the public web with results
     restricted to Reddit. No Reddit or Firecrawl cloud API key is required.
  2. **PRAW** (optional) — requires ``REDDIT_CLIENT_ID`` +
     ``REDDIT_CLIENT_SECRET`` and returns full comment threads and scores.
  3. **Public JSON fallback** — Reddit aggressively
     blocks unauthenticated search from non-browser UAs; this path frequently
     returns ``[{"error": "http None"}]`` even with a browser-like UA.

Python API:
    from scripts.data.reddit import search
    posts = search(subs=["facilities"], queries=["work order backlog"])
"""

from __future__ import annotations

import argparse
import datetime
import os
import sys
from typing import Any

from scripts.data._common import emit_json, http_get, is_enabled
from scripts.data.firecrawl import search_reddit as search_firecrawl

WORKAROUND_KEYWORDS = [
    "we use", "we built", "i made", "i wrote", "i built",
    "workaround", "hack", "instead we", "switched to",
    "gave up and", "ended up", "we just", "diy", "homebrew",
    "duct tape", "manual process", "spreadsheet instead",
    "cobbled together", "rolled our own",
]


def is_workaround(text: str) -> bool:
    if not text:
        return False
    lower = text.lower()
    return any(kw in lower for kw in WORKAROUND_KEYWORDS)


def _try_praw() -> Any | None:
    """Return a PRAW Reddit client if creds + package are available; else None."""
    client_id = os.environ.get("REDDIT_CLIENT_ID", "").strip()
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET", "").strip()
    if not client_id or not client_secret:
        return None
    try:
        import praw  # type: ignore
    except ImportError:
        return None
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=os.environ.get("REDDIT_USER_AGENT", "StartupLab/0.1").strip(),
        read_only=True,
    )


def _praw_scrape(reddit: Any, subreddit_name: str, queries: list[str],
                 limit_top: int, limit_controversial: int,
                 time_filter: str) -> list[dict]:
    results: list[dict] = []
    subreddit = reddit.subreddit(subreddit_name)
    for query in queries:
        for sort, limit in (("top", limit_top), ("controversial", limit_controversial)):
            try:
                for submission in subreddit.search(query, sort=sort,
                                                   time_filter=time_filter, limit=limit):
                    post = {
                        "title": submission.title,
                        "selftext": (submission.selftext or "")[:600],
                        "url": f"https://reddit.com{submission.permalink}",
                        "score": submission.score,
                        "num_comments": submission.num_comments,
                        "created_utc": datetime.datetime.utcfromtimestamp(
                            submission.created_utc).isoformat(),
                        "subreddit": subreddit_name,
                        "sort": sort,
                        "query": query,
                        "flair": submission.author_flair_text or "",
                        "comments": [],
                        "provider": "reddit_oauth",
                    }
                    if submission.score > 5 and submission.num_comments > 0:
                        try:
                            submission.comments.replace_more(limit=0)
                            top_comments = sorted(
                                submission.comments.list(),
                                key=lambda c: getattr(c, "score", 0),
                                reverse=True,
                            )[:25]
                            for c in top_comments:
                                if not hasattr(c, "body"):
                                    continue
                                body = c.body
                                post["comments"].append({
                                    "body": body[:400],
                                    "score": c.score,
                                    "is_workaround": is_workaround(body),
                                })
                        except Exception:
                            pass
                    results.append(post)
            except Exception as e:
                results.append({"error": str(e), "subreddit": subreddit_name,
                                "query": query, "sort": sort,
                                "provider": "reddit_oauth"})
    return results


def _json_fallback_scrape(subreddit_name: str, queries: list[str],
                          limit_top: int) -> list[dict]:
    """Public Reddit JSON search — no auth, no comments, capped at ~25 per sort."""
    results: list[dict] = []
    for query in queries:
        for sort in ("top", "hot"):
            params = {"q": query, "restrict_sr": "1", "sort": sort,
                      "t": "all", "limit": min(limit_top, 25)}
            r = http_get(
                f"https://www.reddit.com/r/{subreddit_name}/search.json",
                params=params,
                headers={"User-Agent": "Mozilla/5.0 (compatible; StartupLab/0.1; +https://startup-lab.local)"},
            )
            if r is None or r.status_code != 200:
                status = r.status_code if r else "no-response"
                results.append({
                    "error": (
                        f"reddit public JSON blocked or unreachable ({status}) — "
                        "expected for unauthenticated search (see module docstring); "
                        "firecrawl is the primary path, this was the last fallback"
                    ),
                    "subreddit": subreddit_name, "query": query})
                continue
            try:
                children = r.json().get("data", {}).get("children", [])
            except ValueError:
                continue
            for child in children:
                d = child.get("data", {}) or {}
                results.append({
                    "title": d.get("title", ""),
                    "selftext": (d.get("selftext") or "")[:600],
                    "url": f"https://reddit.com{d.get('permalink', '')}",
                    "score": d.get("score", 0),
                    "num_comments": d.get("num_comments", 0),
                    "created_utc": datetime.datetime.utcfromtimestamp(
                        d.get("created_utc", 0)).isoformat() if d.get("created_utc") else "",
                    "subreddit": subreddit_name,
                    "sort": sort,
                    "query": query,
                    "flair": d.get("link_flair_text") or "",
                    "comments": [],  # not fetched in fallback
                    "provider": "reddit_json",
                })
    return results


def search(subs: list[str], queries: list[str], limit_top: int = 50,
           limit_controversial: int = 25, time_filter: str = "all") -> list[dict]:
    """Return a flat list of post dicts across every (sub, query, sort) combination."""
    firecrawl_errors: list[dict] = []
    if is_enabled("firecrawl"):
        firecrawl_results: list[dict] = []
        for sub in subs:
            for query in queries:
                rows = search_firecrawl(
                    query=query,
                    subreddit=sub,
                    limit=min(limit_top, 25),
                    time_filter=time_filter,
                )
                firecrawl_results.extend(
                    row for row in rows if "error" not in row
                )
                firecrawl_errors.extend(
                    row for row in rows if "error" in row
                )
        if firecrawl_results:
            return firecrawl_results + firecrawl_errors

    reddit = _try_praw()
    results: list[dict] = []
    for sub in subs:
        if reddit is not None:
            results.extend(_praw_scrape(reddit, sub, queries, limit_top,
                                        limit_controversial, time_filter))
        else:
            results.extend(_json_fallback_scrape(sub, queries, limit_top))
    return results + firecrawl_errors


def main() -> None:
    ap = argparse.ArgumentParser(description="Reddit pain-signal query")
    ap.add_argument("--subs", required=True,
                    help="Comma-separated subreddit names (no r/ prefix)")
    ap.add_argument("--queries", required=True,
                    help="Pipe-separated search queries")
    ap.add_argument("--limit-top", type=int, default=50)
    ap.add_argument("--limit-controversial", type=int, default=25)
    ap.add_argument("--time-filter", default="all",
                    choices=["all", "year", "month", "week", "day"])
    args = ap.parse_args()

    subs = [s.strip() for s in args.subs.split(",") if s.strip()]
    queries = [q.strip() for q in args.queries.split("|") if q.strip()]
    if not subs or not queries:
        print('{"error": "empty --subs or --queries"}', file=sys.stderr)
        sys.exit(1)

    emit_json(search(subs, queries, args.limit_top,
                     args.limit_controversial, args.time_filter))


if __name__ == "__main__":
    main()
