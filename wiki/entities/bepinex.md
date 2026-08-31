---
title: BepInEx
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/BepInEx__BepInEx.md
updated: 2026-08-31
confidence: medium
---

# BepInEx

Plugin and modding framework for **Unity Mono**, **Unity IL2CPP**, and other **.NET-based games**. Primarily C# with chainloading, preloading, logging, and configuration systems for runtime plugin management, plus integrated patching and detour tooling so developers can extend or instrument game behavior on **Windows**, **Linux**, and **macOS**. Used by mod authors and game reverse-engineering communities as a stable loader for managed and native Unity targets. (source: wiki/sources/descriptions/BepInEx__BepInEx.md)

Upstream host for title-specific plugins and research scaffolds such as [[bepinex-il2cppbase]], runtime inspectors like [[unityexplorer]], Harmony moderation/AC plugins ([[wellsanticheat]], [[banmod]]), and debug/cheat command suites ([[danis-nightmare]]). Complements offline [[il2cpp]] dump/resolve tooling and runtime hook libraries such as [[monohook]] when the goal is a persistent in-process plugin host rather than one-off injection.

## Links

- Repo: https://github.com/BepInEx/BepInEx

## Related

[[bepinex-il2cppbase]] · [[unityexplorer]] · [[il2cpp]] · [[monohook]] · [[wellsanticheat]] · [[banmod]] · [[danis-nightmare]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
