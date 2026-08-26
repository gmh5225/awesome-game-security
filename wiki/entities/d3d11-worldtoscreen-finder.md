---
title: D3D11 World-to-Screen Finder
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/DrNseven__D3D11-Worldtoscreen-Finder.md
updated: 2026-08-26
confidence: medium
---

# D3D11 World-to-Screen Finder

**D3D11 World-to-Screen Finder** (DrNseven/D3D11-Worldtoscreen-Finder) is a **Direct3D 11 world-to-screen finder** for locating usable projection math in games. Implemented in **C++** with **DirectX 11 hooking** (MinHook) and a **Dear ImGui in-game overlay**, it brute-forces and tests **matrix or constant-buffer combinations** by drawing model-position text and logging matched targets. Primarily used in game security and cheat research workflows to bootstrap ESP or aiming-related visual experiments. (source: wiki/sources/descriptions/DrNseven__D3D11-Worldtoscreen-Finder.md)

Sits in the DX11 Present-hook + [[world-to-screen]] discovery lane beside educational DX11 hook samples such as [[gh-d3d11-hook]] and overlay scaffolds such as [[d3d12-hook-imgui]] from the same author.

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 11 | Target graphics API; constant-buffer / matrix introspection |
| MinHook | Function interception on DX11 render path |
| Dear ImGui | In-game overlay for model-position text and match feedback |
| Brute-force W2S | Tests matrix/CB combinations; logs matched projection targets |

See [[world-to-screen]] for the projection pipeline and [[present-hook]] for swap-chain Present interception patterns.

## Links

- Repo: https://github.com/DrNseven/D3D11-Worldtoscreen-Finder

## Related

[[world-to-screen]] · [[present-hook]] · [[gh-d3d11-hook]] · [[d3d12-hook-imgui]] · [[d3dhook-imgui]] · [[lab-esp-and-aimbot]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
