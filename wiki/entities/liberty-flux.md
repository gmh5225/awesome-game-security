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

**LibertyFlux** (monstercameron/LibertyFlux) is a research project rewriting Grand Theft Auto IV's RAGE engine in Rust one function at a time, aiming to run the game as a native 64-bit program on Windows, Windows on ARM, and macOS. Targets reverse engineers, engine researchers, and modding communities studying game architecture, legacy porting, and faithful modern reimplementation without distributing proprietary game content. (source: wiki/sources/descriptions/monstercameron__LibertyFlux.md)

## Architecture

Rust **Cargo workspace** with engine subsystem crates plus binary format parsers for archives, models, audio, collision, and other assets. Dedicated tooling supports verification and live function replacement.

## Verification workflow

Rewritten functions are validated side by side against original behavior using **checker workers** and **Ghidra-based analysis**, then swapped into the running game through hooking and **proxy DLL injection**.

## Positioning

**Game Develop / Source** lane beside [[gta-reversed-modern]] (GTA:SA C++ reimplementation) as a Ghidra-assisted incremental Rust port of a RAGE-era title — contrasts with classic-trilogy re3/reVC trees such as [[game-gta-re3]] by targeting GTA IV's 64-bit native port goal rather than binary-compatible SA replacement.

## Links

- Repo: https://github.com/monstercameron/LibertyFlux (README tag: Game Develop / Source)

## Related

[[gta-reversed-modern]] · [[game-gta-re3]] · [[research-rigor]] · [[static-runtime-evidence]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
