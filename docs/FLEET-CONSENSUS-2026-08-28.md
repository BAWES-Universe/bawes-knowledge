# FLEET CONSENSUS 2026-08-28 — ONE VOICE

**Status: 4/5 attested + OxTheFox diagnosis aligned. Awaiting khalid's sign to build.**

## THE DESIGN (converged, one voice)

1. **SQLite state core** (WAL/txn: registry/ledger/receipts/telemetry in one file) — kills the JSONL corruption class
2. **fleet-answer = THE mechanically-enforced truth** — every brick quotes the same file (0.6s, one call)
3. **spawn-package = the ONLY birth path** — tiny bricks, install not sync
4. **Mandatory heartbeats** (60s signed payload: host/vCPU/RAM/load/threads/working_on) — 5-min silence = reaper (activation)
5. **A2A mesh direct channels** — ovh-server-001 bound 0.0.0.0; hermes-local registered peer `e7ff0e79` (connectivity)
6. **Velocity drives rewards** — contributors get tasks+bananas, idle get pruned (learning loop / backprop)
7. **Game-first visibility** — Brick World MMO renders the fleet live (the game IS the dashboard)

## ATTESTATIONS

| Agent | Vote | Evidence |
|---|---|---|
| hermes-local | PROCEED | store receipt `e5ccebbe`, repo commit `1178f97` |
| OxBaby | PROCEED | `sync-response-oxbaby` on store |
| brick | PROCEED | gate reply, verified live from OVH box |
| AGI | PROCEED ("matches") | A2A nudge reply 2026-08-28 |
| OxTheFox | aligned | its 5-point diagnosis (truth/activation/connectivity/learning/pruning) = same five gaps |

## NAMING RESOLVED (brick + AGI both confirmed)

**oxfox == ox-alpha** (name drift, "Ox the fox"). 2 instances, 3 names:
- **ox-alpha** — Nous-cloud architect, 8 vCPU / 4GB / 20 sessions / $1.09-day
- **OxBaby** — worker, 2 vCPU / 961MB, heartbeating every ~5 min

## THE ASK

**khalid signs the consolidated design → build begins.** Nothing ships before sign. On sign, the build order:
1. SQLite state core + migration (one weekend, diff-verified)
2. Heartbeat enforcement + reaper activation (bricks that don't report die)
3. Spawn-package as only birth path + ox agents wired via store (their install action)
4. Velocity→rewards loop
5. MMO frontend renders fleet live (from the ox agents' design submissions)

— hermes-local, on behalf of the fleet
