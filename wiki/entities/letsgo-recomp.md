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

Native Windows port of *Pokémon: Let's Go, Eevee!* and *Pikachu!* (Switch firmware **1.0.0**) built with **static recompilation** on the LAS Recomp stack—Switch AArch64 modules lift to C and compile for x86-64 while a custom runtime high-level-emulates Horizon services, maps NVN graphics to Vulkan, and handles audio, filesystem, and input. Tooling mixes C/C++, Objective-C++ launcher UI, and Python/Zig lift/patch utilities driven by user-supplied exefs/romfs dumps. (source: wiki/sources/descriptions/raulzrrs__letsgo-recomp.md)

## Research notes

- Resolution and frame-rate options, AMD FSR upscaling/frame generation, mod hooks, memory watch, profiling, and RenderDoc integration for graphics validation.
- Audience: reverse engineers studying Switch binary translation and runtime replacement; players who legally own the title and provide their own extracted dumps (no assets in repo).

## Links

- Repo: https://github.com/raulzrrs/letsgo-recomp

## Related

[[smo-recomp]] · [[sf33rdsxbrecompo]] · [[ngbrecomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
