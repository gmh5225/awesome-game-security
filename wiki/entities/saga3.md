---
title: Saga3
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/newlix__saga3.md
updated: 2026-11-24
confidence: medium
---

# saga3

Reverse-engineering and recreation workspace for the fan-hacked Super Famicom *Romancing SaGa 3* (**bokuno**) ROM, aimed at reimplementing the title outside the original cartridge binary. **Go** command-line tools apply **IPS** and **xdelta** patches, disassemble the **65816** event virtual machine, and export maps, dialogue, battles, sprites, and related game data into structured **JSON** for analysis and runtime use. (source: wiki/sources/descriptions/newlix__saga3.md)

The tree documents ROM build chains, **parity gates**, and extensive notes on battle formulas, triggers, and VM semantics. A playable shell runs via **Go** and **Ebitengine** with swappable localization tables; the repository ships tools and verification data only—not copyrighted ROM images (**BYO ROM**). (source: wiki/sources/descriptions/newlix__saga3.md)

Targets ROM hackers, reverse engineers, and preservationists who need reproducible extraction, verification, and localization workflows for classic JRPG binaries—not live anti-cheat or online security research. Sit beside other SNES preservation/remake work ([[zelda3]], [[harvest-moon-snes-decomp]]) and apply [[static-runtime-evidence]] when separating exported JSON/VM semantics from the Ebitengine host runtime. (source: wiki/sources/descriptions/newlix__saga3.md)

## Links

- Repo: https://github.com/newlix/saga3 (README: Reverse-engineering workspace and Go/Ebitengine reimplementation for the bokuno *Romancing SaGa 3* ROM hack—tools and verification data only)

## Related

[[zelda3]] · [[harvest-moon-snes-decomp]] · [[static-runtime-evidence]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]