---
title: goesp
kind: entity
topics: [game-hacking, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/danielkrupinski__GOESP.md
updated: 2026-08-16
confidence: medium
---

# goesp

Cross-platform **CS:GO ESP** research sample from danielkrupinski. Modern C++ with a **Dear ImGui** overlay: reads entity data via memory access and draws player boxes, names, health, and weapons through the **game's own rendering pipeline** rather than a separate transparent window. Supports **Windows and Linux**, illustrating external overlay rendering on both platforms. Aimed at game-security researchers studying ESP implementation patterns and overlay-based cheat detection—not a production cheat guide. (source: wiki/sources/descriptions/danielkrupinski__GOESP.md)

README-tagged `[Cross-platform]`. Pairs with the same author's internal reference [[osiris]] for contrasting in-process vs external ESP overlay lanes on Source 1.

## Architecture highlights

| Component | Role |
|-----------|------|
| Memory access | Out-of-process reads of CS:GO entity state |
| Dear ImGui | Overlay UI and ESP draw substrate |
| Game render path | ESP drawn via the target game's rendering pipeline |
| Platform | Windows and Linux external overlay samples |

See [[csgo-external-esp]] and [[csgo-external-cheat]] for comparable external CS:GO baselines; [[gamesneeze]] and [[csgo-linux-cheat-sdk]] for other Linux CS:GO offensive lanes.

## Links

- Repo: https://github.com/danielkrupinski/GOESP

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[osiris]] · [[csgo-external-esp]] · [[csgo-external-cheat]] · [[present-hook]] · [[world-to-screen]] · [[gamesneeze]] · [[csgo-linux-cheat-sdk]]
