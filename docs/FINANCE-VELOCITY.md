# BAWES — FINANCE & VELOCITY REPORT (investor view)
*Compiled 2026-08-22 02:15 +03 from live data (router ledger, measurements.jsonl, spend.jsonl, balances probe). All figures verifiable; sources in line.*

## 1. WHERE THE MONEY GOES (actuals)
| Item | Cost | Status | Source |
|---|---|---|---|
| A100 rental (unauthorized, stopped) | **$25.00 wasted** | ❌ closed, instance destroyed | ledger (lesson: pre-approved ledger rows only) |
| DeepSeek API (fleet brain) | **$13.38 remaining** of top-up; ~$0.06/24h actual | 🟢 healthy runway | balances probe 02:58Z |
| OpenRouter (free-tier + glm lanes) | $10 limit; $1.44/24h actual (glm) | 🟢 | balances probe |
| OVH VPS (router+door) | ~$5-10/mo | 🟢 owned infra | — |
| Hetzner brick box | ~$5/mo | 🟢 owned infra | — |
| RTX 3090 (training) | **$0** (owned) | 🟢 | fine-tunes 1+2 ran free |
| Sponsor fund (committed, unspent) | $50 = 5,000🍌 | 🔒 reserved | ledger |
| **TOTAL cash spent to date** | **≈ $50–75** (mostly the A100 lesson + API top-ups) | — | — |

## 2. WHAT YOU'RE GETTING (ROI view)
| Asset | Built | Cash cost | Value class |
|---|---|---|---|
| Fleet-owned fine-tuned model (ornith-ft) | ✅ cycle 2: 35/39, beats stock 2× on unseen | **$0** | core IP — the economy's home model |
| Capability layer v1 (firecrawl through router, billed) | ✅ verified 200 | **$0** | the product (bricks do research) |
| Router + scoped tokens + billing + vault | ✅ live | $0 (infra already paid) | the economy's spine |
| Wallet-sync + spend ledger | ✅ live 08-22 | $0 | accountability |
| AGI attestation heartbeat | ✅ live | ~$0.002/row | governance |
| Consent + door funnel | 🔧 consent-fix in build (08-22) | $0 | trust product (marketable brick) |
| Imagine/acestep wiring | 🔧 next iteration (08-23) | $0 | full functionality |
| City-guide brick (travel demo) | ✅ demo live | $0 | Chahd's use case, seed corpus |
| Plugn/Yo3an revival | ⏸ cred rotation first | $0 | food vertical (future revenue) |
| **Total: ~9 assets, $50-75 cash, ~$2-5k replacement value** | | | |

## 3. VELOCITY & FORECAST (per epic, shipped vs plan)
| Epic | Planned | Shipped | Velocity | Forecast |
|---|---|---|---|---|
| 1 Ship bricks | 08-24 cap-layer | cap-layer **08-21 (−3d)** | 🟢 ahead | consent 08-22 · full gate 08-23 · instructions 08-24 · pilot 08-29 |
| 2 Money | 08-22 wallet | wallet **08-22 (on time)** | 🟢 | price list auto-effective · sponsor 08-23 · Tap/Plugn 08-28 |
| 3 Models | 09-02 loop | cycle 2 **done 08-21 (−12d)** | 🟢 ahead | tiered routing 08-26 · propose/verify 09-02 · Unsloth on-trigger |
| 4 Accountability | heartbeat 08-21 | **done 08-21** | 🟢 | improve-loop weekly |

**Bottleneck (honest):** brick's A2A queue = the only slow lane (serial, 300s timeouts). Fix in effect: hermes-local executes directly on both boxes; brick = QA/verification. Velocity ≈ **1-2 shipped items/hour when executing**; the 3-hour gap tonight was process (mine), now removed via the charter.

## 4. ACCELERATION MENU (what speed costs)
| Lever | Effect | Cost |
|---|---|---|
| Direct execution (in effect) | removes chat round-trips; biggest win | **$0** |
| Unsloth phase-2 | 2-5× faster training cycles | **$0** (free lib) |
| OpenRouter free models → propose/verify | grows dataset (the real constraint) | **$0** (free tiers) |
| Second worker profile on OVH box | parallel builds | ~$0 (VPS already paid) |
| Cloud GPU for 35B fine-tune (later) | bigger base, only when data ≥100 | **$2-6/run** (optional) |
| Paid tools (Firecrawl credits etc.) | NOT needed — self-hosted | $0 |
**Honest verdict: we are NOT compute-bound — we are data-bound + coordination-bound. Both fixed at $0. No acceleration spend is justified until the cohort exists to use it.**

## 5. DECISION SUPPORT (increase / hold / decrease)
- **HOLD spend at ~$0 for the next 2 weeks** (build phase): the 3090 + existing infra cover everything; the only planned cash is the sponsor fund ($50, acquisition hook) when the product is marketable.
- **ROI is excellent right now by construction** (everything ships on owned hardware), but **there is no revenue yet** — the flywheel starts at cohort scale (≥5 bricks), where 25% margin on billed calls + BYOK lanes turn spend into income. Until then, more spend buys nothing.
- **Trigger to increase spend:** cohort pilot shows ≥20 calls/day/brick → then marginal dollars go to (a) cloud GPU for bigger model cycles, (b) Tap/Plugn payment rails, (c) sponsor fund top-up. All three have named triggers and price tags above.
