#!/usr/bin/env bash
set -euo pipefail

if git diff --cached --name-only --diff-filter=ACMR | grep -qx "PROGRESS.md"; then
  exit 0
fi

cat <<'EOF'
ERROR: This commit does not update PROGRESS.md.

Please add a progress entry and stage PROGRESS.md before committing.
EOF
exit 1
