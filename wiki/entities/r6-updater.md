---
title: r6-updater
kind: entity
topics: [game-hacking, reverse-engineering, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/Kix48__R6Updater.md
updated: 2026-08-23
confidence: medium
---

# r6-updater

**R6Updater** (Kix48) is a **Rainbow Six Siege offset dumper and updater** for reverse engineers and cheat developers maintaining title-specific data after patches. Implemented in **C++** as a **Visual Studio x64 Windows** tool with separate **pattern-scan** and **memory-module** components, it locates managers and **patch-sensitive offsets** via signature scanning and refreshes usable offsets during an active game session. Framed for post-update signature maintenance and runtime offset extraction against the [[battleye]]-protected Siege client. (source: wiki/sources/descriptions/Kix48__R6Updater.md)

Complements broader R6 external dump tooling such as [[r6-cheat-dumper]] (driver/rendering/animation layout extraction) and runnable externals such as [[r6-external]] and [[r6s-external-v2]] by focusing on lightweight offset/signature refresh rather than full cheat-structure dumps.

## Links

- Repo: https://github.com/Kix48/R6Updater

## Related

[[battleye]] · [[r6-cheat-dumper]] · [[r6-external]] · [[r6s-external-v2]] · [[r6-internal-v3]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
