---
title: EAC DBP
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Schnocker__EAC_dbp.md
updated: 2026-08-21
confidence: medium
---

# EAC DBP

Windows **proof-of-concept** for **debugging applications protected by Easy Anti-Cheat**. Combines a **kernel-mode driver** and **user-mode module** to interfere with selected anti-cheat **callbacks**, **minifilter behavior**, and **control paths**. Implemented in **C/C++** with Visual Studio and WDK project structure, including **user-layer API interception** logic. Primary use case is reverse engineering and controlled security testing of EAC-protected game processes. Listed under `[Debug]`. (source: wiki/sources/descriptions/Schnocker__EAC_dbp.md)

Complements callback-focused bypass samples such as [[eac-bypass]] and integrity PoCs such as [[hiearchy-eac]] by targeting EAC callback/minifilter/control surfaces to enable debugger attachment and process inspection rather than full cheat injection.

## Links

- Repo: https://github.com/Schnocker/EAC_dbp

## Related

[[easy-anti-cheat]] · [[noeye]] · [[kernel-callbacks]] · [[memfilter-fn-driver]] · [[eac-bypass]] · [[hiearchy-eac]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
