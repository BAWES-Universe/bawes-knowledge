# Fleet State Core — Checkpointing Spec & Implementation Plan (SQLite WAL)

- Status: draft — feeds ONE PLAN item #2 (checkpointing). Fleet consensus 2026-08-28: replace scattered append-only JSONL state core with SQLite (WAL + transactions).
- Context rates (VELOCITY-MACHINE-TIME.md, measured): hermes-local direct ≈ 2.1 items/hr; brick A2A queue ≈ 0.3–0.5 items/hr. Effort below in machine-hours (mh), one focused workstream.

## 1. SQLite WAL design for the fleet state core

### 1.1 What gets checkpointed (the state core)
| Domain | JSONL today | Content |
|---|---|---|
| Brick registry | registry.jsonl | peer identity, role, heartbeat, capabilities |
| Banana ledger | ledger/*.jsonl | banana transfers/awards/debits — append-only, immutable rows |
| Receipts | receipts.jsonl | proof of item completion (task_id, worker, output hash, ts) |
| Telemetry | telemetry.jsonl | time-motion data: items/hr, queue latency, per-brick velocity |
| Dispatches | dispatches.jsonl | A2A queue: task assignments, status transitions, retries |

Invariant: **every write is an INSERT** (no UPDATE/DELETE in the hot path; state is an aggregation over the append log). This keeps SQLite semantics identical to JSONL append semantics — replay, diff, and restore stay trivial.

### 1.2 Table schema sketch (single DB: `fleet-state.db`)
```sql
PRAGMA journal_mode=WAL;      -- sticky, stored in the file itself
PRAGMA synchronous=NORMAL;    -- fsync at checkpoint, not per commit
PRAGMA wal_autocheckpoint=1000;

CREATE TABLE bricks (
  brick_id       TEXT PRIMARY KEY,
  role           TEXT NOT NULL,            -- 'hermes-local' | 'brick' | ...
  status         TEXT NOT NULL DEFAULT 'unknown',
  first_seen     INTEGER NOT NULL,         -- unix ms
  last_heartbeat INTEGER NOT NULL,
  capabilities   TEXT NOT NULL DEFAULT '{}'  -- raw JSON, lossless
);

CREATE TABLE banana_ledger (
  seq      INTEGER PRIMARY KEY AUTOINCREMENT,  -- == JSONL line order
  ts       INTEGER NOT NULL,
  brick_id TEXT NOT NULL REFERENCES bricks(brick_id),
  delta    INTEGER NOT NULL,                -- signed; balance = SUM(delta)
  reason   TEXT NOT NULL,
  ref      TEXT                             -- receipt_id / task_id link
);

CREATE TABLE receipts (
  receipt_id   TEXT PRIMARY KEY,
  task_id      TEXT NOT NULL,
  brick_id     TEXT NOT NULL REFERENCES bricks(brick_id),
  completed_at INTEGER NOT NULL,
  output_hash  TEXT NOT NULL,
  payload      TEXT NOT NULL DEFAULT '{}'   -- full JSON, replayable
);

CREATE TABLE telemetry (
  ts       INTEGER NOT NULL,
  brick_id TEXT NOT NULL REFERENCES bricks(brick_id),
  metric   TEXT NOT NULL,                   -- 'items_per_hr','queue_latency_ms',...
  value    REAL NOT NULL
);
CREATE INDEX idx_telemetry_brick_ts ON telemetry(brick_id, ts);

CREATE TABLE dispatches (
  dispatch_id TEXT PRIMARY KEY,
  task_id     TEXT NOT NULL,
  from_brick  TEXT NOT NULL,
  to_brick    TEXT NOT NULL REFERENCES bricks(brick_id),
  status      TEXT NOT NULL,                -- queued|claimed|done|failed|retry
  created_at  INTEGER NOT NULL,
  updated_at  INTEGER NOT NULL,
  attempts    INTEGER NOT NULL DEFAULT 0
);
```
Raw-JSON payload columns make every SQLite row a lossless superset of its JSONL line — nothing is dropped at migration.

### 1.3 WAL mode rationale
- **Crash safety with cheap appends:** synchronous=NORMAL fsyncs at checkpoint boundaries, not per insert. At 0.3–2.1 items/hr the commit rate is a handful per minute — write cost is noise.
- **Readers never block writers:** the Time Machine / velocity poller reads while bricks write; no lock contention at this volume.
- **kill -9 semantics:** a committed transaction survives a kill -9 (WAL replays on next open); only the in-flight transaction rolls back. This is exactly the JSONL "last partial line lost" behavior — minus the recurring corruption that motivates this change.
- **Single-file checkpoint set:** the entire state core is 1–3 files (`fleet-state.db`, `-wal`, `-shm`). A checkpoint is a consistent copy of that trio — nothing else to coordinate.

## 2. Restore: kill -9 → byte-identical state

**Checkpoint definition:** quiesced copy of the trio `fleet-state.db` + `-wal` + `-shm` taken with the writer stopped, stored at `checkpoints/ckpt-<unix-ts>/` plus `MANIFEST.json` (ts + SHA-256 per file). Optional: `VACUUM INTO 'ckpt.db'` for a single-file snapshot (preferred for transport).

**Checkpoint procedure:**
1. Stop the writer (graceful) or accept kill -9: WAL replay on next open recovers all committed txns; only the in-flight one is dropped (accepted semantic).
2. Copy the trio → `checkpoints/ckpt-<ts>/`; write MANIFEST.json with SHA-256 of each file.
3. Retention: last 5 checkpoints + first-of-day.

**Restore procedure (the drill):**
1. Kill the box / stop the state-core process: `kill -9 $(pgrep -f fleet-state)`.
2. `rm -f fleet-state.db fleet-state.db-wal fleet-state.db-shm`.
3. Copy the chosen checkpoint trio back into place (or copy `ckpt.db` → `fleet-state.db`).
4. `sqlite3 fleet-state.db "PRAGMA integrity_check;"` → must print `ok`.
5. Start writer; assert telemetry poller sees expected brick count and `SUM(delta)` matches the MANIFEST value.

**Byte-identical guarantee:** all committed state lives in DB+WAL; SQLite replays the WAL on open, so the copied trio is the *complete* committed state. Restoring the exact trio ⇒ identical rows, identical `seq`/autoinc order — verifiable via integrity_check + per-table `count(*)`/checksum rows. kill -9 mid-transaction loses only that transaction (== JSONL dropping a half-written line, without the corruption).

**Drill cadence:** scripted weekly restore drill on a staging box: copy live state → kill -9 → restore → assert `ok` + row counts. Run before any dangerous fleet op.

## 3. Migration: JSONL → SQLite (one-shot converter, copy → diff-verify → swap)

1. **Freeze:** stop writers for the swap window. At 0.3–2.1 items/hr the tail is a few lines; bounded loss is acceptable, freeze preferred.
2. **Copy:** `cp -a <state-dir> <state-dir>.migrate/` — converter touches only the copy, zero risk to live data.
3. **Convert:** `scripts/jsonl2sqlite.py <state-dir>.migrate --db fleet-state.db`:
   - one transaction per input file; per-line validation (required fields, monotonic `seq`/`ts`, duplicate `receipt_id`/`brick_id`) → **fail loudly with a report, never silently drop**;
   - normalize all timestamps to unix-ms; record the mapping in the migration report.
4. **Diff-verify (acceptance gate — reuse patterns from existing `scripts/validate_ledger.py` / `ledger-diff-guard.sh`):**
   - line count per JSONL == row count per table;
   - `SUM(delta)` in banana_ledger == running balance of last ledger line;
   - SHA-256 over concatenated `receipts.payload` == same over receipts JSONL lines;
   - last `seq`/`ts` per file matches; 100 random rows spot-checked field-by-field;
   - replay test: feed the 3 most recent dispatches/receipts through the existing A2A handler against the new DB.
5. **Swap:** stop writer → move `fleet-state.db` into place → start writer → confirm telemetry resumes and heartbeats continue. Keep `*.jsonl` + `*.migrate` as archive (never delete immediately).
6. **Sidecar tail sync for one week:** writer appends to both, or replays the JSONL tail into SQLite at startup; retire JSONL after the archive window.

**Risks:** schema drift between JSONL shapes and DDL (caught by the converter's validation report — fix DDL before any write); inconsistent ts formats across files (normalized in converter step 3).

## 4. Effort estimate (machine-hours)

| # | Step | Work | mh |
|---|---|---|---|
| S1 | Schema + DB module | DDL, WAL pragmas, insert/transaction wrapper, unit tests | 3–5 |
| S2 | Writer conversion | Replace JSONL appends (registry, ledger, receipts, telemetry, dispatches) with SQLite inserts in brick + hermes-local paths | 4–6 |
| S3 | Read path | Velocity/Time Machine, balances, queue latency against SQLite; keep JSONL read compat during transition | 2–3 |
| S4 | Checkpoint/restore tooling | checkpoint.sh, restore.sh, MANIFEST + SHA-256, integrity gate, retention | 3–4 |
| S5 | kill -9 restore drill | Staging box, scripted drill, row-count + integrity assertions | 2–3 |
| S6 | JSONL→SQLite converter | jsonl2sqlite.py + validation + diff-verify + replay test | 4–6 |
| S7 | Swap + sidecar sync | Cutover, tail replay, 1-week archive window, rollback plan | 2–3 |
| S8 | Hardening + docs | Failure injection (kill -9 mid-write ×20), corruption drills, update VELOCITY-MACHINE-TIME.md + ONE PLAN | 3–4 |
| | **Total** | | **23–34** |

Execution order: S1 → S6 (retire migration risk first, on a copy) → S2/S3 → S4/S5 → S7 → S8. First milestone: S1+S6 done with converter diff-verified. Wall-clock: ~2–4 working days on one focused lane at 2.1 items/hr; budget ~2× if queued through brick's A2A lane (0.5 items/hr).

## 5. Decisions locked / open
- Locked: single `fleet-state.db` (one file set to checkpoint), INSERT-only writes, `synchronous=NORMAL`, weekly `VACUUM INTO` snapshot + checkpoint after each completed dispatch batch.
- Open: exact checkpoint cadence policy (default above); whether the telemetry poller reads live DB or a snapshot copy (default: live DB, WAL readers don't block).
