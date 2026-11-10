---
title: Mario Kart World PC Recomp (MKW-THWOMP)
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/STS78721__MKW-THWOMP.md
updated: 2026-11-10
confidence: medium
---

# mkw-thwomp

**MKW-THWOMP** ([STS78721/MKW-THWOMP](https://github.com/STS78721/MKW-THWOMP)) is a work-in-progress static recompilation that ports *Mario Kart World* (Nintendo **Switch 2**, update **1.8.0**) to native **Windows** with a **Vulkan** renderer. Users supply their own legally dumped **exefs** and **romfs** assets; the repository ships no game binaries. The project targets reverse engineers, preservationists, and researchers studying Switch 2 binaries, graphics APIs, and large-scale static recompilation—not a finished commercial port or online anti-cheat research. (source: wiki/sources/descriptions/STS78721__MKW-THWOMP.md)

## Lift pipeline

A **recomp pipeline** lifts the title’s **ARM64** machine code to **C**, with **Python** tooling and Windows **batch** scripts driving codegen, build, and packaging under **MSYS2** and **Clang**. Progress is explicitly **WIP**. (source: wiki/sources/descriptions/STS78721__MKW-THWOMP.md)

## Runtime host

The host runtime emulates **Switch 2** OS services and maps **NVN 2** onto **Vulkan** (Vulkan **1.3** GPU required). **SDL** covers input, audio, and filesystem integration on Windows. (source: wiki/sources/descriptions/STS78721__MKW-THWOMP.md)

## Research use

Apply [[static-runtime-evidence]] the same way as [[dkb-pc-recomp]], [[totk-pc-recomp]], [[smo-recomp]], and [[letsgo-recomp]]: separate lifted guest ARM64 from reimplemented Switch 2 services and NVN 2 host paths before citing renderer or gameplay fidelity. (source: wiki/sources/descriptions/STS78721__MKW-THWOMP.md)

## Links

- Repo: https://github.com/STS78721/MKW-THWOMP

## Related

[[dkb-pc-recomp]] · [[totk-pc-recomp]] · [[smo-recomp]] · [[letsgo-recomp]] · [[xcx-recomp]] · [[xc2-recomp]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]]
