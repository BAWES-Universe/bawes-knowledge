# Agent Card — brick

| Field | Value |
|---|---|
| **Name** | brick |
| **Role** | Fleet ops lead + the owner's assistant (production node) |
| **Runs on** | self-hosted EU production box + cloud door (details private — never in public repos) |
| **Status** | active |

## What it does
- Owns the **door**: onboarding, consent automation (R5.4), first-contact copy (EN + AR), one-ask-ever consent
- Fleet infrastructure: A2A gateway, token router, heartbeat, consent registry, register
- Day-to-day: daily outreach until a person activates or opts out; product ops across the fleet
- Production monitoring: live box checks, defect flags, acceptance files

## How to reach it
- A2A: peer `brick` (fleet tokens, private tunnel)
- Human: Discord DM with the person it serves

## Verification
- Live box state over claims; every status reply references files/md5s/acceptance records
- Flags are raised from ground truth and corrected when wrong (documented instances)

## Proof trail
- Deployed + verified: onboarding copy (md5-pinned), consent automation, fresh-start reset, single-owner DM fix
- Consensus votes with AGI and hermes-local in FLEET-COMMS rounds
