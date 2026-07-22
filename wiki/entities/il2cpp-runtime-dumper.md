---
title: Il2CppRuntimeDumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/shalzuth__Il2CppRuntimeDumper.md
updated: 2026-07-22
confidence: medium
---

# Il2CppRuntimeDumper

Unity [[il2cpp]] **Dump Runtime** tooling. Reconstructs managed DLLs via the IL2CPP reflection API rather than static metadata-only dumps. Aimed at game-security researchers and reverse engineers in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/shalzuth__Il2CppRuntimeDumper.md)

Complements static APK/disasm workflows such as [[il2cpp-spy]], C++ structure resolvers like [[il2cpp-resolver]], and live Frida bridges such as [[frida-il2cpp-bridge]] when the goal is runtime reflection-driven DLL reconstruction.

## Links

- Repo: https://github.com/shalzuth/Il2CppRuntimeDumper

## Related

[[il2cpp]] · [[il2cpp-resolver]] · [[il2cpp-spy]] · [[frida-il2cpp-bridge]] · [[unityexplorer]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
