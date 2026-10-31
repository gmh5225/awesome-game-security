---
title: FaceOff
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# FaceOff

**FaceOff** (redlanterndev/faceoff) is a portable **Windows** utility that disables FACEIT's kernel anti-cheat when you are not playing and re-enables it before the next match. It is built in **C#** as a WPF desktop app with a small CLI, toggling the FACEIT kernel driver, the **FACEITService** Windows service, and related client processes while persisting original settings locally. Because FACEIT only accepts a driver loaded at boot, the tool guides administrator elevation and restart when turning protection on or off; batch scripts provide the same behavior without the executable. (source: wiki/sources/descriptions/REDLANTERNDEV__FaceOff.md)

## Positioning

README **Explore AntiCheat System:FACEIT** lane—operational kernel AC exposure management, not a bypass for active matches. Pairs with [[anti-cheat-toggle]] virtualization-lab tooling and FACEIT ecosystem research on [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/redlanterndev/faceoff

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[byovd]]
