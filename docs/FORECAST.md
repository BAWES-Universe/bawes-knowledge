# FORECAST — next 8h (machine-computed 2026-08-22T07:05)

- **Measured rate** (60s live sample): **36.0 samples/hr** (n 160->163)
- **Training model**: 12 epochs, batch 4, 9.3s/step (measured cycle-2: 108 steps / 1005s)
- **Trigger**: every +20 samples since last train

## Projected (deterministic given measured rate)
- Dataset at t=8h: **~235 samples**
- Training cycles in window: **4**
  - cycle at 1.26h: train on 163 samples (1.26h)
  - cycle at 3.24h: train on 183 samples (1.42h)
  - cycle at 5.37h: train on 203 samples (1.57h)
  - cycle at 7.65h: train on 223 samples (1.73h)
- Last cycle finishes with lane restart + counter reset; generation resumes after each.
- Variance source: the rate itself (measured hourly; forecast recomputes each run).
