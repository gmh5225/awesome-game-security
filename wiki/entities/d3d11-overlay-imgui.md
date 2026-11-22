---
title: D3D11 Overlay ImGui
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/adamhlt__D3D11-Overlay-ImGui.md
updated: 2026-11-22
confidence: medium
---

# D3D11 Overlay ImGui

**D3D11 Overlay ImGui** (adamhlt/D3D11-Overlay-ImGui) is a Windows **C++ sample** that draws a **Dear ImGui** interface in a **transparent, topmost** layer above a chosen game or application. It uses **DirectX 11** with the official ImGui Win32 and DX11 backends, and **tracks the target window's position, size, and focus** so the overlay stays aligned even when the host does not use DirectX. The same sources build as a **standalone EXE** with an HWND picker for external overlays or as an **injectable DLL** attached to a process main window, in both **x86** and **x64**. Notable behavior includes **click-through** when the menu is hidden, **automatic shutdown** when the target closes, and techniques to **hide the overlay from OBS** and common screen-capture tools—aimed at developers exploring game overlays, injection-based tooling, and related reverse engineering or game-security research on Windows. (source: wiki/sources/descriptions/adamhlt__D3D11-Overlay-ImGui.md)

Contrasts with [[imgui-standalone]] (own render window, no HWND tracking) and [[d3d9-overlay-imgui]] (compositing into a host D3D9 swap chain); sits beside [[d3d9-hook-imgui]], [[d3dhook-imgui]], and [[anti-screenshot-capture]] capture-evasion patterns.

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 11 | Transparent overlay render path (ImGui DX11 backend) |
| HWND tracking | Mirror target window geometry and focus |
| EXE mode | Window picker + external topmost layer |
| DLL mode | In-process attach to target main window |
| UX | Click-through when menu hidden; exit when target closes |
| Capture | Techniques to omit overlay from OBS / common capture |

See [[present-hook]] for in-process DXGI Present hook overlays; this template is primarily an **external layered** DX11 compositor.

## Links

- Repo: https://github.com/adamhlt/D3D11-Overlay-ImGui

## Related

[[anti-screenshot-capture]] · [[obs-game-capture]] · [[present-hook]] · [[imgui]] · [[imgui-standalone]] · [[d3d9-overlay-imgui]] · [[d3d9-hook-imgui]] · [[d3dhook-imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]