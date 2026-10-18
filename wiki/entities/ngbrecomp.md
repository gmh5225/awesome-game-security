---
title: Ninja Gaiden Black Recompiled
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gamboozino__ngbrecomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: medium
---

# ngbrecomp

Static recompilation port of *Ninja Gaiden Black* (2005 original Xbox) to native Linux and Windows. The xboxrecomp toolchain lifts the retail XBE into generated C; a custom runtime replaces Xbox kernel, audio, input, and graphics services. Direct3D calls are intercepted and rendered through a Vulkan backend (with optional xemu NV2A reference paths). Modern PC features include high resolution, widescreen, and keyboard-and-mouse input. Users supply their own disc assets. (source: wiki/sources/descriptions/gamboozino__ngbrecomp.md)

## Stack

- **Lift:** xboxrecomp static binary recompilation (XBE → C).
- **Runtime:** replacement kernel plus audio/input subsystems.
- **Graphics:** D3D intercept → Vulkan (CMake/C/C++ build).

## Audience

Preservationists and reverse engineers studying OG Xbox binary lifting, runtime recreation, and title-specific static recompilation beside emulator and other xboxrecomp forks such as [[jsrf-recomp]].

## Links

- Repo: https://github.com/gamboozino/ngbrecomp

## Related

[[jsrf-recomp]] · [[recompiler]] · [[xemu]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
