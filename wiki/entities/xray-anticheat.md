---
title: XRay AntiCheat
kind: entity
topics: [anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/LB45440078L__xray-anticheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-09
confidence: medium
---

# XRay AntiCheat

**Statistical anti-cheat plugin** for **Paper/Spigot Minecraft** servers (LB45440078L/xray-anticheat). Detects ore-vision and X-Ray style cheating by comparing legitimate mining behavior to ore-informed mining, accumulating **likelihood-ratio evidence** with explainable verdicts rather than simple block-count thresholds. (source: wiki/sources/descriptions/LB45440078L__xray-anticheat.md)

## Capabilities

| Area | Coverage |
|------|----------|
| Signals | Buried vs exposed ore discoveries, tunnel geometry, targeting patterns, inter-discovery timing |
| Evidence | Verdicts with confidence scores and plain-language breakdowns for staff |
| History | Decaying player history so old mining patterns fade from active suspicion |
| Staff UX | In-game commands, GUI, embedded web administration panel |
| Enforcement | Optional ban-wave planning; **human review first** by default (no automatic bans unless configured) |

## Architecture

| Layer | Role |
|-------|------|
| **Analytical core** | Minecraft-free Java module implementing likelihood-ratio models |
| **Persistence** | JDBC-backed storage for mining telemetry and case history |
| **Web admin** | Embedded panel for remote review and configuration |
| **Spigot plugin** | Listens to mining events on the game server and feeds the engine |

Maven multi-module layout keeps detection logic testable outside the live server process.

## Positioning

Listed under **Anti Cheat → Open Source Anti Cheat System** / **game:minecraft**. Complements mining research benches such as [[jevcraft-bench]] (shadow-mode heuristic benchmarking) with production-oriented statistical ore-vision detection and moderator workflows.

## Links

- Repo: https://github.com/LB45440078L/xray-anticheat

## Related

[[jevcraft-bench]] · [[minecraft-anticheat-list]] · [[detector-operations]] · [[research-rigor]] · [[overviews/anti-cheat]]
