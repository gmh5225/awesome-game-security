---
title: tableflipper
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/emlinhax__tableflipper.md
updated: 2026-08-15
confidence: medium
---

# tableflipper

C++ research project that **partially disables [[patchguard]]** (KPP) on Windows builds up to **Windows 11 21H2**. Primarily useful for game security researchers and reverse engineers studying offensive kernel tamper techniques in the cheat / PatchGuard-related README lane—not as a general-purpose AC bypass. (source: wiki/sources/descriptions/emlinhax__tableflipper.md)

Sits alongside runtime PG disable PoCs such as [[upgdsed]] and [[vulnerablepatchguardexploit]], version-specific context-page work such as [[pg1903]], and PG monitoring tooling such as [[sushi]].

## Links

- Repo: https://github.com/emlinhax/tableflipper (README tag: partially disable patchguard up to win11 21H2)

## Related

[[patchguard]] · [[upgdsed]] · [[vulnerablepatchguardexploit]] · [[pg1903]] · [[sushi]] · [[demystifying-patchguard]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
