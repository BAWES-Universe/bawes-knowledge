# FORECAST — next 8h (machine-computed 2026-08-22T08:05)

- **Measured rate** (60s live sample): **12.0 samples/hr** (n 177->178)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~218 samples**
- Training cycles in window: **3**
  - cycle at 1.38h: train on 178 samples (1.38h)
  - cycle at 4.58h: train on 198 samples (1.53h)
  - cycle at 7.94h: train on 218 samples (1.69h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
