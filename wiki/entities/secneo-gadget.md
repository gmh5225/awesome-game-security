---
title: SecNeo Gadget
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/strazzere__secneo-gadget.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# SecNeo Gadget

**SecNeo Gadget** is a Frida-based toolkit for debugging, dumping, and analyzing Android applications protected by the **SecNeo** packer. The project is implemented primarily in **TypeScript**, compiled into injectable Frida agents that hook Java and native layers—including `DexClassLoader` logic, **libDexHelper**, and **ART** native-library loading. (source: wiki/sources/descriptions/strazzere__secneo-gadget.md)

Targets reverse engineers and mobile security researchers who need to unpack or study SecNeo-hardened apps, including **mobile games** and **drone-control** software that rely on this protection. Sits beside strazzere’s broader [[android-unpacker]] work and packer-focused Frida lanes such as [[molt-dex]] and AppSealing RE ([[appsealing-reversal]], [[apppealing-new]]).

## Capabilities

- Anti-debug bypass hooks for protected runtime sessions.
- On-the-fly **DEX dumping** and forced class loading for decrypted bytecode.
- **JDWP** and **jdb** attach workflows for live Java debugging.
- Supporting research scripts and **IDA** annotation helpers.

## Links

- Repo: https://github.com/strazzere/secneo-gadget

## Related

[[frida]] · [[android-unpacker]] · [[appsealing-reversal]] · [[molt-dex]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
