# FORECAST — next 8h (machine-computed 2026-08-22T12:05)

- **Measured rate** (60s live sample): **36.0 samples/hr** (n 238->241)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~301 samples**
- Training cycles in window: **4**
  - cycle at 1.87h: train on 241 samples (1.87h)
  - cycle at 4.45h: train on 261 samples (2.02h)
  - cycle at 7.18h: train on 281 samples (2.18h)
  - cycle at 10.07h: train on 301 samples (2.33h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
