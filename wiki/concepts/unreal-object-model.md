---
title: Unreal Object Model
kind: concept
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/descriptions/mikeroyal__Unreal-Engine-Guide.md
  - wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md
  - wiki/sources/descriptions/gmh5225__ue4_cheat_engine.md
  - wiki/sources/descriptions/gmh5225__fortnite-virtual-offsets.md
  - wiki/sources/descriptions/gmh5225__fortnite-sigs.md
  - wiki/sources/descriptions/gmh5225__FortniteSigsUpdatedEveryUpdate.md
  - wiki/sources/descriptions/gmh5225__fortnite-offsets.md
  - wiki/sources/descriptions/gmh5225__Fortnite-VoyagerTF.md
  - wiki/sources/descriptions/gmh5225__UE-UnrealEngineSDK.md
updated: 2026-08-13
confidence: high
---

# Unreal Object Model

Unreal Engine exposes a reflection-driven C++ object hierarchy. Security and modding research targets **globals**, **UObject layout**, and **version-specific property offsets**—all branch-, build-, and platform-dependent. Apply [[research-rigor]] before generalizing signatures or SDK dumps across titles. (source: wiki/sources/skills/game-engine.md)

## Core hierarchy

```
UObject → UField → UStruct → UClass
UObject → AActor → APawn → ACharacter → APlayerCharacter
```

Reflected property offsets come from version-specific class metadata, not fixed constants.

## Key globals

| Symbol | Role |
|--------|------|
| `GUObjectArray` / `GObjects` | Registered UObject slots; lifecycle and reachability filtering still required |
| `GNames` / `FNamePool` | Name storage; layout and encryption vary by UE version |
| `GWorld` | Current `UWorld*` context |
| `GEngine` | Engine singleton |

## UObject memory layout (typical)

Common fields include vtable, flags, internal index, class pointer, name, and outer pointers. **Order, packing, and presence are build-specific.** Encrypted or pooled name tables (e.g. Valorant, Fortnite) need per-title decrypt paths—see [[valorant-fnamepool]], [[fortnite-fnameentry]]. Title-specific vtable/index offset dumps such as [[fortnite-virtual-offsets]] (Fortnite; `GetPlayerViewPoint`, `ProcessEvent`, `LineOfSightTo`, camera helpers; text-only) document per-build virtual dispatch slots for hook and call-site RE beside full SDK dumpers. (source: wiki/sources/descriptions/gmh5225__fortnite-virtual-offsets.md)

## SDK generation workflow

1. Identify UE version from binary signatures or strings
2. Inject Dumper-7 (or live-script via UE4SS) into the running process
3. Output C++ headers with UObject hierarchy (`UObject`, `FName`, `UClass`, `UFunction`, `UProperty`)
4. Alternatives: external C++ dumpers such as [[unrealdumper-4-25]] (pattern-scan `GObjects`/`GNames`; no inject), modular Frida dumps such as [[ts-ue4dumper]], live explorers such as [[unrealengine4-swissknife]] (source: wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md) UE4-aware Cheat Engine frameworks such as [[ue4-cheat-engine]] (Android; memory scan, `GObject` enumeration, `UProperty` traversal, SDK generation) sit in the same interactive explorer lane. (source: wiki/sources/descriptions/gmh5225__ue4_cheat_engine.md) Pre-collected UE4/UE5 SDK header kits such as [[ue-unreal-engine-sdk]] (gmh5225; class/struct layouts + function signatures for injected internal cheats/mods) complement live dumpers when a title-specific regen is unnecessary. (source: wiki/sources/descriptions/gmh5225__UE-UnrealEngineSDK.md)

Pattern scanners such as [[patternsleuth]] often precede dumpers for address discovery on protected builds. Per-title IDA-style signature collections such as [[fortnite-sigs]] (Fortnite; `GObjects`, `GNames`, `ProcessEvent`, player-controller entry points; gmh5225; build-specific refresh) document byte patterns for locating globals and dispatch helpers when full SDK dumpers are impractical. (source: wiki/sources/descriptions/gmh5225__fortnite-sigs.md) Per-patch signature maintenance such as [[fortnite-sigs-updated-every-update]] (Fortnite; `UWorld`, `GObjects`, `FnFree`, `GetNameByIndex`; pattern-mask notation; gmh5225) tracks UE global churn across Fortnite updates. (source: wiki/sources/descriptions/gmh5225__FortniteSigsUpdatedEveryUpdate.md) Curated per-build offset tables such as [[fortnite-offsets]] (Fortnite; player entities, camera, bone arrays, weapons, engine globals; gmh5225) supply ready-made UE4 structure addresses for external and internal tooling when a full SDK regen is unnecessary. (source: wiki/sources/descriptions/gmh5225__fortnite-offsets.md) External Fortnite clients such as [[fortnite-voyagertf]] (VoyagerTF; ESP / aimbot / game-state reads via out-of-process UE client memory) illustrate how those globals and actor layouts feed RPM-based cheat features without in-process SDK injection. (source: wiki/sources/descriptions/gmh5225__Fortnite-VoyagerTF.md)

Curated UE tooling indexes such as [[unreal-engine-guide]] complement these SDK workflows for developers building engine literacy before title-specific RE. (source: wiki/sources/descriptions/mikeroyal__Unreal-Engine-Guide.md)

## Related

[[source-netvars]] · [[il2cpp]] · [[patternsleuth]] · [[source2gen]] · [[valorant-dumper]] · [[unrealdumper-4-25]] · [[ue-unreal-engine-sdk]] · [[ue4-cheat-engine]] · [[unreal-engine-guide]] · [[fortnite-virtual-offsets]] · [[fortnite-sigs]] · [[fortnite-sigs-updated-every-update]] · [[fortnite-offsets]] · [[fortnite-voyagertf]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
