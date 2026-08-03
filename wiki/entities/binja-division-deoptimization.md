---
title: binja-division-deoptimization
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/jmprdi__binja-division-deoptimization.md
updated: 2026-08-03
confidence: medium
---

# binja-division-deoptimization

Binary Ninja plugin that deoptimizes compiler strength-reduction of division and modulo operations back into readable `/` and `%` forms. Works at MLIL, so it is architecture-agnostic. Useful for game-security researchers and reverse engineers studying offensive techniques in the Cheat Binary Ninja Plugins lane. (source: wiki/sources/descriptions/jmprdi__binja-division-deoptimization.md)

Not a standalone disassembler—scoped to MLIL division/modulo recovery inside Binary Ninja.

## Links

- Repo: https://github.com/jmprdi/binja-division-deoptimization

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binja-kc]] · [[x64dbgbinja]] · [[obfuscation-analysis]]
