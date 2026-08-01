---
title: Il2CppAssemblyUnhollower
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/knah__Il2CppAssemblyUnhollower.md
updated: 2026-08-01
confidence: medium
---

# Il2CppAssemblyUnhollower

Unity [[il2cpp]] **assembly unhollower**: generates proxy .NET assemblies from IL2CPP metadata so C# mods can interact with IL2CPP-compiled Unity games as if they were standard Mono assemblies. Processes `global-metadata.dat` and binary dumps to reconstruct type definitions, method signatures, and field layouts, emitting wrapper assemblies that delegate calls to native IL2CPP methods. Targets Unity modders and game-security researchers on IL2CPP builds where direct .NET reflection is unavailable. (source: wiki/sources/descriptions/knah__Il2CppAssemblyUnhollower.md)

Complements static dumpers such as [[il2cppdumper]], reflection-driven [[il2cpp-runtime-dumper]], and in-process inspectors such as [[unityexplorer]] (which also uses unhollowing for IL2CPP) on the cheat / game engine explorer:Unity lane.

## Links

- Repo: https://github.com/knah/Il2CppAssemblyUnhollower

## Related

[[il2cpp]] · [[il2cpp-runtime-dumper]] · [[il2cppdumper]] · [[unityexplorer]] · [[mono]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
