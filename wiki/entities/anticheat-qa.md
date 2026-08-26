---
title: AntiCheat QA
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/u8012146108-bit__anticheat-qa.md
  - wiki/sources/README-categories.md
updated: 2026-08-26
confidence: medium
---

# AntiCheat QA

**Fabric** client mod for Minecraft **1.21.11** that helps developers **observe, visualize, log, and safely simulate** anti-cheat behavior without providing gameplay cheats or bypasses. Java + Fabric API + mixins; modular ClickGUI and HUD overlay. Aimed at server operators and anti-cheat engineers validating that server protections work as intended. (source: wiki/sources/descriptions/u8012146108-bit__anticheat-qa.md)

## HUD monitors

Reach, movement, rotation, CPS, velocity, ping, FPS, and tick timing — live metrics for comparing client-side signals against server AC thresholds.

## Visualization

ESP, tracers, nametags, fullbright, and FreeCam for inspecting world/entity state during QA sessions (observation-only; not cheat modules).

## QA modules

- **Dashboard overview** — consolidated AC-relevant client metrics.
- **Test simulator** — local detection-event logging for safe offline or authorized-server simulation.
- **Y-Level Probe** — counts client-visible blocks, chests, and entities below Y=0 to verify server-side data stripping (e.g. anti-xray chunk hiding).

Complements headless protocol stress tools such as [[ghostjoin]] and server-side plugins indexed by [[minecraft-anticheat-list]] in the Anti Cheat **Stress Testing** lane.

## Links

- Repo: https://github.com/u8012146108-bit/anticheat-qa

## Related

[[ghostjoin]] · [[local-anticheat-1-8-9]] · [[minecraft-anticheat-list]] · [[cheatcheck]] · [[grim]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
