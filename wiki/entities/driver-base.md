---
title: DriverBase
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/SecondNewtonLaw__DriverBase.md
updated: 2026-08-21
confidence: medium
---

# DriverBase

**Starter template for Windows kernel-mode drivers** built with **CMake** and **KMDF**. Primarily C++, with scaffolding for driver entry, **FindWDK** integration for WDK toolchain discovery, and optional compile-time obfuscation helpers (bundled `obfusheader.h`). The layout simplifies cross-version Windows target configuration while keeping code close to real kernel constraints. Useful for security researchers and low-level developers who need a clean baseline for driver prototyping rather than a full cheat or AC product. (source: wiki/sources/descriptions/SecondNewtonLaw__DriverBase.md)

README lane: obfusheader.h for windows driver.

## Links

- Repo: https://github.com/SecondNewtonLaw/DriverBase
- Bundled obfuscation header: https://github.com/SecondNewtonLaw/DriverBase/blob/dev/Dependencies/obfusheader.h

## Related

[[windows-kernel-rs]] · [[kli]] · [[kernelcloak]] · [[obfusheader-h]] · [[wdutf]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
