---
title: modmap
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/btbd__modmap.md
updated: 2026-08-17
confidence: medium
---

# modmap

**modmap** (btbd/modmap; Extend Manual Map) is a **kernel-assisted DLL manual mapper** that extends an existing loaded module rather than allocating a standalone anonymous region. A companion kernel driver allocates memory immediately after the target module’s end via **`MiAllocateVad`**, expands the module’s **LDR entry** `SizeOfImage` to cover the new range, and maps the payload DLL into that extended region so it appears as part of the legitimate module in process module enumeration. Aimed at game-security researchers studying advanced manual-mapping techniques that evade module-list–based detection. (source: wiki/sources/descriptions/btbd__modmap.md)

Contrasts with conventional user-mode manual mappers such as [[modexmap]] (standalone `VirtualAllocEx` regions) and with BTBD kernel **driver** mappers such as [[umap]] and [[smap]] — here the stealth surface is **host-module extension** plus VAD/LDR blending, not unsigned kernel driver load.

## Links

- Repo: https://github.com/btbd/modmap

## Related

[[modexmap]] · [[kernel-vad-injector]] · [[umap]] · [[smap]] · [[wpp]] · [[hidden-module-detector]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
