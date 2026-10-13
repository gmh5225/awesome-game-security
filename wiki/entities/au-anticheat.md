---
title: AU-Anticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/xav0dev__AU-Anticheat.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# AU-Anticheat

Defensive **Among Us** client plugin for **hosts and players** on the **BepInEx** **IL2CPP** Windows build. Implemented in **C#** for **.NET 6**; hooks game **networking** to validate **RPCs** and **packets**, monitor **movement** and **role** behavior, and **block or score** suspicious actions before they are applied locally. (source: wiki/sources/descriptions/xav0dev__AU-Anticheat.md)

## Host tooling

Configurable cheat detection with **point-based** kick or ban responses, **minimum lobby level** rules, **saved lobby settings** loadouts, **chat filters**, and **local moderation lists** keyed on friend codes. (source: wiki/sources/descriptions/xav0dev__AU-Anticheat.md)

## Posture

Targets community hosts and game-security practitioners who want **client-side hardening** against common Among Us exploits **without** remote telemetry, hardware fingerprinting, or third-party ban services. Complements client-side ACE such as [[among-us-anti-cheat]] and host moderation mods such as [[banmod]] and [[wellsanticheat]]. (source: wiki/sources/descriptions/xav0dev__AU-Anticheat.md)

## Links

- Repo: https://github.com/xav0dev/AU-Anticheat

## Related

[[bepinex]] · [[il2cpp]] · [[among-us-anti-cheat]] · [[banmod]] · [[wellsanticheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
