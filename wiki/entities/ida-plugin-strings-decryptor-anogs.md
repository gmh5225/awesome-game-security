---
title: IDA Plugin Strings Decryptor (Anogs/ACE)
kind: entity
topics: [reverse-engineering, mobile-security, anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/pIat0n__IDA-Plugin-Strings-decryptor-Anogs.md
updated: 2026-10-31
confidence: medium
---

# IDA Plugin Strings Decryptor (Anogs/ACE)

**ida-plugin-strings-decryptor-anogs** ([piat0n/ida-plugin-strings-decryptor-anogs](https://github.com/piat0n/ida-plugin-strings-decryptor-anogs)) is a set of **IDA Pro Python (IDAPython) scripts** that **auto-detect, decrypt, and annotate obfuscated strings** in **Tencent Anogs / ACE (Anti-Cheat Expert, TSS)** shared libraries such as **`libanogs.so`** from **ARM Android** mobile titles (including **PUBG Mobile** profiles). (source: wiki/sources/descriptions/pIat0n__IDA-Plugin-Strings-decryptor-Anogs.md)

## Workflow

- A **master entry script** routes **ARM32** and **ARM64** binaries to **version-specific** decrypt engines.
- **Decryptor and accessor functions** are found heuristically via **cross-references**; on **ARM64**, **ADR / ADRL** instructions can help **infer string-table locations**.
- Recovered plaintext is written as **inline comments** in disassembly and **Hex-Rays** pseudocode, with optional export as **formatted text** and **JSON** (including **call-site metadata**). (source: wiki/sources/descriptions/pIat0n__IDA-Plugin-Strings-decryptor-Anogs.md)

## Research use

Accelerates static RE on ACE-protected Android binaries listed under README **Cheat → RE Tools**, complementing narrative ACE catalogs such as [[ff-ace-anticheat-analysis]] and defensive [[mobile-anti-cheat]] boundary review—not a bypass or live cheat.

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[ida-gameguard-str-dec]] · [[ida-jm-xorstr-decrypt-plugin]] · [[ff-ace-anticheat-analysis]] · [[mobile-anti-cheat]] · [[research-rigor]]

## Links

- Repo: https://github.com/piat0n/ida-plugin-strings-decryptor-anogs
