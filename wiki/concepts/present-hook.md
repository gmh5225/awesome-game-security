---
title: Present Hook
kind: concept
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/wongfei__wda_monitor_trick.md
updated: 2026-07-18
confidence: high
---

# Present Hook

Intercepting the graphics present/swap path (e.g. `IDXGISwapChain::Present`, DX9 `Present`/`EndScene`, `wglSwapBuffers`, `vkQueuePresentKHR`) to draw overlays or copy frames each frame. (source: wiki/sources/skills/graphics-api.md)

## Uses

Internal ESP/menus (often Dear ImGui), wallhack/chams via draw/shader hooks, OBS Game Capture–style backbuffer sharing for streaming or AI visual pipelines.

## Detection surface

VTable/code integrity on Present, call-stack analysis, known hook DLLs (`obs-graphics-hook64.dll`), staging-texture / GPU→CPU readback at frame rate. AC screenshot paths may also hook Present or DXGI Desktop Duplication. Monitor-level WDA/D3D9 samples such as [[wda-monitor-trick]] show display-output intercept and capture helpers outside a single swap-chain Present. (source: wiki/sources/descriptions/wongfei__wda_monitor_trick.md)

## Related

[[overviews/graphics-api]] · [[wda-monitor-trick]] · [[eac-overlay]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
