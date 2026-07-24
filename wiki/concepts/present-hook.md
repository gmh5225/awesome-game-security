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
  - wiki/sources/descriptions/visotw__3d9.md
  - wiki/sources/descriptions/techiew__DirectXHook.md
  - wiki/sources/descriptions/rlybasic__DWM_Hook.md
updated: 2026-07-24
confidence: high
---


# Present Hook

Intercepting the graphics present/swap path (e.g. `IDXGISwapChain::Present`, DX9 `Present`/`EndScene`, `wglSwapBuffers`, `vkQueuePresentKHR`) to draw overlays or copy frames each frame. (source: wiki/sources/skills/graphics-api.md)

## Uses

Internal ESP/menus (often Dear ImGui), wallhack/chams via draw/shader hooks, OBS Game Capture–style backbuffer sharing for streaming or AI visual pipelines. DX11/12 libraries such as [[directxhook]] provide an integrated in-process overlay framework (boxes/textures/text; dinput8 DLL load) on the Present path. (source: wiki/sources/descriptions/techiew__DirectXHook.md)

## Detection surface

VTable/code integrity on Present, call-stack analysis, known hook DLLs (`obs-graphics-hook64.dll`), staging-texture / GPU→CPU readback at frame rate. AC screenshot paths may also hook Present or DXGI Desktop Duplication. Monitor-level WDA/D3D9 samples such as [[wda-monitor-trick]] show display-output intercept and capture helpers outside a single swap-chain Present. (source: wiki/sources/descriptions/wongfei__wda_monitor_trick.md)

[[present-hook-detection]] reconstructs a [[battleye]]-style check: dummy D3D11 swap chain → Present vtable pointer → compare prologue bytes to clean `dxgi.dll` for JMP patches or vtable overwrite. (source: wiki/sources/descriptions/weak1337__PresentHookDetection.md)

Kernel graphics-subsystem hooks such as [[dxgkrnl-hook]] manipulate the screen buffer below the user-mode Present path—another overlay/draw surface for ESP-style research. (source: wiki/sources/descriptions/vmcall__dxgkrnl_hook.md)

User-mode DWM hook samples such as [[dwm-hook]] (C++; rendering / hooking / overlays) draw via Desktop Window Manager composition rather than a single game swap-chain Present. (source: wiki/sources/descriptions/rlybasic__DWM_Hook.md)

DX11 stereoscopic-fix tooling such as [[3d9]] works in the same Present/swap-chain ecosystem (developer-oriented; not an end-user product). (source: wiki/sources/descriptions/visotw__3d9.md)

## Related

[[overviews/graphics-api]] · [[directxhook]] · [[present-hook-detection]] · [[wda-monitor-trick]] · [[eac-overlay]] · [[dwm-hook]] · [[dxgkrnl-hook]] · [[3d9]] · [[battleye]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
