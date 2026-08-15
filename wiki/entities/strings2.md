---
title: strings2
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/glmcdona__strings2.md
updated: 2026-08-15
confidence: medium
---

# strings2

C/C++ utility for extracting printable strings from binary files and live process memory. Aimed at game-security researchers and reverse engineers in the cheat / RE tools lane who need quick string discovery during modding and memory analysis workflows. (source: wiki/sources/descriptions/glmcdona__strings2.md)

Standalone string scanner—not an x64dbg plugin like [[stringsx64dbg]] (in-debugger SearchStringsWidget tab) or an IDA string-association helper like [[ida-function-string-associate]]. Complements static triage (PE viewers such as [[pe-bear]]) and live memory tooling (Cheat Engine, [[libmem]]) when the goal is fast ASCII/Unicode string enumeration from disk images or attached processes.

## Links

- Repo: https://github.com/glmcdona/strings2

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[stringsx64dbg]] · [[ida-function-string-associate]] · [[libmem]]
