---
title: gd-internal
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__gd-internal.md
updated: 2026-08-08
confidence: medium
---

# gd-internal

**Geometry Dash internal cheat** (C++) with an in-process Dear ImGui menu. The custom UI font is **Comfortaa**, loaded into memory from `menu.cpp`; game **signatures** for hooking and offset resolution live in `hookmgr.cpp` (the maintainer notes the game is unlikely to receive further updates, so those patterns may remain stable). Useful for game security researchers and reverse engineers studying offensive techniques in the cheat / **game:geometry dash** lane — internal hook management, signature-based targeting, and ImGui menu wiring. (source: wiki/sources/descriptions/gmh5225__gd-internal.md)

Sits beside rhythm-game samples such as [[osu-aac]] and [[maniac]] (osu! lane) as a title-specific **internal** scaffold rather than external memory tooling.

## Links

- Repo: https://github.com/gmh5225/gd-internal

## Related

[[imgui]] · [[present-hook]] · [[osu-aac]] · [[maniac]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
