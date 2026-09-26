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

Game-agnostic toolkit for Sega Saturn reverse engineering and building native PC ports. Pure Python modules parse disc images, decode and analyze SH-2 executables, map hardware registers, discover functions, match code across programs, and statically recompile SH-2 binaries to C++. A C++20 runtime emulates Saturn hardware — both SH-2 CPUs, VDP1/VDP2 graphics, SCU, SMPC, CD block, and SCSP sound with a Musashi 68000 — and runs recompiled code in an SDL3/OpenGL window with gamepad support. Designed as a submodule in per-game port projects, separating shared Saturn platform knowledge from title-specific logic. (source: wiki/sources/descriptions/vs-sr-dev__saturnkit.md)

Sits in the Cheat **RE Tools** lane beside title-specific retro format docs such as [[pc-wackywheels-doc]] and [[omikron-tns-omk-engine]] — platform toolkit for Saturn disc/CPU analysis and static recompilation rather than a single-game write-up.

## Scope

| Area | Focus |
|------|-------|
| **Disc / IP.BIN** | Disc image parsing and boot metadata |
| **SH-2** | Decode, function discovery, cross-program matching |
| **Static recomp** | SH-2 → C++ translation pipeline |
| **Runtime** | VDP1/2, SCU, SMPC, CD block, SCSP emulation |
| **Integration** | Submodule layout for per-title port repos |

## Links

- Repo: https://github.com/vs-sr-dev/saturnkit [Game-agnostic Sega Saturn RE toolkit: disc/IP.BIN parsing, SH-2 decode, static recompilation to C++, and a hardware runtime (VDP1/2, SCU, SMPC, CD block, SCSP) for native PC ports]

## Related

[[pc-wackywheels-doc]] · [[omikron-tns-omk-engine]] · [[awesome-game-file-format-reversing]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
