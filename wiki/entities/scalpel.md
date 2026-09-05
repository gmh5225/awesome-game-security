---
title: Scalpel
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ntdlll__Scalpel.md
updated: 2026-09-05
confidence: medium
---

# Scalpel

Native Java/Swing Ghidra extension providing a dockable dark-mode hex and ASCII editor inside Ghidra. Terminal-inspired grid follows the Listing cursor, supports arbitrary address jumps, configurable read windows from 256 bytes to 64 KiB, inline byte patching through Ghidra transactions, wildcard hex or quoted UTF-8 string search, and hex/ASCII copy while handling unreadable ranges gracefully. Built with plain Swing and Java 21 for reverse engineers and malware analysts who need fast in-place binary inspection during game-security or anti-cheat RE workflows. (source: wiki/sources/descriptions/ntdlll__Scalpel.md)

Complements [[ghidra-hexeditor]] and standalone workbenches such as [[imhex]] and [[hexwalk]]; sits in the Cheat → RE Tools / Ghidra Plugins lane.

## Links

- Repo: https://github.com/ntdlll/Scalpel

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-hexeditor]] · [[imhex]] · [[hexwalk]]
