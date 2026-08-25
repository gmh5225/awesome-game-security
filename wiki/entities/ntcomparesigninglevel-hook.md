---
title: NtCompareSigningLevel-hook
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/ExpLife0011__NtCompareSigningLevel-hook.md
updated: 2026-08-25
confidence: medium
---

# NtCompareSigningLevel-hook

**NtCompareSigningLevel-hook** (ExpLife0011) is a **kernel and user-mode proof of concept** that **swaps a function pointer inside `NtCompareSigningLevels`** to build **covert driver communication**. Implemented in **C and C++** as a paired **Windows kernel driver** and **usermode controller**. The repository explicitly marks the approach as **abandoned** because **[[patchguard]]** makes it **unstable for practical use**. Most useful as **historical anti-cheat bypass research** on signing-level hook surfaces and their limitations. Listed under cheat / driver communication with README tag `[NtCompareSigningLevels]`. (source: wiki/sources/descriptions/ExpLife0011__NtCompareSigningLevel-hook.md)

Shares the **`NtCompareSigningLevels` covert-comms README lane** with [[data-communication]] and other signing-level / data-pointer hook samples, but targets the **signing-level comparison path** directly rather than a generic `.data` pointer swap.

## Links

- Repo: https://github.com/ExpLife0011/NtCompareSigningLevel-hook

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[patchguard]] · [[data-communication]] · [[data-ptr-swap]] · [[umap-mapper]]
