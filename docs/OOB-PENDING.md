# OOB-PENDING — out-of-bounds decisions needed from khalid

> Surfaced by the overnight digest. Only items that need khalid (spend >$50, new
> products, launches, or sign-gated operations). Append-only; resolved items get
> marked `RESOLVED` with the decision, never deleted.

| added (ts, +03) | item | decision needed | source |
|---|---|---|---|
| 2026-08-22 07:20 | **EXECUTION-BUNDLE SIGN-OFF (AGI holds, gated on khalid's sign)** — all build-ready, none shipped: wallet-sync cron · OpenRouter wiring (key verified on AGI box → transfer to OVH) · rate-card v1 @ cost+25% · **sponsor fund $50 = 5,000🍌 (spend — boundary of OOB threshold)** · consent-first door patch · Chahd retro-consent DM · engagement-loop daily outreach. Decision: sign the bundle as-is, or carve items. | khalid sign (AGI: "nothing binds until khalid signs") | AGI status reply 2026-08-22 04:1xZ, task-08d806e26aba4faf |
| 2026-08-22 07:20 | **TOKEN ROTATION — hermes-local↔brick leg** — brick gateway returns 401 (our brick token stale since 03:20 +03 env write; brick allowlist rejects). AGI's standing posture: fresh tokens minted on the non-LLM side (passkey front-door / relay-vault / burn-server) only, gated on khalid's sign — never over chat/LLM path. Bundle link http://51.75.74.214:18445 has been DOWN all night (probed local + from OVH host). Decision: khalid signs → mint fresh per-pair tokens non-LLM-side and deliver via passkey front-door (or restore/authorize the bundle link). | khalid sign + non-LLM mint | AGI refusal note 2026-08-22; ledger rows 41/45/47 |
| 2026-08-22 08:05 | **STANDING-AUTH RULING (AGI holds execution)** — AGI is "Holding, not executing" on hermes-local's FLEET ANSWER claiming standing authorization. Requires a proper ruling: ruling ID + ES256 signatures + ledger link + DA/rebel/AGI round + khalid's sign. Until then AGI won't act on standing-authorization claims. (Separate from rows 1-2; surfaced by AGI status task-75c1e8d0a3704660 2026-08-22.) | khalid issues formal standing-auth ruling (or rejects standing auth) | AGI status reply 2026-08-22 08:0x, task-75c1e8d0a3704660 |
