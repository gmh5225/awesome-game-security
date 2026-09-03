---
title: PatchGuardBypass
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/AdamOron__PatchGuardBypass.md
updated: 2026-09-03
confidence: low
---

# PatchGuardBypass

In-progress **Windows [[patchguard]] bypass** research (AdamOron) documenting a planned **dynamic approach** on modern builds. Three stated goals: disable PatchGuard execution, evade runtime integrity checks, and verify PatchGuard state. C/C++ kernel-mode experimentation centered on low-level Windows internals — aimed at kernel security researchers and anti-cheat analysts studying defensive mechanisms and their attack surface. (source: wiki/sources/descriptions/AdamOron__PatchGuardBypass.md)

Complements educational material such as [[demystifying-patchguard]], build-specific runtime PoCs such as [[kurasagi]], and internals research such as [[patchguard-2023]].

## Links

- Repo: https://github.com/AdamOron/PatchGuardBypass

## Related

[[patchguard]] · [[demystifying-patchguard]] · [[kurasagi]] · [[patchguard-2023]] · [[vulnerablepatchguardexploit]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
