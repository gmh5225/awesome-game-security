---
title: kurasagi
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/NeoMaster831__kurasagi.md
updated: 2026-08-22
confidence: medium
---

# kurasagi

Proof-of-concept **runtime PatchGuard bypass** targeting recent **Windows 11 24H2 through 25H2** builds. C/C++ kernel-mode components designed for load via a manual mapper such as [[kdmapper]]. Focuses on low-level [[patchguard]] research, crash-prone edge cases, and practical experimentation around **CRITICAL_STRUCTURE_CORRUPTION** behavior — intended for advanced Windows kernel security researchers in controlled lab environments. (source: wiki/sources/descriptions/NeoMaster831__kurasagi.md)

Complements build-specific PG disable PoCs such as [[tableflipper]] (up to 21H2), 2023-era internals research such as [[patchguard-2023]], and multi-method runtime tooling such as [[upgdsed]].

## Links

- Repo: https://github.com/NeoMaster831/kurasagi (README tag: Windows 11 24H2 Runtime PatchGuard Bypass)

## Related

[[patchguard]] · [[kdmapper]] · [[patchguard-2023]] · [[tableflipper]] · [[vulnerablepatchguardexploit]] · [[upgdsed]] · [[demystifying-patchguard]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
