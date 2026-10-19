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

**VulkanWallhack** (DrNseven/VulkanWallhack) is a Windows injectable **C++ DLL** that hooks **Vulkan** rendering APIs to expose geometry through walls in Vulkan-backed titles. It uses **MinHook** for x86/x64 detours and bundled Vulkan headers so hooks can attach early in process startup. Hotkeys toggle wallhack modes and debug logging; comma/period keys **brute-force vertex-buffer strides** when engine layouts differ (documented default stride targets Valheim-style model recognition). (source: wiki/sources/descriptions/DrNseven__VulkanWallhack.md)

Sits in the README `Vulkan` Hook lane beside universal hook scaffolds such as [[universalhookx]], [[vulkan-hook]], and [[kiero2]] runtime API location—focused on **draw-path stride guessing + visibility manipulation** rather than Present-only overlays.

## Architecture highlights

| Component | Role |
|-----------|------|
| MinHook | Vulkan API detours on x86/x64 |
| Early inject | Intercept render pipeline before first frames |
| Stride bruteforce | Locate draw data when buffer layouts vary |
| Hotkey UI | Toggle wallhack, coloring, logging |

See [[draw-call-hook]] for depth/visibility interception patterns and [[frame-observation-boundary]] before attributing Vulkan hook evidence.

## Links

- Repo: https://github.com/DrNseven/VulkanWallhack

## Related

[[draw-call-hook]] · [[vulkan-hook]] · [[universalhookx]] · [[kiero2]] · [[d3d11-wallhack]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
