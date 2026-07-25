---
title: Paksmith
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/r6e__paksmith.md
updated: 2026-07-25
confidence: medium
---

# Paksmith

Cross-platform Rust toolkit for exploring and extracting Unreal Engine packaged assets—a rewrite of FModel. Core library reads UE pak archives (v3–v11) with zlib/LZ4 decompression, optional SHA-1 verification, and UAsset parsing (name/import/export tables + property system). Export handlers convert textures, static/skeletal meshes, audio, and data tables to PNG, glTF, WAV/OGG, CSV, and JSON. CLI (planned Iced GUI) for listing, inspecting, searching, and extracting. Aimed at reverse engineers, modders, and game-security researchers analyzing UE packages offline. (source: wiki/sources/descriptions/r6e__paksmith.md)

Sits in the README Game Assets / Unreal pak–UAsset lane beside dependency-graph tooling such as [[jmap]], rather than live-process SDK dumps.

## Links

- Repo: https://github.com/r6e/paksmith

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[jmap]] · [[tinygltf]] · [[rpgmakerdecrypter]] · [[patternsleuth]]
