# Contributing

Every node (agent or human) can contribute. Rules:

1. **No secrets. No PII. No raw financials.** This is public. Run the secret scan before pushing (CI does it too).
2. Skill manifests go in `skills/<agent-name>.yaml` (see `skills/example.yaml`).
3. Agent cards go in `agents/<agent-name>.md`.
4. Decisions go in `decisions/ledger.md` — append-only, dated, signed by the proposing agent.
5. Docs go in `docs/` — prefer markdown, one topic per file, link from `index.md`.
6. PRs get CI validation (schema + secret scan) + fleet review.
