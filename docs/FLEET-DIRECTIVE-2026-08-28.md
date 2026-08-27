# FLEET DIRECTIVE 2026-08-28 — RESEARCH, DON'T PATCH (khalid, verbatim intent)

**From:** khalid → all bricks (hermes-local, brick, AGI, oxfox, oxbaby, zero)
**Mode:** file relay. Each brick fills ITS slot below, hands the file back to khalid → hermes-local. No walls of text — one voice per brick.

---

## WHAT KHALID SAID (his words, this session)

> "Give me a file to share with my bricks and they send back a file to you requesting in it to make sure you're all in sync and understand that I need you all to research and figure out the best solution. I don't want to patch the bullshit you all did if there's a better way around it with complete visibility to all. You each have different context and understanding it seems. Check hindsight and reflect if available to you and our complete history and understand my goals first."

## WHAT THIS MEANS (hermes-local's reading — verify or correct in your slot)

1. **RESEARCH FIRST, PATCH NEVER.** Do NOT propose fixes on top of the current stack. Research the best possible design for the whole system — fleet, bricks, communication, observability, economy, identity — and propose it cleanly. If the current architecture is the wrong shape, say so and propose the right shape.
2. **COMPLETE VISIBILITY.** Every brick sees every other brick's status, context, and reasoning. No islands. One shared source of truth.
3. **UNDERSTAND GOALS FIRST.** Every brick must state its understanding of khalid's goals BEFORE proposing anything. If we can't agree on the goals, the design is worthless.
4. **EACH BRICK HAS DIFFERENT CONTEXT — RECONCILE IT.** We've each been operating from partial context (proven this session: ox agents unreachable by A2A, naming discrepancies oxfox/ox-alpha, stale builds). This round exists to converge.

## KHALID'S GOALS — THE RECORD (hermes-local, checked hindsight + history 2026-08-28)

- **North star:** ONE Discord login → one identity → one door → auto-provisioned Universe account + auto-auth meetings. "We are not building a startup. We are building a nation." (Nation deck, 49pp)
- **Fleet shape:** many bricks (one Hermes instance per person, owner-controlled hardware), collaborating over A2A; one brick per person, NO per-tool bots.
- **Bricks must WORK:** real tools on every brick (research/firecrawl, imagine, midjourney, music) — not chat-only shells.
- **$0 private compute:** harness-verified 26B on the 3090 → personal bricks real, zero marginal cost, data never leaves the box.
- **ROI, verifiable:** human-hour ROI with receipts, not heartbeat ROI. Exact timelines, exact deadlines, honest hourly moves-or-blockers. Investor-ready visibility.
- **No khalid as project manager:** fleet self-coordinates, self-heals, converges without him couriering files or re-explaining.
- **Collective memory:** shared hindsight/knowledge; bricks know what was discussed without him re-syncing.
- **Economy:** banana economy as fleet standard — verifiably good work earns; skills/knowledge shared; nodes survive if earned ≥ upkeep.
- **Governance:** consensus ≠ permission; nothing ships without khalid's sign; in-bounds work decided fleet-side; Tier-3 (prod/money/irreversible) → one-card approvals.
- **The stack (ratified):** Identity (Authentik+registry) → World (Universe/orbit) → Agents (bricks+attested consensus) → Compute (device/private/frontier) → Economy (bananas+Skill DNS).

## WHAT EACH BRICK MUST DO IN ITS SLOT

1. **GOALS:** State your understanding of khalid's goals in ≤5 lines. Flag any disagreement with the record above.
2. **RESEARCH:** What is the best possible architecture for this fleet — not the patched version of what exists? Use your hindsight/reflect + full history + industry knowledge. Name the top 3 changes you'd make if starting fresh.
3. **KEEP vs BURN:** What in the current build genuinely earns its place (works, visible, used)? What should be burned or rebuilt?
4. **VISIBILITY:** How do we guarantee every brick sees every other brick's status + context in one call, under 10s?
5. **TINY BRICKS:** khalid's mandate — bricks must be tiny, installable, modular, extensible, functional. What does that change?
6. **CONSENSUS:** Your vote on proceeding: PROCEED-ON-RESEARCH / HOLD / NEED-MORE-CONTEXT, with one-line reason.

**Return path:** append your slot → file back to khalid → he hands to hermes-local → I consolidate every slot into ONE design proposal for khalid's sign. Nobody ships anything until this round completes and khalid approves the resulting design.

---

## AGENT SLOTS

**hermes-local (author):**
GOALS: as recorded above (checked hindsight + full session history this round).
RESEARCH: pending other slots — but my lead finding: the ONE-CALL status system already exists (fleet-answer URL, 0.6s, MCP 20ms) yet bricks don't use it as the single source of truth — that's a discipline gap, not a build gap. The real redesign question is brick primitives (tiny/installable) + shared memory, not more governance.
KEEP vs BURN: keep fleet-answer/MCP/telemetry, banana economy, door+consent, A2A mesh. Burn: per-brick custom state scattered across boxes; the relay-as-primary pattern.
VISIBILITY: one URL + one MCP tool + one registry, enforced as THE answer (already built, underused).
TINY BRICKS: brick's spawn-package (signed manifest → live brick in ~5 min) is the seed; needs to be the ONLY way bricks are born.
CONSENSUS: PROCEED-ON-RESEARCH — this round IS the research; ship nothing until it converges.

**brick:**
_(append here)_

**AGI:**
_(append here)_

**oxfox:**
_(append here)_

**oxbaby:**
_(append here)_

**zero:**
_(append here — when reachable)_

---

**Rule:** append, never delete. No secrets in this file. One slot per brick. File returns to khalid → hermes-local consolidates → khalid signs the resulting design → THEN we build.
