---
title: KExecDD
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__KExecDD.md
updated: 2026-08-12
confidence: medium
---

# KExecDD

Proof-of-concept that abuses the signed Microsoft **`KSecDD.sys`** (Kernel Security Support Provider Interface) driver for arbitrary kernel code execution. Injects a DLL into **LSASS**, then uses **`IOCTL_KSEC_IPC_SET_FUNCTION_RETURN`** to invoke arbitrary kernel addresses; demonstrated follow-on disables Driver Signature Enforcement (DSE) by overwriting **`ci.dll!g_CiOptions`**. (source: wiki/sources/descriptions/gmh5225__KExecDD.md)

Uses a trusted-process / signed-helper IOCTL path rather than loading a classic [[byovd]] vulnerable driver. Enhanced successor: [[kexecddplus]].

## Links

- Repo: https://github.com/gmh5225/KExecDD

## Related

[[kexecddplus]] · [[lsass-extend-mapper]] · [[kvc]] · [[dse-hook]] · [[pastdse]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
