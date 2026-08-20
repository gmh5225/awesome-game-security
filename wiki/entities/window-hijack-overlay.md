---
title: Window-Hijack (SurgeGotTappedAgain)
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/SurgeGotTappedAgain__Window-Hijack.md
updated: 2026-08-20
confidence: medium
---

# Window-Hijack (SurgeGotTappedAgain)

C++ proof-of-concept for **external overlay window hijacking** on Windows—reusing an existing overlay window model while preserving native window flags, capturing input through **SetWindowsHookEx**, and rendering with **DirectX 11** and **ImGui** plus dedicated input-handling modules. Aimed at game-security and anti-cheat researchers studying overlay-based tooling and **visibility vs detection tradeoffs**. (source: wiki/sources/descriptions/SurgeGotTappedAgain__Window-Hijack.md)

Distinct from kernel window-handle hijack research in [[window-hijack]] (thesecretclub).

## Links

- Repo: https://github.com/SurgeGotTappedAgain/Window-Hijack

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overlay]] · [[setwindowhookex]] · [[setwindowshookex-injector]] · [[present-hook]] · [[imgui]] · [[window-hijack]]
