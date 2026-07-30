---
title: Shtreeba
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mdilai__Shtreeba.md
updated: 2026-07-30
confidence: medium
---

# Shtreeba

Windows DLL injector that **manually maps** a library into a target process without `LoadLibrary`: resolve imports, apply relocations, and copy PE sections in-process. Includes a UI for selecting targets by process name and a reusable **MMap** library that handles low-level PE section copying, relocation fixups, and import resolution. Useful for studying user-mode manual-map injection—the same tradecraft anti-cheat scanners target when detecting PEB-unlisted executable memory. (source: wiki/sources/descriptions/mdilai__Shtreeba.md)

README lane: Injector.

## Links

- Repo: https://github.com/mdilai/Shtreeba

## Related

[[modexmap]] · [[injectors]] · [[positron]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
