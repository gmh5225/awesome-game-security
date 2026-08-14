---
title: DSEDodge Signed Kernel Driver
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__DSEDodge-Signed-Kernel-Driver.md
updated: 2026-08-14
confidence: medium
---

# DSEDodge Signed Kernel Driver

Signed kernel driver research project designed to bypass Windows Driver Signature Enforcement (DSE). Leverages a legitimately signed driver certificate to load kernel code without triggering DSE validation failures — README entry: *Leveraging PTT to defeat DSE*. (source: wiki/sources/descriptions/gmh5225__DSEDodge-Signed-Kernel-Driver.md)

Adjacent to runtime CI/`g_CiOptions` patch PoCs such as [[dse-hook]] and [[dse-patcher-2]], validation-chain patchers such as [[disabledse]], and leaked-cert signing paths such as [[pastdse]] — here the focus is loading through a properly signed driver image rather than disabling CI globals or patching `SeValidateImageHeader`.

## Links

- Repo: https://github.com/gmh5225/DSEDodge-Signed-Kernel-Driver

## Related

[[dse-hook]] · [[dse-patcher-2]] · [[disabledse]] · [[pastdse]] · [[kvc]] · [[pdfwkrnl-mapper]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
