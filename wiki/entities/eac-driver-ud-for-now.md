---
title: eac-driver-ud-for-now
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-Driver-UD-for-now.md
updated: 2026-08-13
confidence: medium
---

# eac-driver-ud-for-now

Windows **kernel driver** sample (gmh5225) framed to stay **undetected by [[easy-anti-cheat]] driver scanning**. Cross-process **memory read/write** is exposed through a **stealth KM↔UM communication channel** that avoids EAC's known detection vectors for kernel-mode cheats—useful for studying how offensive drivers hide from EAC enumeration and how alternate I/O paths complement syscall/API hook evasion. Listed as a curated **[Sample]**; not a maintained bypass product. (source: wiki/sources/descriptions/gmh5225__EAC-Driver-UD-for-now.md)

## Links

- Repo: https://github.com/gmh5225/EAC-Driver-UD-for-now

## Related

[[easy-anti-cheat]] · [[eac-bypass-1]] · [[eac-injector-driver]] · [[read-write-driver]] · [[r69-driver]] · [[valo-driver]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
