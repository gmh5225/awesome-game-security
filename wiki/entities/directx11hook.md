---
title: DirectX11Hook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/niemand-sec__DirectX11Hook.md
updated: 2026-07-28
confidence: medium
---

# DirectX11Hook

C++ DirectX 11 hook library that intercepts `IDXGISwapChain::Present` and `ID3D11DeviceContext` methods to render custom overlays inside D3D11 apps. Locates the D3D11 vtable via a dummy device, installs function hooks, and draws Dear ImGui menus in the hooked render loop—a base for internal game overlays and cheat-menu research. (source: wiki/sources/descriptions/niemand-sec__DirectX11Hook.md)

## Links

- Repo: https://github.com/niemand-sec/DirectX11Hook

## Related

[[present-hook]] · [[dx11-basehook]] · [[directxhook]] · [[present-hook-detection]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
