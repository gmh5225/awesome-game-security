---
title: PoolParty
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/SafeBreach-Labs__PoolParty.md
updated: 2026-08-21
confidence: medium
---

# PoolParty

Collection of **Windows process injection** techniques that abuse **thread pool internals** to execute code in remote processes. Written in C++; implements multiple variants including worker-factory start-routine overwrite and insertion of **TP_WORK**, **TP_WAIT**, **TP_IO**, **TP_ALPC**, **TP_JOB**, **TP_DIRECT**, and **TP_TIMER** items. Includes native API wrappers, handle hijacking helpers, and structured implementations for each thread-pool primitive. Designed for red-team research and for testing anti-cheat or EDR visibility against low-detection injection tradecraft. (source: wiki/sources/descriptions/SafeBreach-Labs__PoolParty.md)

Contrasts with broader injection catalogs such as [[windows-process-injection]] (thread-pool / fiber / syscall samples), focused TpAllocInject loaders such as [[tartarus-tp-alloc-inject]] (Tartarus' Gate indirect syscalls), and injection-testing harnesses such as [[injectors]].

## Links

- Repo: https://github.com/SafeBreach-Labs/PoolParty

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[tartarus-tp-alloc-inject]] · [[injectors]] · [[the-perfect-injector]]
