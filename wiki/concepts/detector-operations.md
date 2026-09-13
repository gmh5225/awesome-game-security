---
title: Detector Operations
kind: concept
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md
  - wiki/sources/descriptions/modcommunity__dot-server-security.md
updated: 2026-09-13
confidence: high
---

# Detector Operations

Operational concerns for **running detectors in production**: service health, shadow/canary evaluation, rollout/recovery, and separating collector faults from misconduct attribution. Pair with [[research-rigor]] when a detector hit becomes an enforcement recommendation. (source: wiki/sources/skills/anti-cheat.md)

## State separation

| State | Record | Do not infer |
|-------|--------|--------------|
| Collector/service health | Version, restart, resource pressure, queue/pipeline errors | Player misconduct or innocence |
| Evidence validity | Source, coverage, delay, missing/duplicate records, schema compatibility | Missing data equals a measured zero |
| Detector execution | Evaluated/not-evaluated, rule/model version, assumptions, result | A score alone authorizes a sanction |
| Decision state | Evidence, policy version, actor, review/correction history | Infrastructure error is behavioral evidence |

Represent evidence as available, delayed, partial, invalid, unsupported, or not-collected; record evaluated/not-evaluated separately. Access continuity, authentication requirements, and sanctions need separately documented policies. (source: wiki/sources/skills/anti-cheat.md)

## Deployment lifecycle

1. **Shadow / canary** — run new rules without punitive action; measure prevalence, FPR/FNR, precision, recall, calibration, and expected review volume on representative held-out data.
2. **Rollout** — segment by game mode, patch, platform, input method, and population slices; report confidence intervals, not uncalibrated scores in `[0, 1]`.
3. **Recovery** — preserve counterevidence and appeal paths; use human review or independently trusted evidence before high-impact punitive action when false positives remain plausible.

## Collector health vs misconduct

Diagnose the observation path first:

- Heartbeat timing anomalies may reflect scheduling, transport, collector, or backend faults—not cheating.
- Apply documented **access-continuity policy** separately from misconduct attribution; heartbeat failure alone does not establish sanction grounds.
- Service faults, missing uploaded fields, and detector pipeline errors are operational incidents until corroborated by independent signals.

## Time domains

Distinguish source-event time, collector observation, server receipt, and decision time. Record expected/observed coverage window, delay budget, clock uncertainty, duplicates, ordering, and source of missingness. Compare anomalies by region, platform, collector version, and rollout cohort—simultaneous gaps support shared-failure investigation but do not settle root cause; a healthy collector is not proof that every client-origin field is true. (source: wiki/sources/skills/anti-cheat.md)

## Joint error measurement

- Combine **causally distinct** signals; correlated detectors can fail together.
- Maximum-score aggregation or a fixed signal count does not guarantee a lower false-positive rate—measure joint error on held-out populations.
- Retrain periodically when adversaries adapt; validate session-level aggregation for cross-session dependence and drift.

Production server plugins such as [[anticheatsystem]] aggregate modular analyzer hits into JSON-configured suspicion scores before log/report/ban escalation via shared admin APIs—tune thresholds and module weights with shadow/canary runs before enabling automatic sanctions. (source: wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md) Godot dedicated-server addons such as [[dot-server-security]] ship **dry-run by default**, logging rule hits and escalation ladders (warn/gag/mute/kick/ban) without punitive action until operators finish auditing configuration. (source: wiki/sources/descriptions/modcommunity__dot-server-security.md)

## Related

[[research-rigor]] · [[input-provenance]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]
