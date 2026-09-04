---
title: Shark
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/9176324__Shark.md
updated: 2026-09-04
confidence: medium
---

# Shark

Windows **kernel research toolkit** (9176324) focused on **runtime [[patchguard]] disable**. Implemented in C, C++, and assembly for **x86 and x64**, with Visual Studio and NMAKE build scripts. Includes **driver and loader** components and references **virtualization-assisted loading** methods. Primary audience: low-level security researchers studying kernel defenses and PatchGuard bypass mechanics. (source: wiki/sources/descriptions/9176324__Shark.md)

Sits in the cheat / PatchGuard-related lane alongside runtime bypass PoCs such as [[kurasagi]] and [[tableflipper]], educational material such as [[demystifying-patchguard]], and manual-map loaders such as [[kdmapper]] when virtualization-assisted load paths matter.

## Links

- Repo: https://github.com/9176324/Shark

## Related

[[patchguard]] · [[demystifying-patchguard]] · [[kurasagi]] · [[tableflipper]] · [[patchguard-2023]] · [[kdmapper]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
