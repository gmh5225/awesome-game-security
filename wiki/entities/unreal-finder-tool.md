---
title: Unreal Finder Tool
kind: entity
topics: [game-engine, game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/CorrM__Unreal-Finder-Tool.md
updated: 2026-08-26
confidence: medium
---

# Unreal Finder Tool

**C++ Unreal Engine runtime discovery and SDK generation utility** (CorrM). Extracts live engine data from running UE games and emits usable SDK output. Features include `GNames` and `GObjects` discovery, instance dumping, and SDK generation behind an ImGui-based interface. The codebase also bundles kernel-assisted memory read/write components and configuration profiles for different engine targets—useful for Unreal reverse engineering, game analysis, and downstream tooling workflows. Listed under cheat / SDK View. (source: wiki/sources/descriptions/CorrM__Unreal-Finder-Tool.md)

Sits in the Unreal SDK-generation lane beside all-in-one dumpers such as [[uedumper]], injection-based SDK dumpers such as [[ezfndev-uedumper]], in-process generators such as [[dumper-7]], and external pattern-scan workflows—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/CorrM/Unreal-Finder-Tool

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[clean-cheat]] · [[unreal-object-model]] · [[uedumper]] · [[ezfndev-uedumper]] · [[dumper-7]] · [[shh0yauedumper]] · [[re-ue4ss]]
