---
title: EntropyReducer
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__EntropyReducer.md
updated: 2026-08-13
confidence: medium
---

# EntropyReducer

Tool that **lowers PE binary Shannon entropy** to evade **heuristic detection** by AV and anti-cheat scanners. High entropy flags packed or encrypted executables in static scanners. Manipulates **section padding** and **data distribution** to reduce byte-level entropy scores while preserving the executable. Aimed at red-team operators and security researchers studying entropy heuristics—not an AC product. (source: wiki/sources/descriptions/gmh5225__EntropyReducer.md)

Complements shellcode/payload entropy reduction via [[shellcode-entropyfix]], PE packing tutorials such as [[packer-tutorial]], and curated packing resources in [[awesome-executable-packing]].

## Links

- Repo: https://github.com/gmh5225/EntropyReducer

## Related

[[shellcode-entropyfix]] · [[2pack]] · [[packer-tutorial]] · [[awesome-executable-packing]] · [[pepacker]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
