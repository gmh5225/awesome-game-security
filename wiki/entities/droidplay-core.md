---
title: DroidPlay Core
kind: entity
topics: [game-hacking, mobile-security, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/enjoyerofslop__droidplay-core.md
  - wiki/sources/README-categories.md
updated: 2026-11-12
confidence: medium
---

# DroidPlay Core

Native **nxnative** runtime and **DroidPlay** toolchain that packages user-supplied Nintendo Switch dumps into Android apps so a title’s own **ARM** code runs on the device instead of inside a full-system emulator. Android-focused branch of the nxnative engine: **C** and **Java** with Python tooling, **Vulkan** graphics, and a BYO game build pipeline. The stack rewrites Switch **NSO** modules where needed, emulates **Horizon** system calls and SDK services, and applies per-title profiles for shaders, patches, and build-specific fixes. Targets **arm64 Android 10+** with legitimately dumped **NSP** or **XCI** content; MIT license; users supply dumps and `prod.keys`. Useful for Switch binary loading, platform bring-up, compatibility work, and reverse engineering. (source: wiki/sources/descriptions/enjoyerofslop__droidplay-core.md)

## Positioning

Contrasts with JIT/HLE emulators such as [[yuzu-android]] and [[opensw]]: emphasis is **native AArch64 execution** with Horizon syscall/service emulation rather than dynarmic-style CPU recompilation of a desktop emulator port. Pairs with mobile graphics research in [[overviews/mobile-security]], console toolchain study in [[overviews/game-hacking]], and Switch binary/loader RE in [[overviews/reverse-engineering]]. Adjacent non-VM hosts include [[android-compatibility-layer]].

## Links

- Repo: https://github.com/enjoyerofslop/droidplay-core

## Related

[[overviews/game-hacking]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[yuzu-android]] · [[opensw]] · [[android-compatibility-layer]]
