---
title: IL2CPP
kind: concept
topics: [game-engine, game-hacking, mobile-security, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
updated: 2026-07-16
confidence: high
---

# IL2CPP

Unity’s ahead-of-time C++ compilation backend. Managed assemblies become native code (`GameAssembly.dll` / `libil2cpp.so`) plus `global-metadata.dat` describing types, methods, and strings. (source: wiki/sources/skills/game-engine.md)

## Research workflow

1. Locate binary + metadata (desktop or APK/IPA)
2. Run IL2CPPDumper → `dump.cs`, headers, `script.json`
3. Import into IDA/Ghidra; resolve `Il2CppClass` / `MethodInfo` / invoke paths
4. Hook via native hooks or [[frida]] on mobile

Mono builds instead use `Assembly-CSharp.dll` + dnSpy/ILSpy.

## Related

[[frida]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
