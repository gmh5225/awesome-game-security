---
title: MCLA PC
kind: entity
topics: [reverse-engineering, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/3bdull4h2008__mcla-pc.md
  - wiki/sources/README-categories.md
updated: 2026-09-23
confidence: medium
---

# MCLA PC

**MCLA PC** (3bdull4h2008/mcla-pc) is a PC port that recompiles the Xbox 360 version of *Midnight Club: Los Angeles* into native C++ and runs it on Windows with a custom **Direct3D 12** renderer. Listed under README **Xbox**. (source: wiki/sources/descriptions/3bdull4h2008__mcla-pc.md)

## Static recompilation

Uses **XenonRecomp** for static PowerPC-to-C++ translation of the guest XEX binary. Intercepts **Xenos** GPU draw calls and replays them through a shader pipeline that decodes Xenos microcode to **DXIL**, with a **PSO cache** for translated pipeline state. (source: wiki/sources/descriptions/3bdull4h2008__mcla-pc.md)

## Host infrastructure

Includes an Xbox kernel host, **RPF3** packfile virtual filesystem, **VMX128** SIMD hooks, and Python tooling for guest address ownership, soak log analysis, and offline RPF3 archive forensics. (source: wiki/sources/descriptions/3bdull4h2008__mcla-pc.md)

## Stack and audience

Built primarily in C++ with **CMake**, **SDL3**, and **DirectX Shader Compiler**. Targets developers researching Xbox 360 recompilation, game reverse engineering, and native graphics translation rather than general-purpose emulation. (source: wiki/sources/descriptions/3bdull4h2008__mcla-pc.md)

## Links

- Repo: https://github.com/3bdull4h2008/mcla-pc

## Related

[[jsrf-recomp]] · [[recompiler]] · [[xenia]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
