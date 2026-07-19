---
title: Return-address-spoofer
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/veryboreddd__Return-address-spoofer.md
updated: 2026-07-19
confidence: medium
---

# Return-address-spoofer

C/C++ educational sample that **illustrates return-address spoofing**: replacing the return address on the stack before an API or game call so stack-walk / call-origin checks see a legitimate module frame. Centers on memory analysis in the cheat / spoof-stack lane; useful for researchers studying how stack spoofing works and how `Detection:Spoof Stack` counters look at unwind consistency. (source: wiki/sources/descriptions/veryboreddd__Return-address-spoofer.md)

## Links

- Repo: https://github.com/veryboreddd/Return-address-spoofer

## Related

[[skiphook]] · [[cet-research]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
