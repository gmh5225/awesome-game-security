---
title: player-simulation (Fairplay Telemetry)
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/ArghadeepMisra__player-simulation.md
updated: 2026-11-19
confidence: medium
---

# player-simulation (Fairplay Telemetry)

**Fairplay Telemetry** (`player-simulation`, ArghadeepMisra) is a **Maven multi-module Java** stack for end-to-end, real-time anti-cheat analysis over high-volume gameplay telemetry. A simulator synthesizes a large player population (README cites on the order of **~1,000** concurrent actors) and emits thousands of match events per second, including **seeded cheaters**, plus manifests and **ground truth** for honest detector evaluation. Events publish to **Kafka**; replicated **Kafka Streams** detector instances apply **hopping-window** rules to flag **aimbot** and **speedhack** patterns, emit scored evidence, and track per-player sequence integrity to exercise **exactly-once** processing under failure. An optional **verifier** compares stream counts and detection output against simulator ground truth; **Docker Compose**, **Prometheus**, and **Grafana** support local benchmarking and chaos testing—useful before wiring streaming cheat detection into a live title platform. (source: wiki/sources/descriptions/ArghadeepMisra__player-simulation.md)

## Modules

| Piece | Role |
|-------|------|
| Simulator | High-rate synthetic match telemetry + cheat seeds + ground-truth manifests |
| Kafka + Streams detector | Hopping-window aimbot/speedhack rules; scored evidence; sequence-integrity / exactly-once demo |
| Verifier (optional) | Ground-truth reconciliation vs detector output and stream counts |
| Ops | Docker Compose, Prometheus, Grafana for bench and chaos |

## Catalog

README **Anti Cheat** — Fairplay Kafka Streams telemetry lab (simulated players, aimbot/speedhack flags, exactly-once verifier). (source: wiki/sources/descriptions/ArghadeepMisra__player-simulation.md)

## Links

- Repo: https://github.com/ArghadeepMisra/player-simulation

## Related

[[gamerfield-backend]] · [[adaptive-anti-cheat-stream-processor]] · [[anticheat-engine]] · [[cs2-anti-cheat-ml-research]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[overviews/anti-cheat]]