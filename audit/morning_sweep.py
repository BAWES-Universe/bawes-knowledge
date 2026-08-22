#!/usr/bin/env python3
"""MORNING SWEEP (Rebels): review the last 24h of ledger rows against the DA rulebook.
Runs 08:30 daily; findings land in the 09:00 digest. Violations must be answered."""
import json, pathlib, subprocess, datetime, re

LEDGER = pathlib.Path.home() / "bawes-knowledge" / "decisions" / "ledger.md"
OUT = pathlib.Path.home() / "bawes-knowledge" / "docs" / "CHALLENGER-FINDINGS.md"

# Resolve challenger.py repo-relative so the committed artifact is self-consistent:
# 1) next to this script (audit/challenger.py in a repo clone), 2) the repo's audit/ dir,
# 3) the legacy ~/probe location. Falls back through the list.
HERE = pathlib.Path(__file__).resolve().parent
CANDIDATES = [
    HERE / "challenger.py",
    pathlib.Path.home() / "bawes-knowledge" / "audit" / "challenger.py",
    pathlib.Path.home() / "probe" / "challenger.py",
]
CHALLENGER = next((c for c in CANDIDATES if c.exists()), CANDIDATES[0])
PY = "/usr/bin/python3"  # challenger.py is stdlib-only; no venv required

def main():
    lines = LEDGER.read_text().splitlines()
    rows = [l for l in lines if l.strip().startswith("|") and " 2026-" in l]
    recent = rows[-8:]  # last 8 rows ≈ last 24h
    acts = [{"id": f"S{i}", "action": " ".join(r.split("|")[1:4]).strip()[:400]} for i, r in enumerate(recent)]
    acts_path = "/tmp/sweep_actions.jsonl"
    pathlib.Path(acts_path).write_text("\n".join(json.dumps(a) for a in acts))
    r = subprocess.run([PY, str(CHALLENGER), "--retro", acts_path],
                       capture_output=True, text=True, timeout=1500)
    out = r.stdout
    flags = out.count("[FLAG]")
    OUT.write_text(f"# Challenger findings — {datetime.datetime.now().isoformat(timespec='minutes')}\n\n"
                   f"`{out}`\n\n**{flags} flagged rows in the last 24h.** Digests must answer each flag.\n")
    print(f"SWEEP: {flags} flags -> CHALLENGER-FINDINGS.md")

if __name__ == "__main__":
    main()
