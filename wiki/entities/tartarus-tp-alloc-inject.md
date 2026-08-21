---
title: Tartarus-TpAllocInject
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/nettitude__Tartarus-TpAllocInject.md
updated: 2026-07-28
confidence: medium
---

# Tartarus-TpAllocInject

Simple Windows **TpAllocInject** loader that uses **indirect syscalls** via the Tartarus' Gate method. Aimed at game-security researchers and reverse engineers studying offensive cheat / injection:windows tradecraft—especially thread-pool allocation inject paths that avoid classic `CreateRemoteThread` / hooked ntdll call sites. (source: wiki/sources/descriptions/nettitude__Tartarus-TpAllocInject.md)

Contrasts with broader injection catalogs such as [[windows-process-injection]] (includes thread-pool / fiber / syscall samples), thread-pool injection corpora such as [[poolparty]] (worker-factory overwrite + TP_* queue variants; SafeBreach-Labs), user-mode PE manual-map injectors such as [[modexmap]], and injection-testing harnesses such as [[injectors]]. Kernel APC inject counterparts: [[injdrv]] / [[kinject]].

## Links

- Repo: https://github.com/nettitude/Tartarus-TpAllocInject

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[windows-process-injection]] · [[poolparty]] · [[modexmap]] · [[injectors]] · [[injdrv]] · [[kinject]]
