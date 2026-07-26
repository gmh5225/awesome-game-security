---
title: VMPUnpacker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/oureveryday__VMPUnpacker.md
updated: 2026-07-26
confidence: medium
---

# VMPUnpacker

C++ and Python unpacker for VMProtect-packed executables. Uses LZMA decompression to extract the original PE from VMProtect’s packed payload, recovering original sections and import tables. Aimed at reverse engineers and malware analysts who need automated unpacking of VMProtect-packed binaries before deeper RE. (source: wiki/sources/descriptions/oureveryday__VMPUnpacker.md)

Companion surface to other Cheat → Fix VMP research: static/native PE unpack (LZMA → sections/IAT) rather than symbolic-exec handler recovery ([[novmpy]], [[rumba]]), VTIL demos ([[vmdevirt-vtil]]), or .NET runtime dump ([[vmunprotect-dumper]]).

## Links

- Repo: https://github.com/oureveryday/VMPUnpacker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmpy]] · [[rumba]] · [[vmdevirt-vtil]] · [[vmunprotect]] · [[vmunprotect-dumper]]
