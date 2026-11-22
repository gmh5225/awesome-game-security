---
title: D3D9 Overlay ImGui
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/adamhlt__D3D9-Overlay-ImGui.md
updated: 2026-11-22
confidence: medium
---

# D3D9 Overlay ImGui

**D3D9 Overlay ImGui** (adamhlt/D3D9-Overlay-ImGui) is a Visual Studio **C++ template** for drawing a **Dear ImGui** interface and optional custom **Direct3D 9** graphics on top of another Windows application's existing **D3D9 swap chain**. Ships for **x86** and **x64** as either a **standalone EXE** that enumerates open windows and lets you pick a target **HWND** before starting the overlay, or as an **injectable DLL** for in-process attachment. Sample code separates ImGui menu drawing from optional raw `IDirect3DDevice9` calls, toggles visibility with **INSERT**, and bundles the standard Win32 and D3D9 ImGui backends—aimed at overlay developers, reverse engineers, and game security researchers prototyping in-process D3D9 hooks and on-screen tooling UIs. (source: wiki/sources/descriptions/adamhlt__D3D9-Overlay-ImGui.md)

Contrasts with [[d3d9-hook-imgui]] (Detours on `EndScene`/`Reset`) by centering on **compositing into the host swap chain** with an EXE window-picker workflow; sits beside [[direct3d9-overlay]], [[d3dhook-imgui]], and sibling adamhlt templates such as [[imgui-standalone]] and [[d3d11-overlay-imgui]] (external topmost DX11 layer with HWND tracking).

## Architecture highlights

| Component | Role |
|-----------|------|
| Direct3D 9 | Render into the target app's existing swap chain |
| Dear ImGui | Menu and debug UI (Win32 + D3D9 backends) |
| EXE mode | HWND enumeration and target selection before overlay start |
| DLL mode | In-process attach for integrated overlays |
| Sample split | ImGui menu path vs optional raw `IDirect3DDevice9` draws |

See [[present-hook]] for DXGI/D3D9 present-path patterns.

## Links

- Repo: https://github.com/adamhlt/D3D9-Overlay-ImGui

## Related

[[present-hook]] · [[imgui]] · [[d3d9-hook-imgui]] · [[d3dhook-imgui]] · [[direct3d9-overlay]] · [[imgui-standalone]] · [[d3d11-overlay-imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]