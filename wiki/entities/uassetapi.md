---
title: UAssetAPI
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/atenfyr__UAssetAPI.md
updated: 2026-08-18
confidence: medium
---

# UAssetAPI

Low-level C#/.NET library for reading and writing Unreal Engine asset files. Supports a broad range of cooked and uncooked engine versions, many property and export types, JSON round-tripping, Kismet bytecode handling, and optional `.usmap` parsing for unversioned data. Designed to preserve binary fidelity when editing assets programmatically—aimed at modding, tooling, and reverse-engineering workflows for Unreal-based games. (source: wiki/sources/descriptions/atenfyr__UAssetAPI.md)

Underpins the GUI editor [[uassetgui]] in the README Game Assets / Unreal UAsset lane beside pak extractors such as [[paksmith]] and dependency-graph tooling such as [[jmap]], rather than live-process SDK dumps.

## Links

- Repo: https://github.com/atenfyr/UAssetAPI

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[uassetgui]] · [[jmap]] · [[paksmith]] · [[rust-u4pak]] · [[unreal-object-model]]
