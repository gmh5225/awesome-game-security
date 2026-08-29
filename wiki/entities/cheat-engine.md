---
title: Cheat Engine
kind: entity
topics: [game-hacking, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/cheat-engine__cheat-engine.md
  - wiki/sources/descriptions/cheat-engine__UnrealEngineTools.md
  - wiki/sources/descriptions/cheat-engine__ControllerMode.md
  - wiki/sources/descriptions/bbfox0703__Mydev-Cheat-Engine-Tables.md
  - wiki/sources/descriptions/FreeER__CE-Extensions.md
  - wiki/sources/descriptions/Skyrimfus__CE-lua-extensions.md
  - wiki/sources/descriptions/JasonGoemaat__CheatEngineMonoHelper.md
  - wiki/sources/descriptions/NulledNah__cheat-engine-undetectable.md
  - wiki/sources/descriptions/Hexorg__CheatEngineTables.md
  - wiki/sources/descriptions/Eruditi__CE-MCP-Plugin.md
  - wiki/sources/descriptions/abhijeetadarsh__CTTrainer.md
updated: 2026-08-29
confidence: medium
---

# Cheat Engine

**Cheat Engine** (cheat-engine/cheat-engine) is the open-source reference **memory analysis and game-modding IDE**. It combines memory scanning, debugging, disassembly, **Lua** scripting, speedhack, code injection, and a cheat-table / trainer-maker workflow in a graphical environment, with both **user-mode** and optional **kernel-mode driver (DBVM)** components. The large **Delphi/Pascal and C** codebase includes cross-platform support elements. (source: wiki/sources/descriptions/cheat-engine__cheat-engine.md)

Mainly useful for game-security researchers, reverse engineers, and modding communities studying runtime memory modification, scan workflows, and how anti-cheat products detect CE-style tooling. Ecosystem extensions include official Unreal Engine Lua tooling ([[unreal-engine-tools]]), gamepad UI add-on [[controller-mode]], community Lua workflow packs such as [[ce-lua-extensions]] and [[ce-extensions]], Mono introspection helpers such as [[cheatengine-mono-helper]], multi-game `.CT` table collections such as [[mydev-cheat-engine-tables]] and the large forum-curated archive [[cheat-engine-tables]], standalone trainers that import `.CT` tables such as [[freeplay]] and [[cttrainer]], AC-evasion research forks such as [[cheat-engine-undetectable]], DMA plugins ([[cheat-engine-dma-plugin]], [[cheat-engine-ceserver-pcileech]]), remote ceserver ports ([[ceserver-rawmem]], [[wasm-ceserver]]), IDA bridges ([[ce-tracer-ida]], [[doffset]]), agent bridges ([[cheatengine-mcp-bridge]], [[ce-mcp-plugin]], [[dsh-cheatengine]]), and detection research samples ([[detection-cheat-engine]], [[cedetector]]).

## Links

- Repo: https://github.com/cheat-engine/cheat-engine

## Related

[[unreal-engine-tools]] · [[controller-mode]] · [[ce-lua-extensions]] · [[ce-extensions]] · [[cheatengine-mono-helper]] · [[mydev-cheat-engine-tables]] · [[cheat-engine-tables]] · [[freeplay]] · [[cttrainer]] · [[cheat-engine-undetectable]] · [[cheat-engine-dma-plugin]] · [[cheat-engine-ceserver-pcileech]] · [[ceserver-rawmem]] · [[ce-tracer-ida]] · [[detection-cheat-engine]] · [[intro-to-gamehacking]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
