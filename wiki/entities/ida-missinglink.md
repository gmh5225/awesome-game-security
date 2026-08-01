---
title: ida-missinglink
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/kweatherman__ida_missinglink.md
updated: 2026-08-01
confidence: medium
---

# ida-missinglink

IDA plugin that fills in missing indirect **CALL** and **JMP** target information. Especially useful on C++ OOP-heavy executables where virtual dispatch and indirect branches dominate—surfaces where indirect branches actually land when static analysis leaves targets unresolved. (source: wiki/sources/descriptions/kweatherman__ida_missinglink.md)

Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / IDA Plugins lane.

Complements C++ interface recovery via [[ida-vtable-tools]] and in-IDA signature scanning via [[yara4ida]] (same author).

## Links

- Repo: https://github.com/kweatherman/ida_missinglink

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-vtable-tools]] · [[yara4ida]] · [[rtti-parser]] · [[idaplugins]]
