---
title: OBS Hook
kind: entity
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__OBS-Hook.md
updated: 2026-08-11
confidence: low
---

# OBS Hook

gmh5225 research sample that hooks into **OBS Studio's graphics capture system** to render custom overlays through OBS's trusted rendering pipeline. By hijacking OBS's Game Capture hook DLL, custom draw calls can be injected into the captured game's frame without creating a separate overlay window—exploiting OBS's commonly whitelisted status in anti-cheat systems. Aimed at game security researchers studying overlay rendering via trusted-application hijacking rather than a standalone Present vtable hook. (source: wiki/sources/descriptions/gmh5225__OBS-Hook.md)

## Links

- Repo: https://github.com/gmh5225/OBS-Hook

## Related

[[obs-game-capture]] · [[obs-graphics-hook32-hook]] · [[present-hook]] · [[nvidia-overlay-hijack]] · [[discord-overlay-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
