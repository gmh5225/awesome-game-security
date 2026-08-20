---
title: Kernel-Thread-Driver
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Spuckwaffel__Kernel-Thread-Driver.md
updated: 2026-08-20
confidence: medium
---

# Kernel-Thread-Driver

**Windows kernel-thread driver** (Spuckwaffel) paired with a **user-mode controller** for cross-process memory operations. Uses a **status-code communication model** between kernel and user mode to initialize, track connection state, and process commands. Practical tasks include target process setup, memory reading, and module base retrieval. Intended for **anti-cheat bypass research** and **kernel–user architecture experiments** in protected games. Listed under cheat / Thread. (source: wiki/sources/descriptions/Spuckwaffel__Kernel-Thread-Driver.md)

Sits in the **kernel-thread + KM↔UM comms** lane beside other Spuckwaffel kernel samples such as [[simple-mmcopymemory-hook]], cross-process R/W libraries such as [[ntmemory]], and thread-evasion PoCs such as [[zero-thread-kernel]] and [[driver-hide-kernel-thread-iocancelirp]].

## Links

- Repo: https://github.com/Spuckwaffel/Kernel-Thread-Driver

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[simple-mmcopymemory-hook]] · [[ntmemory]] · [[zero-thread-kernel]] · [[driver-hide-kernel-thread-iocancelirp]] · [[uedumper]]
