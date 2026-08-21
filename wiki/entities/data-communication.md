---
title: DataCommunication
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Sinclairq__DataCommunication.md
updated: 2026-08-21
confidence: medium
---

# DataCommunication

**DataCommunication** (Sinclairq) is a proof-of-concept **Windows kernel-to-usermode communication** mechanism built around **swapping a kernel `.data` pointer**. The C++ project ships separate **kernel driver** and **usermode** components, with **pattern scanning** plus helper routines for **memory operations** and **process base lookup**. The design targets **high-speed message and read-write style communication** but carries **stability risks on protected systems**. Intended for **kernel research** and **anti-cheat related experimentation**, not production deployment. Listed under cheat / driver communication with README tag `[NtCompareSigningLevels]`. (source: wiki/sources/descriptions/Sinclairq__DataCommunication.md)

Sits in the **`.data`-pointer covert KM↔UM comms** lane beside [[afd-irp-call-dispatch]], [[data-ptr-swap]], [[comm-data-pointer-swap]], and [[wpp]], and near status-code driver samples such as [[kernel-thread-driver]] and cross-process R/W libraries such as [[ntmemory]].

## Links

- Repo: https://github.com/Sinclairq/DataCommunication

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[afd-irp-call-dispatch]] · [[data-ptr-swap]] · [[kernel-thread-driver]] · [[ntmemory]] · [[access]] · [[hiearchy-eac]]
