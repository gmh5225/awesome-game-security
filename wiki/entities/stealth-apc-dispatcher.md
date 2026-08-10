---
title: stealth-apc-dispatcher
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__StealthAPCDispatcher.md
updated: 2026-08-10
confidence: medium
---

# stealth-apc-dispatcher

Windows kernel tool (gmh5225) demonstrating **stealthy APC (Asynchronous Procedure Call) dispatch**: queues APCs to target threads via paths that avoid standard API-level detection, enabling code execution in arbitrary thread contexts with **encrypted shellcode** while evading anti-cheat APC monitoring heuristics. Aimed at kernel researchers studying APC-based code execution and AC APC-detection bypass—not a production injector. (source: wiki/sources/descriptions/gmh5225__StealthAPCDispatcher.md)

Contrasts with conventional kernel APC injectors such as [[injdrv]] / [[kinject]] (process-notify + standard APC queue APIs) and APC internals study samples such as [[apc-research]]. Defensive RE of AC APC instrumentation includes [[goodeye]] ([[battleye]] BEDaisy per-thread APC callbacks).

## Links

- Repo: https://github.com/gmh5225/StealthAPCDispatcher

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[apc-research]] · [[injdrv]] · [[kinject]] · [[goodeye]] · [[thread-namecalling]] · [[kernel-callbacks]]
