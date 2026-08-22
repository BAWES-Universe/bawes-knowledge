# FORECAST — next 8h (machine-computed 2026-08-22T10:05)

- **Measured rate** (60s live sample): **12.0 samples/hr** (n 207->208)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~248 samples**
- Training cycles in window: **3**
  - cycle at 1.61h: train on 208 samples (1.61h)
  - cycle at 5.05h: train on 228 samples (1.77h)
  - cycle at 8.64h: train on 248 samples (1.92h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
