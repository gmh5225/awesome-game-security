---
title: NHL Legacy Remaster
kind: entity
topics: [reverse-engineering, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/megarohas__nhl-legacy-remaster.md
  - wiki/sources/README-categories.md
updated: 2026-10-16
confidence: medium
---

# NHL Legacy Remaster

**NHL Legacy Remaster** (megarohas/nhl-legacy-remaster) is a Windows port and modernization project for EA Sports *NHL Legacy Edition* (Xbox 360), recompiling the original game to **x86-64** with the **ReXGlue SDK** instead of emulating the console. Listed under README **Xbox**. Does not redistribute game assets. (source: wiki/sources/descriptions/megarohas__nhl-legacy-remaster.md)

## Port stack

Core work is **C++** and **CMake** for the port, launcher, and runtime hooks. The host renderer targets **DirectX 12** or **Vulkan** on PC. (source: wiki/sources/descriptions/megarohas__nhl-legacy-remaster.md)

## RE and mod tooling

A large **Python** toolchain parses EA archive formats, roster databases, uniforms, and Frostbite-era *NHL 24* assets. Documented workflows include manifest-driven codegen from `default.xex`, function hooking, save and franchise-data patching, and research utilities for binaries, textures, and game databases. (source: wiki/sources/descriptions/megarohas__nhl-legacy-remaster.md)

## Audience

Targets developers and researchers studying legacy sports-game binaries, porting techniques, and client-side modding pipelines—not online anti-cheat. End users combine legally owned Xbox 360 game files with built mods for an updated franchise experience on PC. (source: wiki/sources/descriptions/megarohas__nhl-legacy-remaster.md)

## Links

- Repo: https://github.com/megarohas/nhl-legacy-remaster

## Related

[[mcla-pc]] · [[dead-rising-2-case-zero-xenon-recomp]] · [[jsrf-recomp]] · [[idaxex]] · [[ida-vmx128-helper]] · [[xenia]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
