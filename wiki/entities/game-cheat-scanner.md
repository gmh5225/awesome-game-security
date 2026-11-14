---
title: GameCheat Scanner
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/artur0vi4__GameCheatScanner.md
  - wiki/sources/README-categories.md
updated: 2026-11-14
confidence: medium
---

# GameCheat Scanner

**GameCheat Scanner** (artur0vi4/GameCheatScanner) is a Python desktop memory scanner and editor styled as an ArtMoney or Cheat Engine alternative for **single-player and educational** use. It provides a **Tkinter GUI** on Windows 10/11, attaches to game processes via **WinAPI and ctypes**, and can ship as a standalone **PyInstaller** executable. (source: wiki/sources/descriptions/artur0vi4__GameCheatScanner.md)

## Capabilities

- Simultaneous search for one input value across many **integer and floating-point encodings** in little- and big-endian
- Cheat Engine–style **changed** and **unchanged** scan narrowing with **NumPy-accelerated** memory diffs
- Optional **signature-based classification** of common stats (health, ammo, currency)
- **Mock process** on non-Windows hosts to practice attach-and-scan workflow without real memory access

## Use cases

Intended for **modding**, **reverse-engineering practice**, and **offline experimentation**—not online competitive play or anti-cheat evasion. (source: wiki/sources/descriptions/artur0vi4__GameCheatScanner.md)

## Positioning

Listed in the Cheat memory-scanner lane beside [[cheat-engine]], [[pymemory-editor]], [[simple-memory-editor]], and [[pointer-lab]] as a Windows-focused Python Tkinter alternative with multitype parallel encoding search and CE-style auto-narrowing.

## Links

- Repo: https://github.com/artur0vi4/GameCheatScanner

## Related

[[cheat-engine]] · [[pymemory-editor]] · [[simple-memory-editor]] · [[pointer-lab]] · [[mhsx]] · [[overviews/game-hacking]]