---
title: KernelGDIDraw
kind: entity
topics: [graphics-api, windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/BadPlayer555__KernelGDIDraw.md
updated: 2026-08-31
confidence: medium
---

# KernelGDIDraw

Kernel-mode **drawing proof of concept** that hooks **`NtGdiDdDDISubmitCommand`** and renders overlay graphics through **win32k GDI routines**. Implemented in C/C++ as WDK-style driver code; uses **InfinityHook-based syscall interception** to reach the graphics submission path. Demonstrates **screen-update-synchronized drawing** tied to the display refresh flow while documenting practical drawbacks such as **extra latency**. Primary use case is low-level graphics-hook research and anti-cheat evasion experimentation. (source: wiki/sources/descriptions/BadPlayer555__KernelGDIDraw.md)

Sits in the same Ring0 GDI render-draw lane as [[krnl-gdi-render]] and [[kernel-drawing]], beside dxgkrnl-adjacent hook contexts such as [[rigel-driver]] (`NtGdiDdDDINetDispGetNextChunkInfo`) and export-hijack samples such as [[kernel-cheat-for-directx3d]]. Complements ETW syscall interception research under [[infinityhook]].

## Links

- Repo: https://github.com/BadPlayer555/KernelGDIDraw (README tag: `[Kernel + GDI]`)

## Related

[[krnl-gdi-render]] · [[kernel-drawing]] · [[dxgkrnl-hook]] · [[rigel-driver]] · [[infinityhook]] · [[trace-cleaner]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
