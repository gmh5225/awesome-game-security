---
title: Legacy Recreated
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/tamcdonald42__legacy-recreated.md
  - wiki/sources/README-categories.md
updated: 2026-11-10
confidence: medium
---

# Legacy Recreated

Unofficial workbench for studying **Septerra Core 1.04** by pairing a **static recompilation** of the shipping Windows executable with systematic **Ghidra** decompilation toward readable C—without redistributing game assets. (source: wiki/sources/descriptions/tamcdonald42__legacy-recreated.md)

## Stack

| Layer | Role |
|-------|------|
| **M-HT SRW static recompilation** | Builds a modern Windows runnable used as a **behavioral oracle** against retail logic |
| **Java Ghidra scripts** | Function inventory, WinMain-rooted call graphs, type application, decompiled export toward C |
| **MSVC / NASM build + Python helpers** | Tooling around the lift/decomp pipeline |
| **Runtime patches** | Art-pack overrides, blit logging, scaled presentation for engine study |

Documented engine internals include game state machines, object slots, and combat registration. (source: wiki/sources/descriptions/tamcdonald42__legacy-recreated.md)

## Audience

Reverse engineers and preservation researchers who want an evidence-backed path from binary analysis to maintainable code—not live multiplayer anti-cheat or memory-cheat delivery. (source: wiki/sources/descriptions/tamcdonald42__legacy-recreated.md)

## Positioning

README category: **Cheat / RE Tools** (Ghidra decompilation workbench). Aligns with [[static-runtime-evidence]] when treating the SRW build as oracle validation for Ghidra exports, beside PE relink/decomp lanes such as [[openmcm2]] and [[sre-re]].

## Related

[[overviews/reverse-engineering]] · [[static-runtime-evidence]] · [[openmcm2]] · [[sre-re]] · [[ghidra]]

## Links

- Repo: https://github.com/tamcdonald42/legacy-recreated
