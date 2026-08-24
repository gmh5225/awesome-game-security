---
title: OpenBarnyard
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/InfiniteC0re__OpenBarnyard.md
updated: 2026-08-24
confidence: medium
---

# OpenBarnyard

**WIP decompilation of Barnyard and the proprietary TOSHI 2.0 engine** (InfiniteC0re/OpenBarnyard). Open-source C++ reimplementation built on a reconstructed **Toshi** engine, recreating core systems—rendering, animation, collision, GUI, audio, and world simulation—with Windows build targets for **DirectX 8** and **OpenGL** via Premake. Includes reverse-engineering progress tooling that tracks reimplemented methods against original binary addresses, plus an SDK with **Detours**-based hooks, mod loading, ImGui debugging, and sample mods for enhanced graphics and speedrunning. Primary use case is game reverse engineering, engine reconstruction, and modding research around legacy Toshi-based titles. (source: wiki/sources/descriptions/InfiniteC0re__OpenBarnyard.md)

Sits in the Game Engine / source lane beside other readable engine decompilations such as [[rsdkv5-decompilation]] and [[gta-reversed-modern]], with hook/mod surfaces comparable to Detours-based SDK workflows ([[detours]]).

## Links

- Repo: https://github.com/InfiniteC0re/OpenBarnyard (README tag: WIP decompilation of Barnyard and the proprietary TOSHI 2.0 engine, with Ghidra RE workflow)

## Related

[[rsdkv5-decompilation]] · [[gta-reversed-modern]] · [[devilution]] · [[detours]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[research-rigor]]
