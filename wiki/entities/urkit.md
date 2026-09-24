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

**URKit** (Jadis0x/URKit) is a native **C++ modding framework** for Windows x64 **Unity** (Mono and IL2CPP) and **Unreal Engine** titles. Given a target game executable it emits a ready-to-build **CMake** project with attach loaders, runtime hooks, and optional in-game tooling for mod development, reverse engineering, and security research on commercial Windows games. (source: wiki/sources/descriptions/Jadis0x__URKit.md)

README category: Cheat / RE Tools.

## Attach and backends

- **Attach:** proxy-DLL loaders or an injector into the target process.
- **Unity:** Mono and IL2CPP backends.
- **Unreal (experimental):** runtime discovery, `ProcessEvent` hooking, and typed header generation.

## Mod capabilities

Mod developers can find and change game objects, call native methods, hook functions with **SafetyHook**, react to scene changes, and draw **ImGui** overlays. (source: wiki/sources/descriptions/Jadis0x__URKit.md)

## Toolchain

The release bundle includes an SDK generator, project updater, and optional **MCP** development server with an in-game **DevBridge** for build, deploy, and runtime inspection workflows.

## Positioning

Complements codegen libraries such as [[sdkgenny]], [[luagenny]], and [[ue4genny]] with a full mod-project scaffold—CMake output, attach paths, hooks, and overlays—rather than header emit alone. Sits upstream of title-specific gameplay mods in the Unity/UE modding lane beside [[bepinex]], [[unityexplorer]], and [[re-ue4ss]]-style explorers.

## Links

- Repo: https://github.com/Jadis0x/URKit

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[sdkgenny]] · [[luagenny]] · [[ue4genny]] · [[il2cpp]] · [[unreal-object-model]] · [[bepinex]] · [[unityexplorer]]
