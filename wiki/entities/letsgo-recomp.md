---
title: Let's Go Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/raulzrrs__letsgo-recomp.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: medium
---

# letsgo-recomp

Native Windows port of *Pokémon: Let's Go, Eevee!* and *Pikachu!* (Switch firmware **1.0.0**) built with **static recompilation** on the **LAS Recomp** stack—Switch AArch64 executable modules lift to C and compile for x86-64 while a custom runtime high-level-emulates Horizon system services instead of conventional CPU emulation. (source: wiki/sources/descriptions/raulzrrs__letsgo-recomp.md)

## Stack

- **Lift:** Python and Zig toolchain for disassembly, lifting, patching, and one-time per-machine code generation from user-supplied exefs/romfs dumps.
- **Build:** Primarily C/C++; C++ for Vulkan and upscaling paths; Objective-C++ launcher UI.
- **Runtime:** Horizon system HLE, filesystem, audio, and controller input on Windows.
- **Graphics:** NVN mapped to Vulkan; resolution and frame-rate options; AMD FSR upscaling and frame generation.

## Research hooks

Developer-oriented instrumentation includes memory watch, profiling, RenderDoc integration, and mod support—useful for validating NVN→Vulkan translation and runtime boundaries beside static lift artifacts. (source: wiki/sources/descriptions/raulzrrs__letsgo-recomp.md)

## Audience

Reverse engineers and game-security researchers studying Switch binary translation and runtime replacement; players who legally own the title and provide their own extracted dumps (no game assets in the repository).

## Links

- Repo: https://github.com/raulzrrs/letsgo-recomp

## Related

[[smo-recomp]] · [[sf33rdsxbrecompo]] · [[ngbrecomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
