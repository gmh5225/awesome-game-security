---
title: Present Hook
kind: concept
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/skills/graphics-api.md
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/wongfei__wda_monitor_trick.md
  - wiki/sources/descriptions/weak1337__PresentHookDetection.md
  - wiki/sources/descriptions/vmcall__dxgkrnl_hook.md
  - wiki/sources/descriptions/r1cky33__krnl-gdi-render.md
  - wiki/sources/descriptions/visotw__3d9.md
  - wiki/sources/descriptions/techiew__DirectXHook.md
  - wiki/sources/descriptions/rlybasic__DWM_Hook.md
  - wiki/sources/descriptions/mfxiaosheng__dwmhook.md
  - wiki/sources/descriptions/gmh5225__dwmhook.md
  - wiki/sources/descriptions/gmh5225__Vulkan-Hook.md
  - wiki/sources/descriptions/oakboat__DisableNvidiaScreenshot.md
  - wiki/sources/descriptions/rdbo__DX11-BaseHook.md
  - wiki/sources/descriptions/niemand-sec__DirectX11Hook.md
  - wiki/sources/descriptions/nefarius__HydraHook.md
  - wiki/sources/descriptions/marlkiller__d3dhook_imgui.md
  - wiki/sources/descriptions/noahware__winbo.md
  - wiki/sources/descriptions/lainswork__dwm-screen-shot.md
  - wiki/sources/descriptions/kirchesz__kiero2.md
  - wiki/sources/descriptions/justinstenning__Direct3DHook.md
  - wiki/sources/descriptions/hiitiger__goverlay.md
  - wiki/sources/descriptions/guided-hacking__GH_D3D11_Hook.md
  - wiki/sources/descriptions/gmh5225__PUBG_Internal.md
  - wiki/sources/descriptions/gmh5225__PUBG-DX.md
  - wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md
  - wiki/sources/descriptions/gmh5225__OBS-Hook.md
  - wiki/sources/descriptions/gmh5225__League-DirectX11-Internal.md
  - wiki/sources/descriptions/gmh5225__Lazysight.md
  - wiki/sources/descriptions/dantebuilds__swapchain-bottleneck.md
  - wiki/sources/descriptions/crosire__reshade.md
  - wiki/sources/descriptions/bruhmoment21__UniversalHookX.md
updated: 2026-08-17
confidence: high
---



# Present Hook

Intercepting the graphics present/swap path (e.g. `IDXGISwapChain::Present`, DX9 `Present`/`EndScene`, `wglSwapBuffers`, `vkQueuePresentKHR`) to draw overlays or copy frames each frame. (source: wiki/sources/skills/graphics-api.md)

## Uses

Internal ESP/menus (often Dear ImGui), backbuffer copy for OBS Game Capture–style sharing or AI visual pipelines ([[obs-game-capture]]), and OBS graphics-hook hijack samples such as [[obs-graphics-hook32-hook]] (gmh5225; 32-bit OBS hook inject; cheat/overlay research) and [[obs-hook]] (gmh5225; inject custom draw calls through OBS's trusted Game Capture pipeline without a separate overlay window; AC whitelist research) that hijack the same in-process capture surface instead of a fresh swap-chain Present vtable hook. (source: wiki/sources/descriptions/gmh5225__OBS-graphics-hook32-Hook.md) (source: wiki/sources/descriptions/gmh5225__OBS-Hook.md) Cross-API post-processing injectors such as [[reshade]] (crosire; automated frame color/depth access + ReShade FX effects; Renderer / graphics-programmer tooling) sit on the same Present-path inject surface as cheat overlays but target shader post-processing rather than ESP menus. (source: wiki/sources/descriptions/crosire__reshade.md) Cross-API bootstrap via runtime locators such as [[kiero2]] (D3D9–12 / OpenGL / Vulkan method addresses; BYO hooking; CMake FetchContent). (source: wiki/sources/descriptions/kirchesz__kiero2.md) Wallhack/chams that alter geometry rather than overlay menus use [[draw-call-hook]] instead of or alongside Present. DX11/12 libraries such as [[directxhook]] provide an integrated in-process overlay framework (boxes/textures/text; dinput8 DLL load) on the Present path. (source: wiki/sources/descriptions/techiew__DirectXHook.md) Minimal DX11 Present trampoline + ImGui templates such as [[dx11-basehook]] (dummy device → vtable → hooked-frame menu) serve as learning starters for the same internal-overlay path. (source: wiki/sources/descriptions/rdbo__DX11-BaseHook.md) Guided Hacking DX11 hook samples such as [[gh-d3d11-hook]] (heavily commented; dependency-free; README `[DX11]`) extend that educational starter lane for DirectX hook study. (source: wiki/sources/descriptions/guided-hacking__GH_D3D11_Hook.md) Related DX11 Present + `ID3D11DeviceContext` hook libraries such as [[directx11hook]] (dummy device → vtable → ImGui in hooked loop; README `[DX11 Imgui]`) sit in the same internal-overlay base lane. (source: wiki/sources/descriptions/niemand-sec__DirectX11Hook.md) DX9–12 multi-version overlay frameworks such as [[hydrahook]] (runtime DX detect; Detours; ImGui/DirectXTK/OpenCV samples; inject/eject) sit in the same DirectX Hook / Overlay lane. (source: wiki/sources/descriptions/nefarius__HydraHook.md) Cross-API D3D/OpenGL/Vulkan ImGui hook bases such as [[d3dhook-imgui]] (x86/x64; graphics-programmer tooling) extend that internal-overlay lane beyond DX-only starters. (source: wiki/sources/descriptions/marlkiller__d3dhook_imgui.md) Unified multi-backend libraries such as [[universalhookx]] (bruhmoment21; DX9–12 + OpenGL + Vulkan Present/swap hooks via dummy-device vtable resolution; compile-time backend selection) illustrate the same cross-API ImGui overlay bootstrap pattern. (source: wiki/sources/descriptions/bruhmoment21__UniversalHookX.md) PUBG internal samples such as [[pubg-internal]] (gmh5225; MinHook on `IDXGISwapChain::Present`; **FW1FontWrapper** DirectWrite D3D11 ESP text in the Present path; cheat / game:pubg) illustrate title-specific internal overlay rendering without Dear ImGui. (source: wiki/sources/descriptions/gmh5225__PUBG_Internal.md) Related PUBG internals such as [[pubg-dx]] (gmh5225; D3D11 Present hook + **ImGui** menu; weapon-icon ESP textures; VMProtect SDK; cheat / game:pubg) show the same Present-path overlay lane with full Dear ImGui feature stacks. (source: wiki/sources/descriptions/gmh5225__PUBG-DX.md) LoL internal samples such as [[league-directx11-internal]] (gmh5225; D3D11 rendering hooks; ImGui overlay with custom fonts; spell/champion data parsing; named pipe external IPC; cheat / game:lol `[Internal]`) extend that lane with title-specific game-data integration under [[vanguard]]. (source: wiki/sources/descriptions/gmh5225__League-DirectX11-Internal.md) Ironsight internal multihack samples such as [[lazysight]] (gmh5225; DirectX Present-path overlay; ESP/aimbot via entity lists, weapon managers, and world-to-screen SDK reads; cheat / game:ironsight `[Internal]`) show the same internal-overlay lane on a lightweight FPS SDK. (source: wiki/sources/descriptions/gmh5225__Lazysight.md) Vulkan-focused hook frameworks such as [[vulkan-hook]] (gmh5225; intercepts `vkQueuePresentKHR` and related Vulkan calls for ImGui overlay menus and ESP in Vulkan games; C++; Windows x86/x64) extend that lane with API-specific Vulkan present-hook patterns. (source: wiki/sources/descriptions/gmh5225__Vulkan-Hook.md) C#/.NET D3D9–11 capture and overlay libraries such as [[direct3d-hook]] (EasyHook inject + SharpDX; remoting `CaptureInterface`; optional API auto-detect; `TestScreenshot` sample) sit in the same DirectX Hook / capture lane for managed tooling. (source: wiki/sources/descriptions/justinstenning__Direct3DHook.md) DX9–12 overlay frameworks that composite desktop GUI toolkits such as [[goverlay]] (Electron/Qt/CEF/WPF offscreen surfaces; IPC + shared memory; multi-window z-order, drag/resize, alpha-aware input) sit in the same DirectX Hook / companion-overlay lane for web-style in-game UI. (source: wiki/sources/descriptions/hiitiger__goverlay.md)

## Detection surface

VTable/code integrity on Present, call-stack analysis, known hook DLLs (`obs-graphics-hook64.dll`), staging-texture / GPU→CPU readback at frame rate. AC screenshot paths may also hook Present or DXGI Desktop Duplication. Monitor-level WDA/D3D9 samples such as [[wda-monitor-trick]] show display-output intercept and capture helpers outside a single swap-chain Present. (source: wiki/sources/descriptions/wongfei__wda_monitor_trick.md)

[[present-hook-detection]] reconstructs a [[battleye]]-style check: dummy D3D11 swap chain → Present vtable pointer → compare prologue bytes to clean `dxgi.dll` for JMP patches or vtable overwrite. (source: wiki/sources/descriptions/weak1337__PresentHookDetection.md)

Overlay-hijack detectors such as [[winbo]] parse dxgkrnl ETW Present events (caller PID vs window-owner PID) and scan the shared GDI handle table for foreign DCs—defensive Detection:Overlay research rather than Present prologue integrity. (source: wiki/sources/descriptions/noahware__winbo.md)


Kernel graphics-subsystem hooks such as [[dxgkrnl-hook]] manipulate the screen buffer below the user-mode Present path—another overlay/draw surface for ESP-style research. (source: wiki/sources/descriptions/vmcall__dxgkrnl_hook.md)

Kernel-mode GDI render frameworks such as [[krnl-gdi-render]] hook GDI drawing from Ring0 for overlays outside typical user-mode Present paths. (source: wiki/sources/descriptions/r1cky33__krnl-gdi-render.md)

User-mode DWM hook samples such as [[dwm-hook]] (C++; rendering / hooking / overlays) draw via Desktop Window Manager composition rather than a single game swap-chain Present. (source: wiki/sources/descriptions/rlybasic__DWM_Hook.md) DWM overlay projects named [[dwmhook]] span a PoC that hooks DWM composition functions to inject draw calls without a separate overlay window (gmh5225; README `[DWM]`) (source: wiki/sources/descriptions/gmh5225__dwmhook.md) and a fuller DX11 vtable ImGui framework (reflective inject; MinHook/PolyHook2; PDB/DIA compositor symbols; README `[DWM VFTable]`) (source: wiki/sources/descriptions/mfxiaosheng__dwmhook.md). DWM anti-screenshot samples such as [[disablenvidiascreenshot]] (C++; NVIDIA / capture-facing screenshot lane) use the same composition surface to study cheat-side anti-screenshot vs Present-path capture. (source: wiki/sources/descriptions/oakboat__DisableNvidiaScreenshot.md) DWM screenshot / AC research samples such as [[dwm-screen-shot]] (C++; defensive engineers studying DWM capture in the Anti Cheat / Screenshot lane) complement overlay and evasion work on the same composition surface. (source: wiki/sources/descriptions/lainswork__dwm-screen-shot.md)

DX11 stereoscopic-fix tooling such as [[3d9]] works in the same Present/swap-chain ecosystem (developer-oriented; not an end-user product). (source: wiki/sources/descriptions/visotw__3d9.md)

## Platform constraints

Windows provides no first-class API for third-party overlays to compose beside a game's DXGI swapchain; Steam, Discord, FPS counters, and cheat overlays converge on in-process `Present` hooks and DLL injection, creating race conditions and driver-level cascades (TDR/BSOD) when multiple presenters contend outside DWM coordination. Architecture analysis such as [[swapchain-bottleneck]] documents this systemic bottleneck and anti-cheat whitelist friction with legitimate injectors. (source: wiki/sources/descriptions/dantebuilds__swapchain-bottleneck.md)

## Related

[[overviews/graphics-api]] · [[reshade]] · [[swapchain-bottleneck]] · [[obs-game-capture]] · [[obs-graphics-hook32-hook]] · [[obs-hook]] · [[draw-call-hook]] · [[anti-screenshot-capture]] · [[kiero2]] · [[directxhook]] · [[dx11-basehook]] · [[directx11hook]] · [[gh-d3d11-hook]] · [[hydrahook]] · [[d3dhook-imgui]] · [[universalhookx]] · [[vulkan-hook]] · [[pubg-dx]] · [[lazysight]] · [[present-hook-detection]] · [[winbo]] · [[wda-monitor-trick]] · [[eac-overlay]] · [[dwm-hook]] · [[dwmhook]] · [[dwm-screen-shot]] · [[disablenvidiascreenshot]] · [[dxgkrnl-hook]] · [[krnl-gdi-render]] · [[3d9]] · [[direct3d-hook]] · [[goverlay]] · [[battleye]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]

