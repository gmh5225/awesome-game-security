---
title: crossover-patcher
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/dazi2011__crossover-patcher.md
updated: 2026-08-16
confidence: medium
---

# crossover-patcher

**CrossOver Patcher** is an experimental macOS compatibility tool that patches official **CrossOver** installations to improve support for Windows games protected by anti-cheat systems. It targets **Apple Silicon** Macs running **macOS 14+**, applies narrowly scoped, version-bound binary transformations to CrossOver’s **Wine** and **graphics runtime** modules after validating official signatures, file hashes, and PE/Mach-O structure, and ships via a graphical app or closed-source **PatchCore CLI**. The installer creates a separate patched CrossOver copy with authenticated backups and rollback support while leaving game files, anti-cheat components, and existing CrossOver bottles untouched. Explicit support is limited to specific verified CrossOver release builds; documented targets include anti-cheat-protected titles such as **Wuthering Waves**. (source: wiki/sources/descriptions/dazi2011__crossover-patcher.md)

Sits in the macOS **Wine / CrossOver compatibility** lane beside GNU/Linux **Proton/Wine** workflows tracked by AreWeAntiCheatYet and userspace AC-driver study samples such as [[holodori-kernel-bypass]], but focuses on host-runtime patching rather than in-game cheat tooling.

## Links

- Repo: https://github.com/dazi2011/crossover-patcher

## Related

[[holodori-kernel-bypass]] · [[elden-ring-ct-tga]] · [[ptrace-read-teb]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
