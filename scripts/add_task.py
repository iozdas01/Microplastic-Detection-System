#!/usr/bin/env python3
"""Log a founder to-do onto the shared kanban board — the same board the control room shows.

    .venv/bin/python scripts/add_task.py --title "Call the textile mill back"
    .venv/bin/python scripts/add_task.py --owner sandra --title "..." --detail "..." --priority high

The board has ONE author: `data/kanban.json` on `main`. Each founder's terminal writes it
through git — pull, append the task, commit, push — so a task logged in one clone shows on
the other founder's board the next time their control room reads the file. No hosted API
is involved (founder decision 2026-09-09; `api/tasks.js` stays parked).

The owner defaults to whoever this clone belongs to: `git config user.name` / `user.email`
matched against `git_identities` in `founder.md`. Pass `--owner` to log a to-do for the
other founder. The board renders the owner on the card, so a to-do is never ambiguous
about whose it is. `--no-push` leaves it as a local commit for a later push.
"""
from __future__ import annotations

import argparse
import json
import random
import string
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD = ROOT / "data" / "kanban.json"
FOUNDERS = ROOT / "founder.md"
STATUSES = ("backlog", "next", "doing", "done")
PRIORITIES = ("high", "normal", "low")
MAX_ACTIVITY = 100


def founders() -> tuple[dict[str, str], dict[str, list[str]]]:
    """({slug: display name}, {slug: git identities}) from founder.md frontmatter. Slug =
    first segment of the profile filename (izgin-ozdas → izgin), which is what the board
    stores as `owner`."""
    import yaml
    text = FOUNDERS.read_text(encoding="utf-8")
    fm = yaml.safe_load(text.split("---\n", 2)[1]) or {}
    names, idents = {}, {}
    for f in fm.get("founders") or []:
        stem = Path(f.get("profile", "")).stem  # izgin-ozdas
        slug = stem.split("-")[0] if stem else f.get("name", "").split()[0].lower()
        names[slug] = f.get("name", slug)
        idents[slug] = [str(x).lower() for x in (f.get("git_identities") or [])]
    return names, idents


def owner_from_git(names: dict[str, str], idents: dict[str, list[str]]) -> str | None:
    """The founder whose clone this is: git user.name / user.email against founder.md."""
    name = git("config", "user.name", check=False).lower()
    email = git("config", "user.email", check=False).lower()
    for slug, ids in idents.items():
        if (name and name in ids) or (email and email in ids):
            return slug
    first = name.split()[0] if name else ""
    for slug, full in names.items():
        if first and first == full.split()[0].lower():
            return slug
    return None


def resolve_owner(raw: str, known: dict[str, str]) -> str:
    key = raw.strip().lower()
    for slug, name in known.items():
        if key in (slug, name.lower(), name.split()[0].lower(), name.lower().replace(" ", "-")):
            return slug
    sys.exit(f"unknown owner {raw!r}; founders in founder.md are: {', '.join(known)}")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def task_id() -> str:
    # Same shape as api/tasks.js: T-<base36 ms>-<4 random>
    ms = int(time.time() * 1000)
    digits = string.digits + string.ascii_uppercase
    b36 = ""
    while ms:
        ms, r = divmod(ms, 36)
        b36 = digits[r] + b36
    rnd = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"T-{b36}-{rnd}"


def git(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr.strip()}")
    return r.stdout.strip()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--owner", default=None,
                   help="founder first name or profile slug (founder.md); default: whoever this clone's git identity is")
    p.add_argument("--title", required=True, help="the to-do, ≤140 chars, in the founder's words")
    p.add_argument("--detail", default="", help="optional detail, ≤600 chars")
    p.add_argument("--priority", default="normal", choices=PRIORITIES)
    p.add_argument("--status", default="backlog", choices=STATUSES)
    p.add_argument("--no-push", action="store_true", help="commit locally, do not pull or push")
    a = p.parse_args()

    known, idents = founders()
    if a.owner:
        owner = resolve_owner(a.owner, known)
    else:
        owner = owner_from_git(known, idents)
        if not owner:
            sys.exit("cannot tell which founder this clone belongs to: git user.name/email match no "
                     "`git_identities` in founder.md. Pass --owner, or add the identity to founder.md.")
    title = " ".join(a.title.split())[:140]
    detail = " ".join(a.detail.split())[:600]
    if not title:
        sys.exit("a task title is required")

    if not a.no_push:
        git("pull", "--rebase", "--quiet")

    board = json.loads(BOARD.read_text(encoding="utf-8")) if BOARD.exists() else {}
    board.setdefault("version", 1)
    board["tasks"] = board.get("tasks") or []
    board["activity"] = board.get("activity") or []

    ts = now_iso()
    task = {
        "id": task_id(),
        "title": title,
        "detail": detail,
        "priority": a.priority,
        "status": a.status,
        "owner": owner,
        "created_at": ts,
        "updated_at": ts,
    }
    board["tasks"].append(task)
    board["activity"].insert(0, {
        "id": f"{int(time.time()*1000)}-{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}",
        "at": ts,
        "type": "created",
        "task_id": task["id"],
        "title": title,
        "from": None,
        "to": a.status,
        "owner": owner,
    })
    board["activity"] = board["activity"][:MAX_ACTIVITY]
    board["updated_at"] = ts
    BOARD.write_text(json.dumps(board, indent=2) + "\n", encoding="utf-8")

    git("add", str(BOARD.relative_to(ROOT)))
    git("commit", "--quiet", "-m", f"board: add {title} ({known[owner]})"[:120])
    if not a.no_push:
        git("push", "--quiet")

    open_count = sum(1 for t in board["tasks"] if t.get("status") != "done")
    print(f'Board: added "{title}" for {known[owner]} ({a.status} · {open_count} open){"" if not a.no_push else " · not pushed"}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
