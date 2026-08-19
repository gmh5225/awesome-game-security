---
title: integrity
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/afulsamet__integrity.md
updated: 2026-08-19
confidence: medium
---

# integrity

Header-only C library from afulsamet for **runtime memory integrity verification** of Windows PE images. Computes baseline checksums for non-writable sections and re-checks them later to detect unauthorized code modifications. Supports hardware-accelerated CRC32 via SSE4.2 and allows custom checksum algorithms through compile-time configuration. Targets defensive use cases: tamper detection, anti-cheat hardening, and runtime self-protection experiments (`Detection:Memory Integrity`). (source: wiki/sources/descriptions/afulsamet__integrity.md)

Complements live-vs-disk patch discovery such as [[patch-finder]], header-only experiment corpora such as [[integrity-experiments]], and reusable page-guard libraries such as [[memory-guard]].

## Links

- Repo: https://github.com/afulsamet/integrity

## Related

[[patch-finder]] · [[integrity-experiments]] · [[memory-guard]] · [[anticheat-poc]] · [[basic-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
