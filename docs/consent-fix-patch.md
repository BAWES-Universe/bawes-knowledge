# CONSENT-FIX PATCH (draft — brick to apply with its acceptance ritual, EOD 08-22)

## Root cause (verified 08-22 03:00 +03)
- consent-transcripts.jsonl has 3 rows: test users only (9000000000000001xx, hoostralie).
- mishari / chahd / khalid are ALL in funnel state (building) with NO transcript — the consent ASK never fired for them.
- Mechanism: the consent ask is brain-generated (`brain_funnel_reply` → lane call). The router's `/invoke` missing-model bug (fixed 08-21 22:22, token_router.py:755) made direct brain calls 400 — the funnel stalled at building and the ask never completed. Users got door-open fallbacks, not the consent moment.
- Even with the router fixed, nothing RETRIES the ask for already-stalled profiles → retro-ask needed.

## The patch (door_v4.py, in the DM handler before brain_funnel_reply)
Add a recovery gate — brain-free, template-based:
```
# RETRO-CONSENT-ASK (R5.4): profile in funnel state (building/confirming) with NO
# consent transcript -> send the warm consent ask directly (template, no brain
# dependency). Prevents brain-path stalls from silently parking real users.
if (stage in ("building", "confirming")
        and not _has_consent_transcript(user_id)
        and not _consent_ask_sent(user_id)):        # ask-sent log, 1 per user
    reply = _consent_ask_template(lang)             # reuse the R5.3 warm text
    _log_consent_ask(user_id, ts)                   # consent-asks.jsonl
    return reply                                    # DO NOT advance stage
```
Where:
- `_has_consent_transcript(user_id)` = grep TRANSCRIPT/REG_CONSENT for user_id.
- `_consent_ask_sent(user_id)` = new log `state/consent-asks.jsonl` (user_id, ts) — one ask per user, never nag.
- `_consent_ask_template(lang)` = the R5.3 warm consent wording (exists) + explicit "reply yes to confirm / no to hold".

## Acceptance test (brick's ritual — run before/after)
1. Seed a test user at stage "building", no transcript → send DM → expect the consent ask (template), no lane call, ask logged once.
2. Same user DMs again → no second ask (consent-asks.jsonl dedupe), normal funnel reply.
3. User replies "yes" → transcript row written (existing path), register sees consent.
4. Chahd (690554066815811625): after deploy, her thread receives the ONE retro ask — do NOT advance state until she replies in her own words. Same for mishari + khalid.
5. Regression: door-open fallbacks, false-claim guard, lane-down fallback still pass the existing acceptance suite (acceptance-*.md).

## Rollback
Backup door_v4.py before apply (brick's backups-* ritual); revert = restore + restart door_gateway.service.

## Owners
- Draft: hermes-local (03:00 08-22) — root cause from live state files, no code touched on prod.
- Apply + acceptance + deploy: brick (its domain, its ritual) — **deadline EOD 08-22**.
- Verify for real users: hermes-local (transcript rows for chahd/mishari/khalid present = gate green).
