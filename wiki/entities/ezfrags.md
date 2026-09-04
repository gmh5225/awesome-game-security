---
title: ezfrags
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/ALittlePatate__ezfrags.md
updated: 2026-09-04
confidence: medium
---

# ezfrags

Reverse-engineering reconstruction of a well-known legacy FPS cheat (ALittlePatate/ezfrags). The project is mainly **C++** and documents a **decompilation workflow** built on **IDA databases** and incremental reimplementation of original modules. Code and notes track progress on features such as **glow ESP**, **radar**, **no-flash**, **bunny hop**, and related **memory/signature utilities**. Aimed at learners studying cheat internals, malware-style obfuscation patterns, and practical reversing—not a maintained production cheat. (source: wiki/sources/descriptions/ALittlePatate__ezfrags.md)

Pair with other vintage FPS educational samples in the CS 1.6 lane such as [[oxware]] and [[hpp-hack]], and RE learning material such as [[intro-to-gamehacking]] and [[game-reversed-study]].

## Workflow highlights

| Component | Role |
|-----------|------|
| IDA database workflow | Decompilation-first reconstruction from legacy binary artifacts |
| Incremental modules | Feature-by-feature reimplementation (ESP, radar, movement, flash removal) |
| Memory/signature utilities | Pattern and offset helpers typical of GoldSrc-era cheat code |
| Progress notes | Documents reversing decisions and obfuscation patterns for study |

## Links

- Repo: https://github.com/ALittlePatate/ezfrags

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[oxware]] · [[hpp-hack]] · [[1-6-c2]] · [[intro-to-gamehacking]] · [[game-reversed-study]] · [[nullhooks]]
