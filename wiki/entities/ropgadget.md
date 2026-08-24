---
title: ROPgadget
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JonathanSalwan__ROPgadget.md
updated: 2026-08-24
confidence: medium
---

# ROPgadget

Command-line **ROP gadget finder** for discovering return-oriented programming chains in binary files. Written in Python with the Capstone disassembly engine; supports **ELF**, **PE**, **Mach-O**, and raw binaries across many CPU architectures. Offers filtering, search, and optional ROP chain generation for exploit development and binary reverse engineering workflows. (source: wiki/sources/descriptions/JonathanSalwan__ROPgadget.md)

Canonical Python gadget scanner from JonathanSalwan (same author as [[triton]]); complements Rust [[ropgadget-rs]], constraint-driven chain builders [[exrop]] and [[angrop]], and live-process finders such as [[agafi]].

## Links

- Repo: https://github.com/JonathanSalwan/ROPgadget

## Related

[[triton]] · [[ropgadget-rs]] · [[exrop]] · [[angrop]] · [[agafi]] · [[rop-compiler]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
