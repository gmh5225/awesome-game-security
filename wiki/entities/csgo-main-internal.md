---
title: CSGO-MAIN-INTERNAL
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Neaxic__CSGO-MAIN-INTERNAL.md
updated: 2026-08-22
confidence: medium
---

# CSGO-MAIN-INTERNAL

**CSGO-MAIN-INTERNAL** (Neaxic/CSGO-MAIN-INTERNAL) is an **archived internal cheat base** for **Counter-Strike: Global Offensive** on Windows. Written in **C++** and built with **Visual Studio** as an injectable **DLL**, it packages common internal modules—**ESP**, **glow**, **triggerbot**, **bunny hop**, **third-person view**, and **world-to-screen** math—with an **ImGui** menu layered on **DirectX 9**. Primarily useful as a learning reference for researchers studying how internal cheats are structured and extended. (source: wiki/sources/descriptions/Neaxic__CSGO-MAIN-INTERNAL.md)

Sits beside [[csgo-internal-base]] and [[csgo-cheat-base]] in the cheat / game:csgo lane as a modular internal base rather than a minimal scaffold or production HvH stack.

## Feature modules

| Module | Role |
|--------|------|
| ESP | In-world player/entity visualization |
| Glow | Highlighting through glow effects |
| Triggerbot | Automated firing when crosshair on target |
| Bunny hop | Movement automation |
| Third-person view | Camera perspective override |
| World-to-screen | 3D→2D projection for overlays |

See [[world-to-screen]] for ESP projection and [[present-hook]] for DirectX 9 in-process overlay draw paths.

## Links

- Repo: https://github.com/Neaxic/CSGO-MAIN-INTERNAL

## Related

[[csgo-internal-base]] · [[csgo-cheat-base]] · [[csgo-internal]] · [[nullhooks]] · [[csgosimple]] · [[world-to-screen]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
