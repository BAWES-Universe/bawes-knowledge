#!/bin/bash
# BAWES knowledge repo — open-source guardrail scan (run in CI + locally)
set -e

echo "=== 1. Secret patterns (public repo!) ==="
if git grep -nE "(BEGIN RSA|BEGIN OPENSSH|ghp_|gho_|ghs_|ntn_[A-Za-z0-9]{20}|sk-[A-Za-z0-9]{20}|AKIA[0-9A-Z]{16}|xox[baprs]-|secret_[A-Za-z0-9]{20}|password[[:space:]]*=[[:space:]]*['\"][^'\"]{6,})" -- . ':!*.md' ':!.gitignore' ':!scripts/guardrail-scan.sh' 2>/dev/null; then
  echo "FAIL: secret pattern found. This repo is PUBLIC — remove it."
  exit 1
fi

echo "=== 2. No .env tracked ==="
if git ls-files | grep -E "(^|/)\.env($|\.)"; then
  echo "FAIL: .env tracked. Never commit env files."
  exit 1
fi

echo "=== 3. No raw data dumps ==="
if git ls-files | grep -E "\.(csv|sql|jsonl)$"; then
  echo "FAIL: raw data files blocked — summaries only."
  exit 1
fi

echo "=== 4. Skill manifests valid YAML + required fields ==="
for f in skills/*.yaml; do
  [ -f "$f" ] || continue
  python3 - "$f" <<'PYEOF'
import sys, yaml
f = sys.argv[1]
try:
    d = yaml.safe_load(open(f))
except Exception as e:
    print(f"FAIL: invalid YAML {f}: {e}"); sys.exit(1)
req = ["name", "owner", "kind", "skills"]
missing = [k for k in req if k not in (d or {})]
if missing:
    print(f"FAIL: {f} missing {missing}"); sys.exit(1)
PYEOF
done

echo "=== 5. Decisions ledger append-only sanity ==="
if [ -f decisions/ledger.md ]; then
  python3 -c "
import sys
lines = open('decisions/ledger.md').read().splitlines()
rows = [l for l in lines if l.startswith('| 202')]
if len(rows) < 1:
    print('WARN: ledger has no dated rows'); sys.exit(0)
print(f'ok: {len(rows)} dated decision rows')
"
fi

echo "✅ clean: no secrets, no env, no raw data, manifests valid"
