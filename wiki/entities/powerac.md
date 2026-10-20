---
title: PowerAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/katze225__PowerAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: medium
---

# PowerAC

**PowerAC** (katze225/PowerAC) is an open-source **Paper/Spigot** server plugin (Folia-compatible scheduling) focused on **aimbot modules and aim-assist** style combat cheats. A bundled **convolutional neural network** runs entirely inside the plugin, analyzing player rotation telemetry in fixed windows without an external inference service or license server. Operators can collect labeled samples via in-game training commands and retrain asynchronously; packet listeners track movement and rotations; staff tooling covers violation logs, monitoring, and optional **Discord webhook** alerts. A small public API exposes player snapshots and detection events for integration with other plugins. (source: wiki/sources/descriptions/katze225__PowerAC.md)

Self-hosted embedded ML on the authoritative server—beside remote-engine plugins such as [[eigen-anticheat]] and [[thorium-minecraft-plugin]], ONNX scaffold plugins such as [[minecraft-anticheatai]], and per-server ensemble trainers such as [[mlanticheat]]. Operational patterns: [[detector-operations]] · [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/katze225/PowerAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[eigen-anticheat]] · [[minecraft-anticheatai]] · [[mlanticheat]] · [[minecraft-anticheat-list]] · [[ai-aimbot-detection]] · [[detector-operations]]
