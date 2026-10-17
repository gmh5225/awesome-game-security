---
title: sc2-android-recomp
kind: entity
topics: [reverse-engineering, mobile-security, graphics-api]
sources:
  - wiki/sources/descriptions/elkir0__sc2-android-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-17
confidence: medium
---

# sc2-android-recomp

Toolkit and documented methodology for **statically recompiling** a legacy x86-32 Windows game engine to native **ARM64**, with StarCraft II on Android as the reference target. Ships only original helper code—no game binaries or assets—and expects users to generate lifted C and runtime artifacts locally from a legitimate install. (source: wiki/sources/descriptions/elkir0__sc2-android-recomp.md)

## Stack

- **Correctness:** per-function differential testing against Unicorn as a lift oracle.
- **Graphics:** offline D3D9 SM2/3 bytecode → SPIR-V translation; Android Bionic and Vulkan porting helpers.
- **Assets / lift:** MPQ extraction utilities; incremental **pcrecomp** lifter patches for atomics, MMX, and SSE edge cases.
- **Languages:** Python, C/C++, ARM64 assembly, shell scripts; NDK and Vulkan toolchain.

README category: Cheat / RE Tools (static recompilation pipeline).

## Audience

Researchers studying PE lifting, binary translation correctness, legacy DirectX interoperability, and offline personal-use engine porting—not live multiplayer anti-cheat bypass. (source: wiki/sources/descriptions/elkir0__sc2-android-recomp.md)

## Links

- Repo: https://github.com/elkir0/sc2-android-recomp

## Related

[[nfsu2recomp]] · [[motorstorm-mv-recomp]] · [[saturnkit]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
