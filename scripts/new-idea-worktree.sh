#!/usr/bin/env bash
# Create a git worktree scoped to a single idea via sparse-checkout.
#
# Why this exists: git worktrees isolate you at the BRANCH level but they
# materialize the whole working tree by default — so a worktree for one idea
# still contains every OTHER idea's input-context/ and reports/ folders. Any
# subagent, Claude session, grep, or find running inside the worktree can see
# all of them, causing the exact cross-idea context bleed the per-idea folder
# structure was supposed to prevent.
#
# This script applies non-cone sparse-checkout to the new worktree so only:
#   - the shared framework files (CLAUDE.md, ARCHITECTURE.md, methods/, schemas/, ...)
#   - the named idea's input-context/{slug}/ and reports/{slug}/
# are materialized on disk. Every other idea's folders remain in git history
# but disappear from the working tree.
#
# Usage:   scripts/new-idea-worktree.sh <idea-slug>
# Example: scripts/new-idea-worktree.sh my-new-idea

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <idea-slug>" >&2
  echo "Example: $0 my-new-idea" >&2
  exit 1
fi

SLUG="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
WORKTREE_DIR="$REPO_ROOT/.claude/worktrees/$SLUG"
BRANCH="worktree-$SLUG"

# Sanity: the idea's input-context folder should exist. Idea seeds live there.
if [[ ! -d "$REPO_ROOT/input-context/$SLUG" ]]; then
  echo "Error: input-context/$SLUG/ not found." >&2
  echo "Stage the idea's raw inputs at input-context/$SLUG/ before running this." >&2
  exit 2
fi

# Refuse to clobber an existing worktree/branch at this slug.
if [[ -d "$WORKTREE_DIR" ]]; then
  echo "Error: $WORKTREE_DIR already exists." >&2
  echo "Remove it with 'git worktree remove $WORKTREE_DIR' first, or pick a new slug." >&2
  exit 3
fi

# Create the worktree on a new branch off HEAD.
git -C "$REPO_ROOT" worktree add "$WORKTREE_DIR" -b "$BRANCH"

# Enable non-cone sparse-checkout inside the new worktree and apply patterns.
# Non-cone mode gives file-level precision: only this idea's input-context/ and
# reports/ folders materialize; every other idea stays invisible.
git -C "$WORKTREE_DIR" sparse-checkout init --no-cone
git -C "$WORKTREE_DIR" sparse-checkout set \
  '/CLAUDE.md' \
  '/ARCHITECTURE.md' \
  '/README.md' \
  '/api-registry.yaml' \
  '/.env.example' \
  '/.gitignore' \
  '/schemas/**' \
  '/methods/**' \
  '/scripts/**' \
  '/.claude/skills/**' \
  '/.claude/settings.json' \
  '/.claude/settings.local.json' \
  '/input-context/README.md' \
  "/input-context/$SLUG/**" \
  "/reports/$SLUG/**"

echo ""
echo "Worktree ready:"
echo "  path:    $WORKTREE_DIR"
echo "  branch:  $BRANCH"
echo "  scoped:  input-context/$SLUG/  reports/$SLUG/"
echo ""
echo "cd \"$WORKTREE_DIR\""
