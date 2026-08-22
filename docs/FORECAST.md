# FORECAST — next 8h (machine-computed 2026-08-22T05:10)

- **Measured rate** (60s live sample): **12.0 samples/hr** (n 126->127)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~181 samples**
- Training cycles in window: **3**
  - cycle at 0.98h: train on 127 samples (0.98h)
  - cycle at 3.79h: train on 147 samples (1.14h)
  - cycle at 6.75h: train on 167 samples (1.29h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
