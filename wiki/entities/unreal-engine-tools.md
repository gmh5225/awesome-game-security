---
title: Unreal Engine Tools
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/cheat-engine__UnrealEngineTools.md
updated: 2026-08-17
confidence: medium
---

# Unreal Engine Tools

Official **Cheat Engine Lua scripts** (cheat-engine/UnrealEngineTools) that automatically discover and map Unreal Engine runtime structures in a target game process without requiring injection. **UEInfoScanner** locates name pools (`GNames` / FName data), object arrays, `UObject` and `UClass` layouts, `FProperty` chains, and related offsets across UE4 and UE5 builds using memory scans, vtable checks, and signature-style probing. **UEInfoStructureDissect** builds Cheat Engine Structure Dissect definitions from discovered classes and objects, including an FName-to-string custom type for readable field names. The scripts add Unreal Engine menu entries in Cheat Engine for initializing scans, monitoring status, and applying recovered layouts interactively. (source: wiki/sources/descriptions/cheat-engine__UnrealEngineTools.md)

Primary use cases are reverse engineering Unreal Engine games, inspecting object hierarchies and properties in memory, and supporting game-security or cheat-research workflows that rely on [[cheat-engine]]. Sits in the Cheat / Game Engine Explorer:Unreal lane beside live explorers such as [[unrealengine4-swissknife]] and external dumpers such as [[unrealdumper-4-25]], but emphasizes no-inject CE Structure Dissect workflows on top of [[unreal-object-model]] globals.

## Links

- Repo: https://github.com/cheat-engine/UnrealEngineTools

## Related

[[cheat-engine]] · [[unreal-object-model]] · [[unrealengine4-swissknife]] · [[unrealdumper-4-25]] · [[ue4genny]] · [[regenny]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
