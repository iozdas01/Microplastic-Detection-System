"""Shared Reddit + Hacker News reconnaissance for belief-and-hunch ideation.

The language model plans the search; this module performs deterministic collection,
normalization, attribution, and deduplication. It deliberately does not cluster or
score pains. Those are interpretive tasks for the shotgun's recon analyst.

Plan schema:
{
  "belief": "A durable field-level conviction",
  "current_hunch": {                        // required unless mode is "explore"
    "id": "H1",
    "statement": "The founder-confirmed claim every search must examine"
  },
  "mode": "initial_test",                   // initial_test | reframe | explore
  "hypotheses": [
    {
      "id": "P1",
      "label": "Possible workflow pain",
      "queries": ["manual reconciliation workaround", "reporting nightmare"],
      "subreddits": ["consulting", "operations"]
    }
  ]
}

CLI:
    python -m scripts.data.community_recon --plan query-plan.json
    python -m scripts.data.community_recon --plan query-plan.json --dry-run

The JSON response contains normalized ``records``, per-source ``status``, and
summary counts. Redirect stdout to the run's ``raw-corpus.json`` artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from scripts.data._common import emit_json, is_enabled
from scripts.data.hn import search_all as search_hn
from scripts.data.reddit import search as search_reddit


MAX_HYPOTHESES = 6
MAX_QUERIES_PER_HYPOTHESIS = 8
MAX_SUBREDDITS_PER_HYPOTHESIS = 8
BEHAVIORAL_WORKAROUND_MARKERS = (
    "we use",
    "we built",
    "i made",
    "i wrote",
    "i built",
    "instead we",
    "switched to",
    "ended up",
    "we just",
    "spreadsheet instead",
    "cobbled together",
    "rolled our own",
)


def _clean_list(value: Any, limit: int) -> list[str]:
    if not isinstance(value, list):
        return []
    cleaned: list[str] = []
    for item in value:
        text = str(item).strip()
        if text and text not in cleaned:
            cleaned.append(text)
    return cleaned[:limit]


def validate_plan(payload: Any) -> dict[str, Any]:
    """Validate and normalize a reconnaissance plan."""
    if not isinstance(payload, dict):
        raise ValueError("plan must be a JSON object")

    belief = str(payload.get("belief", "")).strip()
    if not belief:
        raise ValueError("plan.belief is required")

    mode = str(payload.get("mode", "initial_test")).strip() or "initial_test"
    if mode not in {"initial_test", "reframe", "explore"}:
        raise ValueError("plan.mode must be initial_test, reframe or explore")

    # `explore` runs before a hunch exists, so it is the one mode that may omit one.
    # Everything else the plan must carry is unchanged, and deliberately so: the belief
    # and at least one hypothesis with real queries are what keep an explore plan from
    # becoming an open-ended trawl. This module still only COLLECTS — it does not
    # cluster or score — so nothing here can invent a finding in any mode.
    raw_hunch = payload.get("current_hunch")
    hunch: dict[str, str] | None = None
    if mode == "explore":
        if raw_hunch:
            raise ValueError(
                "plan.current_hunch must be absent in explore mode - a hunch under "
                "test means the field is not being explored"
            )
    else:
        if not isinstance(raw_hunch, dict):
            raise ValueError("plan.current_hunch is required")
        hunch_id = str(raw_hunch.get("id", "")).strip()
        hunch_statement = str(raw_hunch.get("statement", "")).strip()
        if not hunch_id:
            raise ValueError("plan.current_hunch.id is required")
        if not hunch_statement:
            raise ValueError("plan.current_hunch.statement is required")
        hunch = {"id": hunch_id, "statement": hunch_statement}

    raw_hypotheses = payload.get("hypotheses")
    if not isinstance(raw_hypotheses, list) or not raw_hypotheses:
        raise ValueError("plan.hypotheses must contain at least one item")

    hypotheses: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for position, raw in enumerate(raw_hypotheses[:MAX_HYPOTHESES], start=1):
        if not isinstance(raw, dict):
            continue
        hypothesis_id = str(raw.get("id") or f"P{position}").strip()
        if hypothesis_id in seen_ids:
            raise ValueError(f"duplicate hypothesis id: {hypothesis_id}")
        queries = _clean_list(raw.get("queries"), MAX_QUERIES_PER_HYPOTHESIS)
        if not queries:
            raise ValueError(f"{hypothesis_id} has no queries")
        hypotheses.append({
            "id": hypothesis_id,
            "label": str(raw.get("label", "")).strip() or hypothesis_id,
            "queries": queries,
            "subreddits": _clean_list(
                raw.get("subreddits"), MAX_SUBREDDITS_PER_HYPOTHESIS
            ),
        })
        seen_ids.add(hypothesis_id)

    if not hypotheses:
        raise ValueError("plan has no valid hypotheses")

    return {
        "belief": belief,
        "current_hunch": hunch,
        "mode": mode,
        "hypotheses": hypotheses,
    }


def load_plan(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return validate_plan(json.load(handle))


def _stable_id(source: str, native_id: str, url: str, text: str) -> str:
    identity = native_id or url or text[:240]
    digest = hashlib.sha256(f"{source}:{identity}".encode("utf-8")).hexdigest()[:16]
    return f"{source}-{digest}"


def _behavioral_workaround_excerpt(text: str) -> str:
    """Return a compact observed-behavior excerpt from extracted page text."""
    lowered = text.lower()
    positions = [
        lowered.find(marker)
        for marker in BEHAVIORAL_WORKAROUND_MARKERS
        if marker in lowered
    ]
    if not positions:
        return ""
    position = min(positions)
    start = max(0, position - 180)
    end = min(len(text), position + 420)
    return " ".join(text[start:end].split())


def _normalize_reddit(
    item: dict[str, Any], hypothesis: dict[str, Any]
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    if "error" in item:
        return None, {
            "source": "reddit",
            "hypothesis_id": hypothesis["id"],
            "query": item.get("query", ""),
            "community": item.get("subreddit", ""),
            "error": str(item.get("error", "unknown error")),
        }

    title = str(item.get("title", "")).strip()
    body = str(item.get("selftext", "")).strip()
    url = str(item.get("url", "")).strip()
    comments = item.get("comments") if isinstance(item.get("comments"), list) else []
    workaround_snippets = [
        str(comment.get("body", "")).strip()
        for comment in comments
        if isinstance(comment, dict)
        and comment.get("is_workaround")
        and str(comment.get("body", "")).strip()
    ][:5]
    if not workaround_snippets:
        extracted_workaround = _behavioral_workaround_excerpt(body)
        if extracted_workaround:
            workaround_snippets.append(extracted_workaround)

    record = {
        "record_id": _stable_id("reddit", "", url, f"{title}\n{body}"),
        "source": "reddit",
        "native_type": "post",
        "url": url,
        "community": f"r/{item.get('subreddit', '')}".rstrip("/"),
        "created_utc": item.get("created_utc", ""),
        "title": title,
        "text": body,
        "engagement": {
            "score": item.get("score", 0),
            "comments": item.get("num_comments", 0),
        },
        "workaround_observed": bool(workaround_snippets),
        "workaround_snippets": workaround_snippets,
        "role_hint": item.get("flair", ""),
        "provider": item.get("provider", "unknown"),
        "matched_queries": [str(item.get("query", "")).strip()],
        "hypothesis_ids": [hypothesis["id"]],
    }
    return record, None


def _normalize_hn(
    item: dict[str, Any], hypothesis: dict[str, Any], native_type: str
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    if "error" in item:
        return None, {
            "source": "hacker_news",
            "hypothesis_id": hypothesis["id"],
            "query": item.get("query", ""),
            "error": str(item.get("error", "unknown error")),
        }

    if native_type == "comment":
        native_id = str(item.get("object_id", "")).strip()
        url = str(item.get("comment_url", "")).strip()
        title = str(item.get("story_title", "")).strip()
        text = str(item.get("body", "")).strip()
        engagement = {"points": item.get("points")}
        workaround = bool(item.get("is_workaround"))
    else:
        native_id = str(item.get("object_id", "")).strip()
        url = str(item.get("hn_url", "")).strip()
        title = str(item.get("title", "")).strip()
        text = str(item.get("story_text", "")).strip()
        engagement = {
            "points": item.get("points", 0),
            "comments": item.get("num_comments", 0),
        }
        workaround = False

    record = {
        "record_id": _stable_id("hn", native_id, url, f"{title}\n{text}"),
        "source": "hacker_news",
        "native_type": native_type,
        "url": url,
        "community": "Hacker News",
        "created_utc": item.get("created_utc", ""),
        "title": title,
        "text": text,
        "engagement": engagement,
        "workaround_observed": workaround,
        "workaround_snippets": [text] if workaround and text else [],
        "role_hint": "",
        "matched_queries": [str(item.get("query", "")).strip()],
        "hypothesis_ids": [hypothesis["id"]],
    }
    return record, None


def _merge_record(existing: dict[str, Any], incoming: dict[str, Any]) -> None:
    existing["matched_queries"] = sorted(set(
        existing.get("matched_queries", []) + incoming.get("matched_queries", [])
    ))
    existing["hypothesis_ids"] = sorted(set(
        existing.get("hypothesis_ids", []) + incoming.get("hypothesis_ids", [])
    ))
    snippets = existing.get("workaround_snippets", []) + incoming.get(
        "workaround_snippets", []
    )
    existing["workaround_snippets"] = list(dict.fromkeys(snippets))[:5]
    existing["workaround_observed"] = bool(
        existing.get("workaround_observed") or incoming.get("workaround_observed")
    )


def collect(
    plan: dict[str, Any],
    sources: set[str] | None = None,
    reddit_limit: int = 25,
    hn_hits: int = 60,
    time_filter: str = "year",
) -> dict[str, Any]:
    """Collect and normalize community records for a validated plan."""
    selected = sources or {"reddit", "hn"}
    records_by_id: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, Any]] = []
    calls = {"reddit": 0, "hacker_news": 0}

    reddit_available = "reddit" in selected and (
        is_enabled("firecrawl")
        or is_enabled("reddit_oauth")
        or is_enabled("reddit_json")
    )
    hn_available = "hn" in selected and is_enabled("hacker_news_algolia")

    for hypothesis in plan["hypotheses"]:
        if reddit_available and hypothesis["subreddits"]:
            calls["reddit"] += 1
            reddit_items = search_reddit(
                subs=hypothesis["subreddits"],
                queries=hypothesis["queries"],
                limit_top=reddit_limit,
                limit_controversial=max(5, reddit_limit // 2),
                time_filter=time_filter,
            )
            for item in reddit_items:
                record, error = _normalize_reddit(item, hypothesis)
                if error:
                    errors.append(error)
                elif record:
                    if record["record_id"] in records_by_id:
                        _merge_record(records_by_id[record["record_id"]], record)
                    else:
                        records_by_id[record["record_id"]] = record

        if hn_available:
            calls["hacker_news"] += 1
            hn_payload = search_hn(hypothesis["queries"], hits_per_query=hn_hits)
            for native_type, key in (("comment", "comments"), ("story", "stories")):
                for item in hn_payload.get(key, []):
                    record, error = _normalize_hn(item, hypothesis, native_type)
                    if error:
                        errors.append(error)
                    elif record:
                        if record["record_id"] in records_by_id:
                            _merge_record(records_by_id[record["record_id"]], record)
                        else:
                            records_by_id[record["record_id"]] = record
            for error in hn_payload.get("errors", []):
                errors.append({
                    "source": "hacker_news",
                    "hypothesis_id": hypothesis["id"],
                    "query": error.get("query", ""),
                    "error": str(error.get("error", "unknown error")),
                })

    records = sorted(
        records_by_id.values(),
        key=lambda record: str(record.get("created_utc", "")),
        reverse=True,
    )
    source_counts = {
        "reddit": sum(record["source"] == "reddit" for record in records),
        "hacker_news": sum(record["source"] == "hacker_news" for record in records),
    }
    return {
        "plan": plan,
        "records": records,
        "status": {
            "reddit": {
                "enabled": reddit_available,
                "calls": calls["reddit"],
                "records": source_counts["reddit"],
            },
            "hacker_news": {
                "enabled": hn_available,
                "calls": calls["hacker_news"],
                "records": source_counts["hacker_news"],
            },
            "errors": errors,
        },
        "summary": {
            "records": len(records),
            "workaround_records": sum(
                bool(record.get("workaround_observed")) for record in records
            ),
            "hypotheses": len(plan["hypotheses"]),
        },
    }


def dry_run(plan: dict[str, Any], sources: set[str]) -> dict[str, Any]:
    return {
        "valid": True,
        "plan": plan,
        "planned_calls": {
            "reddit": sum(
                bool(hypothesis["subreddits"]) for hypothesis in plan["hypotheses"]
            ) if "reddit" in sources else 0,
            "hacker_news": len(plan["hypotheses"]) if "hn" in sources else 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect and normalize Reddit + Hacker News reconnaissance"
    )
    parser.add_argument("--plan", required=True, help="Path to query-plan.json")
    parser.add_argument(
        "--sources", default="reddit,hn",
        help="Comma-separated sources: reddit,hn",
    )
    parser.add_argument("--reddit-limit", type=int, default=25)
    parser.add_argument("--hn-hits", type=int, default=60)
    parser.add_argument(
        "--time-filter", default="year",
        choices=["all", "year", "month", "week", "day"],
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Validate the plan and show intended calls without network access",
    )
    args = parser.parse_args()

    try:
        plan = load_plan(args.plan)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        raise SystemExit(2)

    sources = {
        source.strip() for source in args.sources.split(",") if source.strip()
    }
    unsupported = sources - {"reddit", "hn"}
    if unsupported:
        print(json.dumps({
            "error": f"unsupported sources: {', '.join(sorted(unsupported))}"
        }), file=sys.stderr)
        raise SystemExit(2)

    if args.dry_run:
        emit_json(dry_run(plan, sources))
        return

    emit_json(collect(
        plan,
        sources=sources,
        reddit_limit=max(1, args.reddit_limit),
        hn_hits=max(2, args.hn_hits),
        time_filter=args.time_filter,
    ))


if __name__ == "__main__":
    main()
