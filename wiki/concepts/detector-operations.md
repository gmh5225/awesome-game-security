---
title: Detector Operations
kind: concept
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md
updated: 2026-09-09
confidence: high
---

# Detector Operations

Operational concerns for **running detectors in production**: service health, shadow/canary evaluation, rollout/recovery, and separating collector faults from misconduct attribution. Pair with [[research-rigor]] when a detector hit becomes an enforcement recommendation. (source: wiki/sources/skills/anti-cheat.md)

## Deployment lifecycle

1. **Shadow / canary** — run new rules without punitive action; measure prevalence, FPR/FNR, precision, recall, calibration, and expected review volume on representative held-out data.
2. **Rollout** — segment by game mode, patch, platform, input method, and population slices; report confidence intervals, not uncalibrated scores in `[0, 1]`.
3. **Recovery** — preserve counterevidence and appeal paths; use human review or independently trusted evidence before high-impact punitive action when false positives remain plausible.

## Collector health vs misconduct

Diagnose the observation path first:

- Heartbeat timing anomalies may reflect scheduling, transport, collector, or backend faults—not cheating.
- Apply documented **access-continuity policy** separately from misconduct attribution; heartbeat failure alone does not establish sanction grounds.
- Service faults, missing uploaded fields, and detector pipeline errors are operational incidents until corroborated by independent signals.

## Joint error measurement

- Combine **causally distinct** signals; correlated detectors can fail together.
- Maximum-score aggregation or a fixed signal count does not guarantee a lower false-positive rate—measure joint error on held-out populations.
- Retrain periodically when adversaries adapt; validate session-level aggregation for cross-session dependence and drift.

Production server plugins such as [[anticheatsystem]] aggregate modular analyzer hits into JSON-configured suspicion scores before log/report/ban escalation via shared admin APIs—tune thresholds and module weights with shadow/canary runs before enabling automatic sanctions. (source: wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md)

## Related

[[research-rigor]] · [[input-provenance]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]
