# Challenger retro evidence — SUMMARY (raw data excluded per repo guardrail)

## Actions reviewed: 6
| id | action (summary) | flags |
|---|---|---|
| A1 | Engine generates dataset samples every 5 minutes via a cron job, using the local | n/a |
| A2 | The propose/verify engine uses the local fine-tuned model as the generator, with | n/a |
| A3 | Fine-tuned model trained and adopted, deployed as a local lane, but no productio | n/a |
| A4 | Launch timeline estimated as: capability layer 2-4 days, instructions 08-25, pil | n/a |
| A5 | A background bridge service was deployed; it crash-looped 1273 times over an hou | n/a |
| A6 | Attestation heartbeat attests ledger rows after they are committed; nothing revi | n/a |

## Expected-vs-actual: 6 rows
- {'id': 'A1', 'action': 'Engine generates dataset samples every 5 minutes via a cron job, using the l
- {'id': 'A2', 'action': 'The propose/verify engine uses the local fine-tuned model as the generator, 
- {'id': 'A3', 'action': 'Fine-tuned model trained and adopted, deployed as a local lane, but no produ
- {'id': 'A4', 'action': 'Launch timeline estimated as: capability layer 2-4 days, instructions 08-25,
- {'id': 'A5', 'action': 'A background bridge service was deployed; it crash-looped 1273 times over an
- {'id': 'A6', 'action': 'Attestation heartbeat attests ledger rows after they are committed; nothing 

*Full raw rows are reproducible: rerun `audit/challenger.py --retro` with the ruleset in docs/DA-RULEBOOK.md — results land in /tmp, not the repo.*
