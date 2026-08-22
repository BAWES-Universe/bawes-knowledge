# DA RULEBOOK v1 — pre-ship challenger rules (derived from actual errors khalid caught)
*Every planned fleet action is reviewed against these rules by an INDEPENDENT model (challenger) BEFORE it ships. Rule violated = FLAG + answer required. The fleet stops relying on khalid as the only critic.*

## R1. CAPACITY UTILIZATION — no owned asset idles if it can work
Any owned compute/model/tool that can contribute to a running goal MUST be working. Check: is the local model producing? is the GPU used? are free tiers contributing? is any lane parked while paid capacity works? *Violated by: FT model idle while engine used cloud; free lanes fallback-only.*

## R2. CONTINUOUS OVER BATCHED — no artificial cadence
If the work is local and cheap, it runs CONTINUOUSLY, not on a cron. A cadence must be justified by a real constraint (rate limit, cost, external API). 5-min cadences on local work = rule violation. *Violated by: engine on */5 cron.*

## R3. PARALLEL SOURCES — never single-source anything
Independent sources (models, lanes, tools) run in parallel when they exist. Fallback-only wiring is a violation — fallback means idle capacity. *Violated by: free lanes as fallback only.*

## R4. DERIVED DEADLINES — no vibes
Every deadline = effort (machine-hours) ÷ measured lane rate. No date without the math. *Violated by: "2-4 days" capability estimate; serial scheduling.*

## R5. MACHINE TIME — no human-time units
Scheduling, ETAs, and reporting use machine-hours and items/hr per lane — measured, in the digest. *Violated by: day-based estimates.*

## R6. PROBE-GATED — no unmeasured swaps
Any model/lane/tool change ships only with a machine-checkable probe verdict (or an explicit test plan). *Violated by: none tonight (kept discipline) — standing rule.*

## R7. VISIBLE OUTPUT — nothing ships silent
Every action produces a receipt (ledger row, artifact, live-state line) within its window. Silent degradation (crash-loops, dead lanes) = violation, caught by the improve-loop. *Violated by: pool-bridge 1273-restart loop invisible for an hour.*

## R8. NO-KHALID-BOTTLENECK — the fleet self-executes in-bounds
Anything in charter scope executes without asking. Waiting for a signature that standing directives already cover = violation. *Violated by: the 2h20m "waiting for charter" gap.*

## R9. INDEPENDENT CHALLENGE — no self-review
No agent ships its own work without an independent review. The challenger (different model) reviews every ledger-worthy action against R1-R8 pre-ship. *Violated by: everything shipped tonight before this rule existed.*

## Enforcement
- **Pre-ship:** challenger runs on every planned action before commit (git hook + wrapper). PASS → ship. FLAG → answer or fix, then re-review.
- **Morning sweep:** cron reviews the previous 24h of ledger rows against R1-R9; violations go to the digest with the answer.
- **Rulebook evolves:** any error khalid (or the challenger) catches that isn't covered adds a rule. The rulebook learns from every catch.
