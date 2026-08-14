---
title: External-Dayz-Cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__External-Dayz-Cheat.md
updated: 2026-08-13
confidence: medium
---

# External-Dayz-Cheat

**DayZ external ESP cheat** (gmh5225) that runs outside the [[battleye]]-protected Enfusion client. A transparent **DirectX 9 overlay** (`Direct3DCreate9Ex`, `FindWindow`/`GetWindowRect` window tracking) draws player positions, names, health bars, and distance via **D3DXFont** and **D3DXLine** while a **kernel driver** (`Driver.h`/`Imports.h`) supplies cross-process entity memory reads. The cheat walks the game's entity list through SDK-defined offsets and projects world coordinates with [[world-to-screen]] math. (source: wiki/sources/descriptions/gmh5225__External-Dayz-Cheat.md)

Complements [[dayz-cheat]] (standard external ESP/aimbot/item ESP), [[dayzzz]] (SDK generation + overlays), and defensive server-side ML such as [[model-anti-cheat]] for comparing external overlay + driver-backed RPM patterns on DayZ/Enfusion titles.

## Links

- Repo: https://github.com/gmh5225/External-Dayz-Cheat

## Related

[[battleye]] · [[world-to-screen]] · [[present-hook]] · [[dayz-cheat]] · [[dayzzz]] · [[model-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
