---
title: SPR Recomp Project
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md
  - wiki/sources/README-categories.md
updated: 2026-11-16
confidence: medium
---

# spr-recomp-project

**SPR Recomp** ([Elie-0066/SPR-Recomp-Project](https://github.com/Elie-0066/SPR-Recomp-Project)) is an unofficial static recompilation effort that lifts Nintendo **Switch 2** **ARM64** game code for *Splatoon Raiders* into a native **Windows x86-64** executable with a **Vulkan** renderer. Users supply legally obtained dumps; the repository ships no proprietary game assets. (source: wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md)

## Pipeline

**Python** lifters and build orchestration drive codegen and patch application from user-supplied dumps. Architecture follows prior *Tears of the Kingdom* and *Donkey Kong Bananza* recomp efforts. An installer compiles lifted output locally on the user machine. (source: wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md)

## Runtime host

A large **C** runtime emulates Switch OS services for audio, input, and graphics. **NVN2** / **Maxwell** guest shaders translate to **SPIR-V** for the PC **Vulkan** path. (source: wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md)

## Validation

**Unicorn** supports differential testing of the lifter without shipping proprietary assets. (source: wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md)

## Research use

Targets reverse engineers and preservation-minded developers studying Switch 2 binaries on PC—not commercial anti-cheat integration. Apply [[static-runtime-evidence]] labeling alongside [[totk-pc-recomp]], [[dkb-pc-recomp]], [[mkw-thwomp]], and [[emblem-weave]]. (source: wiki/sources/descriptions/Elie-0066__SPR-Recomp-Project.md)

Listed under **Cheat / Source** (README Switch 2 static recompilation lane).

## Links

- Repo: https://github.com/Elie-0066/SPR-Recomp-Project (Static recompilation of *Splatoon Raiders* Switch 2→Windows x86-64 with Vulkan; BYO dump, no game assets)

## Related

[[totk-pc-recomp]] · [[dkb-pc-recomp]] · [[mkw-thwomp]] · [[emblem-weave]] · [[timelink]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]