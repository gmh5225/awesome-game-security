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

**codebreaker-rs** (mlafeldt/codebreaker-rs) is a published Rust **`no_std`** library that encrypts and decrypts cheat codes for the **CodeBreaker PlayStation 2** accessory. It targets **little-endian** hosts and is meant for tools and homebrew that analyze or author PS2 cheat databases—not live online anti-cheat bypass. (source: wiki/sources/descriptions/mlafeldt__codebreaker-rs.md)

README category: **PlayStation** (PS2 cheat-code format / crypto RE).

## Cipher coverage

- **CodeBreaker v1–v6:** legacy encryption schemes used by older device firmware and saved code lists.
- **CodeBreaker v7+:** RC4-based cipher path for newer lists.
- **Mixed lists:** automatic detection when a single database mixes v1–v6 and v7+ entries.
- **Control lines:** special plaintext directives (for example lines that **disable v7 mode**) are recognized alongside game cheat entries. (source: wiki/sources/descriptions/mlafeldt__codebreaker-rs.md)

## Provenance

Implementation lineage comes from reverse-engineering the accessory’s **MIPS firmware** crypto and porting earlier **C** reference code—useful for studying classic console cheat protection, validating format parsers, and building database editors. (source: wiki/sources/descriptions/mlafeldt__codebreaker-rs.md)

## Links

- Repo: https://github.com/mlafeldt/codebreaker-rs

## Related

[[game-cheats]] · [[ps2-ida-vu-micro]] · [[vifterpreter]] · [[bizhawk]] · [[reaperpy]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
