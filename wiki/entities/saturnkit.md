---
title: Saturnkit
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/vs-sr-dev__saturnkit.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# Saturnkit

**Saturnkit** (vs-sr-dev/saturnkit) is a game-agnostic toolkit for Sega Saturn reverse engineering and building native PC ports of Saturn titles. Listed under README **Cheat / RE Tools**. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

## Analysis toolchain

Pure **Python** modules parse disc images and **IP.BIN** boot metadata, decode and analyze **SH-2** executables, map hardware registers, discover functions, and match code across programs. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

## Static recompilation

Translates SH-2 binaries to **C++** through a static recompilation pipeline, separating platform translation from per-title port logic. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

## Hardware runtime

A **C++20** runtime emulates Saturn hardware — dual **SH-2** CPUs, **VDP1** and **VDP2** graphics, **SCU**, **SMPC**, **CD block**, and **SCSP** sound with a **Musashi 68000** — and runs recompiled code in an **SDL3** and **OpenGL** window with gamepad support. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

## Integration model

Designed to embed as a **git submodule** in per-game port projects so shared Saturn platform knowledge stays separate from title-specific logic. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

## Positioning

Sits in the retro-console RE lane beside title-specific format docs such as [[pc-wackywheels-doc]] and [[omikron-tns-omk-engine]] — a platform toolkit for Saturn disc/CPU analysis and static recompilation rather than a single-game write-up. Targets reverse engineers and developers porting or analyzing Sega Saturn titles.

## Links

- Repo: https://github.com/vs-sr-dev/saturnkit [Game-agnostic Sega Saturn RE toolkit: disc/IP.BIN parsing, SH-2 decode, static recompilation to C++, and a hardware runtime (VDP1/2, SCU, SMPC, CD block, SCSP) for native PC ports]

## Related

[[pc-wackywheels-doc]] · [[omikron-tns-omk-engine]] · [[jsrf-recomp]] · [[mcla-pc]] · [[awesome-game-file-format-reversing]] · [[static-runtime-evidence]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
