---
title: thread-namecalling
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/hasherezade__thread_namecalling.md
updated: 2026-08-05
confidence: medium
---

# thread-namecalling

Windows offensive research sample (hasherezade) that abuses **`SetThreadDescription`** / **`GetThreadDescription`**: after setting a thread description locally, **`GetThreadDescription` is invoked remotely on a target thread via APC**, causing the description buffer to be copied into the target process **working set**. Useful for game-security researchers and reverse engineers studying cheat / **injection:windows** tradecraft—especially APC-driven cross-process memory surface manipulation beside kernel APC injectors such as [[injdrv]] / [[kinject]] and working-set monitors such as [[faultline]]. (source: wiki/sources/descriptions/hasherezade__thread_namecalling.md)

## Links

- Repo: https://github.com/hasherezade/thread_namecalling

## Related

[[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[apc-research]] · [[injdrv]] · [[kinject]] · [[windows-process-injection]] · [[faultline]]
