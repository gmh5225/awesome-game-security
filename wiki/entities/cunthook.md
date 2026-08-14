---
title: Cunthook
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__Cunthook.md
updated: 2026-08-14
confidence: medium
---

# Cunthook

Open-source **game hacking framework** (gmh5225) targeting **Team Fortress 2** and other **Source engine** titles. Ships a full in-process SDK with hooks, ESP, aimbot, and assorted gameplay modifications built on the engine's internal interfaces and Boost libraries. README tags it `[Linux]`. (source: wiki/sources/descriptions/gmh5225__Cunthook.md)

Feature-complete TF2/Source 1 internal beside hook-focused starters such as [[teamfortress2-internal]], SE-Owned–lineage samples such as [[fedoraware]], and other Source internals ([[l4d2-cheat]], [[csgo-internal-base]]).

## Hooking model

| Mechanism | Role |
|-----------|------|
| Source engine SDK | Class layouts, netvars, and CreateInterface exports for in-process reads |
| Internal interface hooks | Intercept engine/client virtual methods for ESP, aimbot, and gameplay mods |
| Boost libraries | Supporting C++ infrastructure in the framework tree |

## Links

- Repo: https://github.com/gmh5225/Cunthook

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-engine]] · [[source-netvars]] · [[teamfortress2-internal]] · [[fedoraware]] · [[l4d2-cheat]] · [[csgo-internal-base]] · [[sdk]]
