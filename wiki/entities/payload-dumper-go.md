---
title: payload-dumper-go
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/ssut__payload-dumper-go.md
updated: 2026-07-22
confidence: medium
---

# payload-dumper-go

High-performance Android OTA `payload.bin` dumper written in Go. Extracts partition images with parallelized decompression, payload checksum verification, and direct handling of original zip packages that contain `payload.bin` (xz as an external dependency). Aimed at Android security researchers and ROM developers who need fast partition dumps from OTA update packages before boot-image or filesystem analysis. (source: wiki/sources/descriptions/ssut__payload-dumper-go.md)

Sibling Python tool: [[payload-dumper]]. Adjacent Magisk / boot-image tooling: [[magiskboot]], [[magiskboot-ndk-on-linux]].

## Links

- Repo: https://github.com/ssut/payload-dumper-go

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[payload-dumper]] · [[magiskboot]] · [[magiskboot-ndk-on-linux]]
