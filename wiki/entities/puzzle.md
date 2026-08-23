---
title: Puzzle
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Kudaes__Puzzle.md
updated: 2026-08-23
confidence: medium
---

# Puzzle

**Puzzle** is a collection of **Rust-based** Windows **persistence and evasion** tools demonstrating **minifilter abuse** for stealth and concealment. Techniques include **bind links**, **ID mapping**, **cloud file sync providers**, and **WIM hash manipulation** for post-exploitation hiding. (source: wiki/sources/descriptions/Kudaes__Puzzle.md)

Sits in the cheat / hide lane beside other minifilter stealth samples such as [[memfilter-fn-driver]] and [[hide-file]], and defensive FSFilter references such as [[vaultguard]]. Same-author evasion crates: [[shelter]] (ROP sleep obfuscation) and [[unwinder]] (call-stack spoofing).

## Links

- Repo: https://github.com/Kudaes/Puzzle

## Related

[[memfilter-fn-driver]] · [[hide-file]] · [[vaultguard]] · [[shelter]] · [[unwinder]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
