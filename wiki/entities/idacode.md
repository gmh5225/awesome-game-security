---
title: IDACode
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__idacode.md
updated: 2026-08-08
confidence: medium
---

# IDACode

Integration bridge between IDA Pro and Visual Studio Code that connects both environments so analysts can execute and debug IDAPython scripts from the editor. Still in very early development—bugs are expected. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / IDA Plugins lane. (source: wiki/sources/descriptions/gmh5225__idacode.md)

Workflow tooling rather than analysis logic: complements in-IDA script collections such as [[idawilli]], agent/CLI drivers like [[idac]], and MCP automation via [[ida-pro-mcp]]—IDACode targets IDE-side edit/run/debug of IDAPython instead of remote browsing ([[idarem]]) or multi-user sync ([[idarling]]).

## Links

- Repo: https://github.com/gmh5225/idacode

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[idawilli]] · [[idac]] · [[ida-pro-mcp]] · [[sark]] · [[idaplugins]]
