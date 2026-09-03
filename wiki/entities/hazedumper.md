---
title: hazedumper
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/frk1__hazedumper.md
updated: 2026-08-15
confidence: medium
---

# hazedumper

Auto-updating **CS:GO offset and netvar** repository (frk1) tagged `[Offset]` in the curated list. Publishes memory **signatures** and resolved offsets for `engine.dll` and `client.dll` in JSON, TOML, YAML, C++ headers, C#, and VB. A companion `config.json` defines byte-pattern signatures with relative/absolute addressing for globals such as `dwClientState`, `dwEntityList`, and `dwLocalPlayer`, plus netvar fields (`m_iHealth`, `m_vecOrigin`, etc.), so external memory-reading cheats can track game patches without hand-updating every layout. (source: wiki/sources/descriptions/frk1__hazedumper.md)

Complements runtime dumpers such as [[gh-offset-dumper]], maintained CS:GO offset feeds such as [[csgo-offsets]] and [[blazedumper]], and the [[source-netvars]] parsing workflow.

## Links

- Repo: https://github.com/frk1/hazedumper

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-netvars]] · [[csgo-offsets]] · [[blazedumper]] · [[offsets]] · [[gh-offset-dumper]] · [[csgo-sdk]] · [[sdk]]
