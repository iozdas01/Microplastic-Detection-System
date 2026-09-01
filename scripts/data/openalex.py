#!/usr/bin/env python3
"""Find paper-published researcher emails via OpenAlex and arXiv source files.

This script is deliberately target-first: it accepts a CSV of already-qualified
researchers, finds their recent papers, and extracts only email addresses that the
authors published in an open arXiv source package. It does not guess addresses or
call an email-enrichment provider.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import io
import json
import os
import re
import tarfile
import urllib.parse
import urllib.request
from pathlib import Path


EMAIL_RE = re.compile(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", re.I)
ARXIV_RE = re.compile(r"(?:arxiv:|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", re.I)
PERSONAL_DOMAINS = {
    "gmail.com", "googlemail.com", "hotmail.com", "outlook.com", "yahoo.com",
    "icloud.com", "proton.me", "protonmail.com", "aol.com",
}


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "startup-research-outreach/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def get_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "startup-research-outreach/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def author_score(result: dict, name: str, company: str) -> tuple[int, int]:
    display = result.get("display_name") or ""
    name_score = 2 if normalized(display) == normalized(name) else int(normalized(name) in normalized(display))
    institutions = " ".join(i.get("display_name", "") for i in result.get("last_known_institutions") or [])
    company_score = int(normalized(company) in normalized(institutions) or normalized(institutions) in normalized(company))
    return company_score, name_score


def find_author(api_key: str, name: str, company: str) -> dict | None:
    params = urllib.parse.urlencode({"search": name, "per-page": 10, "api_key": api_key})
    data = get_json(f"https://api.openalex.org/authors?{params}")
    results = data.get("results") or []
    if not results:
        return None
    return max(results, key=lambda item: author_score(item, name, company))


def recent_works(api_key: str, author_id: str, since: str) -> list[dict]:
    short_id = author_id.rsplit("/", 1)[-1]
    params = urllib.parse.urlencode({
        "filter": f"author.id:{short_id},from_publication_date:{since}",
        "sort": "publication_date:desc",
        "per-page": 40,
        "api_key": api_key,
    })
    return get_json(f"https://api.openalex.org/works?{params}").get("results") or []


def work_affiliations(work: dict, author_id: str) -> str:
    pieces: list[str] = []
    for authorship in work.get("authorships") or []:
        if (authorship.get("author") or {}).get("id") != author_id:
            continue
        pieces.extend(authorship.get("raw_affiliation_strings") or [])
        pieces.extend(i.get("display_name", "") for i in authorship.get("institutions") or [])
    return " | ".join(dict.fromkeys(p for p in pieces if p))


def arxiv_id(work: dict) -> str | None:
    candidates: list[str] = []
    ids = work.get("ids") or {}
    candidates.extend(str(v) for v in ids.values() if v)
    for location_key in ("primary_location", "best_oa_location"):
        location = work.get(location_key) or {}
        candidates.extend(str(location.get(k) or "") for k in ("landing_page_url", "pdf_url"))
    for candidate in candidates:
        match = ARXIV_RE.search(candidate)
        if match:
            return match.group(1).removesuffix(".pdf")
    return None


def source_texts(payload: bytes) -> list[str]:
    streams: list[bytes] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            for member in archive.getmembers():
                if not member.isfile() or member.size > 5_000_000:
                    continue
                if not member.name.lower().endswith((".tex", ".txt")):
                    continue
                extracted = archive.extractfile(member)
                if extracted:
                    streams.append(extracted.read())
    except tarfile.TarError:
        try:
            streams.append(gzip.decompress(payload))
        except OSError:
            streams.append(payload)
    return [blob.decode("utf-8", errors="ignore") for blob in streams]


def paper_emails(identifier: str) -> list[str]:
    payload = get_bytes(f"https://export.arxiv.org/e-print/{urllib.parse.quote(identifier)}")
    emails: set[str] = set()
    for text in source_texts(payload):
        cleaned = text.replace("\\_", "_").replace("{at}", "@").replace("[at]", "@")
        emails.update(EMAIL_RE.findall(cleaned))
    return sorted(email for email in emails if email.rsplit("@", 1)[-1].lower() not in PERSONAL_DOMAINS)


def company_matches(affiliations: str, company: str) -> bool:
    left, right = normalized(affiliations), normalized(company)
    aliases = {
        "amazonrobotics": ["amazon", "amazonrobotics"],
        "generalmotors": ["generalmotors", "gm"],
        "physicalintelligence": ["physicalintelligence"],
        "humanoid": ["humanoid"],
        "figure": ["figureai", "figure"],
    }
    keys = aliases.get(right, [right])
    return any(key and key in left for key in keys)


def run(input_path: Path, output_path: Path, since: str) -> None:
    load_env(Path(".env"))
    api_key = os.environ.get("OPENALEX_API_KEY", "")
    if not api_key:
        raise SystemExit("OPENALEX_API_KEY is missing from .env")
    with input_path.open(newline="", encoding="utf-8") as handle:
        targets = list(csv.DictReader(handle))

    rows: list[dict] = []
    for target in targets:
        name, company = target["name"], target["company"]
        author = find_author(api_key, name, company)
        if not author:
            rows.append({**target, "status": "author_not_found"})
            continue
        found = False
        for work in recent_works(api_key, author["id"], since):
            affiliations = work_affiliations(work, author["id"])
            identifier = arxiv_id(work)
            if not identifier:
                continue
            try:
                emails = paper_emails(identifier)
            except Exception:
                continue
            if not emails:
                continue
            rows.append({
                **target,
                "openalex_author_id": author["id"],
                "paper_title": work.get("title", ""),
                "paper_date": work.get("publication_date", ""),
                "paper_url": f"https://arxiv.org/abs/{identifier}",
                "paper_affiliations": affiliations,
                "current_company_on_paper": str(company_matches(affiliations, company)).lower(),
                "published_emails": ";".join(emails),
                "status": "paper_email_found",
            })
            found = True
            break
        if not found:
            rows.append({
                **target,
                "openalex_author_id": author["id"],
                "status": "no_paper_email_found",
            })

    fieldnames = list(dict.fromkeys(key for row in rows for key in row))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--since", default="2022-01-01")
    args = parser.parse_args()
    run(args.input, args.output, args.since)


if __name__ == "__main__":
    main()
