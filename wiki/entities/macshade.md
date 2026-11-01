---
title: MacShade
kind: entity
topics: [graphics-api]
sources:
  - wiki/sources/descriptions/klotzbrocken__MacShade.md
updated: 2026-11-01
confidence: medium
---

# MacShade

macOS application that ports **ReShade 6.8**–style real-time post-processing and shader overlays to games on Apple hardware. A SwiftUI launcher handles game discovery, bundled ReShade FX collections, and per-title presets (classic FPS ports such as Doom, Quake, and Unreal Tournament). The native stack is ReShade-derived: `libmacshade.dylib`, a helper filter tool for process attach, and injection bridges for **Metal**, **OpenGL**, and **Vulkan** (MoltenVK), using **dyld interposing** on the inject path. Primary languages: Swift, C++, Objective-C++, and CMake for the native library. Targets players and modders; the same frame-capture and in-process graphics hooking patterns are relevant to game security and anti-cheat research. (source: wiki/sources/descriptions/klotzbrocken__MacShade.md)

## Links

- Repo: https://github.com/klotzbrocken/MacShade

## Related

[[reshade]] · [[present-hook]] · [[opengl32-enhancer]] · [[overviews/graphics-api]]
