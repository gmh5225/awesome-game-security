---
title: 3DS Game Fixes
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/simplysanatori__3ds-game-fixes.md
updated: 2026-11-12
confidence: medium
---

# 3DS Game Fixes

Catalog of **IPS patches and Action Replay–style cheat codes** that fix graphics glitches and quality-of-life issues in retail Nintendo 3DS titles for **Citra, Azahar, Zakuro**, and **Luma3DS** on hardware. Each title is organized by region and ships an IPS patch against the decompressed ExeFS code segment plus version-guarded cheats that write only when expected bytes are present. Fixes are developed via ARM disassembly and tracing, validated with headless emulator harnesses, GPU traces, and before/after screenshots. A machine-readable catalog and per-game notes document the instruction-level changes—aimed at high-resolution emulator play and lightweight binary-patch research rather than broad ROM or texture replacement. (source: wiki/sources/descriptions/simplysanatori__3ds-game-fixes.md) (source: wiki/sources/README-categories.md)

Sits in the README **Nintendo 3DS** lane beside LLE emulator [[3beans]] and Luma `.3gx` overlay templates [[ctr-composer]] / [[ocarina-ctr-composer]].

## Method

Fixes come from per-title **ARM disassembly and tracing**; a machine-readable catalog and per-game technical notes record how each glitch was found and which instructions changed. Validation uses **headless emulator harnesses**, GPU traces, and before/after screenshots. (source: wiki/sources/descriptions/simplysanatori__3ds-game-fixes.md)

## Links

- Repo: https://github.com/simplysanatori/3ds-game-fixes

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[3beans]] · [[ctr-composer]] · [[ocarina-ctr-composer]] · [[static-runtime-evidence]]
