---
title: AssetStudio (Razviar)
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Razviar__assetstudio.md
updated: 2026-08-22
confidence: medium
---

# AssetStudio (Razviar)

Multi-threaded Unity asset extraction fork covering Unity 2.x through Unity 6. Ships GUI and CLI binaries with parallel bundle loading and parallel export for large-scale asset processing. Implementation is primarily C#/.NET and includes format parsers, decompression routines, and game-specific helper logic. Used for game data mining, modding workflows, and reverse engineering of Unity asset bundles. README lane `[Extracting assets]`. (source: wiki/sources/descriptions/Razviar__assetstudio.md)

Fork of canonical [[assetstudio]] (Perfare). Sits beside bulk offline extractors and editor-style Unity tooling such as [[uabe]], and complements runtime inspectors like [[unityexplorer]] when the goal is serialized bundle dump rather than in-process hierarchy inspection.

## Links

- Repo: https://github.com/Razviar/assetstudio

## Related

[[assetstudio]] · [[il2cppdumper]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[uabe]] · [[uassetgui]] · [[unityexplorer]] · [[unity-game-hacking]] · [[awesome-game-file-format-reversing]] · [[unturned-godot]]
