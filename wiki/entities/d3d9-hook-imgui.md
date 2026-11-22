---
title: D3D9 Hook ImGui
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/adamhlt__D3D9-Hook-ImGui.md
updated: 2026-11-22
confidence: medium
---

# D3D9 Hook ImGui

**D3D9 Hook ImGui** (adamhlt/D3D9-Hook-ImGui) is a Windows **injectable DLL template** that intercepts `IDirect3DDevice9` **EndScene** and **Reset** to draw a **Dear ImGui** overlay inside any DirectX 9 application. Built in **C++** with Visual Studio for **x86** and **x64**, it obtains the device virtual table via the **dummy-device** technique and applies hooks using **Microsoft Detours**. The scaffold handles window resize, fullscreen resets, keyboard toggles, and safe unload so developers mainly customize the menu in source—suited to reverse engineering, game modding, and graphics-hook research needing a ready-made D3D9 + ImGui integration point. (source: wiki/sources/descriptions/adamhlt__D3D9-Hook-ImGui.md)

Sits in the legacy **D3D9 EndScene/Reset** internal-overlay lane beside cross-API starters such as [[d3dhook-imgui]] and [[universal-dear-imgui-hook]], DX9 overlay frameworks such as [[direct3d9-overlay]], and sibling adamhlt samples such as [[imgui-standalone]] (external D3D11 window) and API-specific templates such as [[d3d12-hook-imgui]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Direct3D 9 | Target graphics API; `EndScene` / `Reset` hook points |
| Dummy device | Vtable resolution for `IDirect3DDevice9` |
| Microsoft Detours | Function interception on EndScene/Reset |
| Dear ImGui | In-game overlay menu and debug UI |
| Lifecycle scaffold | Resize, fullscreen reset, keyboard toggle, safe DLL unload |

See [[present-hook]] for DXGI/D3D9 present-path patterns and [[draw-call-hook]] when overlays are not the primary graphics research goal.

## Links

- Repo: https://github.com/adamhlt/D3D9-Hook-ImGui

## Related

[[present-hook]] · [[imgui]] · [[d3dhook-imgui]] · [[direct3d9-overlay]] · [[universal-dear-imgui-hook]] · [[imgui-standalone]] · [[d3d12-hook-imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]