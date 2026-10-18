---
title: AC1_RE (Armored Core PS1)
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/byroweb__AC1_RE.md
  - wiki/sources/README-categories.md
updated: 2026-10-18
confidence: medium
---

# AC1_RE

Reverse-engineering reference and tooling for *Armored Core* (1997 PlayStation, North American SLUS-01323 v1.1). Documents disc and RAM layouts, mission/level loading, text and entity systems, combat physics, and the mission-script virtual machine, with write-ups and verification harnesses. Python utilities extract/repack disc containers and decode geometry and mission data; C behavioral models and MIPS patches validate subsystems against extracted artifacts. Ghidra automation and DuckStation save-state helpers support static and live analysis. Ships documentation and tooling only—users supply a legally owned disc copy for interoperability research, education, and modding (mission editing, localization). (source: wiki/sources/descriptions/byroweb__AC1_RE.md)

## Links

- Repo: https://github.com/byroweb/AC1_RE

## Related

[[static-runtime-evidence]] · [[saturnkit]] · [[ps2-port-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
