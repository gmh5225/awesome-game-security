---
title: revert-mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/zorftw__revert-mapper.md
updated: 2026-07-17
confidence: medium
---

# revert-mapper

Windows research mapper that loads an unsigned kernel driver into memory, runs its entry point, then **reverts** the mapping: frees allocated pages, strips pool tags, and clears leftover references so post-execution artifacts are harder for anti-cheat memory scanners to find. (source: wiki/sources/descriptions/zorftw__revert-mapper.md)

Useful for studying manual-map forensics (pool tags, residual mappings) and how cleanup after driver execution interacts with AC detection—not a production evasion tool.

## Links

- Repo: https://github.com/zorftw/revert-mapper

## Related

[[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
