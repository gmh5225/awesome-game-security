---
title: CS2-EXT
kind: entity
topics: [game-hacking, graphics-api, windows-kernel]
sources:
  - wiki/sources/descriptions/hendodev__cs2-ext.md
updated: 2026-08-05
confidence: medium
---

# CS2-EXT

External Counter-Strike 2 cheat framework (C++17; Visual Studio x64) that runs outside the game process and reads or manipulates game memory from a separate Windows application. Core modules cover game offsets, vector math, cheat features (aimbot, ESP, spinbot), and a configurable menu. Memory access is abstracted through a pluggable kernel driver interface; an ImGui overlay rendered with DirectX 11 and DXGI provides in-game menu and visual feedback. Aimed at game security researchers, reverse engineers, and anti-cheat analysts studying external cheat techniques, memory layout, and kernel-assisted process interaction in modern FPS titles. (source: wiki/sources/descriptions/hendodev__cs2-ext.md)

## Links

- Repo: https://github.com/hendodev/cs2-ext

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[cs2-external-cheat]] · [[cs2-cheat-cpp]] · [[cs2-offsets]] · [[present-hook]] · [[byovd]]
