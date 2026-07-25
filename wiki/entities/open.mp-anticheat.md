---
title: open.mp-anticheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ricardoofnl__open.mp-anticheat.md
updated: 2026-07-24
confidence: medium
---

# open.mp-anticheat

Native open.mp server component (C++) that detects client-side cheats and mods by having the client read its own memory and comparing results against known signatures. Modular detectors cover memory signatures, client-version whitelisting, poison checks, mobile clients, RakNet packet inspection, and spoofers such as Faker5 and SCC-style clientcheck bypasses, targeting tools like s0beit, CLEO, MoonLoader, SilentAim, and similar mods. (source: wiki/sources/descriptions/ricardoofnl__open.mp-anticheat.md)

Builds as a 32-bit shared library with CMake against the open.mp SDK; ships a configurable `anticheat.cfg` for log-only mode and per-cheat ignore/warn/kick/ban actions, and optionally exposes Pawn natives plus an `OnPlayerCheatDetected` callback for gamemode integration. Aimed at open.mp and SA-MP server operators protecting their own multiplayer servers, in the same lightweight server/host AC lane as [[wellsanticheat]] rather than kernel products such as [[easy-anti-cheat]] or [[vanguard]].

## Links

- Repo: https://github.com/ricardoofnl/open.mp-anticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[wellsanticheat]] · [[certael]] · [[magnetite]]
