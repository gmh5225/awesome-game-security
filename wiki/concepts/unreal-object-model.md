---
title: Unreal Object Model
kind: concept
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/descriptions/mikeroyal__Unreal-Engine-Guide.md
  - wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md
updated: 2026-08-06
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

Common fields include vtable, flags, internal index, class pointer, name, and outer pointers. **Order, packing, and presence are build-specific.** Encrypted or pooled name tables (e.g. Valorant, Fortnite) need per-title decrypt paths—see [[valorant-fnamepool]], [[fortnite-fnameentry]].

## SDK generation workflow

1. Identify UE version from binary signatures or strings
2. Inject Dumper-7 (or live-script via UE4SS) into the running process
3. Output C++ headers with UObject hierarchy (`UObject`, `FName`, `UClass`, `UFunction`, `UProperty`)
4. Alternatives: external C++ dumpers such as [[unrealdumper-4-25]] (pattern-scan `GObjects`/`GNames`; no inject), modular Frida dumps such as [[ts-ue4dumper]], live explorers such as [[unrealengine4-swissknife]] (source: wiki/sources/descriptions/guttir14__UnrealDumper-4.25.md)

Pattern scanners such as [[patternsleuth]] often precede dumpers for address discovery on protected builds.

Curated UE tooling indexes such as [[unreal-engine-guide]] complement these SDK workflows for developers building engine literacy before title-specific RE. (source: wiki/sources/descriptions/mikeroyal__Unreal-Engine-Guide.md)

## Related

[[source-netvars]] · [[il2cpp]] · [[patternsleuth]] · [[source2gen]] · [[valorant-dumper]] · [[unrealdumper-4-25]] · [[unreal-engine-guide]] · [[research-rigor]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
