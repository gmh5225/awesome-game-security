---
title: PresentInjector
kind: entity
topics: [game-hacking, windows-kernel, graphics-api]
sources:
  - wiki/sources/descriptions/Nou4r__PresentInjector.md
updated: 2026-08-22
confidence: medium
---

# PresentInjector

Windows **kernel-assisted DLL injection** project from **Nou4r** that loads mapped payloads into protected game processes by **swapping graphics Present pointers**. Combines user-mode and kernel-mode components with **PFN-related memory handling**, pointer-chain techniques, and post-injection cleanup. C/C++ codebase tagged **PTE.User** in the README; primary use case is advanced cheat injection research and anti-cheat bypass experimentation. (source: wiki/sources/descriptions/Nou4r__PresentInjector.md)

Repurposes the [[present-hook]] swap-chain path as an injection primitive rather than an overlay draw surface. Sits in the PTE.User page-table injection lane beside [[executor]], [[fumo-loader]], and [[page-table-injector]], and beside Nou4r kernel externals such as [[pkernelinterface-eft]].

## Links

- Repo: https://github.com/Nou4r/PresentInjector (README tag: PTE.User)

## Related

[[present-hook]] · [[executor]] · [[fumo-loader]] · [[page-table-injector]] · [[pkernelinterface-eft]] · [[windows-kernel-pagehook]] · [[injection]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]]
