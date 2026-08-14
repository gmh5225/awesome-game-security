---
title: CallStackSpoofer-2
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__CallStackSpoofer-2.md
updated: 2026-08-14
confidence: medium
---

# CallStackSpoofer-2

**CallStackSpoofer-2** is an **x64 call-stack spoofing** implementation for Windows that uses **custom assembly trampolines** to forge return addresses and manipulate stack frames so thread stack walks see a clean, module-plausible call chain. Targets **EDR and anti-cheat stack-walking analysis**; ships with **inline ASM support for MSVC**. (source: wiki/sources/descriptions/gmh5225__CallStackSpoofer-2.md)

Sits in the `Cheat > Spoof Stack` lane beside return-address libraries such as [[spoof-stack-safecall]], macro helpers such as [[stack-spoofer-macro]], and research PoCs such as [[silent-moonwalk]].

## Links

- Repo: https://github.com/gmh5225/CallStackSpoofer-2

## Related

[[stack-spoofing]] · [[spoof-stack-safecall]] · [[stack-spoofer-macro]] · [[return-address-spoofer]] · [[thread-stack-spoofer]] · [[silent-moonwalk]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
