---
title: Pymew
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/qb-0__pymew.md
  - wiki/sources/README-categories.md
updated: 2026-11-24
confidence: medium
---

# Pymew

**Pymew** (qb-0/pymew) is a Python library for **external** game memory manipulation and **transparent target-attached overlays**. The high-level API opens processes, enumerates modules and memory regions, reads and writes typed values, and defines struct layouts, including helpers for common game string formats. The overlay stack supports drawing primitives, fonts, colors, input capture, and global hotkeys, with optional **ImGui** integration for on-screen tools. The runtime is implemented primarily in **Nim** and ships as a **pip-installable** extension with type stubs for editors and static checkers. It targets **Windows and Linux** on **64-bit Python 3.7+**. (source: wiki/sources/descriptions/qb-0__pymew.md)

## Capabilities

- External process attach, module/region enumeration, typed memory read/write, and struct layout helpers (incl. common game string formats)
- Transparent overlay render loop: primitives, fonts, colors, input capture, global hotkeys, optional ImGui UI
- Nim-backed native extension with Python type stubs; cross-platform Win/Linux

## Use cases

Aimed at developers building **external cheat prototypes**, **ESP-style visuals**, and similar **game-security or reverse-engineering experiments** in Python—combining out-of-process memory access with a bundled overlay loop in one library, beside PyMeow-based samples such as [[pythoncs2]] and scanner-focused tools such as [[pymemory-editor]]. (source: wiki/sources/descriptions/qb-0__pymew.md)

## Links

- Repo: https://github.com/qb-0/pymew

## Related

[[pymemory-editor]] · [[pythoncs2]] · [[violetwing]] · [[world-to-screen]] · [[present-hook]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]