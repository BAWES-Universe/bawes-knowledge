# EPICS BOARD — khalid-defined, deadline-driven, receipt-tracked
*Compiled 2026-08-21. Every epic: owner · deadline · next visible output (receipt). Status updated in the daily digest. Missed deadline = explicit FLAG row, no silent drift.*

## EPIC 1 — SHIP THE BRICKS (the product) · owner: brick + hermes-local
| # | Item | Owner | Deadline | Next visible output |
|---|---|---|---|---|
| 1.1 | Consent fix (funnel ask fires + Chahd retro-ask; her state: building, no transcript) | brick | **08-22** | Chahd's DM receives the consent ask (screenshot-able); transcript row written |
| 1.2 | Engagement loop (daily owner outreach until activate/opt-out) | brick | **08-23** | First daily outreach message sent to a real owner |
| 1.3 | Capability layer (per-brick tool wiring via router — firecrawl/imagine/acestep) | brick + hermes-local | **08-24** | Router routes a user-brick tool call end-to-end |
| 1.4 | Dry-run gate (Chahd's brick: consent→tools→billing, zero errors) | hermes-local (script ready) | **08-24** | Gate script PASS/FAIL output (~/probe/dry_run_gate.py) |
| 1.5 | Instructions for khalid/Chahd/mishari | hermes-local | **08-25** | Three instruction sets in repo, receipt-backed |
| 1.6 | Pilot cycle (khalid + Chahd post-consent) | fleet | **08-31** | Pilot digest: activations, tool calls, billing rows |

## EPIC 2 — MONEY · owner: brick + hermes-local
| # | Item | Owner | Deadline | Next visible output |
|---|---|---|---|---|
| 2.1 | Price list from live measurements (25%, peg 0.01) | hermes-local | **DONE (ccfd1ac)** | ✅ awaits khalid `sign` |
| 2.2 | Wallet-sync cron (daily balances → spend.jsonl → digest) | hermes-local | **08-22** | First digest with spend + balances |
| 2.3 | Sponsor fund ($50 = 5,000🍌, ledger row per call) | brick | **08-23** | First sponsored call row |
| 2.4 | OpenRouter lanes wired on OVH (free→$0, paid→premium) | brick | **08-23** | Lane round-trip via openrouter (real reply) |
| 2.5 | Tap/Plugn payments (cred rotation → sandbox → merchant guide) | hermes-local + brick | **08-28** | Cred-rotation checklist DONE + Tap merchant guide |

## EPIC 3 — MODELS & EVOLUTION · owner: hermes-local + AGI
| # | Item | Owner | Deadline | Next visible output |
|---|---|---|---|---|
| 3.1 | FT local lane (ornith-ft 10/10) | hermes-local | **DONE** | ✅ live on :11435 systemd |
| 3.2 | Tiered routing (ROUTER-TIERS: probe-gated lanes, fallback, shadow mode) | hermes-local | **08-26** | Shadow-mode log: routing decisions without user impact |
| 3.3 | Propose/verify loop (OpenRouter free models generate samples, deepseek audits, machine gates) | hermes-local | **09-02** | First 20 accepted dataset samples |
| 3.4 | Unsloth phase-2 (dataset ≥100 or 35B attempt) | hermes-local | on-trigger | Trigger-check row in digest |

## EPIC 4 — ACCOUNTABILITY · owner: fleet
| # | Item | Owner | Deadline | Status |
|---|---|---|---|---|
| 4.1 | Attestation heartbeat (every ledger row → AGI ATTESTED/FLAG in ≤15 min) | hermes-local | **DONE** | ✅ live (cron */15, receipts logged) |
| 4.2 | Daily digest (epics status + spend + balances + needs-khalid) | brick | **DONE** | ✅ 09:00 cron |
| 4.3 | Missed-deadline rule: any epic past ETA → FLAG row + surfaced in digest | fleet | standing | active |

## Open khalid items (one word each)
- `sign` — price list (2.1) · `sign` — capability-layer card when it lands (1.3)
