---
title: UPGDSED
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/hfiref0x__UPGDSED.md
updated: 2026-08-05
confidence: medium
---

# UPGDSED

**Universal PatchGuard and DSE Disable** — a Windows C tool for disabling **PatchGuard** (Kernel Patch Protection) and **Driver Signature Enforcement (DSE)** at runtime. Techniques include exploiting vulnerable signed drivers, manipulating **CI.dll** globals, and patching **KPP context** data to load unsigned kernel drivers and modify protected kernel structures. Targets Windows 7 through 11; aimed at kernel researchers studying [[patchguard]] internals, DSE bypass methods, and Windows kernel security mechanisms. (source: wiki/sources/descriptions/hfiref0x__UPGDSED.md)

Adjacent to version-specific PG PoCs such as [[pg1903]], CI/`g_CiOptions` controllers such as [[kvc]], and clock/cert DSE abuse such as [[pastdse]] — here the focus is a multi-method runtime disable spanning both KPP and DSE via [[byovd]]-class primitives and CI/KPP structure manipulation.

## Links

- Repo: https://github.com/hfiref0x/UPGDSED

## Related

[[patchguard]] · [[pg1903]] · [[pastdse]] · [[kvc]] · [[bootbypass]] · [[byovd]] · [[overviews/windows-kernel]]
