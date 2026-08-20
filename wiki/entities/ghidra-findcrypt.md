---
title: ghidra-findcrypt
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/TorgoTorgo__ghidra-findcrypt.md
updated: 2026-08-20
confidence: medium
---

# ghidra-findcrypt

Ghidra analyzer extension that scans binaries for known cryptographic constants and labels matching implementations during analysis. Written in Java and built with Gradle as a standard Ghidra analyzer plugin. A JSON signature database ships with byte patterns for common algorithms such as AES S-boxes, DES tables, MD5, SHA-1, TEA, Salsa, CRC32, and other cipher or hash constants; the analyzer matches those signatures in program memory so reverse engineers can quickly locate crypto routines. Aimed at malware and game-security analysis where identifying encryption and hashing code in disassembled binaries is a common first step. (source: wiki/sources/descriptions/TorgoTorgo__ghidra-findcrypt.md)

Ghidra-native crypto-constant signature detection—complements the IDA-side [[findcrypt-yara]] YARA plugin and general in-Ghidra tooling such as [[ghidra-cpp-class-analyzer]] and [[ghidra-scripts]].

## Links

- Repo: https://github.com/TorgoTorgo/ghidra-findcrypt

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[findcrypt-yara]] · [[ghidra]] · [[ghidra-gradle-plugin]] · [[findyara-ida]]
