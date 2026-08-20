---
title: BizHawk
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/TASEmulators__BizHawk.md
updated: 2026-08-20
confidence: medium
---

# BizHawk

Multi-system **retro game emulator** built primarily for **tool-assisted speedrunning (TAS)** and deterministic frame-by-frame playback. Written mainly in **C# on .NET** with native **C and C++** emulation cores, it supports dozens of platforms including NES, SNES, Game Boy, GBA, Genesis, N64, Nintendo DS, PlayStation, and arcade systems through MAME. (source: wiki/sources/descriptions/TASEmulators__BizHawk.md)

Feature set includes **TAStudio** for movie recording and editing, **Lua scripting** with memory and input APIs, RAM search and watch tools, a hex editor, CPU debuggers with disassemblers, trace logging, savestates, rewind, and cheat decoders for Game Genie and GameShark codes. Aimed at TAS authors, game security researchers, and reverse engineers who need precise control over emulated game state to analyze mechanics, develop or test cheats, and study retro game internals in a reproducible environment.

Sits in the **retro multi-platform emulator** lane beside handheld-focused peers [[feather-gb]] and [[kevboy]], and complements live-memory tooling such as [[cheat-engine]] when work needs deterministic replay rather than attaching to a native PC process.

## Links

- Repo: https://github.com/TASEmulators/BizHawk (README tag: Multi-system C# emulator with memory inspection, rerecording, and per-core debugging tools for retro game analysis)

## Related

[[feather-gb]] · [[kevboy]] · [[gecko]] · [[cheat-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
