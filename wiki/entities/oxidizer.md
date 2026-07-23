---
title: Oxidizer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/sefcom__oxidizer.md
updated: 2026-07-23
confidence: medium
---

# Oxidizer

Fork of angr with Rust-accelerated core components: symbolic execution, CFG recovery, data-flow analysis, and vulnerability detection via native Rust modules. README positions it as a Rust decompiler on angr—high-fidelity pseudocode from stripped binaries, with enum/match/`?` recovery across Rust 1.39–1.93. Useful when RE of Rust game/client binaries needs better structured recovery than stock Hex-Rays-style output. (source: wiki/sources/descriptions/sefcom__oxidizer.md)

## Links

- Repo: https://github.com/sefcom/oxidizer

## Related

[[smallworld]] · [[idadeflat]] · [[ida-rust-demangler]] · [[stp]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
