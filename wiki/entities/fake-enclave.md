---
title: FakeEnclave
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__FakeEnclave.md
updated: 2026-08-13
confidence: medium
---

# FakeEnclave

Proof-of-concept that **abuses Enclave** — framed for low-level Windows, Linux, and mobile researchers studying unconventional kernel and trust-boundary tricks. Written in C++ and C/C++; README category: Some Tricks / Windows Ring0. (source: wiki/sources/descriptions/gmh5225__FakeEnclave.md)

Sits in the **Virtualization-Based Security (VBS)** research lane beside [[hvci]] / Memory Integrity bypass PoCs such as [[zero-hvci]]: here the focus is misusing Enclave isolation within the VBS stack rather than DSE-only hooks or [[byovd]] physmem primitives alone.

## Links

- Repo: https://github.com/gmh5225/FakeEnclave

## Related

[[hvci]] · [[zero-hvci]] · [[byovd]] · [[r0ak]] · [[overviews/windows-kernel]]
