---
title: AC1_RE (Armored Core PS1)
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/byroweb__AC1_RE.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: high
---

# AC1_RE

**AC1_RE** ([byroweb/AC1_RE](https://github.com/byroweb/AC1_RE)) is a reverse-engineering reference and tooling project for *Armored Core* (1997 PlayStation), scoped to the North American **SLUS-01323 (v1.1)** build. It documents file formats, RAM and disc layout, and the runtime pipelines that load missions and levels, drive text and entity systems, simulate combat physics, and execute the **mission-script virtual machine**, with extensive write-ups and cross-reference tables. (source: wiki/sources/descriptions/byroweb__AC1_RE.md)

## Tooling

**Python** utilities extract and repack disc containers, decode geometry and mission data, and reinject rebuilt assets into a user-supplied image. **C behavioral models** and **MIPS patches** verify subsystem behavior against extracted artifacts. **Ghidra** scripts and shell pipelines automate overlay import, decompilation, and xref work; **DuckStation** save-state helpers support live analysis beside static RE. (source: wiki/sources/descriptions/byroweb__AC1_RE.md)

## Assets and research use

Ships **documentation and code only**—no game disc content. Intended for interoperability research, education, and modding (mission editing, localization) with a **legally owned copy** of the game.

## Links

- Repo: https://github.com/byroweb/AC1_RE

## Related

[[static-runtime-evidence]] · [[saturnkit]] · [[ps2-port-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
