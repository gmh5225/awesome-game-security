---
title: YaraVM
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/milankovo__YaraVM.md
updated: 2026-07-30
confidence: medium
---

# YaraVM

IDA Pro processor module and loader for disassembling compiled YARA rule binaries (`.yar.bin`). Enables static analysis of YARA bytecode and regex bytecode inside IDA rather than treating compiled rules as opaque blobs. (source: wiki/sources/descriptions/milankovo__YaraVM.md)

Parses the YARA arena-based file format—namespaces, rules, strings, code sections, and AC transition tables—and ships a custom type library (`libyara.til`) for struct annotation during RE.

Complements in-IDA Yara *file* scanning via [[yarascan-ida]] (apply rules to samples) and other milankovo IDA helpers such as [[ida-search]] and [[ida-enums-helper]].

## Links

- Repo: https://github.com/milankovo/YaraVM

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[yarascan-ida]] · [[ida-search]] · [[ida-enums-helper]] · [[aho-corasick]] · [[apkid]]
