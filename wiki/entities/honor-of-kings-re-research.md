---
title: honor-of-kings-RE-research
kind: entity
topics: [mobile-security, reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md
updated: 2026-07-18
confidence: medium
---

# honor-of-kings-RE-research

Android reverse-engineering research workspace for Honor of Kings (sgame): client binaries, Tencent ACE / `libtersafe` surfaces, and related tooling. (source: wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md)

## What it covers

- Python / [[frida]] APK and ELF analysis: [[il2cpp]] parsing, fog-of-war logic, JNI / method-table discovery, native patching (e.g. `libtersafe`)
- IDA Pro helpers for actors, heroes, FOW managers, crypto, and ACE-related checks
- KernelPatch-style KPMs (`acepeek`) plus decompiled C dumps of anti-cheat driver paths for low-level memory inspection

Audience: mobile game-security and anti-cheat researchers studying Tencent’s protection stack and client attack surface.

## Links

- Repo: https://github.com/wwweeeqqu/honor-of-kings-RE-research

## Related

[[frida]] · [[il2cpp]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
