---
title: UniversalHookX
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/bruhmoment21__UniversalHookX.md
updated: 2026-08-17
confidence: medium
---

# UniversalHookX

Windows C++ DLL library for universal graphics API hooking with Dear ImGui overlay support across DirectX 9/9Ex, 10, 11, 12, OpenGL (`wglSwapBuffers`), and Vulkan (`vkQueuePresentKHR`). Each backend follows the same hooking pattern: dummy device creation to obtain vtable pointers, then Present/swap-path interception with compile-time backend selection. Aimed at game security researchers and overlay developers studying cross-backend graphics API interception and ImGui rendering techniques. (source: wiki/sources/descriptions/bruhmoment21__UniversalHookX.md)

## Links

- Repo: https://github.com/bruhmoment21/UniversalHookX

## Related

[[present-hook]] · [[d3dhook-imgui]] · [[kiero2]] · [[hydrahook]] · [[gameplug]] · [[vulkan-hook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
