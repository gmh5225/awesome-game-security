---
title: TMSRecomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/godofknife__TMSRecomp.md
updated: 2026-11-24
confidence: medium
---

# tms-recomp

Static recompilation of the Nintendo Switch build of *Tokyo Mirage Sessions #FE Encore* into a native **Windows or Linux** desktop program that runs against the player’s own game assets—study material for console lifting, high-level emulation (HLE), and proprietary-engine PC ports rather than live anti-cheat or online security work. (source: wiki/sources/descriptions/godofknife__TMSRecomp.md)

## Stack

- **Lift:** Python **AArch64→C++** lifter; **Clang** + **CMake** build.
- **Runtime:** C++ host emulating Switch kernel, IPC, filesystem, audio, and movie services.
- **Graphics:** **NVN→Vulkan** with optional **DLSS** and **FSR** upscaling; **SDL3** input; SPIR-V shader tooling.
- **Validation:** Instruction-level diff tests; Python utilities for setup, packaging, and subtitles.
- **Mods:** Documented lifting pipeline with saves/mods support in the BYO-dump workflow.

## Audience

Reverse engineers and porting researchers comparing Switch static-recomp pipelines beside [[smo-recomp]], [[letsgo-recomp]], and [[timelink]]. Users must supply their own dump; the repository ships no retail assets.

## Links

- Repo: https://github.com/godofknife/TMSRecomp

## Related

[[smo-recomp]] · [[letsgo-recomp]] · [[totk-pc-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]