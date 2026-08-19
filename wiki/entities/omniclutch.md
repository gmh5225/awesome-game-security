---
title: OmniClutch
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/WeiNaYongQ__OmniClutch.md
updated: 2026-08-19
confidence: medium
---

# OmniClutch

Lightweight **Fabric** client mod for **Minecraft Java Edition 1.21+** that automatically performs clutch maneuvers to prevent lethal fall damage. During free fall it monitors the player, uses downward raycasts to detect imminent impact, and selects an appropriate clutch item from the hotbar—water buckets, boats, hay bales, or slime blocks. A client-side state machine drives placement with configurable **Gaussian reaction delays** and smooth camera rotation interpolation to mimic human input and reduce anti-cheat detection. Targets survival and PvP scenarios where manual clutching is too slow. (source: wiki/sources/descriptions/WeiNaYongQ__OmniClutch.md)

## Architecture

| Component | Role |
|-----------|------|
| Free-fall monitor | Tracks player state during descent |
| Downward raycasts | Detects imminent ground impact |
| Hotbar item selector | Chooses water, boat, hay bale, or slime block clutch |
| Client-side FSM | Orchestrates placement timing and camera motion |
| Gaussian delays + camera interpolation | Human-like reaction timing and look-vector smoothing |

## Links

- Repo: https://github.com/WeiNaYongQ/OmniClutch

## Related

[[lenrete-mod]] · [[eafe]] · [[windfall-anticheatf]] · [[seiun-ac]] · [[local-anticheat-1-8-9]] · [[phantom-client]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
