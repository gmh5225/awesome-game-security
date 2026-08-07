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
  - wiki/sources/descriptions/sunnamed434__UnityVulnerableEntryPoint.md
  - wiki/sources/descriptions/sneakyevilSK__IL2CPP_Resolver.md
  - wiki/sources/descriptions/sinai-dev__UnityExplorer.md
  - wiki/sources/descriptions/shalzuth__Il2CppRuntimeDumper.md
  - wiki/sources/descriptions/sailro__EscapeFromTarkov-Trainer.md
  - wiki/sources/descriptions/reahly__mono-external-lib.md
  - wiki/sources/descriptions/mono__mono.md
  - wiki/sources/descriptions/oobbb__android-il2cpp-modspeed.md
  - wiki/sources/descriptions/nneonneo__Il2CppVersions.md
  - wiki/sources/descriptions/zushinzackery2-ship-it__Unity202x-eXternalrEsolve.md
  - wiki/sources/descriptions/kp7742__IL2CPPDumper.md
  - wiki/sources/descriptions/knah__Il2CppAssemblyUnhollower.md
  - wiki/sources/descriptions/khang06__Il2CppDumper-YuanShen.md
  - wiki/sources/descriptions/jbro129__android-modding.md
  - wiki/sources/descriptions/gmh5225__qiling-il2cpp-dump.md
updated: 2026-08-07
confidence: high
---

# IL2CPP

Unity’s ahead-of-time C++ compilation backend. Managed assemblies become native code (`GameAssembly.dll` / `libil2cpp.so`) plus `global-metadata.dat` describing types, methods, and strings. (source: wiki/sources/skills/game-engine.md)

## Object model

```
Il2CppDomain → Il2CppAssembly → Il2CppImage → Il2CppClass
Il2CppClass: fields, methods, vtable, static_fields pointer
```

Key native API patterns (names/signatures drift by Unity version):

- `il2cpp_domain_get()` — domain singleton
- `il2cpp_class_from_name()` — class lookup by namespace + name
- `il2cpp_runtime_invoke()` — call managed methods from native code

`global-metadata.dat` holds the string pool, type definitions, and method signatures. Some protected titles encrypt metadata and require custom decryptors before IL2CPPDumper or [[frida-il2cpp-bridge]] can run.

## Research workflow

1. Locate binary + metadata (desktop or APK/IPA)
2. Run IL2CPPDumper (desktop or Android-focused [[il2cppdumper]]) → `dump.cs`, headers, `script.json`
3. Import into IDA/Ghidra; resolve `Il2CppClass` / `MethodInfo` / invoke paths (match layouts to the title’s Unity IL2CPP generation via references such as [[il2cpp-versions]])
4. Hook via native hooks or [[frida]] on mobile

Cross-version IL2CPP header/metadata collections such as [[il2cpp-versions]] track structure and API drift across Unity releases. (source: wiki/sources/descriptions/nneonneo__Il2CppVersions.md) For APK-oriented disassembly and two-build diffs, [[il2cpp-spy]] compares selected Unity IL2CPP APKs side by side. (source: wiki/sources/descriptions/yukiarrr__Il2cppSpy.md) On iOS, speed/modding tooling such as [[unityspeedtools]] (C/C++ / Objective-C) targets Unity IL2CPP analysis in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md) Android-focused static IL2CPP dump tooling such as [[il2cppdumper]] (C/C++; `libil2cpp.so` + metadata → dump output; cheat / game engine explorer:Unity) sits in the same explorer lane. (source: wiki/sources/descriptions/kp7742__IL2CPPDumper.md) Title-specific Genshin Impact dump forks such as [[il2cppdumper-yuanshen]] (khang06; cwd output; cheat / game engine explorer:Unity) sit beside generic dumpers when analysts target miHoYo’s Unity IL2CPP build. (source: wiki/sources/descriptions/khang06__Il2CppDumper-YuanShen.md) The [[android-modding]] collection also indexes kagurazakasanae's Il2CppDumper YuanShen fork for Genshin `UserAssembly.dll` method dumps on Android. (source: wiki/sources/descriptions/jbro129__android-modding.md) On Android, IL2CPP `Time`-class speed hacks such as [[android-il2cpp-modspeed]] (C++ native; `deltaTime` / `timeScale` / fixed timestep hooks) sit in the same explorer:Unity lane. (source: wiki/sources/descriptions/oobbb__android-il2cpp-modspeed.md) Title-specific Android RE notes such as [[honor-of-kings-re-research]] pair Frida/Python IL2CPP parsing with native/`libtersafe` and ACE surfaces. (source: wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md) Live Frida dumps across Unity 5.3.0–6000.1.x often use [[frida-il2cpp-bridge]]. (source: wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md) C++ resolvers such as [[il2cpp-resolver]] target Unity IL2CPP structure resolution in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/sneakyevilSK__IL2CPP_Resolver.md) Runtime dumpers such as [[il2cpp-runtime-dumper]] reconstruct DLLs via the IL2CPP reflection system rather than static metadata alone. (source: wiki/sources/descriptions/shalzuth__Il2CppRuntimeDumper.md) Emulation-based dumpers such as [[qiling-il2cpp-dump]] (Qiling sandbox; emulates IL2CPP runtime init to trigger metadata registration; obfuscated/anti-tamper titles; cheat / game engine explorer:Unity) recover metadata without running the full game when static dumps fail. (source: wiki/sources/descriptions/gmh5225__qiling-il2cpp-dump.md) Metadata-to-proxy-assembly unhollowers such as [[il2cpp-assembly-unhollower]] (knah; wrapper .NET assemblies delegating to native IL2CPP methods; enables C# modding without Mono reflection) sit in the same explorer lane. (source: wiki/sources/descriptions/knah__Il2CppAssemblyUnhollower.md) In-process runtime inspectors such as [[unityexplorer]] (BepInEx/MelonLoader; hierarchy / REPL / freecam; reflection + IL2CPP unhollowing for Mono and IL2CPP) sit in the same explorer lane for live state inspection. (source: wiki/sources/descriptions/sinai-dev__UnityExplorer.md) External read-only Unity 2020–2023 introspection such as [[unity202x-externalresolve]] (er2; GOM blind scan; IL2CPP metadata rebuild; W2S; DumpSDK; Mono + IL2CPP auto-detect) complements inject-based inspectors and Mono-only [[mono-external-lib]]. (source: wiki/sources/descriptions/zushinzackery2-ship-it__Unity202x-eXternalrEsolve.md)

Mono builds instead use `Assembly-CSharp.dll` + dnSpy/ILSpy on the embedded [[mono]] CLR (JIT IL, SGen GC, P/Invoke interop). (source: wiki/sources/descriptions/mono__mono.md) Educational vulnerable-entry demos such as [[unity-vulnerable-entrypoint]] (C#; runtime init / Assembly-CSharp load / MonoBehaviour lifecycle) map Mono-side injection surfaces that IL2CPP AOT largely removes. (source: wiki/sources/descriptions/sunnamed434__UnityVulnerableEntryPoint.md) External (no-inject) Mono metadata readers such as [[mono-external-lib]] reconstruct classes/methods/fields/offsets from process memory for Unity Mono titles. (source: wiki/sources/descriptions/reahly__mono-external-lib.md) Discontinued Mono-era EFT trainers such as [[escapefromtarkov-trainer]] mark the 1.0 / IL2CPP pivot as a hard break for internal modding complexity. (source: wiki/sources/descriptions/sailro__EscapeFromTarkov-Trainer.md)

## Related

[[unreal-object-model]] · [[source-netvars]] · [[android-modding]] · [[frida]] · [[frida-il2cpp-bridge]] · [[il2cpp-versions]] · [[il2cpp-resolver]] · [[il2cpp-runtime-dumper]] · [[qiling-il2cpp-dump]] · [[il2cpp-assembly-unhollower]] · [[il2cppdumper]] · [[il2cppdumper-yuanshen]] · [[il2cpp-spy]] · [[unityexplorer]] · [[unityspeedtools]] · [[android-il2cpp-modspeed]] · [[unity-vulnerable-entrypoint]] · [[mono]] · [[mono-external-lib]] · [[unity202x-externalresolve]] · [[escapefromtarkov-trainer]] · [[honor-of-kings-re-research]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
