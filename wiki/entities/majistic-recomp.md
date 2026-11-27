---
title: Majistic Recomp
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/kelvynzucco__majistic-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-27
confidence: medium
---

# Majistic Recomp

**Majistic Recomp** (kelvynzucco/majistic-recomp) statically recompiles *Majin and the Forsaken Kingdom* from Xbox 360 retail data into a native Windows program by lifting PowerPC guest code to C++ with the **ReXGlue** and **ReIGlue** toolchain derived from [[xenia]]. Users supply their own disc assets; the repository ships no copyrighted game content. Listed under README **Xbox** (PPC lifting, D3D12/Vulkan runtimes, BYO-asset preservation tooling). (source: wiki/sources/descriptions/kelvynzucco__majistic-recomp.md) (source: wiki/sources/README-categories.md)

## Lift and runtime

**CMake**-driven prototype builds center on a large set of **ReXGlue** patches for **Direct3D 12** and **Vulkan** rendering, **XMA** audio, and frame-timing diagnostics, plus title-specific fixes for shaders, animation, camera, and UI behavior. (source: wiki/sources/descriptions/kelvynzucco__majistic-recomp.md)

## Launcher and tooling

A **Tauri** and **Rust** desktop launcher with web front-end assets orchestrates setup, save handling, updates, and shader prebuild export tooling backed by **SDL3**, **Dear ImGui**, **FFmpeg**, and **Tracy**. (source: wiki/sources/descriptions/kelvynzucco__majistic-recomp.md)

## Research use

Targets preservation researchers, porting developers, and reverse engineers studying **console-to-PC static recompilation**, **Xenos** GPU translation, and local **shader and pipeline reconstruction** from retail disc data—not live anti-cheat or online-service analysis. Apply [[static-runtime-evidence]] the same way as other ReXGlue Xbox 360 ports such as [[futari-recomp]] and [[wwe-svr2009-recomp]]. (source: wiki/sources/descriptions/kelvynzucco__majistic-recomp.md)

## Positioning

Sits in the README **Xbox** ReXGlue static-recomp cluster beside [[futari-recomp]], [[wwe-svr2009-recomp]], and [[nhl-legacy-remaster]], and XenonRecomp reference ports such as [[mcla-pc]] and [[dead-rising-2-case-zero-xenon-recomp]]. Pair guest lift boundaries with [[recompiler]] and HLE playback via [[xenia]] when comparing runtime vs ahead-of-time translation. (source: wiki/sources/descriptions/kelvynzucco__majistic-recomp.md)

## Links

- Repo: https://github.com/kelvynzucco/majistic-recomp

## Related

[[futari-recomp]] · [[wwe-svr2009-recomp]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[mcla-pc]] · [[recompiler]] · [[xenia]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]