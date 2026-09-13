---
title: Engine Artifact Selection
kind: concept
topics: [game-engine]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/descriptions/apistol78__traktor.md
updated: 2026-09-13
confidence: high
---

# Engine Artifact Selection

Workflow for choosing a collection resource that matches a **concrete engine artifact and question**—not merely the engine brand. Pair with [[engine-trust-boundaries]] to classify whether the disputed object is source, generated metadata, serialized data, an editor extension, or a shipped module before selecting a tool. (source: wiki/sources/skills/game-engine.md)

## Apply the boundary first

1. Identify artifact type (source tree, metadata dump, serialized asset, editor plugin, runtime module).
2. Select one README-backed resource whose stated role matches that artifact.
3. Record exact revision, build/backend, and the observation the resource explains.
4. Keep the artifact map separate from any security finding or attribution.

A benign version mismatch, unavailable symbols, cooked data, or an editor-only component can explain an apparent discrepancy without an attack. Do not infer a compromised build from engine identification or a reader's output alone. Route authoritative-state questions to game-server-security; plugin publication and update trust to game-supply-chain-security; rendering observations to [[overviews/graphics-api]]. (source: wiki/sources/skills/game-engine.md)

## Select by artifact and question

| README location (representative) | Select when | Common confusion | Expected review output |
|----------------------------------|-------------|------------------|------------------------|
| `Game Engine > Source`: [[unity-cs-reference]] | Checking documented C# engine/editor behavior against an identified Unity build | C# reference source ≠ complete native engine or game source; match stated Unity version/branch | Source-subset map, exact build/backend, supported claim, missing native or game-specific evidence |
| `Game Develop > Source`: [[godot-demo-projects]] | Selecting a small owned baseline to understand a feature or diagnose a version difference | Demo projects ≠ `Game Engine > Source` engine implementations; master targets dev builds, stable branches target releases | Demo revision + engine-version pair, expected behavior, observation, target differences |
| `Game Engine > Game Engine Plugins:Unreal`: RiderSourceCodeAccess | Classifying an editor integration in a plugin or build inventory | Editor source-editor integration ≠ shipped player module; check plugin descriptors and packaged artifacts | Editor/build/runtime role ledger, declared compatibility, packaged modules, required privileges |
| `Game Assets`: [[uassetapi]] | Interpreting owned serialized Unreal assets or explaining a reader mismatch | Asset library ≠ live object reflection or native memory layout; parse failure alone is not corruption | Asset provenance, reader revision, format/version assumptions, supported fields, unresolved parse evidence |
| `Game Engine > Source`: [[traktor]] | Studying full OSS engine architecture—multi-backend rendering (DX11/Vulkan/Metal), Lua scripting, P2P replication, Avalanche asset server, editor MCP—against shipped commercial titles | Engine source tree ≠ a specific game's protected binaries; match platform/backend when comparing to Steam/PSN/iOS/macOS releases | Engine submodule map, active backend, platform target, observation scope, gaps vs shipped title |

These are selection examples from the skill resource guide—not endorsements of every repository in the same category. Use [[resource-selection]] provenance fields and [[repository-navigation]] for local lookup, casing, and snapshot limits. (source: wiki/sources/skills/game-engine.md)

## Untrusted-asset and plugin scenarios

- **Untrusted asset** — establish that the artifact reaches an importer before reviewing schema checks, external-resource access, and processing budgets.
- **Plugin execution** — establish that the plugin is packaged and loaded with relevant permissions before assessing provenance and isolation.

## Related

[[engine-trust-boundaries]] · [[resource-selection]] · [[repository-navigation]] · [[unreal-object-model]] · [[il2cpp]] · [[source-netvars]] · [[research-rigor]] · [[overviews/game-engine]]
