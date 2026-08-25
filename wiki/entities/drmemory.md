---
title: Dr. Memory
kind: entity
topics: [reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/DynamoRIO__drmemory.md
updated: 2026-08-25
confidence: medium
---

# Dr. Memory

**Dr. Memory** is a dynamic memory debugger that detects common runtime memory errors in native programs. Built largely in C and C++ on top of the **DynamoRIO** instrumentation platform, it finds uninitialized reads, out-of-bounds accesses, use-after-free, double frees, and leaks, with additional Windows-specific checks for handle and GDI misuse. It runs on unmodified binaries across Windows, Linux, macOS, and Android on IA-32, AMD64, and ARM targets. The project is widely used for software hardening and security bug hunting, including reliability testing of game and anti-cheat code. (source: wiki/sources/descriptions/DynamoRIO__drmemory.md)

Sits beside DynamoRIO-based coverage fuzzing ([[winafl]]), lightweight DBI ([[tinyinst]]), and the broader [[dynamic-binary-instrumentation]] taxonomy.

## Links

- Repo: https://github.com/DynamoRIO/drmemory

## Related

[[winafl]] · [[tinyinst]] · [[dynamic-binary-instrumentation]] · [[rev-tools-setup]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
