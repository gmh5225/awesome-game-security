---
title: league-unpacker
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__League-Unpacker.md
updated: 2026-08-11
confidence: medium
---

# league-unpacker

**DLL injection** tool that **decrypts League of Legends' protected `.text` code section** and dumps the decrypted executable bytes for **static analysis** in disassemblers such as IDA Pro (gmh5225; cheat / game:lol `[Dump]`). Requires **manual base-address input** for correct disassembly. Aimed at game security researchers and reverse engineers studying LoL client code encryption under [[vanguard]]-protected Riot clients. (source: wiki/sources/descriptions/gmh5225__League-Unpacker.md)

Sits beside [[league-dumper]] and [[lol-unpackman]] in the LoL dump/unpack lane—`.text` decrypt-and-dump for static RE rather than full process-memory PE reconstruction or live offset feeds.

## Links

- Repo: https://github.com/gmh5225/League-Unpacker

## Related

[[vanguard]] · [[league-dumper]] · [[lol-unpackman]] · [[lol-offset-dumper]] · [[lol-patcher]] · [[league-base]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
