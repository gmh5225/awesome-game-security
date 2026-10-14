---
title: Universal Asset Ripper
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/laurentvv__universal-asset-ripper.md
updated: 2026-10-14
confidence: medium
---

# Universal Asset Ripper

Engine-agnostic TypeScript/Node.js platform for extracting assets from commercial game packages and feeding AI-assisted reverse-engineering workflows. Native parsers cover Godot PCK, Unreal PAK/IoStore, Unity bundles and IL2CPP metadata, and Windows PE resources (icons, Delphi forms). The CLI auto-detects engine/framework, catalogs and filters assets, runs Shannon entropy scans for AES key hunting, and emits structured evidence bundles. An integrated MCP server exposes the same operations to coding agents—aimed at modders, engine researchers, and security analysts doing offline package reconnaissance. (source: wiki/sources/descriptions/laurentvv__universal-asset-ripper.md)

README **Game Assets** lane beside UE-focused [[paksmith]]/[[uassetgui]] tooling and cross-engine indexes such as [[awesome-game-file-format-reversing]].

## Links

- Repo: https://github.com/laurentvv/universal-asset-ripper

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[paksmith]] · [[uassetgui]] · [[uassetapi]] · [[asset-ripper]] · [[awesome-game-file-format-reversing]]
