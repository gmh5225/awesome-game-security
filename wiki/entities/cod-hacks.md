---
title: CoD_Hacks
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/attilathedud__CoD_Hacks.md
updated: 2026-08-18
confidence: medium
---

# CoD_Hacks

Educational Call of Duty v1.5 cheat collection demonstrating classic FPS internal and external architectures in C++. Samples span a multi-feature **Desk.dll** (wallhack, chams, night-mode, no-fog), internal ESP via **world-to-screen** hooking, **OpenGL** wallhack through `glDrawElements` interception, a syscall-based internal wallhack, and an external trainer using **pattern scanning**. Screenshots document each technique for researchers studying OpenGL hooking, game-loop interception, and signature-based memory scan workflows. (source: wiki/sources/descriptions/attilathedud__CoD_Hacks.md)

Useful as a vintage OpenGL-era reference beside other title-specific COD samples such as [[cod7-tools]] and beginner walkthroughs such as [[intro-to-gamehacking]] / [[lab-esp-and-aimbot]].

## Links

- Repo: https://github.com/attilathedud/CoD_Hacks

## Related

[[world-to-screen]] · [[draw-call-hook]] · [[present-hook]] · [[cod7-tools]] · [[intro-to-gamehacking]] · [[hl2esp]] · [[libmem]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
