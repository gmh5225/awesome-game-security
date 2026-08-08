---
title: il2cpp-finder
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__il2cpp-finder.md
updated: 2026-08-08
confidence: medium
---

# il2cpp-finder

Unity [[il2cpp]] metadata locator that scans game executables and shared libraries for `global-metadata.dat` signatures, `CodeRegistration`, and `MetadataRegistration` pointers. Helps reverse engineers find the entry points needed for IL2CPP dumping and analysis on unfamiliar or obfuscated Unity binaries. (source: wiki/sources/descriptions/gmh5225__il2cpp-finder.md)

Complements static dumpers such as [[il2cppdumper]], emulation-based [[qiling-il2cpp-dump]], and live Frida bridges such as [[frida-il2cpp-bridge]] when analysts must first locate metadata registration structures before running a full dump workflow.

## Links

- Repo: https://github.com/gmh5225/il2cpp-finder

## Related

[[il2cpp]] · [[il2cppdumper]] · [[qiling-il2cpp-dump]] · [[frida-il2cpp-bridge]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
