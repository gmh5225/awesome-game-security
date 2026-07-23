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
  - wiki/sources/descriptions/syoyo__tinygltf.md
  - wiki/sources/descriptions/techiew__DirectXHook.md
  - wiki/sources/descriptions/sultim-t__xash-rt.md
  - wiki/sources/descriptions/stungeye__UE5-With-Dear-ImGui.md
  - wiki/sources/descriptions/storm-devs__storm-engine.md
  - wiki/sources/descriptions/stevinz__awesome-game-engine-dev.md
  - wiki/sources/descriptions/ssloy__tinyrenderer.md
  - wiki/sources/descriptions/ssloy__tinyraytracer.md
  - wiki/sources/descriptions/springmusk026__Imgui-Unity.md
  - wiki/sources/descriptions/springmusk026__ImGui-Unity-With-Layout.md
  - wiki/sources/descriptions/springmusk026__Android-ModMenu-SemiJni.md
  - wiki/sources/descriptions/springmusk026__Android-Mod-Menu-Kotlin.md
  - wiki/sources/descriptions/sanqiuu__AndroidCheatTemplate.md
  - wiki/sources/descriptions/solenum__exengine.md
  - wiki/sources/descriptions/scottcgi__Mojoc.md
  - wiki/sources/descriptions/skrixx68__Dota2-Overlay-2.0.md
  - wiki/sources/descriptions/simply-codes__Fortnite-External-P2C.md
  - wiki/sources/descriptions/serjam__mwclap.md
  - wiki/sources/descriptions/samuelgr__Xidi.md
updated: 2026-07-23
confidence: high
---

# Graphics API

Interception and overlay rendering across DirectX, OpenGL, and Vulkan—Present/SwapBuffers hooks, DXGI swap chains, shader/draw interception, screenshot surfaces, and capture pipelines used by both overlays and AI visual cheats. (source: wiki/sources/skills/graphics-api.md)

## Key sub-areas

- **DirectX:** DX9 EndScene/Present; DX11/12 `IDXGISwapChain::Present`; draw-call hooks. Vintage commercial DX9 engine trees such as [[storm-engine]] (Akella Sea Dogs / PotC; full renderer + scene graph) sit in the adjacent Game Engine / DX9 study lane. (source: wiki/sources/descriptions/storm-devs__storm-engine.md)
- **OpenGL / Vulkan / Metal:** `wglSwapBuffers`, `vkQueuePresentKHR`, custom layers; OpenGL Game Develop samples such as [[3d-racing-game]] (racing scene; M/N scene switch). (source: wiki/sources/descriptions/xinyu-evolutruster__3D-Racing-Game.md) Minimal C99 OpenGL engines such as [[exengine]] (lighting / IQM / scene + entity; learning-oriented) sit in the adjacent Game Engine / OpenGL source lane. (source: wiki/sources/descriptions/solenum__exengine.md) Pure-C OpenGLES3 mobile engines such as [[mojoc]] (C99; cross-platform) sit in the same Game Engine / OpenGL ES source lane. (source: wiki/sources/descriptions/scottcgi__Mojoc.md) Xash3D FWGS path-tracing forks such as [[xash-rt]] (C/C++; OpenGL / realtime PT; Renderer lane) extend that OpenGL remaster/research surface. (source: wiki/sources/descriptions/sultim-t__xash-rt.md) Unity VR samples such as [[the-seed-link-future]] (C#; OpenGL / shader focus) sit in the adjacent Game Engine / graphics-research lane. (source: wiki/sources/descriptions/whx-prog__The-Seed-Link-Future.md) Full-engine Vulkan/DX12 trees such as [[wind-effects]] (HLSL deferred/PBR, TAA/SSAO/SSR, volumetric sky) provide a study surface for modern render-pipeline internals. (source: wiki/sources/descriptions/udinmoInc__WindEffects.md) Experimental hot-reloading Vulkan frameworks such as [[island]] (GLSL/Slang live reload; ray tracing / Vulkan Video; Linux+Windows incl. RPi 5) sit in the same Vulkan / Renderer prototyping lane. (source: wiki/sources/descriptions/tgfrerer__island.md) Unity-centered C++ 2D/3D community trees such as [[u3d]] sit in the adjacent Game Engine / graphics-research lane. (source: wiki/sources/descriptions/u3d-community__U3D.md) Apple Metal engine tutorials such as [[metal-game-engine-tutorial]] extend that lane to Metal-backed engine/graphics study. (source: wiki/sources/descriptions/twohyjr__Metal-Game-Engine-Tutorial.md) Curated engine-dev indexes such as [[awesome-game-engine-dev]] (DirectX/OpenGL-oriented tools for engine creation) sit in the adjacent Game Engine / guide lane. (source: wiki/sources/descriptions/stevinz__awesome-game-engine-dev.md) HTML5 engines such as [[turbulenz-engine]] (TypeScript/JS; WebGL 3D) extend that lane to browser WebGL runtime study. (source: wiki/sources/descriptions/turbulenz__turbulenz_engine.md)
- **Overlays:** internal ImGui-on-Present, external layered windows, DWM/Steam/NVIDIA hijacks; Steam-overlay samples such as [[steam-overlay-x64]] (C; modding / memory analysis). (source: wiki/sources/descriptions/xo1337__steam-overlay-x64.md) NVIDIA GeForce Experience overlay–dependent COD Warzone samples such as [[mwclap]] (overlay enabled + fullscreen borderless) sit in the NVIDIA Overlay Hijack lane. (source: wiki/sources/descriptions/serjam__mwclap.md) Title-specific Dota 2 overlay samples such as [[dota2-overlay-2-0]] (C/C++; cheat / game:dota2) sit in the same Cheat Overlay lane. (source: wiki/sources/descriptions/skrixx68__Dota2-Overlay-2.0.md) Shader-oriented external Fortnite samples such as [[fortnite-external-p2c]] (C++; cheat / game:fortnite [External]) sit in the same overlay / shader-research lane. (source: wiki/sources/descriptions/simply-codes__Fortnite-External-P2C.md) DX11/12 Present-hook overlay frameworks such as [[directxhook]] (C++; integrated in-game draw via dinput8 DLL; boxes/textures/text callbacks) sit in the DirectX Hook / Overlay lane. (source: wiki/sources/descriptions/techiew__DirectXHook.md) EAC-oriented PoCs such as [[eac-overlay]] (C++; alternate surfaces / window manipulation vs overlay monitoring) sit in the Anti Cheat Screenshot / Detection:Overlay lane. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md) Kernel-side DWM composition research such as [[double-callback]] (C/C++; DWM in kernel / render-draw) extends the same surface below user-mode Present hooks. (source: wiki/sources/descriptions/wbaby__DoubleCallBack.md) Graphics-kernel buffer hooks such as [[dxgkrnl-hook]] (dxgkrnl screen-buffer manip / player-box overlays) sit in the same Ring0 render-draw lane. (source: wiki/sources/descriptions/vmcall__dxgkrnl_hook.md) iOS ImGui mod-menu samples such as [[imgui-ios-mod-menu]] extend the same cheat / render-draw surface to mobile. (source: wiki/sources/descriptions/xProHackerx__imgui-ios-mod-menu.md) Android ImGui native-app samples such as [[android-native-app-imgui]] (Java/C++) cover the parallel Android lane. (source: wiki/sources/descriptions/vrolife__android_native_app_imgui.md) Android Unity ImGui mod-menu templates such as [[imgui-unity]] (OpenGL ES + IL2CPP/Mono; cheat / render-draw) sit in the same mobile overlay lane. (source: wiki/sources/descriptions/springmusk026__Imgui-Unity.md) Layout-polished sibling [[imgui-unity-with-layout]] (tabs / styled widgets / save-load) extends that Unity-on-Android ImGui surface. (source: wiki/sources/descriptions/springmusk026__ImGui-Unity-With-Layout.md) Java `WindowManager` floating-menu + semi-JNI native hook templates such as [[android-modmenu-semijni]] sit in the same Android mod-menu / overlay lane without GLES ImGui. (source: wiki/sources/descriptions/springmusk026__Android-ModMenu-SemiJni.md) Kotlin Android-view floating overlay + native C++/JNI templates such as [[android-mod-menu-kotlin]] sit in the same `[IL2CPP Menu]` / overlay lane. (source: wiki/sources/descriptions/springmusk026__Android-Mod-Menu-Kotlin.md) Unity Android cheat frameworks such as [[android-cheat-template]] (C/C++; OpenGL / Unity / hooking) sit in the same game engine explorer:Unity / overlay lane. (source: wiki/sources/descriptions/sanqiuu__AndroidCheatTemplate.md) Engine-side Dear ImGui wiring such as [[ue5-with-dear-imgui]] (UE 5.0.1 C++ sample) sits in the Unreal plugin / in-engine UI lane rather than Present-hook overlays. (source: wiki/sources/descriptions/stungeye__UE5-With-Dear-ImGui.md)
- **Anti-screenshot:** BitBlt / DXGI Desktop Duplication / Present interception vs evasion; WDA/monitor-hook samples such as [[wda-monitor-trick]] (C++; D3D9 display intercept / capture helpers) illustrate monitor-level capture research. (source: wiki/sources/descriptions/wongfei__wda_monitor_trick.md)
- **OBS capture:** Game Capture injects graphics-hook DLLs—detection-relevant for AC and AI cheats; streamer-facing Keyboard Mapper plugins such as [[input-overlay]] (C++; keyboard/mouse/gamepad indicators in the OBS render path) sit in the same OBS overlay/plugin surface. (source: wiki/sources/descriptions/univrsal__input-overlay.md)
- Title-specific internals such as [[battlefield-1-internal]] (Battlefield 1; DirectX + hooking + SDK generation) illustrate in-process graphics/hook research samples. (source: wiki/sources/descriptions/younasiqw__BattleField-1-Internal.md)
- DirectX remaster / compatibility mods such as [[gta4-rtx]] (GTA IV → NVIDIA RTX Remix path-traced pipeline; custom Remix runtime + ASI Loader) sit in the DirectX Compatibility lane. (source: wiki/sources/descriptions/xoxor4d__gta4-rtx.md) DirectInput↔XInput controller proxy DLLs such as [[xidi]] (C++; virtual mapping / deadzone / force-feedback translation) extend the same Compatibility lane. (source: wiki/sources/descriptions/samuelgr__Xidi.md)
- DX11 stereoscopic-fix tooling such as [[3d9]] (developer-oriented; broken stereo effects in DX11 games) sits in the DirectX Tools lane. (source: wiki/sources/descriptions/visotw__3d9.md)
- Frame profilers such as [[tracy]] (CPU zones + GPU timing for OpenGL / Vulkan / Direct3D; client + standalone viewer) sit in the adjacent Game Testing / graphics-performance lane. (source: wiki/sources/descriptions/wolfpld__tracy.md)
- Software-raster / Image Codec helpers such as [[olive-c]] (single-header C; lines/triangles/circles/text into raw pixel buffers; no deps) sit below GPU Present hooks as a minimal CPU raster study surface. (source: wiki/sources/descriptions/tsoding__olive.c.md)
- Educational software 3D renderers such as [[tinyrenderer]] (~500 lines bare C++; Bresenham / raster / z-buffer / shading / texture·normal·shadow maps / AO; course for OpenGL/Vulkan/Metal/DX internals) sit in the Renderer lane as a full CPU pipeline study surface. (source: wiki/sources/descriptions/ssloy__tinyrenderer.md) Companion ray-tracing courses such as [[tinyraytracer]] (brief CG/rendering course for graphics programmers; not production-physically-realistic) sit in the same Renderer fundamentals lane. (source: wiki/sources/descriptions/ssloy__tinyraytracer.md)
- Wavefront OBJ mesh parsers such as [[tinyobjloader]] (single-header C++; verts/normals/UVs/MTL) sit in the adjacent Wavefront Obj / asset-ingest lane upstream of GPU draw paths. (source: wiki/sources/descriptions/tinyobjloader__tinyobjloader.md)
- glTF 2.0 loaders such as [[tinygltf]] (header-only C++11; JSON/GLB; meshes/materials/textures/animations/skins) sit in the Game Assets / glTF lane upstream of the same draw paths. (source: wiki/sources/descriptions/syoyo__tinygltf.md)

## Related concepts

[[present-hook]] · [[directxhook]] · [[battlefield-1-internal]] · [[gta4-rtx]] · [[xidi]] · [[xash-rt]] · [[3d9]] · [[storm-engine]] · [[steam-overlay-x64]] · [[mwclap]] · [[dota2-overlay-2-0]] · [[fortnite-external-p2c]] · [[input-overlay]] · [[eac-overlay]] · [[double-callback]] · [[dxgkrnl-hook]] · [[wda-monitor-trick]] · [[3d-racing-game]] · [[exengine]] · [[mojoc]] · [[the-seed-link-future]] · [[wind-effects]] · [[island]] · [[u3d]] · [[metal-game-engine-tutorial]] · [[awesome-game-engine-dev]] · [[turbulenz-engine]] · [[imgui-ios-mod-menu]] · [[imgui-unity]] · [[imgui-unity-with-layout]] · [[android-modmenu-semijni]] · [[android-mod-menu-kotlin]] · [[android-cheat-template]] · [[android-native-app-imgui]] · [[ue5-with-dear-imgui]] · [[tracy]] · [[olive-c]] · [[tinyrenderer]] · [[tinyraytracer]] · [[tinygltf]] · [[tinyobjloader]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]

## README map

`DirectX` (~34: Guide/Hook/Tools/Emulation/Compatibility/Overlay; incl. D3D12 Present/shader injectors + cross-API DX/GL/Vulkan runtime shader capture/flatten/replace), `OpenGL` (~3), `Vulkan` (~9; cross-platform runtime API locators like kiero/kiero2), plus broader `Renderer` (~17; educational soft-3D / ray-tracing courses such as [[tinyrenderer]] / [[tinyraytracer]]) / `3D Graphics` (~4; Metal/DX12/Vulkan kits + WebGL/splat editors) / `Mathematics` (~7; gamedev math libs upstream of render math) / `Image Codec` (~5; stb + portable wgpu/Rhai raster editors + GIF/APNG; soft-raster helpers such as [[olive-c]]), adjacent `Wavefront Obj` (~2; [[tinyobjloader]]) / `Game Assets` glTF helpers such as [[tinygltf]] / `AI` (~5; image→mesh/splat/sprite for engine import), Cheat Overlay/Render, and Anti Cheat Screenshot / Detection:ESP|Overlay. (source: wiki/sources/README-categories.md) (source: wiki/sources/descriptions/tsoding__olive.c.md) (source: wiki/sources/descriptions/ssloy__tinyrenderer.md) (source: wiki/sources/descriptions/ssloy__tinyraytracer.md) (source: wiki/sources/descriptions/tinyobjloader__tinyobjloader.md) (source: wiki/sources/descriptions/syoyo__tinygltf.md)
