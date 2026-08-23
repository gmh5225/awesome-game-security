---
title: Dumpy
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Kudaes__Dumpy.md
updated: 2026-08-23
confidence: medium
---

# Dumpy

**Dumpy** is a **Rust-based** Windows **LSASS memory dumping** tool that avoids directly opening `lsass.exe`. Instead it **enumerates and duplicates existing process handles** via native Windows object and system-information APIs, reducing obvious direct-open telemetry. Output supports **XOR-protected dumps**, optional **HTTP upload**, and a **decryption mode** to restore captured data. (source: wiki/sources/descriptions/Kudaes__Dumpy.md)

Useful for controlled offensive security research and **detection-evasion testing** around credential-extraction tooling — complementary to handle-theft dumps such as [[lsass-dump-that-lsass]], minimal handle-hijack teaching PoCs such as [[handle-ripper]], and elevated-handle memory toolkits such as [[nobastian-v2]]. Same-author evasion crates: [[shelter]], [[unwinder]], and [[puzzle]].

README category: Reuse opened handles By LSASS (Elevating Handle).

## Links

- Repo: https://github.com/Kudaes/Dumpy

## Related

[[lsass-dump-that-lsass]] · [[handle-ripper]] · [[nobastian-v2]] · [[kslkatz]] · [[minidump]] · [[kvcforensic]] · [[shelter]] · [[unwinder]] · [[puzzle]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
