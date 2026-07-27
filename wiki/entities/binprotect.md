---
title: binprotect
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/noahware__binprotect.md
updated: 2026-07-27
confidence: medium
---

# binprotect

x64 PE **bin-to-bin obfuscator** in C++ that rewrites compiled binaries without adding a new section or requiring source. Includes a custom assembler/disassembler on binwrite, PE parsing with exception directories, RTTI, frame-pointer scanning, relocations, and jump-table recovery; obfuscation runs at basic-block level on disassembled functions. Aimed at software-protection research under Anti Cheat → Obfuscation Engine / PE structural constraints. (source: wiki/sources/descriptions/noahware__binprotect.md)

Useful as a no-new-section PE rewrite reference alongside post-compile mutators such as [[alcatraz]] and bin2bin virtualizers such as [[nocturne]].

## Links

- Repo: https://github.com/noahware/binprotect

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[alcatraz]] · [[nocturne]] · [[wprotect]] · [[vxlang-page]] · [[2pack]]
