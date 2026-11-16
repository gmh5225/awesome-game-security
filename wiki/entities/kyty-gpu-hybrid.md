---
title: Kyty GPU Hybrid
kind: entity
topics: [graphics-api, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/zorde23__kyty-gpu-hybrid.md
updated: 2026-11-16
confidence: medium
---

# Kyty GPU Hybrid

**Kyty-gpu-hybrid** (zorde23/kyty-gpu-hybrid) is a development branch of the **Kyty PlayStation 5 emulator** focused on a **hybrid graphics stack** that executes guest GPU work on the host PC. (source: wiki/sources/descriptions/zorde23__kyty-gpu-hybrid.md)

The tree is primarily **C++20** with **CMake**, plus a **Rust pipeline-sharing server** that distributes compiled GPU pipeline data across installs. A guest-side **command processor** (PM4 dispatch, tiling, and PSSR-related paths) couples to a host **Vulkan** renderer built with SPIR-V tooling, compute tiler shaders, and buffer/texture caches. Supporting layers include **SDL3** and **ImGui** for the UI, **Zydis** and **xbyak** for guest code patching, **ZArchive** for compressed disc images, and **OpenXR** with **Opus** for headset and DualSense audio. (source: wiki/sources/descriptions/zorde23__kyty-gpu-hybrid.md)

README describes it as a **Kyty PS5 GPU stack** (command processor, shader recompiler, Vulkan) packaged as a **DLL** for hybrid PS5-on-PC compatibility layers (**GPL-2.0** fork). It targets emulator authors, graphics researchers, and reverse engineers studying how PS5 titles drive the GPU and iterating on compatibility and rendering correctness—not online anti-cheat bypass.

## Links

- Repo: https://github.com/zorde23/kyty-gpu-hybrid

## Related

[[slopstation]] · [[reaperpy]] · [[prospero-eden-encore]] · [[gbar5]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]