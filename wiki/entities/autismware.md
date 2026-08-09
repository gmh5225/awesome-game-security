---
title: autismware
kind: entity
topics: [game-hacking, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__autismware.md
updated: 2026-08-09
confidence: medium
---

# autismware

C++ internal CS:GO cheat that hooks the Source engine in-process via interface capture and VMT hooking. Implements ESP, aimbot, backtrack, skin changer, and miscellaneous gameplay modifications with an ImGui configuration menu—the standard CS:GO internal cheat feature stack. Aimed at game-security researchers studying Source engine cheat feature implementation. (source: wiki/sources/descriptions/gmh5225__autismware.md)

README tags it `[HvH]`. Treat as a feature-complete internal sample for studying typical Source 1 hook and menu patterns.

## Hooking model

| Mechanism | Role |
|-----------|------|
| Interface capture | Resolve Source exports (`IVEngineClient`, entity list, etc.) via CreateInterface |
| VMT hooking | Intercept virtual methods on engine/client interfaces |
| ImGui menu | In-game configuration UI for feature toggles |

Compare [[aqhax-csgo]] and [[csgo-kns]] for comparable VMT-hook feature stacks and [[csgo-internal-base]] for a teaching-oriented scaffold.

## Links

- Repo: https://github.com/gmh5225/autismware

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[aqhax-csgo]] · [[csgo-internal-base]] · [[csgo-kns]] · [[csgosimple]] · [[legit-csgo-cheat-menu]] · [[vac3-inhibitor]]
