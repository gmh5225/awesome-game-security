---
title: PowerAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/katze225__PowerAC.md
  - wiki/sources/README-categories.md
updated: 2026-10-20
confidence: high
---

# PowerAC

**PowerAC** (katze225/PowerAC) is an open-source **Paper/Spigot** server plugin (**Folia-compatible** scheduling) for **Minecraft** operators who want lightweight, **self-hosted** combat cheat detection—aimbot modules and **aim-assist** style rotation cheats rather than a cloud-backed commercial AC. (source: wiki/sources/descriptions/katze225__PowerAC.md)

## Detection pipeline

- **Signal** — packet listeners track player movement and view rotations; the bundled **convolutional neural network** scores rotation telemetry in **fixed windows** entirely inside the JVM plugin (no external inference service or license server). (source: wiki/sources/descriptions/katze225__PowerAC.md)
- **Adaptation** — in-game training commands collect **labeled samples**; the rotation model **retrains asynchronously** on-server so cohort-specific aim-assist profiles can be refined without shipping telemetry to a vendor backend. (source: wiki/sources/descriptions/katze225__PowerAC.md)
- **Operations** — staff monitor detections, persist violation logs, and can route alerts through optional **Discord webhooks**; a small **public API and events** expose player snapshots and detection alerts for companion plugins. (source: wiki/sources/descriptions/katze225__PowerAC.md)

Self-hosted embedded ML on the authoritative server—beside remote-engine plugins such as [[eigen-anticheat]] and [[thorium-minecraft-plugin]], ONNX scaffold plugins such as [[minecraft-anticheatai]], and per-server ensemble trainers such as [[mlanticheat]]. Operational patterns: [[detector-operations]] · [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/katze225/PowerAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[eigen-anticheat]] · [[minecraft-anticheatai]] · [[mlanticheat]] · [[minecraft-anticheat-list]] · [[ai-aimbot-detection]] · [[detector-operations]]
