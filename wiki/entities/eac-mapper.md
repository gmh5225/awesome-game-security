---
title: eac-mapper
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Compiled-Code__eac-mapper.md
updated: 2026-08-26
confidence: medium
---

# eac-mapper

**eac-mapper** (Compiled-Code/eac-mapper) is a Windows **kernel mapping proof of concept** in C++ that targets a **session-driver integrity blind spot** in [[easy-anti-cheat]]. It documents how **read-only section checks** can be bypassed when drivers are **not globally mapped** in the anti-cheat execution context, and demonstrates **patching** plus **hook placement** strategies for low-noise user-kernel communication in that scenario. Primary use case: [[easy-anti-cheat]] internals research and defensive understanding of mapper-style attack paths. README category: cheat / `[gdrv.sys]`. (source: wiki/sources/descriptions/Compiled-Code__eac-mapper.md)

Sits in the **EAC-specific session-driver mapper** lane beside generic session-space mappers such as [[driver-session-mapper]] and [[callmewin32kdriver]], but focuses on exploiting EAC's non-global driver mapping context rather than generic win32k session load paths alone.

## Links

- Repo: https://github.com/Compiled-Code/eac-mapper

## Related

[[easy-anti-cheat]] · [[gdrv-loader]] · [[cve-2018-19320]] · [[kdmapper]] · [[known-driver-mappers]] · [[driver-session-mapper]] · [[callmewin32kdriver]] · [[bypassing-easyanticheat-integrity-check]] · [[map-page]] · [[mm-copy-memory]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
