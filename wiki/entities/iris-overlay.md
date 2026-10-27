---
title: Iris (HUD Overlay)
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/allnighter51__Iris.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: high
---

# Iris (HUD Overlay)

**Iris** (allnighter51/Iris) is a Windows desktop **external HUD compositor** aimed at players and creators who want custom on-screen HUDs with **minimal CPU and GPU overhead**. Rust/Tauri 2 on the native side and React/TypeScript for the UI drive Win32 **layered topmost** windows that stack transparent PNG/WebP assets over borderless or windowed games **without DLL injection or game memory reads**. (source: wiki/sources/descriptions/allnighter51__Iris.md)

## Modules

| Component | Role |
|-----------|------|
| **Vault** | Store and calibrate overlay assets |
| **Layering Studio** | Stack and position multi-layer HUD layouts |
| **Display Controller** | Monitor targeting, scaling, automatic profile switching when games are detected |

Click-through transparency keeps mouse/keyboard input routed to the game. Optional **WDA_EXCLUDEFROMCAPTURE** (“streamer mode”) applies display affinity so many capture APIs omit the overlay HWND—see [[anti-screenshot-capture]]. (source: wiki/sources/descriptions/allnighter51__Iris.md)

Upstream framing positions Iris for HUD use **without** the inject/RPM patterns that commonly trigger kernel and user-mode anti-cheat on titles protected by Vanguard, Easy Anti-Cheat, BattlEye, or Ricochet; that is a design intent, not a guarantee of evasion. (source: wiki/sources/descriptions/allnighter51__Iris.md)

README category: Cheat / overlay (same no-hook external lane as [[crosshair-z]]).

## Evidence framing

Apply [[frame-observation-boundary]] before treating “no inject” as undetectable: separate-process layered HWNDs still have compositor, capture-path, topmost-window enumeration, and anti-screenshot policy interactions distinct from Present hooks.

## Links

- Repo: https://github.com/allnighter51/Iris

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[crosshair-z]] · [[present-hook]] · [[anti-screenshot-capture]] · [[iris]] (disambiguation: irisengine game engine)
