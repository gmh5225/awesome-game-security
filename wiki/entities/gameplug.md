---
title: GamePlug
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gameplug-labs__gameplug.md
updated: 2026-08-15
confidence: medium
---

# GamePlug

C++ multi-API interception framework for Windows game modders and developers who need a reusable injection and overlay layer across rendering backends. Hooks Vulkan and DirectX 9/10/11/12 via proxy DLLs (`dinput8.dll`, `version.dll`, `winmm.dll`), loads plugins through a unified C++ interface with shared Dear ImGui context, and supports both 32-bit and 64-bit targets. Built with CMake (C++23); uses MinHook, SafetyHook, Dear ImGui, spdlog, and volk. Additional capabilities include D3D9 texture replacement and dumping, configurable resolution overrides, and keyboard toggles for the overlay. (source: wiki/sources/descriptions/gameplug-labs__gameplug.md)

## Links

- Repo: https://github.com/gameplug-labs/gameplug

## Related

[[present-hook]] · [[hydrahook]] · [[d3dhook-imgui]] · [[kiero2]] · [[vulkan-hook]] · [[directxhook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
