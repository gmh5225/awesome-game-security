---
title: HumptyLock
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/wh1te4ever__HumptyLock.md
updated: 2026-08-13
confidence: medium
---

# HumptyLock

iOS **XNU kernel read/write** exploit for **iOS 14.0–14.4.2**, delivered as an **Xcode app** that triggers the chain from its main view controller. Core logic is C with an Objective-C wrapper: dangling **lockf** structures, **Mach out-of-line port** spraying, **NECP socket kalloc** heap grooming, and **pipe-based memory corruption** yield stable kernel read/write primitives. Extends **Coruna Pendulum PE** with offset handling, **PAC pointer unsigning**, and **kernel-base discovery** for full kernel memory access. Tested on iPhone 6s through 11 Pro. (source: wiki/sources/descriptions/wh1te4ever__HumptyLock.md)

Lab-oriented iOS kernel exploitation for jailbreak development and mobile platform RE—pairs with [[coruna]] / Pendulum PE study, same-author [[xnu-1day-practice]], and post-KRW tooling such as [[kfd-explorer]].

## Links

- Repo: https://github.com/wh1te4ever/humptylock

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[coruna]] · [[xnu-1day-practice]] · [[kfd-explorer]] · [[darksword-kexploit-fun]] · [[oob-entry]]
