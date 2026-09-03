---
title: csgo-auto-dumper
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Akandesh__csgo_auto_dumper.md
updated: 2026-09-03
confidence: medium
---

# csgo-auto-dumper

**Windows C++ automation utility** that tracks **Counter-Strike: Global Offensive** updates and triggers offset dumping (Akandesh; cheat `[Auto Dump]` / game:csgo). Uses **steamcmd** commands, **build ID** parsing, and a **timed polling loop** to detect new game builds; when an update is found it launches a local dumper executable and follow-up scripts to refresh generated offset data. Primarily intended for maintaining up-to-date reverse-engineering artifacts with minimal manual work. (source: wiki/sources/descriptions/Akandesh__csgo_auto_dumper.md)

Complements maintained CS:GO offset feeds such as [[hazedumper]] and [[csgo-offsets]], runtime dumpers such as [[gh-offset-dumper]], and Akandesh's Facepunch Rust pipeline [[rust-auto-dumper]]; downstream CS:GO SDK and cheat samples such as [[csgo-sdk]] and [[csgo-cheat]] consume similar post-patch offset workflows.

## Links

- Repo: https://github.com/Akandesh/csgo_auto_dumper

## Related

[[hazedumper]] · [[csgo-offsets]] · [[gh-offset-dumper]] · [[rust-auto-dumper]] · [[csgo-sdk]] · [[csgo-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
