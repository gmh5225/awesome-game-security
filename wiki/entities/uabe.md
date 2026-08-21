---
title: UABE
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/SeriousCache__UABE.md
updated: 2026-08-21
confidence: medium
---

# UABE

Desktop editor for Unity `.assets` and AssetBundle files across multiple engine versions. Implemented mainly in C++ with a Win32-based interface, CMake build support, and a plugin architecture. Bundled plugins import and export textures, text assets, audio clips, meshes, and raw resource data to common formats such as PNG, WAV, OBJ, and DAE. Primary use cases are Unity modding, asset inspection, and game content research workflows. (source: wiki/sources/descriptions/SeriousCache__UABE.md)

Sits in the README **Extracting assets** / Game Assets lane beside offline Unreal tooling such as [[paksmith]] and [[uassetgui]], and complements runtime Unity inspectors like [[unityexplorer]] when the goal is serialized bundle edit rather than in-process hierarchy inspection.

## Links

- Repo: https://github.com/SeriousCache/UABE

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[unityexplorer]] · [[unity-game-hacking]] · [[unturned-godot]] · [[awesome-game-file-format-reversing]] · [[paksmith]] · [[uassetgui]]
