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

**Fabric** client mod for Minecraft **1.21.11** that helps developers **observe, visualize, log, and safely simulate** anti-cheat behavior without providing gameplay cheats or bypasses. Java + Fabric API + mixins; modular ClickGUI and HUD monitors for reach, movement, rotation, CPS, velocity, ping, FPS, and tick timing; visualization tools (ESP, tracers, nametags, fullbright, FreeCam). QA modules include a dashboard overview, a **test simulator** for local detection-event logging, and a **Y-Level Probe** counting client-visible blocks, chests, and entities below Y=0 to verify server-side data stripping. Aimed at server operators and anti-cheat engineers validating that server protections work as intended. (source: wiki/sources/descriptions/u8012146108-bit__anticheat-qa.md)

Complements headless protocol stress tools such as [[ghostjoin]] and server-side plugins indexed by [[minecraft-anticheat-list]] in the Anti Cheat **Stress Testing** lane.

## Links

- Repo: https://github.com/u8012146108-bit/anticheat-qa

## Related

[[ghostjoin]] · [[minecraft-anticheat-list]] · [[cheatcheck]] · [[grim]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
