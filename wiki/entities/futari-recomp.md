---
title: Futari Recomp
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/springah__futari_recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-07
confidence: medium
---

# Futari Recomp

**Futari Recomp** (springah/futari_recomp) statically recompiles the Xbox 360 retail build of *Mushihimesama Futari* into native Windows and macOS executables instead of emulating the console at runtime. Listed under README **Xbox** (static recompilation of Mushihimesama Futari via ReXGlue, optional Vulkan renderer Renut; BYO assets and dumping docs). (source: wiki/sources/descriptions/springah__futari_recomp.md) (source: wiki/sources/README-categories.md)

## Static recompilation

CMake/C++ project bundling the **ReXGlue** SDK for PowerPC guest lift, Xbox kernel/filesystem abstractions, and a **Renut** graphics layer with Direct3D and Vulkan backends, shader caching, and tooling to dump or translate guest GPU programs. Python utilities and documentation cover XEX module analysis, disc image extraction, and preparing user-supplied game data through a launcher workflow. (source: wiki/sources/descriptions/springah__futari_recomp.md)

## Stack and audience

Targets reverse engineers and preservation-oriented developers studying Xbox 360 binaries, static recompilation pipelines, and how legacy arcade-style titles move to modern desktop platforms— not online anti-cheat or live-service analysis. (source: wiki/sources/descriptions/springah__futari_recomp.md)

## Positioning

Sits in the README **Xbox** ReXGlue static-recomp cluster beside [[wwe-svr2009-recomp]] and [[nhl-legacy-remaster]], and XenonRecomp ports such as [[mcla-pc]] and [[dead-rising-2-case-zero-xenon-recomp]]. Pair XEX tooling with [[idaxex]] and [[ida-vmx128-helper]] for upstream Xenon binary work. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/springah/futari_recomp

## Related

[[wwe-svr2009-recomp]] · [[nhl-legacy-remaster]] · [[mcla-pc]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[recompiler]] · [[xenia]] · [[idaxex]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
