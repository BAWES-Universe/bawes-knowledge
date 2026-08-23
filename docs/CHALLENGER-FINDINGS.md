# Challenger findings — 2026-08-22T08:34

`[FLAG] S0: 2026-08-22 07:32   OVERNIGHT-COORD 5 — PIPELINE: all 4 services ACTIVE (ornith-f
      - R6: Wrapper owns lane restart + counter reset on completion, but no machine-checkable probe verdict is attached before the restarted lane ships.
      - R2: OVERNIGHT-COORD 5 introduces a batched overnight cadence without stating a real constraint (rate window, maintenance, etc.) that justifies b
      - R4: CYCLE 3 is reported as 'STILL in flight' with elapsed 2h39m, but no derived deadline from effort/machine-hours divided by measured lane rate
      - R1: train_qlora_v2.py shows 99.9% CPU / 1.49GB RSS, suggesting CPU-only execution; if owned GPU/fine-tune capacity exists, it appears idle rathe
[FLAG] S1: 2026-08-22 07:32   OVERNIGHT-COORD 5 — CONSENT re-verified direct (OVH double-ho
      - R1: Retrieved docs (scientist-neurologist-001) report 110/76/41 registered-but-idle bricks; this action does nothing to activate them, leaving o
      - R2: 'OVERNIGHT-COORD 5' imposes a fixed overnight batch cadence with no real constraint shown, violating continuous processing.
      - R3: Consent verification relies only on one serial OVH double-hop path ([jump-host] -> [door-host]); no parallel independent source is used
      - R4: 'brick deadline-reminde' is truncated and not derived from effort/machine-hours divided by measured lane rate, so the deadline is unvalidate
      - R5: Report is scheduled in human terms — calendar date 2026-08-22 and 'OVERNIGHT' — not in machine-hours.
      - R6: 'Fix live on door' ships without an attached machine-checkable probe verdict, so the lane/tool change is not probe-gated.
      - R9: This OVERNIGHT-COORD entry appears to self-verify consent status with no independent challenge, and no ledger-worthy independent review is e
[FLAG] S2: 2026-08-22 07:32   OVERNIGHT-COORD 5 receipt   fleet
      - R2: OVERNIGHT-COORD batches 5 items into an overnight cadence with no documented real constraint; work must flow continuously, not on an artific
      - R5: The action is stamped and reported in human-clock terms (2026-08-22 07:32, overnight) instead of machine-hours or derived lane-rate units.
      - R6: No machine-checkable probe verdict is attached; if OVERNIGHT-COORD touches a lane, model, or tool, it ships ungated.
      - R8: Fleet-wide coordination and receipt sign-off create a redundant in-bounds approval path; the work should self-execute unless an exception is
      - R9: No independent challenger review is recorded on this ledger-worthy action; the coordination appears to self-attest its own receipt.
[FLAG] S3: 2026-08-22 08:05   OVERNIGHT-COORD 6 — PEERS: AGI reachable + auth OK (19903). S
      - R1: AGI reachable + auth OK yet hermes-local is still 'Holding, not executing'; an owned asset that can work is being left idle.
      - R8: Standing-auth hold persists with empty approval/sign queue — in-bounds work appears to be waiting on redundant authorization instead of self
      - R7: TASK_STATE_COMPLETED without a visible output artifact/receipt for the status ping; completion status alone is silent degradation.
[FLAG] S4: 2026-08-22 08:05   OVERNIGHT-COORD 6 — TOKEN ROTATION: NO fresh A2A_PEER_TOKENS 
      - R1: Owned asset [door-host]:18445 is verified DOWN on /health and / yet the action reports 'Nothing applied' and leaves it idle without documen
      - R2: 'OVERNIGHT-COORD 6 — TOKEN ROTATION' enforces an artificial nightly cadence with no real constraint; the reply confirms a batched 'no fresh 
      - R3: The bundle is re-probed from a single source (curl from ubuntu@[door-host] itself); independent parallel probes, e.g. external /health and 
      - R5: Reporting uses human wall-clock (2026-08-22 08:05) and narrative plan terms rather than machine-hours or measured lane-rate-derived scheduli
[PASS] S5: 2026-08-22 08:05   OVERNIGHT-COORD 6 — PIPELINE: all 4 services ACTIVE (ornith-f
[FLAG] S6: 2026-08-22 08:05   OVERNIGHT-COORD 6 — CONSENT re-verified direct (OVH double-ho
      - R2: OVERNIGHT-COORD is an artificial batch cadence; no real constraint is cited for deferring consent verification to a nightly tick instead of 
      - R5: The action schedules/reports in human clock terms ('overnight', 2026-08-22 08:05) rather than machine-hours/lane rate.
      - R7: The corrected tally is internally inconsistent: transcript has 14 rows but the stated tally is 12×9000000000000xxx + hoostralie = 13 entries
[FLAG] S7: 2026-08-22 08:05   OVERNIGHT-COORD 6 receipt   fleet
      - R1: No evidence in the action that owned assets are kept working; overnight coordination may leave capacity idle (per discord-Follow the Butterf
      - R2: The 'OVERNIGHT-COORD' label suggests batched overnight execution without citing a real constraint; violates continuous-over-batched (per dis
      - R3: No indication of parallel sources; coordination appears serialized, and independent sources are not shown running in parallel.
      - R4: No deadline is derived from effort/machine-hours ÷ measured lane rate; the receipt contains no metric basis (per discord-Follow the Butterfl
      - R5: Reporting is not in machine-hours; the entry only has a wall-clock timestamp, not machine-hour accounting for the coordination work.
      - R6: No machine-checkable probe verdict accompanies the coordination; any model/lane/tool change inside this action is unverified.
      - R8: No proof the work self-executed; the receipt does not exclude waiting on redundant signatures or approvals.
      - R9: No independent review is attached to this ledger-worthy coordination receipt; self-review cannot be ruled out.
--- retro done: 34 flags total ---
`

**7 flagged rows in the last 24h.** Digests must answer each flag.
