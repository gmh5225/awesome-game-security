---
title: Ferret
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Petru101__ferret.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# Ferret

**Ferret** (Petru101/ferret) is a Linux desktop memory editor for finding and changing in-game values such as health, gold, and ammo without traditional scan-first workflows. Written in **Rust** with a **GTK 4** and **libadwaita** GUI, it uses screen capture and **OCR** so you click numbers visible in the game window, narrows candidates as you play, and can persist values across restarts via pointer paths and engine-specific browsing for Unreal, Unity, Godot, GameMaker, Java, Python, and other runtimes. (source: wiki/sources/descriptions/Petru101__ferret.md)

## Architecture

- Flatpak UI stays sandboxed; a separate host helper performs **ptrace**-based read and write
- OCR-click narrowing, freeze/set, and auto re-resolve after restarts (Cheat Engine–style ergonomics)
- Blocks or warns on online titles using local anti-cheat process checks and an embedded **AreWeAntiCheatYet** game list

## Use cases

Targets **single-player and offline** use on native Linux and **Proton/Wine** games—for modding, testing, and studying how titles store state—in the same practical space as Cheat Engine, [[pince]], or GameConqueror on Linux. (source: wiki/sources/descriptions/Petru101__ferret.md)

## Positioning

Listed under **Cheat → Debugging** beside cross-platform scanners such as [[pymemory-editor]] and Linux GDB workflows such as [[pince]] and [[edb-debugger]].

## Links

- Repo: https://github.com/Petru101/ferret

## Related

[[pymemory-editor]] · [[pince]] · [[edb-debugger]] · [[cheat-engine]] · [[are-we-anti-cheat-yet]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
