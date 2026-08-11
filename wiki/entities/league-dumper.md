---
title: league-dumper
kind: entity
topics: [game-hacking, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__LeagueDumper.md
updated: 2026-08-11
confidence: medium
---

# league-dumper

**Process memory dumper** adapted for **League of Legends** anti-cheat protections (gmh5225; cheat / game:lol `[Dump]`). Forked from **Process Dump** with modifications for LoL **code encryption**: hidden module discovery, loose code-chunk extraction, and import reconstruction with clean-hash filtering. Aimed at game security researchers and reverse engineers studying offensive dump techniques under [[vanguard]]-protected Riot clients. (source: wiki/sources/descriptions/gmh5225__LeagueDumper.md)

Sits beside [[lol-offset-dumper]] and [[lol-unpackman]] in the LoL dump/unpack lane—full process-memory PE reconstruction rather than live offset feeds or `.text` section decrypt-only tooling.

## Links

- Repo: https://github.com/gmh5225/LeagueDumper

## Related

[[vanguard]] · [[lol-offset-dumper]] · [[lol-unpackman]] · [[lol-patcher]] · [[league-base]] · [[ksdumper-11]] · [[nemesis]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
