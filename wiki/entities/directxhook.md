---
title: DirectXHook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/techiew__DirectXHook.md
updated: 2026-07-20
confidence: medium
---

# DirectXHook

C++ library that hooks DirectX 11 and DirectX 12 so custom graphics draw inside the game window as an **integrated** overlay (not an external layered window). Builds as a DLL (commonly loaded via dinput8 proxy injection); supports 32-bit and 64-bit. Includes an overlay framework for boxes, textures, and text via a simple callback API, plus example overlays/mods for in-game HUDs and gameplay tweaks—aimed at modders and reverse engineers needing in-process DX Present hooks. (source: wiki/sources/descriptions/techiew__DirectXHook.md)

## Links

- Repo: https://github.com/techiew/DirectXHook

## Related

[[present-hook]] · [[present-hook-detection]] · [[eac-overlay]] · [[steam-overlay-x64]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
