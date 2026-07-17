---
title: Graphics API
kind: overview
topics: [graphics-api]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/README-categories.md
updated: 2026-07-17
confidence: high
---

# Graphics API

Interception and overlay rendering across DirectX, OpenGL, and Vulkan—Present/SwapBuffers hooks, DXGI swap chains, shader/draw interception, screenshot surfaces, and capture pipelines used by both overlays and AI visual cheats. (source: wiki/sources/skills/graphics-api.md)

## Key sub-areas

- **DirectX:** DX9 EndScene/Present; DX11/12 `IDXGISwapChain::Present`; draw-call hooks
- **OpenGL / Vulkan:** `wglSwapBuffers`, `vkQueuePresentKHR`, custom layers
- **Overlays:** internal ImGui-on-Present, external layered windows, DWM/Steam/NVIDIA hijacks
- **Anti-screenshot:** BitBlt / DXGI Desktop Duplication / Present interception vs evasion
- **OBS capture:** Game Capture injects graphics-hook DLLs—detection-relevant for AC and AI cheats

## Related concepts

[[present-hook]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]

## README map

`DirectX` (~31: Guide/Hook/Tools/Emulation/Compatibility/Overlay; incl. D3D12 runtime shader injectors), `OpenGL` (~3), `Vulkan` (~9; runtime API locators like kiero/kiero2), plus broader `Renderer` / `3D Graphics`, Cheat Overlay/Render, and Anti Cheat Screenshot / Detection:ESP|Overlay. (source: wiki/sources/README-categories.md)
