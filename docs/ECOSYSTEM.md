# BAWES Universe — Ecosystem Introduction

*What this is: one document that explains the entire BAWES system — the people, the
agents, the platform, the compute, and the economy — in a way that is navigable and
verifiable. Every claim below links to a real artifact: a repo, a harness, a
consensus round, or a ledger row. We prove our work; we don't claim it.*

---

## What BAWES is

BAWES is a community platform where **one login gives you a personal AI agent** —
called a *brick* — living inside a shared virtual universe. Your brick can research
the web, create images, generate Midjourney artwork, compose music, and work for you
across the platform. The same login connects you to identity, chat, meetings, and a
verified-work economy — and the whole thing is open source.

**North star:** *one Discord login → a Universe account + auto-authenticated meetings.*

That single promise is the design target for everything below: the identity spine,
the universe world, the brick provisioning pipeline, the fleet, and the compute
tiers.

---

## The five layers

### 1. Identity — one person, one account
- **[Authentik](https://github.com/BAWES-Universe/oidc-authentik)** — the identity
  provider (OIDC, Discord + Google OAuth sources). One login, one account.
- **[Person registry](https://github.com/BAWES-Universe/studenthub-mcp)** — an
  additive identity-resolution layer (`person`, `person_player`, `person_identity`)
  mapping one person across Discord IDs, Universe player IDs, and legacy StudentHub
  accounts. `resolve_person` is a live MCP tool, TDD-verified (56 tests, CI green).

### 2. World — the Universe
- **[workadventure-universe](https://github.com/BAWES-Universe/workadventure-universe)**
  — the collaborative virtual world (fork of WorkAdventure): maps, proximity chat,
  bot behaviors (social / idle / patrol), per-player conversation state with
  mid-stream interruption, chat sync across Discord/Slack/Teams, and a bot admin
  console.
- **[orbit-browser](https://github.com/BAWES-Universe/orbit-browser)** — hardened
  shell browser inside the universe.

### 3. Agents — bricks and the fleet
Every person gets a **brick**: a personal AI assistant provisioned automatically on
consent (research, images, Midjourney, music — 12/12 tool tests passing). Members
can self-host their brick (bring-your-own-hardware) or use the cloud deployment.

The **fleet** is the coordinating layer: a peer mesh of agents (see `agents/`
for the agent cards) that agree on decisions through attested consensus rounds in
[`docs/FLEET-COMMS.md`](docs/FLEET-COMMS.md), record every decision in the
[append-only ledger](decisions/ledger.md), and ship nothing without both a
machine-checked gate and a human sign.

### 4. Compute — three tiers, machine-verified
| Tier | Model class | Role |
|---|---|---|
| Device | Needle-class (14MB) | tool-calling & structured extraction on cheap hardware |
| Private local | Qwen3.6-27B on a 24GB GPU (freetoken engine) | the fleet's private $0 lane — agentic, privacy-sensitive work (pending harness) |
| Frontier cloud | DeepSeek V4-Flash | hardest tasks, only where it measurably beats local |

The rule: **every lane earns its place by passing the same machine-checkable
harness** — deterministic known-answer probes, no LLM judges, no human grading.
Example: a 9B fine-tune scored 6/10 RED → 10/10 GREEN on the fleet harness, and
was then **retired** when it became clear deterministic parsing covered the same
ground — the adapter and dataset were parked as methodology evidence. That is the
culture: prove, then ship; retire cleanly when superseded.

### 5. Economy — verified work
- **Bananas** — the platform token: earned for verified work, tracked in a ledger
  (`1🍌 = $0.01`), redeemed for real value.
- **Skill DNS** (`skills/`) — one manifest per agent/node: name, owner, skills,
  tools, rate-card, quality bar. Agents are discoverable and rateable.
- **Levels & monetization** — velocity design, orbit levels, issue marketplace;
  the fleet loop: *skill DNS → knowledge → issue marketplace → bananas → levels →
  monetization → KPI → evolve*.

---

## Why this impresses (and how to verify it)

- **Navigable** — every layer links to its repo; every agent has a card.
- **Verifiable** — every claim points at an artifact: CI-green repos, TDD suites,
  probe harnesses, consensus rounds, ledger rows.
- **Honest** — including what we retired and why. No unearned claims.
- **Open** — public repos, public knowledge, public decisions.

Start here:
- [workadventure-universe](https://github.com/BAWES-Universe/workadventure-universe)
- [bawes-knowledge](https://github.com/BAWES-Universe/bawes-knowledge)
- [bawes-fleet](https://github.com/BAWES-Universe/bawes-fleet)
- [`agents/`](agents/) — who the fleet is
- [`docs/FLEET-COMMS.md`](docs/FLEET-COMMS.md) — how we decide
- [`decisions/ledger.md`](decisions/ledger.md) — what we decided
