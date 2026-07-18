---
title: Graphics API
kind: overview
topics: [graphics-api]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md
  - wiki/sources/descriptions/xoxor4d__gta4-rtx.md
  - wiki/sources/descriptions/xo1337__steam-overlay-x64.md
  - wiki/sources/descriptions/xinyu-evolutruster__3D-Racing-Game.md
  - wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md
  - wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md
updated: 2026-07-18
confidence: high
---

# Graphics API

Interception and overlay rendering across DirectX, OpenGL, and Vulkan—Present/SwapBuffers hooks, DXGI swap chains, shader/draw interception, screenshot surfaces, and capture pipelines used by both overlays and AI visual cheats. (source: wiki/sources/skills/graphics-api.md)

## Key sub-areas

- **DirectX:** DX9 EndScene/Present; DX11/12 `IDXGISwapChain::Present`; draw-call hooks
- **OpenGL / Vulkan:** `wglSwapBuffers`, `vkQueuePresentKHR`, custom layers; OpenGL Game Develop samples such as [[3d-racing-game]] (racing scene; M/N scene switch). (source: wiki/sources/descriptions/xinyu-evolutruster__3D-Racing-Game.md)
- **Overlays:** internal ImGui-on-Present, external layered windows, DWM/Steam/NVIDIA hijacks; Steam-overlay samples such as [[steam-overlay-x64]] (C; modding / memory analysis). (source: wiki/sources/descriptions/xo1337__steam-overlay-x64.md) EAC-oriented PoCs such as [[eac-overlay]] (C++; alternate surfaces / window manipulation vs overlay monitoring) sit in the Anti Cheat Screenshot / Detection:Overlay lane. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md) iOS ImGui mod-menu samples such as [[imgui-ios-mod-menu]] extend the same cheat / render-draw surface to mobile. (source: wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md)
- **Anti-screenshot:** BitBlt / DXGI Desktop Duplication / Present interception vs evasion
- **OBS capture:** Game Capture injects graphics-hook DLLs—detection-relevant for AC and AI cheats
- Title-specific internals such as [[battlefield-1-internal]] (Battlefield 1; DirectX + hooking + SDK generation) illustrate in-process graphics/hook research samples. (source: wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md)
- DirectX remaster / compatibility mods such as [[gta4-rtx]] (GTA IV → NVIDIA RTX Remix path-traced pipeline; custom Remix runtime + ASI Loader) sit in the DirectX Compatibility lane. (source: wiki/sources/descriptions/xoxor4d__gta4-rtx.md)

## Related concepts

[[present-hook]] · [[battlefield-1-internal]] · [[gta4-rtx]] · [[steam-overlay-x64]] · [[eac-overlay]] · [[3d-racing-game]] · [[imgui-ios-mod-menu]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]

## README map

`DirectX` (~32: Guide/Hook/Tools/Emulation/Compatibility/Overlay; incl. D3D12 runtime shader injectors), `OpenGL` (~3), `Vulkan` (~9; runtime API locators like kiero/kiero2), plus broader `Renderer` (~16) / `3D Graphics` (~4), Cheat Overlay/Render, and Anti Cheat Screenshot / Detection:ESP|Overlay. (source: wiki/sources/README-categories.md)
