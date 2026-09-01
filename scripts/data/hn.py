"""HackerNews query via Algolia HN Search — no key required.

CLI:
    python -m scripts.data.hn --queries "maintenance backlog|work order triage" \
        [--hits 100]

Emits JSON `{comments: [...], stories: [...], errors: [...]}` on stdout.

Python API:
    from scripts.data.hn import search_all
    data = search_all(["maintenance backlog"])
"""

from __future__ import annotations

import argparse
import datetime
import sys
import urllib.parse

from scripts.data._common import emit_json, http_get

WORKAROUND_KEYWORDS = [
    "we use", "we built", "i made", "i wrote", "i built",
    "workaround", "hack", "instead we", "switched to",
    "gave up and", "ended up", "we just", "diy", "homebrew",
    "duct tape", "manual process", "spreadsheet instead",
    "cobbled together", "rolled our own", "hacked together",
]

ALGOLIA_ENDPOINT = "https://hn.algolia.com/api/v1/search"

# Algolia's HN index is configured with removeWordsIfNoResults: when a long
# natural-language query has no exact hits, it silently drops words until
# something matches — so "verify toolpath before cutting" degrades to any recent
# post containing "cutting" or "before". One recon run shipped 1,475 HN records
# of which the head of the corpus was TTRPG tools and hyperscaler threads
# (2026-08-20). The filter below re-imposes relevance client-side: a record must
# contain at least half of the query's content words to count as a match.
_STOPWORDS = frozenset(
    "the a an of to in on for is are was were be been it its this that than then "
    "we i you they he she my our your and or not no do does did when who what "
    "how why with without before after first last new out up down off".split()
)


def _content_words(query: str) -> list[str]:
    return [w for w in query.lower().split() if w not in _STOPWORDS and len(w) > 2]


def matches_query(query: str, *texts: str) -> bool:
    """True when enough of the query's content words appear in the record."""
    words = _content_words(query)
    if not words:
        return True
    haystack = " ".join(t.lower() for t in texts if t)
    hit = sum(1 for w in words if w in haystack)
    needed = 1 if len(words) == 1 else max(2, -(-len(words) // 2))  # ceil(n/2), floor 2
    return hit >= needed


def is_workaround(text: str) -> bool:
    if not text:
        return False
    lower = text.lower()
    return any(kw in lower for kw in WORKAROUND_KEYWORDS)


def _strip_html(text: str) -> str:
    """Light HTML-entity + tag cleanup for Algolia comment_text."""
    if not text:
        return ""
    replacements = [
        ("<p>", "\n"), ("</p>", ""), ("<i>", ""), ("</i>", ""),
        ("<pre><code>", "```\n"), ("</code></pre>", "\n```"),
        ("&#x27;", "'"), ("&quot;", '"'), ("&amp;", "&"),
        ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " "),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text.strip()


def _hn_item_url(object_id: str) -> str:
    return f"https://news.ycombinator.com/item?id={object_id}"


def _search(query: str, tags: str, hits_per_query: int) -> list[dict]:
    params = {"query": query, "tags": tags, "hitsPerPage": hits_per_query}
    url = f"{ALGOLIA_ENDPOINT}?{urllib.parse.urlencode(params)}"
    r = http_get(url, headers={"User-Agent": "StartupLab/0.1 hn-mining"}, timeout=30)
    if r is None or r.status_code != 200:
        return [{"error": f"http {r.status_code if r else 'None'}",
                 "query": query, "tag": tags}]
    try:
        return r.json().get("hits", []) or []
    except ValueError:
        return [{"error": "invalid_json", "query": query, "tag": tags}]


def search_comments(query: str, hits_per_query: int = 100) -> list[dict]:
    """Search HN comments matching a query."""
    hits = _search(query, "comment", hits_per_query)
    results = []
    for hit in hits:
        if "error" in hit:
            results.append(hit)
            continue
        body = _strip_html(hit.get("comment_text", ""))
        if not matches_query(query, body, hit.get("story_title", "")):
            continue
        created_at_i = hit.get("created_at_i", 0)
        results.append({
            "type": "comment",
            "query": query,
            "body": body[:600],
            "author": hit.get("author", ""),
            "points": hit.get("points"),
            "created_utc": datetime.datetime.utcfromtimestamp(created_at_i).isoformat()
                if created_at_i else "",
            "story_id": hit.get("story_id"),
            "story_title": hit.get("story_title", ""),
            "story_url": hit.get("story_url", ""),
            "comment_url": _hn_item_url(hit.get("objectID")),
            "object_id": hit.get("objectID"),
            "is_workaround": is_workaround(body),
        })
    return results


def search_stories(query: str, hits_per_query: int = 50) -> list[dict]:
    """Search HN stories matching a query."""
    hits = _search(query, "story", hits_per_query)
    results = []
    for hit in hits:
        if "error" in hit:
            results.append(hit)
            continue
        title = hit.get("title", "") or hit.get("story_title", "")
        story_text = _strip_html(hit.get("story_text", "") or "")
        if not matches_query(query, title, story_text):
            continue
        created_at_i = hit.get("created_at_i", 0)
        results.append({
            "type": "story",
            "query": query,
            "title": title,
            "story_text": story_text[:600],
            "author": hit.get("author", ""),
            "points": hit.get("points", 0),
            "num_comments": hit.get("num_comments", 0),
            "created_utc": datetime.datetime.utcfromtimestamp(created_at_i).isoformat()
                if created_at_i else "",
            "external_url": hit.get("url", ""),
            "hn_url": _hn_item_url(hit.get("objectID")),
            "object_id": hit.get("objectID"),
        })
    return results


def _rank(items: list[dict]) -> list[dict]:
    """Rank stories by points; comments by recency (points often null)."""
    def key(item: dict):
        if item.get("type") == "story":
            return (item.get("points") or 0)
        return item.get("created_utc") or ""
    return sorted(items, key=key, reverse=True)


def search_all(queries: list[str], hits_per_query: int = 100) -> dict:
    all_results: dict[str, list] = {"comments": [], "stories": [], "errors": []}
    for query in queries:
        for hit in search_comments(query, hits_per_query):
            (all_results["errors"] if "error" in hit else all_results["comments"]).append(hit)
        for hit in search_stories(query, hits_per_query // 2):
            (all_results["errors"] if "error" in hit else all_results["stories"]).append(hit)
    all_results["stories"] = _rank(all_results["stories"])
    all_results["comments"] = _rank(all_results["comments"])
    return all_results


def main() -> None:
    ap = argparse.ArgumentParser(description="HackerNews Algolia query")
    ap.add_argument("--queries", required=True,
                    help="Pipe-separated search queries")
    ap.add_argument("--hits", type=int, default=100,
                    help="Max hits per query per tag (comments) — stories get half")
    args = ap.parse_args()

    queries = [q.strip() for q in args.queries.split("|") if q.strip()]
    if not queries:
        print('{"error": "empty --queries"}', file=sys.stderr)
        sys.exit(1)

    emit_json(search_all(queries, args.hits))


if __name__ == "__main__":
    main()
