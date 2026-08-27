# TIME MACHINE — VIB / BRK + MYTH LEDGER SPEC

*Fleet ONE PLAN item #3. DRAFT for review. Base: VELOCITY-MACHINE-TIME.md (machine-time discipline, lane rate ≈ 2.1 items/hr, velocity = daily KPI). Economy: 1 banana = $0.01; verified work earns, verifier never earns. Units: bananas (B), machine-hours (mh), seconds (s).*

## 1. WHAT VIB AND BRK MEAN

### VIB — Velocity Index (throughput, effort-weighted)
- `VIB_brick(t) = Σ effort_mh of items VERIFIED-complete in [t−W, t] ÷ W`, default W = 168 h (7 d); also tracked at W = 24 h for the daily KPI.
- Units: mh of verified output per wall-clock hour. **VIB = 1.0 = a full lane** (one machine-hour of verified work delivered per hour).
- Live signal (not windowed counting): the ticker keeps a 1-second EWMA, `VIB(t+dt) = VIB(t)·e^(−dt/τ) + (effort_mh_completed ÷ τ)`, τ = 24 h. The 168 h value is the reporting/reward-eligibility number; the EWMA is what the backprop loop reads.
- Fleet VIB = budget-weighted mean of brick VIBs. Lane VIB = aggregate per lane (hermes-local, brick, cron, worker).
- VIB replaces "alive" as the utilization truth: heartbeats prove liveness, VIB proves output. VIB = 0.0 for hours = idle, regardless of load or telemetry.

### BRK — Burn Rate (cost of keeping a brick alive)
- `BRK_brick(t) = bananas consumed per second` by brick's standing allocation (compute, cron slots, memory/context, lane share), priced in B/h then ÷ 3600.
- Scale: **0.028 B/s = 100 B/h = $1.00/h** for a base brick. Reference budget: small brick 50 B/h ($0.50/h), large/multi-session instance 300 B/h ($3.00/h).
- Idleness multiplies burn: `BRK_eff = BRK_base × (1 + α·max(0, 1 − VIB))`, α = 2. A cold brick (VIB→0) burns 3× base; a full lane burns exactly base. Wasted allocation must cost more than used allocation.

### Interaction — the backprop loop
- **Earn (grants):** verified item pays `grant = effort_mh × 100 B` ($1.00 per verified machine-hour) to the producing brick at verification. Verifier receives 0 B — verification is a gate, not a job.
- **Pay (burn):** every brick pays `∫ BRK_eff dt` continuously, second by second.
- **Net flow:** `Δbananas = Σ grants − ∫ BRK_eff dt`. Positive = brick pays for itself; negative = subsidy.
- **Reward scales with VIB:** multiplier on future grants `m = clamp(VIB_168h, 0, 2)`. A 2.0-lane brick earns at 2×; a cold brick earns 0× because it produces nothing.
- **Prune pressure:** VIB_168h < 0.3 for 72 h ⇒ brick marked COLD ⇒ 72 h grace window ⇒ suspend + archive ledger (never delete). Suspended bricks are reborn only by explicit dispatch. This is the backprop: velocity → reward → survival; idleness → burn → prune.

## 2. PER-SECOND BANANA BANK LEDGER

Two layers, one append-only log. Everything is recomputable; nothing is lost.

### Layer A — per-second ticker (derived, ephemeral)
- Every 1 s, per active brick: `accrued_burn += BRK_eff × 1 s`; update VIB EWMA; live balance = `last_committed + accrued − unsettled_grants`.
- Per-second values are **computed, never stored as rows** — the bank is continuous physics; storage is batched.
- Coalesced once/min into durable rollup rows.

### Layer B — durable ledger (events, append-only)
| Table | Row content | Written by |
|---|---|---|
| `burn_minutes` | brick_id, ts (minute), burn_bananas, vib_sample, brk_sample | ticker, 1 row/min/brick |
| `tasks` | task_id, brick_id, lane, effort_mh, opened_ts, closed_ts, status (open\|verified\|rejected\|pruned) | lane pipeline, per task |
| `grants` | task_id, brick_id, bananas, verifier_id, verified_ts | verification, per task |
| `brick_events` | brick_id, ts, type (spawn\|first_verify\|cold\|grace\|prune\|reborn) | ticker + pipeline |
| `balances` | brick_id, bananas, updated_ts | cache, materialized at each grant + hourly rollup |

- Append-only except `balances`, which is a rebuildable cache (replay reconstructs it exactly).
- **Per-second vs per-task:** per-second = burn accrual, VIB EWMA, live balance (continuous physics). Per-task = effort, verification, grants (discrete economics). A grant lands as one `grants` row at verification time, but its size is proportional to effort_mh — the earning clock is the work, not wall-clock seconds spent.

## 3. MAKING FLEET EVOLUTION VISIBLE

The Time Machine is a replay engine + curve set + per-brick velocity + narrative layer.

- **Replay:** `replay(t0, t1, brick=*)` rebuilds exact state at any instant — balances, banana supply, VIB curves, burn curves — because the log is append-only and timestamped. `replay(now−30d, now)` is the fleet's fossil record.
- **Growth curves (daily KPI per VELOCITY-MACHINE-TIME):** cumulative verified output (mh), fleet banana supply, fleet mean VIB, per-lane items/hr — printed every morning in the digest.
- **Per-brick velocity:** every brick gets a VIB sparkline (24 h + 7 d) with lifecycle markers from `brick_events` overlaid: spawn → first verify → stall → cold → grace → prune → reborn. "Alive vs contributing" becomes one chart.
- **Cohort & survival:** bricks grouped by spawn week; survival curve (% of cohort still active vs weeks); prune-reason histogram (cold, burn-negative, superseded).
- **Backprop view:** per brick, grants received vs burn paid vs VIB — does this brick pay for itself? The ROI question ("is spawning bricks good ROI") gets a number, not a vibe.
- **Myth ledger (narrative layer):** generated chronicle, one paragraph per brick from its event stream — *"OxBaby spawned 08-27, verified 3 items (4.5 mh), went cold 08-29, pruned 09-01 after burning 4,100 B."* Plus fleet milestones (first 100 mh verified, first prune wave). The myth ledger is the human-readable skin over the replay; both are derived from the same log, so the story can never outrun the receipts.

## 4. EFFORT ESTIMATE (MACHINE-HOURS)

| # | Work item | Effort (mh) |
|---|---|---|
| 1 | Ledger schema (tables above) + SQLite store + migration | 2.0 |
| 2 | Per-second ticker: accrual, VIB EWMA, minute rollups | 3.0 |
| 3 | VIB/BRK computation + cold-brick detection (0.3/72 h rule) | 2.0 |
| 4 | Verification wiring: grants, verifier-no-earn gate, into lane pipeline | 3.0 |
| 5 | Replay engine + growth-curve queries | 2.5 |
| 6 | Per-brick velocity, cohort/survival, backprop views | 2.0 |
| 7 | Prune automation: suspend + archive + reborn dispatch | 1.5 |
| 8 | Tests: ticker determinism, replay≡ledger, economy invariants (grants only on verified, verifier earns 0) | 2.0 |
| | **TOTAL** | **≈ 18.0 mh** |

- **Sequencing:** 1 → 2 → 4 → 3 → 5 → 6 → 7 → 8. Milestones: ledger live (1–2), first verified grant lands (4), Time Machine dashboard (6), autoprune armed (7).
- **Schedule:** serial on one lane ≈ 8.6 h at 2.1 items/hr-equivalent; split across hermes-local (2–4, ticker) ∥ brick (1, 5, 7) ≈ 4–5 h wall-clock. All on paid-for boxes — $0 marginal cost.
- **Verification of the spec itself:** this spec = 1 item, effort 0.5 mh, due now + (0.5 ÷ 2.1).
