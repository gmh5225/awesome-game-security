---
title: unflutter
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/zboralski__unflutter.md
updated: 2026-07-17
confidence: medium
---

# unflutter

Static analyzer for Flutter/Dart AOT snapshots. Recovers class names, function names, and type information lost during AOT compilation by extracting Dart snapshot metadata from Flutter APKs and iOS apps. Python tool that parses the Dart VM snapshot format and emits reconstructed symbols for mobile security researchers and reverse engineers. (source: wiki/sources/descriptions/zboralski__unflutter.md)

Complements APK/IPA triage (apktool/jadx) when the interesting logic lives in Flutter AOT blobs rather than Java/Kotlin or Objective-C surfaces.

## Links

- Repo: https://github.com/zboralski/unflutter

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[il2cpp]] · [[apktool-mcp-server]]
