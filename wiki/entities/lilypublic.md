---
title: lilypublic
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/dot1991__lilypublic.md
updated: 2026-08-16
confidence: medium
---

# lilypublic

Game **cheat framework** combining kernel-mode and user-mode components with **DBVM** hypervisor integration for physical memory read/write, pattern scanning, and **object callbacks**. User-mode side adds encrypted strings, compile-time obfuscation, shellcode injection helpers, and remote process manipulation; overlays render through multiple backends — DirectComposition, DirectDraw, and DirectX 9/11 — with an **ImGui** menu. Aimed at game-security researchers studying advanced cheat architectures that stack hypervisor access, kernel drivers, and overlay rendering. (source: wiki/sources/descriptions/dot1991__lilypublic.md)

Sits in the kernel cheat-framework lane beside [[ultra-driver-game-cheat]] and DBVM-assisted stacks such as [[anti-cheat-amateur]]; overlay backends align with DirectX hook / present research in [[overviews/graphics-api]].

## Links

- Repo: https://github.com/dot1991/lilypublic

## Related

[[anti-cheat-amateur]] · [[ultra-driver-game-cheat]] · [[cheatengine-mcp-bridge]] · [[detection-cheat-engine-ring0]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
