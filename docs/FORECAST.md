# FORECAST — next 8h (machine-computed 2026-08-22T13:05)

- **Measured rate** (60s live sample): **0.0 samples/hr** (n 241->241)
- **Training model**: 12 epochs, batch 4, 34.8s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~241 samples**
- Training cycles in window: **1**
  - cycle at 6.99h: train on 241 samples (6.99h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
