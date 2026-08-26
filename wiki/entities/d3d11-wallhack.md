---
title: D3D11 Wallhack
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/DrNseven__D3D11-Wallhack.md
updated: 2026-08-26
confidence: medium
---

# D3D11 Wallhack

**D3D11 Wallhack** (DrNseven/D3D11-Wallhack) is a **Direct3D 11 hook-based wallhack** for **32-bit and 64-bit Windows games**. Implemented in **C++** with **Detours** and **Dear ImGui**, it injects a DLL, hooks rendering paths, and provides a **menu-driven workflow** for identifying target models via **stride and index-count logging**. Primarily intended for cheat prototyping and graphics pipeline analysis in game security research. (source: wiki/sources/descriptions/DrNseven__D3D11-Wallhack.md)

Sits in the DX11 [[draw-call-hook]] / wallhack lane beside educational DX11 samples such as [[gh-d3d11-hook]] and sibling DrNseven tools such as [[d3d11-worldtoscreen-finder]] and [[d3d12-hook-imgui]].

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 11 | Target graphics API; draw/render-path interception |
| Detours | Function interception on DX11 rendering paths |
| Dear ImGui | In-game menu for model identification workflow |
| Stride / index logging | Menu-driven target-model discovery via draw-call metadata |
| DLL inject | In-process hook lifecycle for 32/64-bit Windows titles |

See [[draw-call-hook]] for depth-state and draw-interception patterns and [[present-hook]] when overlays complement draw-path modification.

## Links

- Repo: https://github.com/DrNseven/D3D11-Wallhack

## Related

[[draw-call-hook]] · [[present-hook]] · [[gh-d3d11-hook]] · [[d3d11-worldtoscreen-finder]] · [[d3d12-hook-imgui]] · [[cod-hacks]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
