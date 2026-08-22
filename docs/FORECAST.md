# FORECAST — next 8h (machine-computed 2026-08-22T14:05)

- **Measured rate** (60s live sample): **107.9 samples/hr** (n 251->260)
- **Training model**: 12 epochs, batch 4, 34.8s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~280 samples**
- Training cycles in window: **2**
  - cycle at 7.54h: train on 260 samples (7.54h)
  - cycle at 15.85h: train on 280 samples (8.12h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
