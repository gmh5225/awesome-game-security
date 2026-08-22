---
title: React
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/g4vrk__React.md
updated: 2026-08-22
confidence: medium
---

# React

Aim-focused anti-cheat plugin for Minecraft **Paper** and **Folia** servers. Written in Java, it analyzes player rotation patterns to judge whether aiming behavior is physically plausible. Local heuristic checks use GCD-error scoring, acceleration-delta tracking, and mode-averaged rotation quantization instead of brittle static thresholds. An optional machine-learning verdict layer can batch rotation samples to a separate inference service for confidence-scored aimbot detection, while the core plugin remains fully standalone. Configurable checks, streak-based violation buffering with decay, async packet processing via **PacketEvents**, and staff alerts rather than automatic bans round out the operator workflow. Targets server operators who need specialized combat aim protection for PvP environments. (source: wiki/sources/descriptions/g4vrk__React.md)

## Detection stack

GCD-error scoring, acceleration-delta tracking, and mode-averaged rotation quantization for physically plausible aim analysis; optional separate ML inference service for confidence-scored aimbot verdicts; streak-based violation buffering with decay; async PacketEvents packet processing; staff alerts without automatic bans.

## Links

- Repo: https://github.com/g4vrk/React

## Related

[[guardac]] · [[mlanticheat]] · [[minecraft-anti-cheat]] · [[minecraft-anticheatai]] · [[arrow-anticheat]] · [[windfall-anticheat]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
