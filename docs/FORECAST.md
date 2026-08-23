# FORECAST — next 8h (machine-computed 2026-08-23T07:05)

- **Measured rate** (60s live sample): **0.0 samples/hr** (n 333->333)
- **Training model**: 12 epochs, batch 4, 34.8s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~333 samples**
- Training cycles in window: **1**
  - cycle at 9.66h: train on 333 samples (9.66h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
