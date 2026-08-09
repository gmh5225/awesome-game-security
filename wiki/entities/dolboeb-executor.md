---
title: dolboeb-executor
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__dolboeb-executor.md
updated: 2026-08-09
confidence: medium
---

# dolboeb-executor

Kernel-mode code executor that loads a vulnerable signed driver and abuses its IOCTL interface to run custom kernel shellcode or call arbitrary kernel functions from user mode. README tags **`Capcom.sys`** as the backend — a historically abused Capcom driver in the canonical [[byovd]] / LOLdriver lane. Aimed at kernel exploitation researchers studying BYOVD-based kernel code execution. (source: wiki/sources/descriptions/gmh5225__dolboeb-executor.md)

Sits in the same arbitrary kernel execution lane as [[lenovo-exec]] and [[pdfwkrnl-exploit]], and complements access-primitive utilities such as [[kur]] and [[vdk]].

## Links

- Repo: https://github.com/gmh5225/dolboeb-executor

## Related

[[byovd]] · [[lenovo-exec]] · [[pdfwkrnl-exploit]] · [[kur]] · [[vdk]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
