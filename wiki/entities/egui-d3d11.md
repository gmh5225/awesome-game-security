---
title: egui-d3d11
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__egui-d3d11.md
updated: 2026-08-09
confidence: medium
---

# egui-d3d11

Rust library that renders **egui** (immediate-mode GUI) directly onto **Direct3D 11** surfaces for in-game overlay menus via D3D11 **Present** hooks. Converts egui mesh output to D3D11 vertex/index buffers, compiles HLSL shaders for textured triangle rendering, uploads font-atlas textures, and translates Win32 keyboard/mouse input into egui format—with D3D11 state backup/restore to avoid corrupting the host game's rendering pipeline. (source: wiki/sources/descriptions/gmh5225__egui-d3d11.md)

Targets cheat developers and security researchers building or studying ImGui-style overlay menus injected into DirectX 11 games. README category: `[Menu]`. Sits beside Rust egui cheat UIs such as [[proext]] and DX11 ImGui hook libraries such as [[directx11hook]], [[d3dhook-imgui]], and [[gh-d3d11-hook]] in the [[present-hook]] lane.

## Links

- Repo: https://github.com/gmh5225/egui-d3d11

## Related

[[present-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[directx11hook]] · [[d3dhook-imgui]] · [[gh-d3d11-hook]] · [[dx11-basehook]] · [[proext]]
