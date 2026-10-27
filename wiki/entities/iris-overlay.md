---
title: Iris (HUD Overlay)
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/allnighter51__Iris.md
  - wiki/sources/README-categories.md
updated: 2026-10-27
confidence: medium
---

# Iris (HUD Overlay)

**Iris** (allnighter51/Iris) is a Windows desktop **external HUD compositor**: Rust/Tauri 2 native code plus a React/TypeScript UI drives Win32 layered topmost windows that stack transparent PNG/WebP assets over borderless or windowed games **without DLL injection or game memory reads**. The Vault stores calibrated assets; Layering Studio builds multi-layer layouts; Display Controller handles monitor targeting, scaling, and automatic profile switching on game detection. Click-through transparency keeps input in the game; optional **WDA_EXCLUDEFROMCAPTURE** streamer mode hides overlays from capture software. (source: wiki/sources/descriptions/allnighter51__Iris.md)

README category: Cheat / overlay (same no-hook external lane as [[crosshair-z]]).

## Evidence framing

Apply [[frame-observation-boundary]] before treating “no inject” as undetectable: separate-process layered HWNDs still have compositor, capture-path, and anti-screenshot policy interactions distinct from Present hooks.

## Links

- Repo: https://github.com/allnighter51/Iris

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[crosshair-z]] · [[present-hook]] · [[anti-screenshot-capture]] · [[iris]] (disambiguation: irisengine game engine)
