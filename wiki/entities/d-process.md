---
title: d-process
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gigbh__d-process.md
updated: 2026-08-15
confidence: medium
---

# d-process

Lightweight **Linux decoy process generator** that spawns fake background processes with a user-chosen executable name. A shell wrapper compiles a minimal C program on demand and launches it under `nohup`, so the decoy appears in `/proc` and process-listing tools with the requested name. A single command spawns decoys; a `killall` subcommand terminates all running fakes. Written in C and shell script for game-security research, anti-cheat testing, and studying or evading process-enumeration and tracker presence checks. (source: wiki/sources/descriptions/gigbh__d-process.md)

Offensive process-list manipulation on Linux — not a Windows PEB/process-hiding rootkit like [[blanket]] or a full injection framework like [[mandibule]]. Complements defensive suspicious-process scanners in educational AC PoCs such as [[anticheat-poc]] and [[basic-anti-cheat]].

## Links

- Repo: https://github.com/gigbh/d-process

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[anticheat-poc]] · [[basic-anti-cheat]] · [[mandibule]] · [[procmap]]
