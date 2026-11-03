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

**SecNeo Gadget** is a Frida-based toolkit for debugging, dumping, and analyzing Android apps protected by the SecNeo packer. TypeScript agents hook Java and native layers—including DexClassLoader paths, libDexHelper, and ART native-library loading—with anti-debug bypass hooks, on-the-fly DEX dumping, forced class loading for decrypted bytecode, JDWP/jdb attach workflows, and supporting research scripts plus IDA annotation helpers. Aimed at mobile security researchers unpacking SecNeo-hardened games and related protected APKs. (source: wiki/sources/descriptions/strazzere__secneo-gadget.md)

## Links

- Repo: https://github.com/strazzere/secneo-gadget

## Related

[[frida]] · [[appsealing-reversal]] · [[molt-dex]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
