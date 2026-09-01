#!/bin/sh
# Install the repo's git hooks. Run once per clone.
#
#     scripts/hooks/install.sh
#
# Uses core.hooksPath so the hooks stay versioned in scripts/hooks/ rather than being
# copied into .git/hooks, where they would drift from the repo and be invisible in
# review. Works from any worktree — hooksPath is shared with the main checkout.

set -e

REPO="$(git rev-parse --show-toplevel)"
cd "$REPO"

chmod +x scripts/hooks/pre-commit
git config core.hooksPath scripts/hooks

# Merge driver for generated artifacts (see .gitattributes). `true` means "keep
# ours, exit clean" — the pre-commit staleness check then forces a regenerate,
# so ours is never what ships. Without this, every merge conflicts on
# control-room.html and the resolution is always "rerun the generator".
git config merge.keep-ours.name "keep ours; regenerate before commit"
git config merge.keep-ours.driver "true"

echo "Installed: core.hooksPath = scripts/hooks"
echo "Installed: merge driver keep-ours (generated artifacts)"
echo "Active hooks:"
for h in scripts/hooks/*; do
    case "$h" in
        */install.sh) ;;
        *) echo "  - $(basename "$h")" ;;
    esac
done
echo ""
echo "Verify with: python3 scripts/validate_repo.py"
echo "Uninstall with: git config --unset core.hooksPath"
