---
title: YW4 Recomp
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/ILFforever__YW4Recomp.md
  - wiki/sources/README-categories.md
updated: 2026-11-18
confidence: medium
---

# yw4recomp

Native **Windows and Linux** port of *Yo-kai Watch 4++* (Nintendo Switch firmware **2.2.0**) via **static recompilation** in the **N64Recomp** style: verified main **NSO** AArch64 machine code lifts to generated C/C++ sources while users supply their own dumped game assets at build and run time—no commercial binaries ship in the repository. (source: wiki/sources/descriptions/ILFforever__YW4Recomp.md)

## Stack

- **Lift:** Python AArch64-to-C recompiler; CMake build integration; golden instruction tests against ARM64 reference runs.
- **RE tooling:** Ghidra-oriented analysis and recon scripts for Switch module layout and lift boundaries.
- **Runtime:** C/C++ host high-level-emulates Nintendo SDK services; audio, filesystem, and input on desktop targets.
- **Graphics:** Vulkan path with shader translation and a custom engine-level renderer (resolution scaling, widescreen, TAA, optional **DLSS** or **FSR**).
- **Distribution:** Rust **Tauri** launcher for Windows/Linux packaging; **LayeredFS**-style mod support.

## Audience

Developers and researchers studying console binary reverse engineering, static recompilation pipelines, and native ports of closed-platform games—not anti-cheat or live online security. Apply [[static-runtime-evidence]] the same way as [[smo-recomp]], [[letsgo-recomp]], and [[totk-pc-recomp]]: separate lifted guest code from reimplemented Horizon/SDK host services before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/ILFforever__YW4Recomp.md)

## Links

- Repo: https://github.com/ilfforever/yw4recomp

## Related

[[smo-recomp]] · [[letsgo-recomp]] · [[totk-pc-recomp]] · [[timelink]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]