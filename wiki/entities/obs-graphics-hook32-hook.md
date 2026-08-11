---
title: OBS Graphics Hook32 Hook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md
updated: 2026-08-11
confidence: low
---

# OBS Graphics Hook32 Hook

gmh5225 C++ sample focused on **OBS graphics-hook** interception—the 32-bit (`hook32`) variant of OBS Studio's in-process Game Capture inject path. The technique replaces a function pointer ("the old way") to hook OBS's graphics-hook layer for overlay or frame-export research rather than building a standalone Present vtable hook from scratch. Useful for game security researchers and reverse engineers studying offensive cheat/overlay techniques adjacent to legitimate OBS Game Capture. (source: wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md)

## Links

- Repo: https://github.com/gmh5225/OBS-graphics-hook32-Hook

## Related

[[obs-game-capture]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
