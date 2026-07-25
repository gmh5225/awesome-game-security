---
title: DX11-BaseHook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/rdbo__DX11-BaseHook.md
updated: 2026-07-25
confidence: medium
---

# DX11-BaseHook

Minimal C++ DirectX 11 hooking base that intercepts `IDXGISwapChain::Present` to draw custom overlays inside D3D11 apps. Creates a dummy D3D11 device to locate the Present vtable, installs a trampoline hook, and renders Dear ImGui menus in the hooked frame—aimed as a starting template for internal game overlays and cheat-menu learning. (source: wiki/sources/descriptions/rdbo__DX11-BaseHook.md)

## Links

- Repo: https://github.com/rdbo/DX11-BaseHook

## Related

[[present-hook]] · [[present-hook-detection]] · [[directxhook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
