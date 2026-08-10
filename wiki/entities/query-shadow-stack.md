---
title: QueryShadowStack
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__QueryShadowStack.md
updated: 2026-08-10
confidence: medium
---

# QueryShadowStack

Windows proof-of-concept for querying and interacting with Intel CET (Control-flow Enforcement Technology) shadow-stack data. Demonstrates reading shadow-stack contents, detecting shadow-stack mismatches, and exploring how CET's shadow-stack mechanism affects return-address integrity checking. Aimed at kernel security researchers studying CET shadow-stack internals and their impact on exploitation techniques under the README `Windows Security Features` / Shadow Stack lane. (source: wiki/sources/descriptions/gmh5225__QueryShadowStack.md)

Complements broader CET material such as [[cet-research]] and KM shadow-stack analysis such as [[windows-kernel-shadow-stack]] when modeling hardware-enforced return-address integrity alongside VBS/[[hvci]] baselines.

## Links

- Repo: https://github.com/gmh5225/QueryShadowStack (README tag: Shadow Stack)

## Related

[[cet-research]] · [[windows-kernel-shadow-stack]] · [[patchguard]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
