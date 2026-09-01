#!/usr/bin/env python3
"""Extract the founder's own messages from Claude Code session transcripts.

Their working sessions are the richest source this skill has, for two reasons at once:
the messages are where the real thinking happened (surprise, correction, a sharp
offhand sentence), and they are unedited samples of how the founder actually writes.
One harvest serves both post-material mining and voice calibration.

Transcripts live at ~/.claude/projects/<slug>/*.jsonl, one line per event. Only `user`
events with real prose are wanted; everything else here is noise the harness inserted —
slash-command wrappers, command stdout, tool results, system reminders, injected skill
bodies, and subagent sidechains.

Usage:
    python3 harvest_sessions.py                      # all sessions, newest first
    python3 harvest_sessions.py --days 7             # recent only
    python3 harvest_sessions.py --min-chars 200      # substantial messages only
    python3 harvest_sessions.py --voice              # samples suited to voice calibration
    python3 harvest_sessions.py --json               # machine-readable
    python3 harvest_sessions.py --project-dir PATH   # non-default transcript location
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Harness-generated wrappers. A message that opens with one of these was not typed by
# the founder even though it is recorded as a `user` event.
NOISE_PREFIXES = (
    "<local-command-caveat>",
    "<local-command-stdout>",
    "<command-name>",
    "<command-message>",
    "<system-reminder>",
    "<user-prompt-submit-hook>",
    "Base directory for this skill:",
    "Caveat: The messages below were generated",
    "[Request interrupted",
    "API Error",
)

NOISE_PATTERNS = (
    re.compile(r"^\s*<command-(name|args|message)>", re.I),
    re.compile(r"^\s*Result of calling the", re.I),
)

# Voice mode wants prose, not operational instructions. These signal a message that is
# a work order rather than the founder talking — useful as material, useless as a
# sample of how they write when they mean something.
OPERATIONAL = re.compile(
    r"^\s*(run|fix|commit|push|read|open|check|rerun|continue|go ahead|yes|ok|okay|"
    r"do it|proceed|next|update|delete|add|remove)\b[\s,.!]*$",
    re.I,
)


def default_project_dir() -> Path | None:
    """Map the current working directory to its Claude Code transcript folder."""
    slug = str(Path.cwd().resolve()).replace("/", "-")
    candidate = Path.home() / ".claude" / "projects" / slug
    return candidate if candidate.is_dir() else None


def is_noise(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped.startswith(NOISE_PREFIXES):
        return True
    return any(p.match(stripped) for p in NOISE_PATTERNS)


def extract_text(message: dict) -> str:
    """Pull founder-typed prose out of one message, skipping tool results."""
    content = message.get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = [
        block.get("text", "")
        for block in content
        if isinstance(block, dict) and block.get("type") == "text"
    ]
    return "\n".join(parts)


def strip_trailing_noise(text: str) -> str:
    """Drop system-reminder blocks the harness appends to otherwise-real messages."""
    return re.sub(r"<system-reminder>.*?</system-reminder>", "", text, flags=re.S).strip()


def harvest(project_dir: Path, days: int | None, min_chars: int, voice: bool) -> list[dict]:
    cutoff = (
        datetime.now(timezone.utc) - timedelta(days=days) if days is not None else None
    )
    out: list[dict] = []

    for path in sorted(project_dir.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            if event.get("type") != "user" or event.get("isSidechain"):
                continue

            text = strip_trailing_noise(extract_text(event.get("message", {}) or {}))
            if is_noise(text) or len(text) < min_chars:
                continue
            if voice and OPERATIONAL.match(text):
                continue

            stamp = event.get("timestamp", "")
            if cutoff and stamp:
                try:
                    if datetime.fromisoformat(stamp.replace("Z", "+00:00")) < cutoff:
                        continue
                except ValueError:
                    pass

            out.append({
                "session": path.stem,
                "timestamp": stamp,
                "branch": event.get("gitBranch", ""),
                "chars": len(text),
                "text": text,
            })

    out.sort(key=lambda r: r["timestamp"], reverse=True)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project-dir", type=Path, default=None)
    ap.add_argument("--days", type=int, default=None, help="only messages from the last N days")
    ap.add_argument("--min-chars", type=int, default=80, help="drop short acknowledgements")
    ap.add_argument("--voice", action="store_true", help="filter to prose suited to voice calibration")
    ap.add_argument("--limit", type=int, default=0, help="cap the number returned (0 = no cap)")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    project_dir = args.project_dir or default_project_dir()
    if not project_dir or not project_dir.is_dir():
        print(
            "No transcript directory found. Run from the project root, or pass "
            "--project-dir ~/.claude/projects/<slug>/",
            file=sys.stderr,
        )
        return 1

    rows = harvest(project_dir, args.days, args.min_chars, args.voice)
    if args.limit:
        rows = rows[: args.limit]

    if args.as_json:
        json.dump(rows, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    if not rows:
        print("No founder messages matched. Try lowering --min-chars or widening --days.")
        return 0

    print(f"# {len(rows)} founder messages from {project_dir.name}\n")
    for row in rows:
        when = row["timestamp"][:16].replace("T", " ")
        print(f"## {when} · {row['session'][:8]} · {row['chars']} chars\n")
        print(row["text"])
        print("\n---\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
