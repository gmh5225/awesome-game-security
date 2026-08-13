---
title: Mono
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mono__mono.md
  - wiki/sources/descriptions/gmh5225__EFT-MonoEFT.md
updated: 2026-08-13
confidence: medium
---

# Mono

Open-source implementation of the .NET Framework runtime (CLR): JIT/AOT compiler, SGen garbage collector, class libraries, and an embeddable C API. Unity historically embeds Mono as its managed scripting backend—IL execution, P/Invoke interop, and managed-to-native bridging—making the runtime a primary target for game modding and security research on pre-[[il2cpp]] Unity titles. (source: wiki/sources/descriptions/mono__mono.md)

## Security-relevant surfaces

- **JIT IL execution** — runtime-compiled managed code; hook/trampoline targets for internal mods
- **Embeddable C API** — `MonoDomain`, `MonoClass`, `mono_runtime_invoke`, metadata introspection (basis for tools like [[mono-external-lib]])
- **P/Invoke / native interop** — boundary between managed game logic and native engine code
- **Contrast with IL2CPP** — Unity’s AOT path removes JIT/reflection surfaces Mono-era cheats relied on; see [[il2cpp]]
- **Title-specific internals** — Mono-based EFT samples such as [[eft-monoeft]] hook managed shot/ESP paths (`CreateShot`, `GameWorld.RegisteredPlayers`, OnGUI overlays) for method-hooking and game-object introspection study. (source: wiki/sources/descriptions/gmh5225__EFT-MonoEFT.md)

## Links

- Repo: https://github.com/mono/mono

## Related

[[il2cpp]] · [[mono-external-lib]] · [[unity-vulnerable-entrypoint]] · [[unityexplorer]] · [[escapefromtarkov-trainer]] · [[eft-monoeft]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
