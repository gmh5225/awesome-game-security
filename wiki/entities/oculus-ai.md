---
title: OculusAI
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gobgolaxi__OculusAI.md
  - wiki/sources/README-categories.md
updated: 2026-11-28
confidence: medium
---

# OculusAI

**OculusAI** (gobgolaxi/OculusAI) is a **server-side** Minecraft Java anti-cheat **plugin** for **Paper** and **Folia**. It scores suspicious **PvP aim** movement and **end-crystal** combat with **machine-learning** models, alongside classical wall and hitbox validation. The stack is primarily **Java**, built with **Gradle**, and integrates **ProtocolLib** plus a **hosted OculusAI API** for server linking, dashboards, and optional cloud-backed updates. (source: wiki/sources/descriptions/gobgolaxi__OculusAI.md)

## Detection and enforcement

- **Neural checks** — probabilistic aim and crystal-combat scoring rather than purely rule-based thresholds alone.
- **Classical combat checks** — wall and hitbox validation layered with ML outputs.
- **Suspicion buffers** — per-player rolling suspicion with separate **alert** and **punishment** thresholds.

## Operator tooling

- **Staff workflows** — live monitoring, in-game configuration menus, journals, and bypass controls.
- **Evidence** — browser-viewable punishment replays with short combat recordings via the API.
- **Research** — dataset-collection tooling and NPC or arena test setups for training and evaluation.

Targets multiplayer server operators and anti-cheat practitioners who want **probabilistic** cheat detection on authoritative Java servers—same **hosted-API + on-server feature extraction** lane as [[mkac]], with embedded on-server models such as [[powerac]], [[wepac]], and [[mlanticheat]] as alternatives that avoid cloud inference.

## Links

- Repo: https://github.com/gobgolaxi/OculusAI

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[mkac]] · [[eigen-anticheat]] · [[paiac]] · [[minecraft-anticheatai]]