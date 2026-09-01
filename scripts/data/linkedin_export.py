"""LinkedIn data export — parse the founder's own LinkedIn archive.

Replaces the browser-based 1st-degree network sweep (Pass 1 of
`startup-outreach-targets`) with a local file parse: zero browser tokens, zero
rate limits, and complete rather than search-sampled.

Get the archive: LinkedIn → Settings → Data Privacy → Get a copy of your data →
"Want something in particular" → tick **Connections**, **Messages**, and
**Invitations** → Request archive. LinkedIn emails a zip in ~10 min – 24 h.
Unzip it to `private/linkedin-export/` (gitignored — it holds other people's
personal data and must never be committed).

CLI:
    python -m scripts.data.linkedin_export inspect
    python -m scripts.data.linkedin_export connections \\
        --title "Head of Estates" --title "Reliability Engineer" \\
        --domain-noun chiller --domain-noun HVAC \\
        --exclude recruiter --exclude robotics --slug your-idea-slug
    python -m scripts.data.linkedin_export history --slug your-idea-slug

Python API:
    from scripts.data.linkedin_export import parse_connections, build_history
    payload = parse_connections(titles=["Head of Estates"])

No registry gate: this reads local files the founder downloaded. There is no
endpoint, no key, and nothing to enable. It still writes to the intel manifest
so a run is auditable alongside the API sources.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from scripts.data._common import REPO_ROOT, emit_json, log_manifest

# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------

DEFAULT_EXPORT_DIR = REPO_ROOT / "private" / "linkedin-export"

# LinkedIn has renamed these files across archive versions; match on stem.
FILE_ALIASES = {
    "connections": ("connections",),
    "messages": ("messages",),
    "invitations": ("invitations",),
}

# ---------------------------------------------------------------------------
# Column aliases — archives differ by vintage and locale, so never index by
# position and never assume one exact header string.
# ---------------------------------------------------------------------------

COLUMNS = {
    "connections": {
        "first_name": ("first name", "firstname"),
        "last_name": ("last name", "lastname"),
        "url": ("url", "profile url", "public profile url"),
        "email": ("email address", "email"),
        "company": ("company", "current company"),
        "position": ("position", "title", "current position"),
        "connected_on": ("connected on", "connected"),
    },
    "messages": {
        "conversation_id": ("conversation id",),
        "from": ("from",),
        "from_url": ("sender profile url", "from profile url"),
        "to": ("to",),
        "to_url": ("recipient profile urls", "to profile url", "recipient profile url"),
        "date": ("date", "sent at", "sent date"),
        "content": ("content", "message"),
        "folder": ("folder",),
    },
    "invitations": {
        "from": ("from",),
        "to": ("to",),
        "sent_at": ("sent at", "sentat", "date"),
        "message": ("message",),
        "direction": ("direction",),
        "inviter_url": ("inviterprofileurl", "inviter profile url"),
        "invitee_url": ("inviteeprofileurl", "invitee profile url"),
    },
}

# Seniority / connector words that carry no domain meaning. Stripped from a
# title phrase before matching so "Head of Estates Operations" also matches
# "Director of Estates Operations" and "Estates Operations Manager".
GENERIC_ROLE_TOKENS = {
    "head", "director", "manager", "lead", "leader", "chief", "vp", "svp",
    "evp", "president", "senior", "snr", "junior", "principal", "global",
    "group", "executive", "officer", "assistant", "deputy", "interim",
    "of", "the", "and", "for", "in", "at", "a", "an", "to", "with", "on",
}

DATE_FORMATS = (
    "%d %b %Y",        # 19 Jul 2025      (Connections.csv)
    "%d %B %Y",        # 19 July 2025
    "%Y-%m-%d",        # 2025-07-19
    "%m/%d/%y",        # 07/19/25
    "%m/%d/%Y",        # 07/19/2025
    "%Y/%m/%d",
)


# ---------------------------------------------------------------------------
# Normalization helpers
# ---------------------------------------------------------------------------


def _tokens(text: str) -> list[str]:
    """Lowercase word tokens, punctuation folded to spaces, 1-char tokens dropped."""
    if not text:
        return []
    cleaned = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return [t for t in cleaned.split() if len(t) > 1]


def _phrase_requirements(phrase: str) -> tuple[set[str], str]:
    """Split a title phrase into (required domain tokens, raw substring fallback).

    Generic seniority words are dropped so title variants still match. If a
    phrase is entirely generic or entirely short tokens (``O&M``), the caller
    falls back to a raw substring test.
    """
    toks = _tokens(phrase)
    required = {t for t in toks if t not in GENERIC_ROLE_TOKENS}
    if not required:
        required = set(toks)
    return required, phrase.strip().lower()


def _matches(phrase: str, *fields: str) -> bool:
    """True if every required token of `phrase` appears across the given fields."""
    haystack = " ".join(f for f in fields if f)
    if not haystack:
        return False
    required, raw = _phrase_requirements(phrase)
    if required:
        return required <= set(_tokens(haystack))
    return bool(raw) and raw in haystack.lower()


def normalize_profile_url(url: str) -> str:
    """Reduce a LinkedIn profile URL to its `/in/<slug>` identity, or '' if not one.

    Drops query strings, tracking params, locale subdomains, and trailing
    slashes so the same person joins across Connections / messages /
    Invitations, all of which format the URL differently.
    """
    if not url:
        return ""
    u = url.strip().split("?")[0].split("#")[0].rstrip("/")
    m = re.search(r"/in/([^/]+)", u, flags=re.IGNORECASE)
    if not m:
        return ""
    return m.group(1).lower()


def _norm_person(name: str) -> str:
    """Fallback join key when profile URLs are missing or URN-style."""
    return " ".join(_tokens(name))


def _parse_date(value: str) -> str:
    """Best-effort ISO date. Returns '' when unparseable rather than raising."""
    if not value:
        return ""
    raw = value.strip()
    # "2025-07-19 14:23:11 UTC" → take the date half
    head = raw.split(" ")[0] if re.match(r"^\d{4}-\d{2}-\d{2}", raw) else raw
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(head, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    # Some archives use "2025-07-19 14:23:11 UTC" with a space before UTC only.
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", raw)
    return m.group(1) if m else ""


def _get(row: dict[str, str], kind: str, field: str) -> str:
    """Read a logical field from a row using the alias table."""
    for alias in COLUMNS[kind][field]:
        if alias in row:
            return (row[alias] or "").strip()
    return ""


# ---------------------------------------------------------------------------
# File discovery + CSV reading
# ---------------------------------------------------------------------------


def _iter_source_files(export_path: Path) -> Iterable[tuple[str, bytes]]:
    """Yield (lowercase filename, raw bytes) from a directory or a .zip archive."""
    if export_path.is_file() and export_path.suffix.lower() == ".zip":
        with zipfile.ZipFile(export_path) as zf:
            for info in zf.infolist():
                if info.is_dir() or not info.filename.lower().endswith(".csv"):
                    continue
                yield Path(info.filename).name.lower(), zf.read(info)
        return
    if export_path.is_dir():
        for p in sorted(export_path.rglob("*.csv")):
            yield p.name.lower(), p.read_bytes()


def find_export(export_path: Path | str | None = None) -> tuple[Path, dict[str, bytes]]:
    """Locate the archive and return (resolved path, {kind: raw csv bytes}).

    Accepts an unzipped directory or the .zip straight from LinkedIn. Raises
    FileNotFoundError with an actionable message when nothing is there.
    """
    path = Path(export_path) if export_path else DEFAULT_EXPORT_DIR
    if not path.exists():
        raise FileNotFoundError(
            f"No LinkedIn export at {path}. Download it from LinkedIn → Settings → "
            f"Data Privacy → Get a copy of your data (tick Connections, Messages, "
            f"Invitations), then unzip to {DEFAULT_EXPORT_DIR} or pass --export."
        )

    found: dict[str, bytes] = {}
    for filename, raw in _iter_source_files(path):
        stem = Path(filename).stem.lower()
        for kind, aliases in FILE_ALIASES.items():
            if kind in found:
                continue
            if any(stem == a or stem.startswith(a) for a in aliases):
                found[kind] = raw
    if not found:
        raise FileNotFoundError(
            f"Found {path} but no Connections/messages/Invitations CSV inside it. "
            f"Check the archive actually contains those files."
        )
    return path, found


def read_export_csv(raw: bytes) -> list[dict[str, str]]:
    """Parse an export CSV into lowercase-keyed dicts.

    LinkedIn prefixes Connections.csv with a "Notes:" preamble before the real
    header row, so the header is sniffed rather than assumed to be line 1.
    """
    text = raw.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()

    header_idx = 0
    for i, line in enumerate(lines[:15]):
        low = line.lower()
        if ("first name" in low and "last name" in low) or \
           ("conversation id" in low) or \
           ("direction" in low and "sent at" in low) or \
           (low.startswith("from,") and "to" in low):
            header_idx = i
            break

    body = "\n".join(lines[header_idx:])
    reader = csv.DictReader(io.StringIO(body))
    rows: list[dict[str, str]] = []
    for row in reader:
        rows.append({
            (k or "").strip().lower(): (v if isinstance(v, str) else "")
            for k, v in row.items()
        })
    return rows


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def load_connections(files: dict[str, bytes]) -> list[dict[str, Any]]:
    """All 1st-degree connections, normalized."""
    out = []
    for row in read_export_csv(files.get("connections", b"")):
        first = _get(row, "connections", "first_name")
        last = _get(row, "connections", "last_name")
        name = " ".join(p for p in (first, last) if p).strip()
        url = _get(row, "connections", "url")
        if not name and not url:
            continue
        slug = normalize_profile_url(url)
        out.append({
            "name": name,
            "first_name": first,
            "last_name": last,
            "linkedin_url": f"https://www.linkedin.com/in/{slug}/" if slug else url,
            "profile_slug": slug,
            "company": _get(row, "connections", "company"),
            "position": _get(row, "connections", "position"),
            "connected_on": _parse_date(_get(row, "connections", "connected_on")),
            "email": _get(row, "connections", "email"),
            "degree": "1st",
        })
    return out


def load_messages(files: dict[str, bytes]) -> list[dict[str, Any]]:
    out = []
    for row in read_export_csv(files.get("messages", b"")):
        out.append({
            "conversation_id": _get(row, "messages", "conversation_id"),
            "from": _get(row, "messages", "from"),
            "from_slug": normalize_profile_url(_get(row, "messages", "from_url")),
            "to": _get(row, "messages", "to"),
            "to_slug": normalize_profile_url(_get(row, "messages", "to_url")),
            "date": _parse_date(_get(row, "messages", "date")),
            "content": _get(row, "messages", "content"),
            "folder": _get(row, "messages", "folder").lower(),
        })
    return out


def load_invitations(files: dict[str, bytes]) -> list[dict[str, Any]]:
    out = []
    for row in read_export_csv(files.get("invitations", b"")):
        out.append({
            "from": _get(row, "invitations", "from"),
            "to": _get(row, "invitations", "to"),
            "sent_at": _parse_date(_get(row, "invitations", "sent_at")),
            "message": _get(row, "invitations", "message"),
            "direction": _get(row, "invitations", "direction").upper(),
            "inviter_slug": normalize_profile_url(_get(row, "invitations", "inviter_url")),
            "invitee_slug": normalize_profile_url(_get(row, "invitations", "invitee_url")),
        })
    return out


def detect_account_owner(messages: list[dict[str, Any]]) -> str:
    """Infer whose archive this is: the person present in the most conversations.

    Robust to lopsided send/receive ratios — the owner appears in every thread,
    any counterparty appears in one or two.
    """
    seen: dict[str, set[str]] = defaultdict(set)
    for m in messages:
        conv = m.get("conversation_id") or ""
        for who in (m.get("from"), m.get("to")):
            if who:
                seen[who].add(conv)
    if not seen:
        return ""
    return max(seen.items(), key=lambda kv: len(kv[1]))[0]


# ---------------------------------------------------------------------------
# History — who has already been contacted
# ---------------------------------------------------------------------------


def build_history(files: dict[str, bytes], owner: str | None = None) -> dict[str, Any]:
    """Per-counterparty message + invitation history, keyed by slug AND by name.

    Both key spaces are returned in one dict because archives are inconsistent
    about profile URLs — the join falls back to normalized name when the slug
    is missing or URN-style (`ACoAAB...`).
    """
    messages = load_messages(files)
    invitations = load_invitations(files)
    owner = owner or detect_account_owner(messages)
    owner_key = _norm_person(owner)

    records: dict[str, dict[str, Any]] = {}
    # Every record is reachable by BOTH its profile slug and its normalized name.
    # Archives mix vanity slugs (Connections.csv) with URN slugs (`ACoAAB…` in
    # messages.csv) for the same person, so a slug-only index silently misses.
    index: dict[str, str] = {}

    def _rec(slug: str, name: str) -> dict[str, Any]:
        name_key = _norm_person(name)
        key = index.get(slug) or index.get(name_key) or slug or name_key
        if not key:
            return {}
        if key not in records:
            records[key] = {
                "name": name,
                "profile_slug": slug,
                "message_count": 0,
                "outbound_count": 0,
                "inbound_count": 0,
                "first_message": "",
                "last_message": "",
                "last_direction": "",
                "they_replied": False,
                "invitation_sent": "",
                "invitation_received": "",
                "join_method": "profile_url" if slug else "name",
            }
        rec = records[key]
        if slug and not rec["profile_slug"]:
            rec["profile_slug"] = slug
            rec["join_method"] = "profile_url"
        if name and not rec["name"]:
            rec["name"] = name
        for alias in (slug, name_key):
            if alias:
                index[alias] = key
        return rec

    for m in messages:
        sender_is_owner = _norm_person(m["from"]) == owner_key
        if sender_is_owner:
            other_name, other_slug, direction = m["to"], m["to_slug"], "outbound"
        else:
            other_name, other_slug, direction = m["from"], m["from_slug"], "inbound"

        rec = _rec(other_slug, other_name)
        if not rec:
            continue
        rec["message_count"] += 1
        if direction == "outbound":
            rec["outbound_count"] += 1
        else:
            rec["inbound_count"] += 1
            rec["they_replied"] = True

        date = m["date"]
        if date:
            if not rec["first_message"] or date < rec["first_message"]:
                rec["first_message"] = date
            if not rec["last_message"] or date >= rec["last_message"]:
                rec["last_message"] = date
                rec["last_direction"] = direction

    for inv in invitations:
        if inv["direction"] == "OUTGOING" or _norm_person(inv["from"]) == owner_key:
            rec = _rec(inv["invitee_slug"], inv["to"])
            field = "invitation_sent"
        else:
            rec = _rec(inv["inviter_slug"], inv["from"])
            field = "invitation_received"
        if rec and inv["sent_at"] and not rec[field]:
            rec[field] = inv["sent_at"]

    for rec in records.values():
        rec["suggested_outreach_status"], rec["status_rationale"] = _suggest_status(rec)

    return {"owner": owner, "records": records, "index": index}


def _suggest_status(rec: dict[str, Any]) -> tuple[str, str]:
    """Map raw history to a contacts.md outreach_status suggestion.

    Deliberately conservative — these are historical, pre-repo interactions, not
    outcomes of a tracked outreach cycle. The skill surfaces the rationale and
    the founder confirms before anything is written.
    """
    if rec["inbound_count"] > 0:
        return "replied", (
            f"{rec['inbound_count']} inbound message(s), last {rec['last_message']} — "
            f"they have replied to you before"
        )
    if rec["outbound_count"] > 0:
        return "no_reply", (
            f"{rec['outbound_count']} outbound message(s) since {rec['first_message']}, "
            f"no reply in the archive"
        )
    if rec["invitation_sent"]:
        return "invited", f"invitation sent {rec['invitation_sent']}, never messaged"
    return "pending", "no prior messages or invitations in the archive"


def lookup_history(history: dict[str, Any], slug: str, name: str) -> dict[str, Any]:
    """Find a person's history by slug, falling back to normalized name."""
    records = history.get("records", {})
    index = history.get("index", {})
    if slug and slug in index:
        return records.get(index[slug], {})
    key = _norm_person(name)
    if key and key in index:
        return {**records.get(index[key], {}), "join_method": "name"}
    return {}


# ---------------------------------------------------------------------------
# ICP filtering
# ---------------------------------------------------------------------------


def filter_connections(
    connections: list[dict[str, Any]],
    titles: list[str] | None = None,
    domain_nouns: list[str] | None = None,
    excludes: list[str] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Split connections into (kept, rejected) against the assumption's ICP.

    Titles match against `position` only; domain nouns match against position OR
    company (a domain-titled engineer at an unnamed firm and any role at an operator
    are both worth surfacing). Excludes are checked first and win outright.

    With no filters at all, everything is kept — the caller wanted the raw network.
    """
    titles = [t for t in (titles or []) if t.strip()]
    domain_nouns = [d for d in (domain_nouns or []) if d.strip()]
    excludes = [e for e in (excludes or []) if e.strip()]

    kept, rejected = [], []
    for c in connections:
        position, company = c.get("position", ""), c.get("company", "")

        hit_exclude = next(
            (e for e in excludes if _matches(e, position, company)), None
        )
        if hit_exclude:
            rejected.append({**c, "rejected_by": "exclude", "rejected_on": hit_exclude})
            continue

        if not titles and not domain_nouns:
            kept.append({**c, "matched_on": [], "match_basis": "unfiltered"})
            continue

        matched = [t for t in titles if _matches(t, position)]
        basis = "title" if matched else ""
        noun_hits = [d for d in domain_nouns if _matches(d, position, company)]
        if noun_hits:
            matched += noun_hits
            basis = basis or "domain_noun"

        if matched:
            kept.append({**c, "matched_on": matched, "match_basis": basis})
        else:
            rejected.append({**c, "rejected_by": "no_icp_match", "rejected_on": ""})

    return kept, rejected


# ---------------------------------------------------------------------------
# Top-level API
# ---------------------------------------------------------------------------


def parse_connections(
    export_path: Path | str | None = None,
    titles: list[str] | None = None,
    domain_nouns: list[str] | None = None,
    excludes: list[str] | None = None,
    with_history: bool = True,
    limit: int | None = None,
    include_rejected: bool = False,
    slug: str | None = None,
) -> dict[str, Any]:
    """Parse the export and return ICP-filtered 1st-degree contacts as JSON-ready dict."""
    path, files = find_export(export_path)
    connections = load_connections(files)
    kept, rejected = filter_connections(connections, titles, domain_nouns, excludes)

    history: dict[str, Any] = {}
    if with_history and ("messages" in files or "invitations" in files):
        history = build_history(files)

    contacts = []
    for c in kept:
        contact = {
            **c,
            "signal_type": "profile_fit",
            "signal_multiplier": 1.0,
            "signal_source_url": "linkedin_export:Connections.csv",
        }
        if history:
            prior = lookup_history(history, c["profile_slug"], c["name"])
            contact["prior_contact"] = prior or {
                "message_count": 0,
                "suggested_outreach_status": "pending",
                "status_rationale": "no prior messages or invitations in the archive",
            }
        contacts.append(contact)

    # Never-contacted first — those are the real net-new outreach targets.
    contacts.sort(key=lambda c: (
        c.get("prior_contact", {}).get("message_count", 0),
        c.get("connected_on", ""),
    ))
    if limit:
        contacts = contacts[:limit]

    payload: dict[str, Any] = {
        "source": "linkedin_export",
        "export_path": str(path),
        "parsed_at": datetime.now(timezone.utc).isoformat(),
        "account_owner": history.get("owner", ""),
        "files_found": sorted(files.keys()),
        "filters": {
            "titles": titles or [],
            "domain_nouns": domain_nouns or [],
            "excludes": excludes or [],
        },
        "counts": {
            "total_connections": len(connections),
            "kept": len(kept),
            "rejected": len(rejected),
            "returned": len(contacts),
            "already_messaged": sum(
                1 for c in contacts
                if c.get("prior_contact", {}).get("message_count", 0) > 0
            ),
        },
        "contacts": contacts,
    }
    if include_rejected:
        payload["rejected"] = rejected

    log_manifest(slug, {
        "source": "linkedin_export",
        "mode": "connections",
        "total_connections": len(connections),
        "kept": len(kept),
        "titles": titles or [],
    })
    return payload


def parse_history(
    export_path: Path | str | None = None,
    slug: str | None = None,
    owner: str | None = None,
) -> dict[str, Any]:
    """Return every person the founder has messaged or invited, with suggested status."""
    path, files = find_export(export_path)
    history = build_history(files, owner=owner)
    records = list(history["records"].values())
    records.sort(key=lambda r: r.get("last_message", ""), reverse=True)

    status_counts = Counter(r["suggested_outreach_status"] for r in records)
    payload = {
        "source": "linkedin_export",
        "export_path": str(path),
        "parsed_at": datetime.now(timezone.utc).isoformat(),
        "account_owner": history["owner"],
        "counts": {
            "people": len(records),
            "by_suggested_status": dict(status_counts),
        },
        "people": records,
    }
    log_manifest(slug, {
        "source": "linkedin_export",
        "mode": "history",
        "people": len(records),
    })
    return payload


def inspect_export(export_path: Path | str | None = None) -> dict[str, Any]:
    """Preflight: what's in the archive, is it parseable, how stale is it."""
    path, files = find_export(export_path)
    connections = load_connections(files) if "connections" in files else []
    messages = load_messages(files) if "messages" in files else []
    invitations = load_invitations(files) if "invitations" in files else []

    dates = [c["connected_on"] for c in connections if c["connected_on"]]
    dates += [m["date"] for m in messages if m["date"]]

    return {
        "source": "linkedin_export",
        "export_path": str(path),
        "files_found": sorted(files.keys()),
        "files_missing": sorted(set(FILE_ALIASES) - set(files)),
        "account_owner": detect_account_owner(messages),
        "counts": {
            "connections": len(connections),
            "messages": len(messages),
            "invitations": len(invitations),
            "conversations": len({m["conversation_id"] for m in messages if m["conversation_id"]}),
        },
        "latest_activity": max(dates) if dates else "",
        "connections_with_position": sum(1 for c in connections if c["position"]),
        "connections_with_url": sum(1 for c in connections if c["profile_slug"]),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse a LinkedIn data export into outreach candidates.")
    parser.add_argument("--export", default=None,
                        help=f"Export dir or .zip (default: {DEFAULT_EXPORT_DIR})")
    sub = parser.add_subparsers(dest="mode", required=True)

    sub.add_parser("inspect", help="Show what the archive contains and whether it parses")

    p_conn = sub.add_parser("connections", help="ICP-filtered 1st-degree contacts")
    p_conn.add_argument("--title", action="append", default=[],
                        help="Title phrase from icp_valid_titles (repeatable)")
    p_conn.add_argument("--domain-noun", action="append", default=[],
                        help="Domain noun matched against position OR company (repeatable)")
    p_conn.add_argument("--exclude", action="append", default=[],
                        help="icp_out_of_scope pattern (repeatable)")
    p_conn.add_argument("--limit", type=int, default=None)
    p_conn.add_argument("--include-rejected", action="store_true",
                        help="Also emit non-matching connections, for filter tuning")
    p_conn.add_argument("--no-history", action="store_true",
                        help="Skip the message-history join")
    p_conn.add_argument("--slug", default=None, help="Idea slug, for manifest logging")

    p_hist = sub.add_parser("history", help="Everyone already messaged or invited")
    p_hist.add_argument("--owner", default=None,
                        help="Your own name as it appears in messages.csv (auto-detected)")
    p_hist.add_argument("--slug", default=None, help="Idea slug, for manifest logging")

    args = parser.parse_args()

    try:
        if args.mode == "inspect":
            emit_json(inspect_export(args.export))
        elif args.mode == "connections":
            emit_json(parse_connections(
                export_path=args.export,
                titles=args.title,
                domain_nouns=args.domain_noun,
                excludes=args.exclude,
                with_history=not args.no_history,
                limit=args.limit,
                include_rejected=args.include_rejected,
                slug=args.slug,
            ))
        elif args.mode == "history":
            emit_json(parse_history(
                export_path=args.export, slug=args.slug, owner=args.owner))
    except FileNotFoundError as e:
        print(f"[error] {e}", file=sys.stderr)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
