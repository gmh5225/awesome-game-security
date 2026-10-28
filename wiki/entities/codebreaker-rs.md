---
title: codebreaker-rs
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/mlafeldt__codebreaker-rs.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# codebreaker-rs

**codebreaker-rs** (mlafeldt/codebreaker-rs) is a Rust **`no_std`** library that encrypts and decrypts cheat codes for the **CodeBreaker PlayStation 2** accessory. It implements legacy schemes from **CodeBreaker v1 through v6** and the **v7+ RC4-based** cipher, including automatic detection of mixed code lists and special control lines (for example lines that disable v7 mode). The crate targets little-endian platforms and is intended for tools and homebrew that analyze or author PS2 cheat databases. (source: wiki/sources/descriptions/mlafeldt__codebreaker-rs.md)

README category: **PlayStation** (PS2 cheat-code format / crypto RE).

## Technical notes

Derived from reverse-engineering the device’s **MIPS firmware** crypto and porting earlier C implementations—useful for classic console cheat protection study and database tooling, not online anti-cheat bypass.

## Links

- Repo: https://github.com/mlafeldt/codebreaker-rs

## Related

[[game-cheats]] · [[reaperpy]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
