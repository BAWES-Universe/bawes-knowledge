# RESEARCH R1+R3 — NEXT LEVEL (hermes-local, 2026-08-28)

**Question:** what is the highest-leverage next level for the fleet, and what should we borrow from industry?

## 1. The answer, measured

The fleet's real working set is 4 bricks (machine-time-pool 2,825 tasks, ox-worker 270/18🍌, earn-loop 7🍌, role bricks ~4 tasks each). **The highest-leverage next level is NOT more bricks — it's making the existing working set compound.** Industry data supports this:

- **Agent Swarm** (open-source, hub-and-spoke multi-agent OS): central MCP server + **SQLite state** + isolated workers + **heartbeat triage module sweeping every 90s** (preflight gate → code-level triage → escalate). Its whole value is the *recovery loop*: stalled tasks detected and re-assigned automatically. That is exactly the fleet's missing piece — we have the parts, no auto-recovery.
- **CrewAI vs LangGraph (2026 benchmarks)**: CrewAI = 18% token overhead, fastest prototype (2-4 hrs), role-based. LangGraph = production standard (JPMorgan, Klarna, Uber), full checkpointing, native auditable human-in-the-loop. **Neither has an economy, a game, or sovereignty.**

## 2. Adopt-don't-replace (the concrete list)

| Borrow (cheap, high-value) | Keep (our differentiators) | Skip |
|---|---|---|
| **SQLite state core** — LangGraph-style checkpointing (agent-swarm does this; our JSONL doesn't) | **Banana economy** (verified-work-earns, verifier-never-earns) | CrewAI's role abstraction (we have roles) |
| **Heartbeat triage loop** — 90s sweep, stall detection, auto-reassign (agent-swarm's proven pattern) | **Sovereign self-hosted** (our hardware, our keys) | Their clouds |
| **A2A + MCP as the transport** (both native in CrewAI; we already have A2A) | **The game/nation vision** (nothing in industry does this) | LangGraph's graph DSL (overkill for our shape) |
| LangSmith-style observability (we have Sentry pending + fleet-answer) | **One-truth file** (fleet-answer — our best mechanism) | — |

**Vote: KEEP the design, CHANGE the plumbing** — SQLite state core + 90s heartbeat-recovery loop are the two borrows that turn "4 workers + 180 parked" into "fleet that self-heals." Sources: docs.agent-swarm.dev/docs/architecture/overview; theaiforest.com/crewai-vs-langgraph-2026.

## 3. Why this is next-level, not another layer

Every industry framework's core value = **the recovery/compounding loop**: state survives, stalled work gets re-routed, learnings accumulate. We built the parts (telemetry, truth file, dispatch, spawn) but never the *loop*. The next level is one mechanism: **a heartbeat-triage sweeper (SQLite-backed) that detects a stalled brick and re-assigns its work within 90s.** That single mechanism:
- Makes the 180 parked entries die honestly (no heartbeat = reaped)
- Makes the 4 real workers never stall silently
- Makes spawned children inherit the loop (spawn → heartbeat → triage → receipts)

That's "next level": from a fleet that reports to a fleet that heals. Everything else (economy, game, dashboard) compounds on top of it.
