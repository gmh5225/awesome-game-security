---
title: AssetStudio
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Perfare__AssetStudio.md
updated: 2026-08-22
confidence: high
---

# AssetStudio

Canonical desktop C# tool for exploring, extracting, and exporting Unity assets and AssetBundles. Supports a wide range of Unity versions and asset types — textures, audio, fonts, meshes, shaders, and animation-related data. Decompresses bundles, inspects scene hierarchies, and exports to practical formats such as images, OBJ, JSON, and FBX-related outputs. Commonly used by reverse engineers, modders, and game-security analysts who need to inspect Unity game content. README lane `[Extracting assets]`. (source: wiki/sources/descriptions/Perfare__AssetStudio.md)

Same Perfare author as [[il2cppdumper]]. Sits in the README **Extracting assets** / Game Assets lane beside editor-style [[uabe]] and multi-threaded fork [[assetstudio-razviar]]; complements runtime inspectors like [[unityexplorer]] when the goal is serialized bundle dump rather than in-process hierarchy inspection.

## Links

- Repo: https://github.com/Perfare/AssetStudio

## Related

[[il2cppdumper]] · [[assetstudio-razviar]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[uabe]] · [[uassetgui]] · [[unityexplorer]] · [[unity-game-hacking]] · [[awesome-game-file-format-reversing]] · [[unturned-godot]]
