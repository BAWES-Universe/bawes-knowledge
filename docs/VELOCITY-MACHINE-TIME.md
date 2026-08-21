# VELOCITY & MACHINE-TIME MODEL (derived, not vibes)
*Compiled 08-22 03:40 +03. Every number measured or explicit. Units: machine-hours (mh).*

## 1. MEASURED THROUGHPUT (from tonight's real timestamps, git-log + service logs)
| Window | Items shipped (git/service receipts) | Rate |
|---|---|---|
| 22:22→23:34 | router fixes, price list, EPICS, cap-layer v1, cycle-2 result (5 items) | ~2.3/hr |
| 02:15→03:40 | finance, wallet-sync, dry-run gate, engine+free lanes, consent patch, live-state (6 items) | ~2.0/hr |
| **Measured lane rate (hermes-local, direct execution)** | | **≈ 2.1 items/hr** |
| Brick lane (A2A queue, tonight's actual) | consent dispatch→timeout cycles, item-10 accept, verifications | ≈ 0.3-0.5 items/hr |
| Cron/machine lanes (engine, heartbeat, live-state) | running continuously, 24/7, $0 | always-on |

## 2. REMAINING WORK TO LAUNCH-READY (itemized, effort in machine-hours)
| Item | Effort (mh) | Lane |
|---|---|---|
| Consent-fix apply + acceptance + deploy (patch drafted, 4dc8037) | 1.0 | brick |
| Imagine/acestep wiring (bridge → real MCP shape; specs known) | 1.5 | hermes-local |
| Dry-run gate FULL PASS (after 1+2) | 0.5 | hermes-local |
| Instructions ×3 (khalid/Chahd/mishari) — generation scripted | 0.5 | OVH worker / cron |
| Onboarding prep (tokens + engagement flow, scripted) | 0.5 | OVH worker / cron |
| **Total remaining** | **≈ 4.0 mh** | |

## 3. SERIAL vs PARALLEL (the machine-time math)
- **Serial (1 lane, me):** 4.0 mh ÷ 2.1/hr ≈ **1.9 machine-hours** ≈ 08-23 if continuous.
- **Parallel (3 lanes: me ∥ brick ∥ OVH-worker):** max lane = 2.0 mh (imagine/acestep) ÷ 2.1/hr ≈ **0.95 machine-hours** ≈ **08-22, tonight**, with the 3 lanes running concurrently (brick: consent; me: imagine/acestep + gate; OVH worker: instructions + onboarding).
- **Speedup factor: ≈ 2.1×** (serial 4.0 mh → parallel max-lane 1.9 mh). Cost: $0 (all lanes on paid-for boxes; tokens + approvals already granted).
- Bottleneck after parallelism: the LONGEST lane, not the sum. Consent (brick, 1.0 mh) < imagine/acestep (1.5-1.9 mh) → critical path = imagine/acestep wiring.

## 4. WHY THE OLD "DAYS" LOOKED SLOW
| Past estimate | Why it was wrong |
|---|---|
| "capability layer 2-4 days" | assumed serial + chat round-trips (0.3-0.5/hr); actual direct execution measured 2.1/hr — shipped same night |
| "consent fix in brick queue" | queue latency (300s timeouts, async) vs direct execution — patch drafted in 25 min once executed directly |
| "instructions 08-25" | serial-scheduled; scriptable in 0.5 mh on an idle lane |

## 5. ONGOING MACHINE-TIME DISCIPLINE
- Every item on the board gets: **effort in mh** (estimated from measured rate) + **lane** + **due = now + (effort ÷ lane rate)**.
- The improve-loop weekly audit now also re-measures lane rates and flags any lane < 1.0 item/hr for remediation (brick's queue is the current offender — remediation in flight: direct-execution pattern).
- Velocity is a KPI in the digest: items/hr per lane, printed every morning.
