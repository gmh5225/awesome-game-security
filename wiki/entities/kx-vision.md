---
title: KX-Vision
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/husnaintariq577__kx-vision.md
  - wiki/sources/README-categories.md
updated: 2026-09-28
confidence: medium
---

# KX-Vision

**KX-Vision** (husnaintariq577/kx-vision) is an open-source **ESP overlay** for **Guild Wars 2** that draws nearby players, events, and world objects on top of the live client. Implemented in **C++23** as a Windows Visual Studio project, it hooks **DirectX 11** presentation with **MinHook**, renders through **ImGui** and **GLM**, and documents Guild Wars 2 engine internals for reverse engineers and game-security researchers. (source: wiki/sources/descriptions/husnaintariq577__kx-vision.md)

README category: Cheat / DirectX / Overlay · game:guild wars 2.

## Render and hook surface

- **D3D11 Present hook** — internal overlay on the client swap path ([[present-hook]]).
- **ImGui + GLM** — world/player/event visualization layered over the running frame.

## Memory and threading

The codebase documents a **game-thread hook** and **capture-and-store** pattern for safely reading **ContextCollection** data across separate logic and render threads—typical MMO client threading where render-time reads race live simulation state. Layout comes from **ReClass-derived structures** and **generated API headers** for memory offsets. (source: wiki/sources/descriptions/husnaintariq577__kx-vision.md)

## Positioning

Sits in the **MMO client-overlay** lane beside title-specific D3D11 samples such as [[dota2-overlay-2-0]] and [[dota2-overlay-offset-updater]], but emphasizes **documented engine internals** and cross-thread memory access patterns rather than offset-only maintenance tooling. Complements generic DX11 Present starters such as [[dx11-basehook]] and [[gh-d3d11-hook]] with a shipping-MMO case study for [[world-to-screen]] ESP research.

## Links

- Repo: https://github.com/husnaintariq577/kx-vision

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[present-hook]] · [[world-to-screen]] · [[imgui]] · [[dota2-overlay-2-0]]
