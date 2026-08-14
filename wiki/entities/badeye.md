---
title: BadEye
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__BadEye.md
updated: 2026-08-14
confidence: medium
---

# BadEye

C++ **memory-analysis** research sample (gmh5225) studying [[battleye]] handle validation. It works because of two BE assumptions: BattlEye trusts that an opened process handle already carries the access rights BE needs, and BE uses that handle mainly to resolve **EPROCESS** before calling **`MmCopyVirtualMemory`** for cross-process scanning—not to re-validate handle rights on every read path. Useful for game-security researchers and reverse engineers studying offensive handle/memory paths in the cheat / explore anticheat system:be lane. (source: wiki/sources/descriptions/gmh5225__BadEye.md)

Complements handle-stripping race research such as [[battleye-handler-bypass]] and usermode elevation libs such as [[libelevate]] by focusing on what BE does *after* a handle survives object-callback stripping.

## Links

- Repo: https://github.com/gmh5225/BadEye

## Related

[[battleye]] · [[battleye-handler-bypass]] · [[libelevate]] · [[goodeye]] · [[cheat-driver]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
