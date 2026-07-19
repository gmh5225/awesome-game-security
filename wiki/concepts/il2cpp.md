---
title: IL2CPP
kind: concept
topics: [game-engine, game-hacking, mobile-security, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/yukiarrr__Il2cppSpy.md
  - wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md
  - wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md
  - wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md
updated: 2026-07-19
confidence: high
---

# IL2CPP

Unity’s ahead-of-time C++ compilation backend. Managed assemblies become native code (`GameAssembly.dll` / `libil2cpp.so`) plus `global-metadata.dat` describing types, methods, and strings. (source: wiki/sources/skills/game-engine.md)

## Research workflow

1. Locate binary + metadata (desktop or APK/IPA)
2. Run IL2CPPDumper → `dump.cs`, headers, `script.json`
3. Import into IDA/Ghidra; resolve `Il2CppClass` / `MethodInfo` / invoke paths
4. Hook via native hooks or [[frida]] on mobile

For APK-oriented disassembly and two-build diffs, [[il2cpp-spy]] compares selected Unity IL2CPP APKs side by side. (source: wiki/sources/descriptions/yukiarrr__Il2cppSpy.md) On iOS, speed/modding tooling such as [[unityspeedtools]] (C/C++ / Objective-C) targets Unity IL2CPP analysis in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md) Title-specific Android RE notes such as [[honor-of-kings-re-research]] pair Frida/Python IL2CPP parsing with native/`libtersafe` and ACE surfaces. (source: wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md) Live Frida dumps across Unity 5.3.0–6000.1.x often use [[frida-il2cpp-bridge]]. (source: wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md)

Mono builds instead use `Assembly-CSharp.dll` + dnSpy/ILSpy.

## Related

[[frida]] · [[frida-il2cpp-bridge]] · [[il2cpp-spy]] · [[unityspeedtools]] · [[honor-of-kings-re-research]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
