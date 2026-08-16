---
title: gvmp-anticheat
kind: entity
topics: [anti-cheat, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/divodeuxsevres__gvmp-anticheat.md
updated: 2026-08-16
confidence: medium
---

# gvmp-anticheat

**User-mode C++ anti-cheat for GTA V multiplayer (GVMP)** — built for the German roleplay server [GVMP.de](https://gvmp.de) and integrated with the **alt:V** multiplayer framework. Implements cheat detection, player tracking, and security monitoring via **ENet** networking and **DirectX** rendering hooks. Uses pattern scanning, **MinHook**-based function interception, process integrity checks, and a **CMake** build system. Useful for game server operators and anti-cheat engineers studying client-side cheat detection in GTA V multiplayer environments. (source: wiki/sources/descriptions/divodeuxsevres__gvmp-anticheat.md)

Distinct from the gmh5225 [[alt-v-anticheat-guide]] (documentation) and offensive ScriptHookV mod-menu samples such as [[phake]]; this is a **production client-side AC reference implementation** for alt:V rather than a cheat or kernel driver.

## Links

- Repo: https://github.com/divodeuxsevres/gvmp-anticheat

## Related

[[alt-v-anticheat-guide]] · [[open.mp-anticheat]] · [[mtasa-blue]] · [[present-hook]] · [[ntminhook]] · [[phake]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
