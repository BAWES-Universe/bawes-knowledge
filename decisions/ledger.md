# Fleet consensus ledger

Append-only. Every decision: date, proposer, verdicts, khalid approval status.
Consensus ≠ permission — khalid's explicit approval is the final gate.

| Date | Decision | Proposer | Verdicts | khalid | Status |
|------|----------|----------|----------|--------|--------|
| 2026-08-12 | bawes-knowledge repo created (public, open source) | khalid | — | ✅ approved | LIVE |
| 2026-08-21 | Peer admission: hermes-local as registered A2A peer of AGI + brick (allowlist add, least-privilege) | khalid | — | ✅ approved | LIVE — wiring: brick + AGI add peer entry; AGI verifies ledger directly |
| 2026-08-21 | Vast instance 48034454 destroyed — A100 80GB on-demand, unapproved spend (hard spend rule #1 violated); audit V-7 closed, teardown row fa43c00daeb46aa7, zero instances billing | brick | ✅ brick, ✅ hermes-local | ✅ approved | DONE |
| 2026-08-21 | Services pool direction — banana-priced MCP services (hermes-local: imagine/acestep/midjourney; brick: accounting/linear/video; future providers incl. mishari encouraged to list & earn) | khalid | spec draft: brick ✅; AGI verifier weigh-in in flight | ✅ approved | DESIGN — rate-card v1 pending khalid margin |
| 2026-08-21 | Services-pool earning model RATIFIED (universal): every provider earns bananas for tools/MCPs/services they list — hermes-local, brick, mishari, shahd/chahd, all brick owners. Per-call earnings rows, AGI-verified quality, rate card = khalid-set. | khalid | — | ✅ approved | LIVE (design) — unlock: capability-layer build + rate-card v1 + sponsor fund |
| 2026-08-21 | ORNITH-1.5:9b probe → fleet consensus **NO-ADOPT** (machine-scored, brick harness, 4 models: ornith 6/10 RED [extraction 2/4, structured 1/3, coding 3/3 — best of four], deepseek-r1-7b 1/10, qwen3-4b 4/10, gemma-3-27b 2/10; extraction = binding constraint, 0/4 clear it). ornith retained as S3 candidate for code-only/long-context edge lanes only. Status quo, zero operational change. Artifact ~/probe/probe-report-2026-08-21.json. | fleet consensus: brick ✅, hermes-local ✅ (AGI attests per DA pipeline) | — | NO-ADOPT | COMPLETE |
| 2026-08-21 | FLEET-MODELS v1 — fine-tune experiment APPROVED (khalid): QLoRA fine-tune of ornith-1.5:9B on OUR 10-task JSON-discipline dataset, run on hermes-local RTX 3090 (local hardware, $0 cloud spend; Vast budget deferred pending first results). Gate: machine probe before/after — a fine-tune that doesn't beat stock on the probe never deploys. Pipeline: DA → Rebels → AGI → khalid. | khalid | — | ✅ approved | EXECUTING — GPU check → dataset prep → QLoRA (idle-scheduled) → probe gate |
