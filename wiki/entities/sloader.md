---
title: sloader
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/akawashiro__sloader.md
updated: 2026-08-18
confidence: medium
---

# sloader

**sloader** is an alternative **ELF dynamic loader** written in modern C++ that aims to replace glibc's `ld-linux.so` for educational and experimental use. It implements library loading and symbol resolution in a more readable codebase than glibc internals, ships build/test infrastructure and custom glibc testing workflows, and documents loader design trade-offs and current limitations. Primary audience: systems and security researchers studying Linux program loading, linker internals, and low-level runtime mechanics. (source: wiki/sources/descriptions/akawashiro__sloader.md)

Complements PS5/Java and Android ELF loader research such as [[elfloader]] and [[rudroid]] by exposing a standalone Linux `ld-linux.so` replacement rather than console- or mobile-specific load paths. Differs from packers such as [[harmless]] that encrypt and stub-load ELF payloads — sloader targets full dynamic-linker behavior for linker-internals study.

## Links

- Repo: https://github.com/akawashiro/sloader

## Related

[[elfloader]] · [[rudroid]] · [[mojoelf]] · [[harmless]] · [[river]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
