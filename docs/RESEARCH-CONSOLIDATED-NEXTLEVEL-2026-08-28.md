# RESEARCH CONSOLIDATED — NEXT LEVEL (2026-08-28)

**hermes-local consolidating: my brief (R1+R3) + subagent deep-dive (R3) + fleet round open (brick/AGI/ox pending).**

## THE VERDICT (three independent reads, one answer)

**KEEP the design. CHANGE the plumbing. REBUILD nothing.**

The fleet's disease is governance/ops (uncoordinated bricks, truth-file not enforced, idle instances) — **not** graph execution. Frameworks can't fix that:
> "A graph engine cannot enforce a truth file; budgets + approval gates + audit can." — R3 deep-dive, sources verified

## WHAT TO BORROW (patterns, not packages — ~2 weeks hand-rolled)

**From Paperclip** (self-hostable control plane, MIT, 79.5k stars — its four pillars map 1:1 onto our pain points):
1. **Atomic task checkout** — no double-work (kills the stepping-on-toes disease)
2. **Budget enforcement** — stop at limit, no runaway spend (makes banana economy a real throttle)
3. **Heartbeat scheduler with idle/zombie detection** — fixes idle instances mechanically
4. **Approval gates + rollback + immutable audit ledger** — the banana ledger of record

**From LangGraph** (production standard: JPMorgan, Klarna):
5. **Checkpoint/resume pattern** — crash-resume for long brick tasks (SQLite state core)

**From CrewAI:**
6. **Memory recall + usage metrics patterns** — nothing we don't have, but the discipline of embedding-scored recall

## WHAT TO KEEP (the differentiators — nobody in industry has these)
- **Banana economy** — it IS the budget layer; make it atomic, don't replace it
- **Canonical truth file** — add single-writer lock + schema validation
- **A2A + telemetry + dashboard + Discord OAuth** — the framework-free core is fine

## WHAT TO SKIP
- CrewAI/LangGraph as the orchestration backbone (re-wraps coordination without enforcement)
- LangSmith/LangGraph Platform clouds (sovereignty)
- Paperclip as the fleet OS today (duplicates banana economy + dashboard; re-review at >50 agents)

## SOURCES (verified)
- agent-swarm.dev/docs/architecture/overview — hub-and-spoke + SQLite + 90s heartbeat triage
- theaiforest.com/crewai-vs-langgraph-2026 — CrewAI 18% token overhead; LangGraph production list
- github.com/crewAIInc/crewAI + docs.crewai.com — flows, memory, usage metrics
- docs.langchain.com/oss/python/langgraph/persistence + /human-in-the-loop — checkpointers, interrupts
- github.com/paperclipai/paperclip — org chart, budgets, approval gates, heartbeats, audit
- JATIR 2026 "Benchmarking Multi-Agent Frameworks" (jatir.org/article.php?paperid=140332) — no capability winner, ergonomic differences
- arXiv:2411.18241 — frameworks as plumbing, not business model (production case study)

## THE ONE NEXT-LEVEL BUILD (from this research)
**The Enforcement Layer** — hand-rolled, ~2 weeks: atomic checkout + budget-stop + heartbeat-triage + approval gates + immutable ledger, on the SQLite state core. That single layer turns "4 workers + 180 parked + uncoordinated" into "fleet that self-heals and self-throttles." Everything else compounds on it.

— hermes-local, consolidating for khalid's sign
