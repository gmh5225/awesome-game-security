---
title: VkHook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/sorche942__VkHook.md
updated: 2026-11-19
confidence: medium
---

# VkHook

Linux **implicit Vulkan layer** (C++20 / Meson; Vulkan 1.3) that sits between the application and the driver to post-process **swapchain** images and optionally captured **scene depth**. Targets native Vulkan titles and Direct3D games under Wine or Proton (DXVK, vkd3d-proton). Ships **OpenDLSS-NR (DLSS5)** on supported NVIDIA hardware, runtime compilation and chaining of **ReShade `.fx`** shaders, automatic or manual depth-buffer capture, and a **Dear ImGui** configuration overlay with input blocking on X11 and Wayland. Builds cover x86-64 and 32-bit Proton layouts; optional **Flatpak** Vulkan layer packaging. Useful for graphics hooking research, modding, and studying how Vulkan layers alter rendering without patching game binaries. (source: wiki/sources/descriptions/sorche942__VkHook.md)

Contrasts with Windows `vkQueuePresentKHR` hook frameworks such as [[vulkan-hook]]; sits beside Linux implicit-layer references such as [[vocem-overlay]], [[cyberpunk-better-shaders]], and [[ayypex]]; complements generic injectors such as [[reshade]] on the post-processing axis.

## Links

- Repo: https://github.com/sorche942/VkHook

## Related

[[present-hook]] · [[vocem-overlay]] · [[cyberpunk-better-shaders]] · [[vulkan-hook]] · [[reshade]] · [[imgui]] · [[kiero2]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]