---
title: Vulkan Wallhack
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/DrNseven__VulkanWallhack.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Vulkan Wallhack

**VulkanWallhack** (DrNseven/VulkanWallhack) is a Windows injectable **Visual Studio C++ DLL** that hooks **Vulkan** graphics APIs to expose **players or geometry through walls** in titles that use the Vulkan renderer. **MinHook** provides x86/x64 function detours; bundled Vulkan headers let hooks intercept the render pipeline **early in process startup** (inject before first frames). Runtime hotkeys toggle wallhack, **alternate coloring**, and debug logging; comma/period keys **brute-force vertex-buffer strides** to locate draw data when engine layouts differ—a documented default stride targets **Valheim-style** model recognition, illustrating how stride guessing couples with API hooks to manipulate **depth or visibility**. (source: wiki/sources/descriptions/DrNseven__VulkanWallhack.md)

Aimed at game security, anti-cheat, and reverse-engineering audiences studying **client-side visual cheats** and what defenders must monitor (hooked Vulkan entry points, pipeline/draw anomalies, in-process detours). Sits in the README `Vulkan` Hook lane beside universal hook scaffolds such as [[universalhookx]], [[vulkan-hook]], and [[kiero2]], and beside sibling DrNseven DX samples such as [[d3d11-wallhack]]—focused on **draw-path stride guessing + visibility manipulation** rather than Present-only overlays.

## Architecture highlights

| Component | Role |
|-----------|------|
| MinHook | Vulkan API detours on x86/x64 |
| Early inject | Intercept render pipeline before first frames |
| Stride bruteforce | Locate draw data when buffer layouts vary |
| Hotkey UI | Toggle wallhack, alternate coloring, debug logging |
| Valheim default stride | Example vertex layout for model recognition |

See [[draw-call-hook]] for depth/visibility interception patterns and [[frame-observation-boundary]] before attributing Vulkan hook evidence.

## Links

- Repo: https://github.com/DrNseven/VulkanWallhack

## Related

[[draw-call-hook]] · [[vulkan-hook]] · [[universalhookx]] · [[kiero2]] · [[d3d11-wallhack]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
