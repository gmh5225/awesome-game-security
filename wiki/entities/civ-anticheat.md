---
title: CivAnticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/msc1488__CivAnticheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-11
confidence: medium
---

# CivAnticheat (AntiCheatAI)

**CivAnticheat** (msc1488/CivAnticheat; marketed as **AntiCheatAI**) is a **Paper 1.21+** Minecraft server plugin that combines live anti-cheat detection with optional gameplay telemetry recording for training and monitoring. It is implemented in **Java 21** with Maven and the Paper API. (source: wiki/sources/descriptions/msc1488__CivAnticheat.md)

## Detection stack

- **Rule-based checks** — aim snap, attack rate, reach, and related deterministic combat/movement signals.
- **Adaptive local anomaly model** — learns each player’s movement and rotation baseline and scores suspicion via **z-score** comparison on-server (not a remote LLM or external inference API).
- **Enforcement** — suspicious players can trigger admin alerts and delayed kicks.
- **Per-viewer ESP masking** — hides other players from a given observer when ray tracing shows they should not be visible, targeting ESP-style cheating.

## Operator tooling

In-game commands support train sessions, player watch, status inspection, and **CSV telemetry export** under the plugin data folder. Behavior is tuned through **YAML** configuration.

Targets Minecraft server administrators and researchers studying server-side game security and practical anti-cheat design on Paper—same authoritative Java-server operator lane as [[mlanticheat]] and [[minecraft-anticheatai]], with on-server adaptive scoring distinct from cloud-inference plugins such as [[guardac]] and [[shard]].

## Links

- Repo: https://github.com/msc1488/CivAnticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[minecraft-anticheat-list]] · [[grim]] · [[minecraft-anti-cheat]] · [[thorium-minecraft-plugin]]
