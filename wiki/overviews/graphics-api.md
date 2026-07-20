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
  - wiki/sources/descriptions/wongfei__wda_monitor_trick.md
  - wiki/sources/descriptions/wolfpld__tracy.md
  - wiki/sources/descriptions/whx-prog__The-Seed-Link-Future.md
  - wiki/sources/descriptions/wbaby__DoubleCallBack.md
  - wiki/sources/descriptions/vrolife__android_native_app_imgui.md
  - wiki/sources/descriptions/vmcall__dxgkrnl_hook.md
  - wiki/sources/descriptions/visotw__3d9.md
  - wiki/sources/descriptions/univrsal__input-overlay.md
  - wiki/sources/descriptions/udinmoInc__WindEffects.md
  - wiki/sources/descriptions/u3d-community__U3D.md
  - wiki/sources/descriptions/twohyjr__Metal-Game-Engine-Tutorial.md
  - wiki/sources/descriptions/turbulenz__turbulenz_engine.md
  - wiki/sources/descriptions/tgfrerer__island.md
  - wiki/sources/descriptions/tsoding__olive.c.md
  - wiki/sources/descriptions/tinyobjloader__tinyobjloader.md
  - wiki/sources/descriptions/techiew__DirectXHook.md
updated: 2026-07-20
confidence: high
---

# Graphics API

Interception and overlay rendering across DirectX, OpenGL, and Vulkan—Present/SwapBuffers hooks, DXGI swap chains, shader/draw interception, screenshot surfaces, and capture pipelines used by both overlays and AI visual cheats. (source: wiki/sources/skills/graphics-api.md)

## Key sub-areas

- **DirectX:** DX9 EndScene/Present; DX11/12 `IDXGISwapChain::Present`; draw-call hooks
- **OpenGL / Vulkan / Metal:** `wglSwapBuffers`, `vkQueuePresentKHR`, custom layers; OpenGL Game Develop samples such as [[3d-racing-game]] (racing scene; M/N scene switch). (source: wiki/sources/descriptions/xinyu-evolutruster__3D-Racing-Game.md) Unity VR samples such as [[the-seed-link-future]] (C#; OpenGL / shader focus) sit in the adjacent Game Engine / graphics-research lane. (source: wiki/sources/descriptions/whx-prog__The-Seed-Link-Future.md) Full-engine Vulkan/DX12 trees such as [[wind-effects]] (HLSL deferred/PBR, TAA/SSAO/SSR, volumetric sky) provide a study surface for modern render-pipeline internals. (source: wiki/sources/descriptions/udinmoInc__WindEffects.md) Experimental hot-reloading Vulkan frameworks such as [[island]] (GLSL/Slang live reload; ray tracing / Vulkan Video; Linux+Windows incl. RPi 5) sit in the same Vulkan / Renderer prototyping lane. (source: wiki/sources/descriptions/tgfrerer__island.md) Unity-centered C++ 2D/3D community trees such as [[u3d]] sit in the adjacent Game Engine / graphics-research lane. (source: wiki/sources/descriptions/u3d-community__U3D.md) Apple Metal engine tutorials such as [[metal-game-engine-tutorial]] extend that lane to Metal-backed engine/graphics study. (source: wiki/sources/descriptions/twohyjr__Metal-Game-Engine-Tutorial.md) HTML5 engines such as [[turbulenz-engine]] (TypeScript/JS; WebGL 3D) extend that lane to browser WebGL runtime study. (source: wiki/sources/descriptions/turbulenz__turbulenz_engine.md)
- **Overlays:** internal ImGui-on-Present, external layered windows, DWM/Steam/NVIDIA hijacks; Steam-overlay samples such as [[steam-overlay-x64]] (C; modding / memory analysis). (source: wiki/sources/descriptions/xo1337__steam-overlay-x64.md) DX11/12 Present-hook overlay frameworks such as [[directxhook]] (C++; integrated in-game draw via dinput8 DLL; boxes/textures/text callbacks) sit in the DirectX Hook / Overlay lane. (source: wiki/sources/descriptions/techiew__DirectXHook.md) EAC-oriented PoCs such as [[eac-overlay]] (C++; alternate surfaces / window manipulation vs overlay monitoring) sit in the Anti Cheat Screenshot / Detection:Overlay lane. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md) Kernel-side DWM composition research such as [[double-callback]] (C/C++; DWM in kernel / render-draw) extends the same surface below user-mode Present hooks. (source: wiki/sources/descriptions/wbaby__DoubleCallBack.md) Graphics-kernel buffer hooks such as [[dxgkrnl-hook]] (dxgkrnl screen-buffer manip / player-box overlays) sit in the same Ring0 render-draw lane. (source: wiki/sources/descriptions/vmcall__dxgkrnl_hook.md) iOS ImGui mod-menu samples such as [[imgui-ios-mod-menu]] extend the same cheat / render-draw surface to mobile. (source: wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md) Android ImGui native-app samples such as [[android-native-app-imgui]] (Java/C++) cover the parallel Android lane. (source: wiki/sources/descriptions/vrolife__android_native_app_imgui.md)
- **Anti-screenshot:** BitBlt / DXGI Desktop Duplication / Present interception vs evasion; WDA/monitor-hook samples such as [[wda-monitor-trick]] (C++; D3D9 display intercept / capture helpers) illustrate monitor-level capture research. (source: wiki/sources/descriptions/wongfei__wda_monitor_trick.md)
- **OBS capture:** Game Capture injects graphics-hook DLLs—detection-relevant for AC and AI cheats; streamer-facing Keyboard Mapper plugins such as [[input-overlay]] (C++; keyboard/mouse/gamepad indicators in the OBS render path) sit in the same OBS overlay/plugin surface. (source: wiki/sources/descriptions/univrsal__input-overlay.md)
- Title-specific internals such as [[battlefield-1-internal]] (Battlefield 1; DirectX + hooking + SDK generation) illustrate in-process graphics/hook research samples. (source: wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md)
- DirectX remaster / compatibility mods such as [[gta4-rtx]] (GTA IV → NVIDIA RTX Remix path-traced pipeline; custom Remix runtime + ASI Loader) sit in the DirectX Compatibility lane. (source: wiki/sources/descriptions/xoxor4d__gta4-rtx.md)
- DX11 stereoscopic-fix tooling such as [[3d9]] (developer-oriented; broken stereo effects in DX11 games) sits in the DirectX Tools lane. (source: wiki/sources/descriptions/visotw__3d9.md)
- Frame profilers such as [[tracy]] (CPU zones + GPU timing for OpenGL / Vulkan / Direct3D; client + standalone viewer) sit in the adjacent Game Testing / graphics-performance lane. (source: wiki/sources/descriptions/wolfpld__tracy.md)
- Software-raster / Image Codec helpers such as [[olive-c]] (single-header C; lines/triangles/circles/text into raw pixel buffers; no deps) sit below GPU Present hooks as a minimal CPU raster study surface. (source: wiki/sources/descriptions/tsoding__olive.c.md)
- Wavefront OBJ mesh parsers such as [[tinyobjloader]] (single-header C++; verts/normals/UVs/MTL) sit in the adjacent Wavefront Obj / asset-ingest lane upstream of GPU draw paths. (source: wiki/sources/descriptions/tinyobjloader__tinyobjloader.md)

## Related concepts

[[present-hook]] · [[directxhook]] · [[battlefield-1-internal]] · [[gta4-rtx]] · [[3d9]] · [[steam-overlay-x64]] · [[input-overlay]] · [[eac-overlay]] · [[double-callback]] · [[dxgkrnl-hook]] · [[wda-monitor-trick]] · [[3d-racing-game]] · [[the-seed-link-future]] · [[wind-effects]] · [[island]] · [[u3d]] · [[metal-game-engine-tutorial]] · [[turbulenz-engine]] · [[imgui-ios-mod-menu]] · [[android-native-app-imgui]] · [[tracy]] · [[olive-c]] · [[tinyobjloader]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]

## README map

`DirectX` (~33: Guide/Hook/Tools/Emulation/Compatibility/Overlay; incl. D3D12 Present/shader injectors for title-specific pixel-shader replace), `OpenGL` (~3), `Vulkan` (~9; cross-platform runtime API locators like kiero/kiero2), plus broader `Renderer` (~17) / `3D Graphics` (~4; Metal/DX12/Vulkan kits + WebGL/splat editors) / `Mathematics` (~7; gamedev math libs upstream of render math) / `Image Codec` (~5; stb + portable wgpu/Rhai raster editors + GIF/APNG; soft-raster helpers such as [[olive-c]]), adjacent `Wavefront Obj` (~2; [[tinyobjloader]]) / `AI` (~5; image→mesh/splat/sprite for engine import), Cheat Overlay/Render, and Anti Cheat Screenshot / Detection:ESP|Overlay. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/tsoding__olive.c.md) (source: wiki/sources/descriptions/tinyobjloader__tinyobjloader.md)
