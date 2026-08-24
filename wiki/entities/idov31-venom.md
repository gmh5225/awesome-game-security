---
title: Venom (Idov31)
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Idov31__Venom.md
updated: 2026-08-24
confidence: medium
---

# Venom (Idov31)

Windows **covert network communication** library (Idov31): single-header **C++** that avoids opening an obvious socket in the caller process. Instead it spawns a **hidden detached browser process** and **reuses one of its sockets** for send and receive. Implementation relies on **Win32 and Winsock internals**, including **handle discovery and duplication**. Intended for **evasion-oriented networking research** in offensive security and stealth tooling contexts. (source: wiki/sources/descriptions/Idov31__Venom.md)

Slug disambiguated from [[venom]] (sad0p; Linux LKM rootkit hooking sample). Complements handle-theft PoCs such as [[handle-ripper]] and low-footprint external access such as [[launcher-abuser]] on the borrowed-handle / telemetry-evasion research lane.

## Links

- Repo: https://github.com/Idov31/Venom [A library that meant to perform evasive communication using stolen browser socket]

## Related

[[venom]] · [[handle-ripper]] · [[launcher-abuser]] · [[ndisapi]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
