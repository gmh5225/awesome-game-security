---
title: Apex-Legends-Offset-Dumper
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/dhanax26__Apex-Legends-Offset-Dumper.md
updated: 2026-08-16
confidence: medium
---

# Apex-Legends-Offset-Dumper

Windows **offset dumper** (dhanax26; cheat / game:apex legends `[Offset]`) that reads the running **Apex Legends** process to extract **memory offsets**, **CreateInterface** pointers, and **netvars** via **pattern scanning** and **netvar enumeration**. Outputs addresses used by cheat tooling—including **SwapChain** pointers—that can survive minor game updates without full manual layout refresh. Useful for game-security researchers studying Source-engine offset dumping and the memory-access requirements anti-cheat must enforce under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/dhanax26__Apex-Legends-Offset-Dumper.md)

Complements general Source dumpers such as [[gh-offset-dumper]], static SDK trees such as [[apex-legends-sdk]] and [[apex-legends-sdk-remaster]], and full cheat samples in the same title lane.

## Links

- Repo: https://github.com/dhanax26/Apex-Legends-Offset-Dumper

## Related

[[easy-anti-cheat]] · [[source-netvars]] · [[gh-offset-dumper]] · [[apex-legends-sdk]] · [[apex-legends-sdk-remaster]] · [[apex-full-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
