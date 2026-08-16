---
title: rehlds
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/dreamstalker__rehlds.md
updated: 2026-08-16
confidence: medium
---

# rehlds

Reverse-engineered, bugfixed reimplementation of the **Half-Life Dedicated Server (HLDS)** (builds 6152/6153) by dreamstalker. Rebuilt using **DWARF debug info** from the original Linux `engine_i486.so` binary; fixes numerous defects found during reverse engineering while maintaining full compatibility with the GoldSource engine protocol, HLTV, and game mods. Aimed at game server operators, engine researchers, and modders studying GoldSource internals—not a cheat or anti-cheat artifact. (source: wiki/sources/descriptions/dreamstalker__rehlds.md)

Distinct from full GoldSrc engine-component reimplementations such as [[regs]], decompiled/reconstructed rebuilds such as [[goldsource-rebuild]], CS1.6 server game-DLL drop-ins such as [[regamedll-cs]], and master-server protocol work such as [[hlmaster]]; this is the **HLDS dedicated-server** lane for running improved Half-Life 1 servers beside other GoldSrc study surfaces.

## Links

- Repo: https://github.com/dreamstalker/rehlds (README tag: [Reverse-engineered HLDS])

## Related

[[regs]] · [[goldsource-rebuild]] · [[hlmaster]] · [[regamedll-cs]] · [[source-engine]] · [[hl-mods]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[research-rigor]]
