---
title: PESignAnalyzer
kind: entity
topics: [reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/leeqwind__PESignAnalyzer.md
updated: 2026-08-01
confidence: medium
---

# PESignAnalyzer

Simple Windows PE file signature information extractor. Reads embedded Authenticode / code-signing certificate metadata from PE files that carry one or more embedded signatures. Aimed at game-security researchers and reverse engineers studying cheat and RE tooling trust chains. (source: wiki/sources/descriptions/leeqwind__PESignAnalyzer.md)

Complements PE structure viewers such as [[totalpe2]] and offensive Authenticode transplant tooling such as [[sigthief]] / [[sigflip]]: here the focus is read-only signature metadata extraction, not signing, digest computation ([[pedigest]]), or certificate theft.

## Links

- Repo: https://github.com/leeqwind/PESignAnalyzer

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[totalpe2]] · [[sigthief]] · [[sigflip]] · [[pedigest]] · [[osslsigncode]]
