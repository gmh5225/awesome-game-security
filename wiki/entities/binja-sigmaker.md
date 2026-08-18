---
title: binja-sigmaker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/apekros__binja_sigmaker.md
updated: 2026-08-18
confidence: medium
---

# binja-sigmaker

Binary Ninja plugin that generates byte-pattern signatures from disassembled functions. Python implementation packaged for Binary Ninja plugin manager compatibility. Emits IDA-style wildcard signatures suitable for runtime pattern scanning and can fall back to function-start signatures when needed. (source: wiki/sources/descriptions/apekros__binja_sigmaker.md)

Typical uses include reverse engineering, cheat or anti-cheat signature authoring, and binary update diffing—finding stable function anchors across patched game clients or security modules.

Unlike [[bndb2pat]], which exports IDA FLIRT `.pat` libraries for stripped-binary function identification, binja-sigmaker targets runtime scan patterns in the same lane as [[ida-sigmaker]], [[sigmakerex]], and [[ida-pro-sigmaker]].

## Links

- Repo: https://github.com/apekros/binja_sigmaker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-sigmaker]] · [[sigmakerex]] · [[ida-pro-sigmaker]] · [[bndb2pat]] · [[hyara]] · [[patternsleuth]] · [[x64dbgbinja]]
