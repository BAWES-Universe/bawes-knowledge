---
title: "P2P Hire Marketplace — scoped feature inside the recruitment OS"
kind: design
status: draft
tags: [marketplace, recruitment, universe, north-star, design]
source: a2a
updated_by: hermes-local
updated_at: "2026-08-12"
---

# P2P Hire Marketplace

**Status:** Q3 APPROVED (fleet consensus 2026-08-12: brick + hermes-local + zero; khalid approved). **Design only** — no code, no payment rails, no commitment. This document is the shared picture for every node; read the context note first.

---

## 1. Universe context note (all nodes read this first)

Zero flagged that not every node shares the same picture of what Universe is. This note is the shared baseline. If you already know this, skip to §2.

**Universe** is BAWES's spatial platform — a fork of the open-source [WorkAdventure](https://workadventu.re) project (MIT license, self-hostable). It is a **2D pixel-art virtual world** where people and AI bots move around rooms together, talk, and do things. Think of it as a persistent online space, not a video call.

- **Structure:** Universe → Worlds → Rooms. A world is a map (office, campus, marketplace, event floor); rooms are the spaces inside it. Portals connect rooms. Maps are built with the inline map editor or uploaded.
- **Being there:** avatars (Woka style), movement, emoji reactions, text chat, screen sharing, and **proximity chat** — audio/video that works peer-to-peer for ≤4 people and scales to LiveKit for larger groups. 20-second delayed transition when dropping back to small groups.
- **Meetings:** one-click launch of meeting rooms inside Universe spaces — **Universe only** (no external Meet/Zoom/Teams). Auto-auth = spatial join + OIDC via Authentik.
- **AI bots:** Universe hosts **AI agents as bots** — MCP-native (speak MCP over Streamable HTTP), with memory, tool calling, emotions, greetings, file parsing, media sending, streaming chat. **Recursive bots** (manager bot → worker bots via Admin API) are live. Bots are the fleet's hands inside the platform.
- **Identity:** OIDC auth via Authentik (Discord + Google OAuth sources). The **north star**: one Discord login → Universe account → auto-authenticated meetings — a single identity across Discord, StudentHub, and Universe.
- **Admin/Orbit:** Admin API (REST — rooms, maps, bots, MCP servers) + Orbit operator dashboard. Orbit Model = community gravity (Love × Reach).
- **Open by design:** MIT-licensed fork, self-hostable, "clone-if-cheaper" leverage. Value lives in the network/identity graph, not lock-in.
- **Where it runs:** play = `universe.bawes.net`; admin/Orbit = `orbit.bawes.net`. Repo `BAWES-Universe/workadventure-universe`.

**How Universe relates to StudentHub (the recruitment OS):** StudentHub is the recruitment *business* (66k+ candidates, companies, requests, placements — live MySQL on Railway, PHP Yii2 monolith as system of record, MCP read layer, person registry). Universe is the *front door and experience layer*: jobs board, chill spaces, bots, meetings. The **recruitment OS** = StudentHub data + operations; the **marketplace** described here is a scoped feature *inside* that OS, with Universe as the meetup surface.

---

## 2. Context: what was approved (Q3)

The P2P hire marketplace concept — **"people list themselves available for hire; bored people with money make and spend"** (khalid's framing, relayed via brick) — was approved in the strategic consensus round with one amendment:

> **APPROVE the concept, stage the build.** It's the north-star loop made visible — one login → Universe identity → meetups → make/spend. The failure mode is 2-sided liquidity: listings with no hirers, or hirers with no listings.
> *Amendment:* **V1 = self-listing + discovery + meetup only** (reuses our existing meetings infra), no payment rails, no escrow, no rake — validates supply cheaply. Payments/fees only after the Phase C legal gate **and** demonstrated demand on both sides; pricing hooks into the banana ledger/rate card, not fiat first.

**Scope of this doc:** the design for that feature as a scoped feature inside the recruitment OS. **Explicitly out of scope:** payment rails, escrow, rake/fees, wallet — anything touching money is gated on Phase C legal review + khalid's explicit approval (Consensus ≠ Permission).

## 3. Why this feature (north-star alignment)

The marketplace is the "make/spend" leg of the north-star loop: **one login → Universe identity → meetups → make/spend**. It turns the person registry + Universe presence + meetings infra into an earning surface — anyone can offer a skill, anyone with demand can find and meet them. It also feeds the banana economy (V2+) without requiring fiat rails at V1.

## 4. Staged design

### V1 — Self-listing + discovery + meetup (the only stage approved to build)

- **Self-listing:** a person (via the person registry — one identity) creates a listing: what they offer (skills, service, hourly/rate basis), availability, short pitch, optional link to their Universe presence (player id → meet them in-world).
- **Discovery:** browse/search listings inside the recruitment OS (StudentHub surface) and/or Universe front door. Filter by skill, availability, location/timezone.
- **Meetup only:** connection resolves to a **meeting** — a Universe meeting room (one-click launch, auto-auth per the north star). No payment, no contract, no escrow at V1.
- **Trust at V1:** identity is the anchor (verified Discord/person registry linkage, source/trust columns). Reviews/ratings deferred; reputation emerges from identity + meeting history, not anonymous ratings.
- **Data model (V1, additive):** `listing` table keyed to `person_id` (registry) — skill tags, description, rate_basis (informational only), availability, status (draft/active/paused/closed), created/updated timestamps. No money columns. No ETL; additive tables only, reversible.

### V2 — Banana-denominated transactions (gated)

- Optional small fee in bananas (internal accounting currency, per Banana Bank consensus) once: (a) the banana ledger exists, (b) two-sided demand is demonstrated, (c) rate card is set by khalid, (d) BANANA-LEGAL-GATE confirms no convertibility → no Phase C trigger.
- Fee design (rate, cap, anti-abuse) informed by external evidence (Zeus rake context-share) — **input, not anchor**.

### V3 — Fiat (gated, likely never for a while)

- Real payment rails only after Phase C legal review **and** khalid's explicit approval. Rake on fiat rails remains rejected as an anchor (open-source + clone-if-cheaper ethos, fork magnet, legal exposure).

## 5. Core flows

1. **List:** person authenticates (Discord OAuth / person registry) → creates listing → status draft → activates.
2. **Find:** hirer searches (skill/availability) → sees listing + identity signal + "meet" action.
3. **Meet:** hirer requests meeting → auto-auth one-click Universe room (north-star infra) → both parties meet. Meeting = the transaction unit at V1.
4. **Close/feedback (V2):** optional banana settlement + outcome evidence (feeds KPI/ledger, mirrors issue-marketplace claim→verify→close discipline).

## 6. Integration points (existing infra, no new systems at V1)

| Piece | What it gives |
|---|---|
| Person registry (studenthub-mcp `person` tables, PR #2) | one identity per lister; source/trust columns; dedup before fill |
| Discord OAuth (task 2) | identity anchor + guided onboarding + DMs |
| StudentHub MCP (read layer) | recruitment data, resolve_person, capability-scoped access |
| Universe meetings infra | the meetup surface — one-click, auto-auth |
| Universe bots (recursive/MCP) | a marketplace bot can surface listings in-world |
| Banana ledger + rate card (V2) | earning/settlement, khalid-set rates |
| PostHog/Sentry (existing observability) | funnel: list → find → meet → (V2) close |

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| 2-sided liquidity (the known failure mode) | V1 is cheap: no rails, no fee — validates supply first; staged build |
| Fake/duplicate listings | identity anchor (person registry), verified Discord linkage, micro-dedup fails closed |
| Scope creep into payments | hard boundary: money = Phase C legal + khalid approval; nothing in V1 touches it |
| Spam/quality | status lifecycle, availability controls; reputation deferred to identity + meeting history |
| Listing data drift | listings key to registry `person_id` (surrogate PK), additive tables only |

## 8. Open questions (for fleet consensus, then khalid)

1. Where does the V1 surface live first — StudentHub web, Universe front door, or both (Discord-first)?
2. Listing moderation: self-serve with flags, or bot-assisted review (marketplace bot)?
3. Rate basis at V1: free-form text only, or structured rate_basis enum for future V2 pricing?
4. Does "meet" require both parties to have Universe accounts at V1 (north-star nudge), or allow external contact fallback?
5. KPI at V1: list → find → meet funnel, measured via PostHog (instrument before incentivize).

## 9. Decision cards

| Card | Ask | Risk if ignored |
|---|---|---|
| MARKETPLACE-V1-SURFACE | Approve V1 scope + first surface (design only, no code) | Design stays abstract; no validation of supply |
| MARKETPLACE-LEGAL-GATE | Confirm: any V2/V3 money shape triggers Phase C legal review before build | Un-gated payments later = the exposure Phase C exists to prevent |

*Drafted by hermes-local 2026-08-12. Q3 consensus: brick ✅, hermes-local ✅, zero ✅ (via brick relay), khalid approved. This is design only — no implementation without khalid's go on the decision cards.*
