---
title: LibertyFlux
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/monstercameron__LibertyFlux.md
  - wiki/sources/README-categories.md
updated: 2026-10-04
confidence: medium
---

# LibertyFlux

**LibertyFlux** (monstercameron/LibertyFlux) is a research project rewriting Grand Theft Auto IV's RAGE engine in Rust one function at a time, aiming to run the game as a native 64-bit program on Windows, Windows on ARM, and macOS. The codebase is a Rust Cargo workspace with engine subsystem crates, binary format parsers for archives, models, audio, collision, and other assets, plus tooling for verification and live function replacement. Rewritten functions are validated side by side against original behavior using checker workers and Ghidra-based analysis, then swapped into the running game through hooking and proxy DLL injection. Targets reverse engineers, engine researchers, and modding communities studying game architecture, legacy porting, and faithful modern reimplementation without distributing proprietary game content. (source: wiki/sources/descriptions/monstercameron__LibertyFlux.md)

Sits in the **Game Develop / Source** lane beside [[gta-reversed-modern]] (GTA:SA C++ reimplementation) as a Ghidra-assisted incremental Rust port of a RAGE-era title.

## Links

- Repo: https://github.com/monstercameron/LibertyFlux (README tag: Game Develop / Source)

## Related

[[gta-reversed-modern]] · [[research-rigor]] · [[static-runtime-evidence]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
