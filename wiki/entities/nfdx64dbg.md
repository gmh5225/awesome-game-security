---
title: NFD x64dbg
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/horsicq__nfdx64dbg.md
updated: 2026-08-05
confidence: medium
---

# NFD x64dbg

[[x64dbg]] plugin that embeds **Nauz File Detector (NFD)** static scanning inside the debugger. Adds an NFD tab to scan the currently loaded module or file and view detection results for compilers, linkers, packers, protectors, and related binary signatures. Written in C++ with Qt UI components; integrates through the x64dbg plugin SDK with build scripts for 32-bit and 64-bit Windows targets. Aimed at reverse engineers and malware or game-security analysts who need in-debugger static identification of how a binary was built or protected. (source: wiki/sources/descriptions/horsicq__nfdx64dbg.md)

Not a standalone file triage tool—live module/file static ID inside [[x64dbg]]; the upstream standalone scanner is [[nauz-file-detector]]. Complementary to peers such as [[stringsx64dbg]] (string search/browse) and [[idenlibx]] (static-library function naming).

## Links

- Repo: https://github.com/horsicq/nfdx64dbg

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[nauz-file-detector]] · [[x64dbg]] · [[x64dbg-plugin-manager]] · [[stringsx64dbg]] · [[idenlibx]]
