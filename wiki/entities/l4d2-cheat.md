---
title: L4D2 Cheat
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__L4D2-Cheat.md
updated: 2026-08-12
confidence: medium
---

# L4D2 Cheat

Internal **Left 4 Dead 2** cheat (gmh5225) built on the Source engine SDK. Provides ESP, aimbot, and gameplay modifications through VMT hooking and engine interface exploitation in the Valve Source engine. README tags it `[Linux]`. (source: wiki/sources/descriptions/gmh5225__L4D2-Cheat.md)

Feature-complete L4D2 internal sample beside starter scaffolds such as [[l4d2-basic]] and other Source 1 internals ([[teamfortress2-internal]], [[csgo-internal-base]]).

## Hooking model

| Mechanism | Role |
|-----------|------|
| Engine interface exploitation | Resolve Source exports (`IVEngineClient`, entity list, etc.) via CreateInterface |
| VMT hooking | Intercept virtual methods on engine/client interfaces |
| Source engine SDK | In-process reads and gameplay feature modules (ESP, aimbot, mods) |

## Links

- Repo: https://github.com/gmh5225/L4D2-Cheat

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-engine]] · [[l4d2-basic]] · [[teamfortress2-internal]] · [[csgo-internal-base]] · [[source-netvars]] · [[sourceengineexplorer]]
