---
title: Dead Rising 2 Case Zero Xenon Recomp
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-07
confidence: medium
---

# Dead Rising 2 Case Zero Xenon Recomp

**Dead Rising 2: Case Zero Xenon Recomp** (wivi514/Dead_Rising_2_Case_Zero_Xenon_Recomp) statically recompiles the Xbox 360 exclusive *Dead Rising 2: Case Zero* (XBLA) into a native Windows/Linux port without a full emulator. Listed under README **Xbox**. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md)

## Static recompilation

Uses **XenonRecomp** and **XenosRecomp** for ahead-of-time PowerPC guest translation, executed in a custom C++ runtime with a **Vulkan** renderer, SDL input, ffmpeg-based **XMA** audio, and kernel high-level emulation with honest-failure stubs. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md)

## Tooling and documentation

Ships Python and C++ utilities for STFS/XEX package extraction, shader translation, GPU PM4 command processing, and automated jump-table recovery, with documentation on Xbox 360 binary analysis and recompilation pitfalls. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md)

## Stack and audience

Built in C++ and Python with HLSL shaders and CMake. Targets researchers and developers studying Xbox 360 reverse engineering, static recompilation, and game preservation—not live anti-cheat analysis. (source: wiki/sources/descriptions/wivi514__Dead_Rising_2_Case_Zero_Xenon_Recomp.md)

## Links

- Repo: https://github.com/wivi514/Dead_Rising_2_Case_Zero_Xenon_Recomp

## Related

[[mcla-pc]] · [[jsrf-recomp]] · [[recompiler]] · [[xenia]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
