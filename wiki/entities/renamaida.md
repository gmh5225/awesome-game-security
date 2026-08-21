---
title: Renamaida
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/kirovgrad__Renamaida.md
updated: 2026-08-02
confidence: medium
---

# Renamaida

IDA Pro plugin (Python) that automatically renames unidentified functions in firmware and statically linked binaries by matching them against pre-generated instruction signatures from known open-source or statically linked libraries. Each function is encoded as a sequence of architecture-specific instruction tokens; candidates are scored with the Jaro-Winkler similarity algorithm and renamed when similarity exceeds **0.83** and the function contains at least **ten** instructions. (source: wiki/sources/descriptions/kirovgrad__Renamaida.md)

Users build custom JSON signature databases with an included generator script by compiling target libraries with full debug symbols. The repository ships sample signatures for strongSwan VPN libraries on ARMv5TE. Complements linker `.MAP` import ([[ida-pro-loadmap]]), static-library ID ([[idenlib]]), and struct recovery ([[symless]]) when only stripped firmware or embedded images are available. Cloud ML similarity matching via [[reai-ida]] offers an alternate path when custom signature DBs are unavailable.

## Links

- Repo: https://github.com/kirovgrad/Renamaida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-pro-loadmap]] · [[idenlib]] · [[symless]] · [[reai-ida]] · [[finger]] · [[ida-efiutils]] · [[embedded-hacking]] · [[idaplugins]]
