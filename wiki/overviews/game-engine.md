---
title: Game Engine
kind: overview
topics: [game-engine]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md
  - wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md
  - wiki/sources/descriptions/zhitkur__DayZzz.md
updated: 2026-07-17
confidence: high
---



# Game Engine

Engine internals, plugins, detectors, and SDK workflows that underpin modding, reverse engineering, and anti-cheat integration points—especially Unreal, Unity ([[il2cpp]] / Mono), Source, Godot, and custom engines. (source: wiki/sources/skills/game-engine.md)

## Key sub-areas

**Engines:** Unreal (GObjects/GNames/GWorld, Dumper-7/UE4SS), Unity (IL2CPPDumper + metadata, Mono/dnSpy), Source (NetVars / CreateInterface), Godot/Lumix plugins.

**Security-relevant surfaces:** object models and property offsets, rendering hooks ([[present-hook]]), network replication, engine-specific AC protection categories in the README. UE4 static-variable obfuscation (e.g. [[static-variables-obfuscator-ue4]]) raises the cost of memory scanners like Cheat Engine against non-dynamic game data. (source: wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md) Per-title Unreal dumps such as Fortnite FLTokens/offsets ([[fortnite-fltokens-and-offsets]]) show how quickly build-bound token and offset maps go stale. (source: wiki/sources/descriptions/zinx-YT__Fortnite-Fltokens-and-offsets.md)


**SDK generation:** UE version signatures → dumpers; Unity `global-metadata.dat` + `GameAssembly.dll` / `libil2cpp.so`; Source ClientClass → RecvTable maps. Per-title DayZ SDK/modding workflows (e.g. [[dayzzz]]) sit in the same Cheat SDK CodeGen / overlay lane. (source: wiki/sources/descriptions/zhitkur__DayZzz.md)

## Related concepts

[[il2cpp]] · [[present-hook]] · [[frida]] (mobile IL2CPP) · [[static-variables-obfuscator-ue4]] · [[fortnite-fltokens-and-offsets]] · [[dayzzz]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]



## README map

`Game Engine` (~134 links: guides, source, Unreal/Unity/Godot/Lumix plugins, detectors). Adjacent: `Game Assets` / `Game Hot Patch` (UE/glTF tools, HybridCLR/xLua), `Game Develop` (MCP server/security + AI Agents), `AI` image→3D/sprite pipelines, plus Cheat SDK CodeGen and Anti Cheat `Game Engine Protection:*` subtrees. (source: wiki/sources/README-categories.md)
