---
title: sguard_limit
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/H3d9__sguard_limit.md
updated: 2026-08-25
confidence: medium
---

# sguard_limit

Windows toolkit to **restrict or patch behaviors** in an **ACE-Guard** protected game client (H3d9). Combines a **user-mode C++ controller** with a **kernel-mode module** (C and assembly) for memory patching and process manipulation. Includes virtual memory operations, **VAD traversal**, suspend/resume control, and **detour-based hooks** in a Visual Studio solution. Aimed at anti-cheat reverse engineering and bypass experimentation—not general application development. (source: wiki/sources/descriptions/H3d9__sguard_limit.md)

Complements Tencent ACE documentation such as [[starrail-ace-b]] and offensive samples such as [[hi3-ace-b]]. Sits beside kernel VAD/process-manipulation research such as [[kernel-vad-injector]] and [[wkpe]], and driver analysis tooling such as [[kace]].

## Links

- Repo: https://github.com/H3d9/sguard_limit

## Related

[[starrail-ace-b]] · [[hi3-ace-b]] · [[anti-cheat-amateur]] · [[kernel-vad-injector]] · [[wkpe]] · [[kace]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
