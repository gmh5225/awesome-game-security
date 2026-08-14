---
title: CET-win10
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__CET-win10.md
updated: 2026-08-14
confidence: medium
---

# CET-win10

Research project exploring Intel Control-flow Enforcement Technology (CET) support on Windows 10. Investigates shadow-stack and indirect branch tracking (IBT) mechanisms as implemented by the Windows kernel for forward-edge and backward-edge control-flow integrity (CFI) protection. Aimed at kernel security researchers studying how Windows 10 enables hardware-enforced CFI under the README `Windows Security Features` / CET lane. (source: wiki/sources/descriptions/gmh5225__CET-win10.md)

Complements broader CET material such as [[cet-research]], KM shadow-stack analysis such as [[windows-kernel-shadow-stack]], and shadow-stack query PoCs such as [[query-shadow-stack]] when modeling how CET raises the cost of ROP-style control-flow abuse alongside VBS/[[hvci]] baselines.

## Links

- Repo: https://github.com/gmh5225/CET-win10 (README tag: CET)

## Related

[[cet-research]] · [[windows-kernel-shadow-stack]] · [[query-shadow-stack]] · [[patchguard]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
