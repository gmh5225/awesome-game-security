---
title: GameOverlayUIHook
kind: entity
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Unkn0wnH4ck3r__GameOverlayUIHook.md
updated: 2026-08-20
confidence: medium
---

# GameOverlayUIHook

C++ **Steam overlay UI hook** example from Unkn0wnH4ck3r. Hooks Steam's overlay process to draw custom UI elements by intercepting **PaintTraverse** in the **VGUI** pipeline and using **shared memory** to communicate render data. Includes fallback shape-drawing logic and documents practical constraints of overlay rendering. Primarily useful for overlay-hook research in game security and anti-cheat experimentation—not a maintained product. README **Steam** tag. (source: wiki/sources/descriptions/Unkn0wnH4ck3r__GameOverlayUIHook.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| VGUI `PaintTraverse` hook | Intercepts overlay UI paint path in Steam's overlay process |
| Shared memory | Transports render data between hook logic and draw path |
| Fallback shape drawing | Basic draw when primary UI path is unavailable |
| Documented constraints | Notes practical limits of Steam overlay rendering |

Contrasts with DXGI Present-path hijacks such as [[steam-hook-render-poc]] (custom draw via `GameOverlayRenderer`) and general Steam overlay RE such as [[steam-overlay-x64]]. Pair with [[present-hook]] for in-game swap-chain overlays and [[discord-overlay-hook]] / [[nvidia-overlay-hijack]] for other trusted third-party overlay hijack lanes.

## Links

- Repo: https://github.com/Unkn0wnH4ck3r/GameOverlayUIHook

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[present-hook]] · [[steam-hook-render-poc]] · [[steam-overlay-x64]] · [[discord-overlay-hook]] · [[nvidia-overlay-hijack]]
