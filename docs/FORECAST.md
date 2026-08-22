# FORECAST — next 8h (machine-computed 2026-08-22T11:05)

- **Measured rate** (60s live sample): **24.0 samples/hr** (n 219->221)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~278 samples**
- Training cycles in window: **3**
  - cycle at 1.71h: train on 221 samples (1.71h)
  - cycle at 4.41h: train on 241 samples (1.87h)
  - cycle at 7.27h: train on 261 samples (2.02h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
