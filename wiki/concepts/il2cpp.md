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
  - wiki/sources/descriptions/gmh5225__il2cpp-finder.md
  - wiki/sources/descriptions/gmh5225__frida-il2cpp-datacollector.md
  - wiki/sources/descriptions/gmh5225__Goose_Goose_Duck_Hack.md
  - wiki/sources/descriptions/gmh5225__FallGuysSharp.md
  - wiki/sources/descriptions/gmh5225__Il2Cpp-HookScripts.md
  - wiki/sources/descriptions/gmh5225__Rust-RustInternal.md
  - wiki/sources/descriptions/gmh5225__PokemonGoDumper.md
  - wiki/sources/descriptions/matheusbranhann__taskbarhero-bot.md
  - wiki/sources/descriptions/gmh5225__MatScan.md
  - wiki/sources/descriptions/gmh5225__IL22CPP.md
  - wiki/sources/descriptions/gmh5225__FakerAndroid.md
  - wiki/sources/descriptions/gmh5225__DummyDlls_NARAKA_1_9_21.md
  - wiki/sources/descriptions/gmh5225__DevourMenu.md
  - wiki/sources/descriptions/gmh5225__DevourClient.md
  - wiki/sources/descriptions/gmh5225__BepInEx-IL2CPPBase.md
  - wiki/sources/descriptions/gmh5225__BLOCKPOST-Cheat.md
  - wiki/sources/descriptions/gmh5225__AutoGunfireReborn.md
  - wiki/sources/descriptions/focus-creative-games__hybridclr.md
  - wiki/sources/descriptions/extremeblackliu__IL2CPP_Resolver_External.md
  - wiki/sources/descriptions/repinek__fallguys-frida-modmenu.md
  - wiki/sources/descriptions/djkaty__Il2CppInspector.md
updated: 2026-08-16
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

`global-metadata.dat` holds the string pool, type definitions, and method signatures. Some protected titles encrypt metadata and require custom decryptors before IL2CPPDumper or [[frida-il2cpp-bridge]] can run. Unity IL2CPP hot-update runtimes such as [[hybridclr]] (focus-creative-games; C/C++; live-update / game hot-patch; modding + IL2CPP analysis) extend AOT IL2CPP with interpreter-based assembly loading for patching workflows. (source: wiki/sources/descriptions/focus-creative-games__hybridclr.md)

## Research workflow

1. Locate binary + metadata (desktop or APK/IPA); metadata locators such as [[il2cpp-finder]] (gmh5225; scan executables/shared libraries for `global-metadata.dat` signatures plus `CodeRegistration` / `MetadataRegistration` pointers; obfuscated or unfamiliar builds) help find dump entry points before running IL2CPPDumper. (source: wiki/sources/descriptions/gmh5225__il2cpp-finder.md)
2. Run IL2CPPDumper (desktop or Android-focused [[il2cppdumper]]) or cross-platform C# [[il2cpp-inspector]] (djkaty; `global-metadata.dat` + IL2CPP binaries → type/method metadata, IDA/Ghidra/Binary Ninja scripts, C++ headers, DLL injection scaffolds; all IL2CPP versions/platforms; [Il2Cpp Dump]) (source: wiki/sources/descriptions/djkaty__Il2CppInspector.md) → `dump.cs`, headers, `script.json`
3. Import into IDA/Ghidra; resolve `Il2CppClass` / `MethodInfo` / invoke paths (match layouts to the title’s Unity IL2CPP generation via references such as [[il2cpp-versions]])
4. Hook via native hooks or [[frida]] on mobile; Android IL2CPP/Mono hook script templates such as [[il2cpp-hook-scripts]] (gmh5225; Frida + native templates for method intercept, logic patches, runtime data extraction) complement dump/harvest tooling when analysts need reusable hook scaffolds. (source: wiki/sources/descriptions/gmh5225__Il2Cpp-HookScripts.md) APK-to-Android-Studio rebuild tooling such as [[fakerandroid]] (gmh5225; IL2CPP C++ scaffolding + fakeCpp JNI `.so` hooks; javaScaffolding for package/class-matched Java extensions) offers a Gradle-project modding path beside Frida when analysts want smali-aware rebuilds. (source: wiki/sources/descriptions/gmh5225__FakerAndroid.md)

Cross-version IL2CPP header/metadata collections such as [[il2cpp-versions]] track structure and API drift across Unity releases. (source: wiki/sources/descriptions/nneonneo__Il2CppVersions.md) For APK-oriented disassembly and two-build diffs, [[il2cpp-spy]] compares selected Unity IL2CPP APKs side by side. (source: wiki/sources/descriptions/yukiarrr__Il2cppSpy.md) On iOS, speed/modding tooling such as [[unityspeedtools]] (C/C++ / Objective-C) targets Unity IL2CPP analysis in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/xxzzddxzd__unitySpeedTools.md) Android-focused static IL2CPP dump tooling such as [[il2cppdumper]] (C/C++; `libil2cpp.so` + metadata → dump output; cheat / game engine explorer:Unity) sits in the same explorer lane. (source: wiki/sources/descriptions/kp7742__IL2CPPDumper.md) Title-specific Genshin Impact dump forks such as [[il2cppdumper-yuanshen]] (khang06; cwd output; cheat / game engine explorer:Unity) sit beside generic dumpers when analysts target miHoYo’s Unity IL2CPP build. (source: wiki/sources/descriptions/khang06__Il2CppDumper-YuanShen.md) The [[android-modding]] collection also indexes kagurazakasanae's Il2CppDumper YuanShen fork for Genshin `UserAssembly.dll` method dumps on Android. (source: wiki/sources/descriptions/jbro129__android-modding.md) On Android, IL2CPP `Time`-class speed hacks such as [[android-il2cpp-modspeed]] (C++ native; `deltaTime` / `timeScale` / fixed timestep hooks) sit in the same explorer:Unity lane. (source: wiki/sources/descriptions/oobbb__android-il2cpp-modspeed.md) Title-specific Android RE notes such as [[honor-of-kings-re-research]] pair Frida/Python IL2CPP parsing with native/`libtersafe` and ACE surfaces. (source: wiki/sources/descriptions/wwweeeqqu__honor-of-kings-RE-research.md) Live Frida dumps across Unity 5.3.0–6000.1.x often use [[frida-il2cpp-bridge]]. (source: wiki/sources/descriptions/vfsfitvnm__frida-il2cpp-bridge.md) Mobile runtime IL2CPP data collectors such as [[frida-il2cpp-datacollector]] (gmh5225; Frida script porting Cheat Engine's MonoDataCollector to Android/iOS; enumerate classes, dump method signatures, field offsets, and type metadata at runtime for SDK generation) complement that bridge when the goal is CE-style live metadata harvesting on mobile. (source: wiki/sources/descriptions/gmh5225__frida-il2cpp-datacollector.md) C++ resolvers such as [[il2cpp-resolver]] target Unity IL2CPP structure resolution in the cheat / game engine explorer:Unity lane. (source: wiki/sources/descriptions/sneakyevilSK__IL2CPP_Resolver.md) C++ IL2CPP internal-reflection remakes such as [[il22cpp]] (gmh5225; metadata resolution, managed type reconstruction, IL2CPP VM interface for modding) sit beside those resolvers when analysts need native reflection-system parity in C++. (source: wiki/sources/descriptions/gmh5225__IL22CPP.md) Runtime dumpers such as [[il2cpp-runtime-dumper]] reconstruct DLLs via the IL2CPP reflection system rather than static metadata alone. (source: wiki/sources/descriptions/shalzuth__Il2CppRuntimeDumper.md) Emulation-based dumpers such as [[qiling-il2cpp-dump]] (Qiling sandbox; emulates IL2CPP runtime init to trigger metadata registration; obfuscated/anti-tamper titles; cheat / game engine explorer:Unity) recover metadata without running the full game when static dumps fail. (source: wiki/sources/descriptions/gmh5225__qiling-il2cpp-dump.md) Metadata-to-proxy-assembly unhollowers such as [[il2cpp-assembly-unhollower]] (knah; wrapper .NET assemblies delegating to native IL2CPP methods; enables C# modding without Mono reflection) sit in the same explorer lane. (source: wiki/sources/descriptions/knah__Il2CppAssemblyUnhollower.md) In-process runtime inspectors such as [[unityexplorer]] (BepInEx/MelonLoader; hierarchy / REPL / freecam; reflection + IL2CPP unhollowing for Mono and IL2CPP) sit in the same explorer lane for live state inspection. (source: wiki/sources/descriptions/sinai-dev__UnityExplorer.md) External read-only Unity 2020–2023 introspection such as [[unity202x-externalresolve]] (er2; GOM blind scan; IL2CPP metadata rebuild; W2S; DumpSDK; Mono + IL2CPP auto-detect) complements inject-based inspectors and Mono-only [[mono-external-lib]]. (source: wiki/sources/descriptions/zushinzackery2-ship-it__Unity202x-eXternalrEsolve.md) External IL2CPP runtime resolvers such as [[il2cpp-resolver-external]] (extremeblackliu; C++; `global-metadata.dat` + IL2CPP binary parse via RPM; class/method/field/type resolution without injection; cheat / game engine explorer:Unity) sit in the same no-inject external lane when analysts need IL2CPP-specific metadata for external cheat scaffolding. (source: wiki/sources/descriptions/extremeblackliu__IL2CPP_Resolver_External.md)

Mono builds instead use `Assembly-CSharp.dll` + dnSpy/ILSpy on the embedded [[mono]] CLR (JIT IL, SGen GC, P/Invoke interop). (source: wiki/sources/descriptions/mono__mono.md) Educational vulnerable-entry demos such as [[unity-vulnerable-entrypoint]] (C#; runtime init / Assembly-CSharp load / MonoBehaviour lifecycle) map Mono-side injection surfaces that IL2CPP AOT largely removes. (source: wiki/sources/descriptions/sunnamed434__UnityVulnerableEntryPoint.md) External (no-inject) Mono metadata readers such as [[mono-external-lib]] reconstruct classes/methods/fields/offsets from process memory for Unity Mono titles. (source: wiki/sources/descriptions/reahly__mono-external-lib.md) Discontinued Mono-era EFT trainers such as [[escapefromtarkov-trainer]] mark the 1.0 / IL2CPP pivot as a hard break for internal modding complexity. (source: wiki/sources/descriptions/sailro__EscapeFromTarkov-Trainer.md) External C# IL2CPP trainers such as [[taskbarhero-bot]] (TaskbarHero; batch reads, AOB scan, IL2CPP offset resolution, ACTk bypass, ObscuredInt R/W, build-hash offset cache; WPF dashboard + headless CLI) illustrate no-inject external memory editing and client-side protection bypass on Unity IL2CPP titles. (source: wiki/sources/descriptions/matheusbranhann__taskbarhero-bot.md) Facepunch Rust internal samples such as [[rust-rustinternal]] (C++; Mono/IL2CPP method hooks + direct Unity game-object memory for ESP/aimbot/no-recoil; EAC-protected FPS; gmh5225) illustrate desktop Unity IL2CPP offensive hooking beside mobile dump/hook tooling. (source: wiki/sources/descriptions/gmh5225__Rust-RustInternal.md) Goose Goose Duck internal samples such as [[goose-goose-duck-hack]] (gmh5225; IL2CPP runtime manipulation + ImGui overlay; dumped Assembly-CSharp + ACTk bypasses for ESP/role reveal/gameplay mods) illustrate social-deduction Unity IL2CPP in-process hooking when hidden role state is client-side. (source: wiki/sources/descriptions/gmh5225__Goose_Goose_Duck_Hack.md) Reusable BepInEx IL2CPP mod-menu base scaffolds such as [[bepinex-il2cppbase]] (gmh5225; C# rendering/audio/physics hooks; cheat / `[IL2CPP Menu]`) sit upstream of title-specific Unity IL2CPP menu samples when analysts need a shared plugin skeleton rather than a single-game fork. (source: wiki/sources/descriptions/gmh5225__BepInEx-IL2CPPBase.md) Devour co-op horror IL2CPP mod-menu samples such as [[devour-menu]] (ImGui overlay + IL2CPP hooks; toggleable gameplay mods; cheat / `[Menu]`; gmh5225) illustrate desktop Unity IL2CPP in-process mod menus on co-op horror titles. (source: wiki/sources/descriptions/gmh5225__DevourMenu.md) Sibling Devour client samples such as [[devour-client]] (gmh5225; broader QoL/cheat memory manipulation on the Unity IL2CPP client) illustrate alternate in-process Unity IL2CPP modding surfaces beside overlay mod menus. (source: wiki/sources/descriptions/gmh5225__DevourClient.md) BLOCKPOST FPS IL2CPP cheat samples such as [[blockpost-cheat]] (gmh5225; C/C++; IL2CPP analysis + native hooking; cheat / game:blockpost) illustrate desktop Unity IL2CPP offensive hooking on FPS titles beside social-deduction samples. (source: wiki/sources/descriptions/gmh5225__BLOCKPOST-Cheat.md) Gunfire Reborn Unity IL2CPP runtime module-injection samples such as [[autogunfire-reborn]] (gmh5225; C#; inject Unity modules at runtime into IL2CPP builds; cheat / game:gunfire reborn) illustrate desktop roguelike-FPS managed injection beside party-game samples. (source: wiki/sources/descriptions/gmh5225__AutoGunfireReborn.md) Fall Guys C# IL2CPP internal samples such as [[fall-guys-sharp]] (gmh5225; managed code injection into IL2CPP runtime; movement hacks and gameplay mods; cheat / game:fallguys) illustrate desktop party-game IL2CPP in-process hooking beside kernel external stacks such as [[flying-guys]]. (source: wiki/sources/descriptions/gmh5225__FallGuysSharp.md) Fall Guys **Android** IL2CPP Frida mod-menu samples such as [[fallguys-frida-modmenu]] (repinek; TypeScript + [[frida-il2cpp-bridge]] + frida-java-menu overlay; Objection/APKEditor APK patch; movement/teleport/ban-bypass/platform-spoof; cheat / game:fallguys mobile) contrast that desktop lane with mobile Frida instrumentation. (source: wiki/sources/descriptions/repinek__fallguys-frida-modmenu.md) Title-specific Pokemon GO IL2CPP dump tooling such as [[pokemongo-dumper]] (gmh5225; C#/C++; cheat / game:pokemongo) sits in the mobile title lane beside generic dumpers. (source: wiki/sources/descriptions/gmh5225__PokemonGoDumper.md) Version-pinned NARAKA: BLADEPOINT v1.9.21 dummy DLL collections such as [[dummy-dlls-naraka-1-9-21]] (gmh5225; IL2CPP metadata → C# class/method stubs; modding / cheat / RE; `[Dump]`) sit as pre-built SDK outputs beside live dumpers. (source: wiki/sources/descriptions/gmh5225__DummyDlls_NARAKA_1_9_21.md) Facepunch Rust multi-threaded material scanners such as [[matscan]] (gmh5225; C++; IL2CPP analysis + memory analysis; cheat / game engine explorer:Unity) illustrate Unity material enumeration on IL2CPP desktop titles. (source: wiki/sources/descriptions/gmh5225__MatScan.md)

## Related

[[unreal-object-model]] · [[source-netvars]] · [[android-modding]] · [[hybridclr]] · [[fakerandroid]] · [[frida]] · [[frida-il2cpp-bridge]] · [[frida-il2cpp-datacollector]] · [[il2cpp-hook-scripts]] · [[il2cpp-versions]] · [[il22cpp]] · [[il2cpp-resolver]] · [[il2cpp-resolver-external]] · [[il2cpp-runtime-dumper]] · [[qiling-il2cpp-dump]] · [[il2cpp-finder]] · [[il2cpp-assembly-unhollower]] · [[il2cpp-inspector]] · [[il2cppdumper]] · [[il2cppdumper-yuanshen]] · [[il2cpp-spy]] · [[unityexplorer]] · [[unityspeedtools]] · [[android-il2cpp-modspeed]] · [[unity-vulnerable-entrypoint]] · [[mono]] · [[mono-external-lib]] · [[unity202x-externalresolve]] · [[escapefromtarkov-trainer]] · [[taskbarhero-bot]] · [[rust-rustinternal]] · [[goose-goose-duck-hack]] · [[bepinex-il2cppbase]] · [[autogunfire-reborn]] · [[blockpost-cheat]] · [[devour-menu]] · [[devour-client]] · [[fall-guys-sharp]] · [[fallguys-frida-modmenu]] · [[matscan]] · [[pokemongo-dumper]] · [[dummy-dlls-naraka-1-9-21]] · [[honor-of-kings-re-research]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
