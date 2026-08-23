---
title: Win32.Nebula
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/Lima-X__Win32.Nebula.md
updated: 2026-08-23
confidence: medium
---

# Win32.Nebula

**Lima-X** proof-of-concept **packed and protected module loader framework** for Windows x64. Written mainly in C++, it separates a lightweight **loader library** from a **builder utility** that patches, encrypts, and packs binaries. The design exposes SDK-style APIs, a dynamic service-manager concept, and low-level Windows-internals implementation choices. Primary use case is research into **software protection**, **loader architecture**, and **anti-analysis techniques** seen in malware and anti-cheat ecosystems—not a turnkey commercial protector. README tags it `[PE X64]`. (source: wiki/sources/descriptions/Lima-X__Win32.Nebula.md)

Useful as a modular loader/packer reference alongside [[polyengine]], [[atom-pe-packer]], and [[wizard-loader]]—not a full unpacker or AC product.

## Links

- Repo: https://github.com/Lima-X/Win32.Nebula

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[polyengine]] · [[atom-pe-packer]] · [[hm-pe-packer]] · [[pe-packer]] · [[wizard-loader]] · [[windows-process-injection]] · [[rs-ldr]]
