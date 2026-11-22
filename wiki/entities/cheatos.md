---
title: CheatOS
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/tertit133__cheatos.md
updated: 2026-11-22
confidence: medium
---

# CheatOS

**CheatOS** (tertit133/cheatos) is a compact **Windows x64** memory scanner and trainer framework modeled after **Cheat Engine**: attach to processes, enumerate regions, run background scans, and manipulate live game memory. It is built in **C++20** with **CMake**, using **Dear ImGui** and **DirectX 11** for a docking UI and a modular engine for attachment and scanning work. (source: wiki/sources/descriptions/tertit133__cheatos.md)

Capabilities include typed first- and next-scan filters, byte patterns with wildcards, bookmarked addresses with a high-frequency value-freezer thread, and **BFS pointer-chain discovery** rooted in module images. The tool can load and save a practical subset of Cheat Engine **`.CT` tables** through **pugixml**, which makes it useful for reverse engineers, trainer authors, and game security researchers who want a small, readable codebase to study memory scanning and trainer behavior on Windows.

## Links

- Repo: https://github.com/tertit133/cheatos

## Related

[[cheat-engine]] · [[cttrainer]] · [[pointer-lab]] · [[simple-memory-editor]] · [[cheat-engine-tables]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]