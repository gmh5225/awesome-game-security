---
title: Vulkan-Hook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Vulkan-Hook.md
updated: 2026-08-09
confidence: medium
---

# Vulkan-Hook

C++ Vulkan API hooking framework that intercepts `vkQueuePresentKHR` and other Vulkan rendering calls to inject overlay rendering inside Vulkan-based games on Windows x86/x64. Enables Dear ImGui overlay menus and ESP drawing by injecting custom rendering commands in the present path—Vulkan-specific hook patterns distinct from DirectX Present/vtable approaches. Aimed at game security researchers studying Vulkan rendering pipeline hooking and overlay techniques. (source: wiki/sources/descriptions/gmh5225__Vulkan-Hook.md)

## Links

- Repo: https://github.com/gmh5225/Vulkan-Hook

## Related

[[present-hook]] · [[d3dhook-imgui]] · [[asdf-overlay]] · [[kiero2]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
