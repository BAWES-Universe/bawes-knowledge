# FORECAST — next 8h (machine-computed 2026-08-22T06:05)

- **Measured rate** (60s live sample): **24.0 samples/hr** (n 141->143)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~206 samples**
- Training cycles in window: **4**
  - cycle at 1.11h: train on 143 samples (1.11h)
  - cycle at 3.21h: train on 163 samples (1.26h)
  - cycle at 5.46h: train on 183 samples (1.42h)
  - cycle at 7.86h: train on 203 samples (1.57h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
