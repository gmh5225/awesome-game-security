---
title: idenLib
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/secrary__idenLib.md
updated: 2026-07-23
confidence: medium
---

# idenLib

IDA Pro C++ plugin for identifying statically linked library functions in stripped PE binaries. Matches function byte patterns against a known-library signature database (FLIRT-adjacent, different matching approach) to recover names from Visual C++ runtime, STL, and other commonly linked libraries—helping rename unknown functions in stripped Windows executables. (source: wiki/sources/descriptions/secrary__idenLib.md)

Sits in the Cheat Library Function Identification / IDA Plugins lane. Dynamic counterpart: [[idenlibx]] (x64dbg plugin). Complements IDA signature tooling such as [[ida-fusion]] and [[yarascan-ida]].

## Links

- Repo: https://github.com/secrary/idenLib

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idenlibx]] · [[ida-fusion]] · [[yarascan-ida]] · [[idaplugins]] · [[x64dbg]]
