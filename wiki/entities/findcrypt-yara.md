---
title: findcrypt-yara
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__findcrypt-yara.md
updated: 2026-08-08
confidence: medium
---

# findcrypt-yara

IDA Pro plugin (FindCrypt) that identifies cryptographic constants and algorithm implementations in disassembled binaries using YARA rules. Scans for known byte patterns of AES S-boxes, DES permutation tables, SHA hash constants, CRC lookup tables, and other crypto signatures, annotating identified locations with algorithm names. Python plugin aimed at malware analysts and reverse engineers locating cryptographic code in unknown binaries. (source: wiki/sources/descriptions/gmh5225__findcrypt-yara.md)

Built-in crypto-constant signature detection—not a general-purpose custom YARA rule runner.

Complements the Ghidra-side [[ghidra-findcrypt]] analyzer (Java Gradle extension; JSON crypto-constant signatures; labels AES/DES/MD5/SHA/TEA/Salsa/CRC32 routines during Ghidra analysis; TorgoTorgo) and general in-IDA YARA tooling such as [[findyara-ida]] (custom rule scan + match navigation), [[yara4ida]], [[yarascan-ida]], rule generation via [[hyara]], and compiled-rule analysis via [[yaravm]].

## Links

- Repo: https://github.com/gmh5225/findcrypt-yara

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[findyara-ida]] · [[yara4ida]] · [[yarascan-ida]] · [[hyara]] · [[yaravm]] · [[ghidra-findcrypt]] · [[idaplugins]]
