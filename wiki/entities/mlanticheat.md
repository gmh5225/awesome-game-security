---
title: MLAntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gravemaulr__MLAntiCheat.md
updated: 2026-08-20
confidence: medium
---

# MLAntiCheat

Combat anti-cheat plugin for Minecraft **Paper** servers **1.21.4+**. Written in Java 21, it analyzes how players aim and fight, then scores that behavior with machine-learning models trained on data from the operator's own server. The stack combines ensemble neural and logistic models, anomaly detection, and feature extraction from combat rotations, with optional **PacketEvents** integration for more accurate packet-level rotation tracking. Operators label legitimate and cheating players during fights to build training sets, then use **Shadow Mode** to review alerts and recorded evidence before enabling punishments. Staff alerts, an admin GUI, automatic retraining from reviewed player data, configurable floating score tags, and a physical dummy for safe combat testing round out the operator workflow. Targets PvP server administrators who want adaptive, server-specific cheat detection instead of fixed rules-based anti-cheat. (source: wiki/sources/descriptions/gravemaulr__MLAntiCheat.md)

## Detection stack

Ensemble neural + logistic models and anomaly detection over combat rotation features; operator-labeled per-server training sets; Shadow Mode alert review before punishments; optional PacketEvents packet-level rotation tracking; staff alerts, admin GUI, automatic retraining, floating score tags, and combat dummy for safe testing.

## Links

- Repo: https://github.com/gravemaulr/mlanticheat

## Related

[[minecraft-anticheatai]] · [[minecraft-anti-cheat]] · [[dakotaac]] · [[antiguard]] · [[windfall-anticheat]] · [[ycbr-anticheat]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
