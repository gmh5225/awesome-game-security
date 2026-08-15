---
title: kfd
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/felix-pb__kfd.md
updated: 2026-08-15
confidence: medium
---

# kfd

Kernel-level file-descriptor exploit framework for iOS/macOS that chains XNU kernel vulnerabilities into stable arbitrary kernel read/write. Targets iOS 15 and 16 on version-specific builds; C implementation aimed at jailbreak developers and iOS security researchers studying XNU kernel exploitation, sandbox escape, and post-exploit tooling. (source: wiki/sources/descriptions/felix-pb__kfd.md)

Upstream KRW primitive for post-exploit tools such as [[kfd-explorer]] and contemporary jailbreak/kernel-R/W study trees [[dopamine]], [[dirty-zero]], and [[xnu-1day-practice]]—distinct from userland injectors ([[opainject]]) and checkm8-era hook frameworks ([[xnuspy]]).

## Links

- Repo: https://github.com/felix-pb/kfd

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[kfd-explorer]] · [[xnu-1day-practice]] · [[dopamine]] · [[dirty-zero]] · [[humptylock]] · [[xnuspy]]
