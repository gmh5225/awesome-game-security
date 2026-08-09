---
title: cheat-attack-thread-slemu
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__cheat-attack-thread-slemu.md
updated: 2026-08-09
confidence: medium
---

# cheat-attack-thread-slemu

Thread-based cheat execution PoC that uses **sleep emulation** or **thread state / scheduling manipulation** to evade anti-cheat thread scanning. It alters thread context or scheduling state so cheat worker threads are harder to spot during system-thread enumeration that flags suspicious start addresses or anomalous thread state. (source: wiki/sources/descriptions/gmh5225__cheat-attack-thread-slemu.md)

README tag: **Heartbeat Testing** — useful for studying heartbeat / thread-presence checks and stealthy thread execution alongside kernel threadless PoCs such as [[zero-thread-kernel]] and defensive enumerators such as [[system-thread-finder]].

## Links

- Repo: https://github.com/gmh5225/cheat-attack-thread-slemu

## Related

[[zero-thread-kernel]] · [[system-thread-finder]] · [[dll-thread-injection-detector]] · [[thread-stack-spoofer]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
