---
title: blazedumper
kind: entity
topics: [game-hacking, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/Akandesh__blazedumper.md
updated: 2026-09-03
confidence: medium
---

# blazedumper

Maintained **Counter-Strike: Global Offensive offset database** (Akandesh; cheat `[Offset]` / game:csgo). Ships machine-readable **JSON** plus **C++** and **C#** offset definitions for direct integration into external tools and SDK scaffolds. Includes **signature patterns** and configuration data designed to refresh automatically through a companion updater pipeline—aimed at reverse engineers and tooling developers who need current memory layouts after game patches. (source: wiki/sources/descriptions/Akandesh__blazedumper.md)

Complements auto-updating CS:GO feeds such as [[hazedumper]] and [[csgo-offsets]], Akandesh's build-watch pipeline [[csgo-auto-dumper]], and runtime dumpers such as [[gh-offset-dumper]]; downstream samples such as [[csgo-cheat]] consume similar post-patch offset workflows.

## Links

- Repo: https://github.com/Akandesh/blazedumper

## Related

[[hazedumper]] · [[csgo-offsets]] · [[csgo-auto-dumper]] · [[gh-offset-dumper]] · [[csgo-sdk]] · [[csgo-cheat]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
