---
title: Pyarmor
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/dashingsoft__pyarmor.md
updated: 2026-08-16
confidence: medium
---

# Pyarmor

**Python command-line obfuscator** that transforms `.py` scripts into still-runnable obfuscated `.py` output so protected code can replace originals without changing the deployment model. Supports multiple obfuscation modes that trade security against performance, including irreversible identifier renaming and converting selected functions to optimized C extensions. Runtime licensing controls include machine binding and expiration dates; on Windows, output can be further shielded with Themida. Runs on Python 2 and 3 across Windows, Linux (including embedded and Raspberry Pi), and macOS on common architectures. Primary use case is shipping Python applications or libraries without exposing readable source. (source: wiki/sources/descriptions/dashingsoft__pyarmor.md)

Script-language protection reference alongside [[javascript-obfuscator]] and [[rust-obfuscator]] — not a game anti-cheat product.

## Links

- Repo: https://github.com/dashingsoft/pyarmor

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[javascript-obfuscator]] · [[rust-obfuscator]] · [[obfcoder]] · [[volatility3]]
