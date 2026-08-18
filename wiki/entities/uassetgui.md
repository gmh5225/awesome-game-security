---
title: UAssetGUI
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/atenfyr__UAssetGUI.md
updated: 2026-08-18
confidence: medium
---

# UAssetGUI

C# GUI tool for viewing and editing Unreal Engine `.uasset` and `.umap` files. Parses the UAsset binary format and displays exports, imports, name maps, property data, and asset metadata in an interactive tree view with editing support. Supports multiple Unreal Engine versions from UE4 through UE5. Aimed at Unreal modders and game researchers who need to inspect or modify cooked asset files without the Unreal Editor. (source: wiki/sources/descriptions/atenfyr__UAssetGUI.md)

Sits in the README Game Assets / Unreal UAsset lane beside pak extractors such as [[paksmith]] and dependency-graph tooling such as [[jmap]], rather than live-process SDK dumps.

## Links

- Repo: https://github.com/atenfyr/UAssetGUI

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[jmap]] · [[paksmith]] · [[rust-u4pak]] · [[unreal-object-model]]
