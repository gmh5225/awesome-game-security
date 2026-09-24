---
title: URKit
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Jadis0x__URKit.md
  - wiki/sources/README-categories.md
updated: 2026-09-24
confidence: medium
---

# URKit

Native C++ mod SDK generator for Windows x64 Unity (Mono/IL2CPP) and Unreal Engine titles (Jadis0x). From a target game executable it emits ready-to-build CMake projects with proxy-DLL or injector attach paths, SafetyHook function hooks, scene-change callbacks, and ImGui overlays. The toolchain bundles an SDK generator, project updater, and optional MCP development server with in-game DevBridge for build, deploy, and runtime inspection. Experimental UE support covers runtime discovery, ProcessEvent hooking, and typed header generation. Listed under Cheat / RE Tools. (source: wiki/sources/descriptions/Jadis0x__URKit.md)

Complements codegen libraries such as [[sdkgenny]], [[luagenny]], and [[ue4genny]] with a full mod-project scaffold rather than header emit alone.

## Links

- Repo: https://github.com/Jadis0x/URKit

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[sdkgenny]] · [[luagenny]] · [[ue4genny]] · [[il2cpp]] · [[unreal-object-model]]
