---
title: mempeek
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gamozolabs__mempeek.md
updated: 2026-08-15
confidence: medium
---

# mempeek

Linux command-line tool for live process memory inspection via `/proc/pid/mem`. Offers Cheat Engine–style value scanning with constraint filters (equal, not-equal, changed, increased, decreased, range). Uses the libprocmem crate to parse `/proc/pid/maps` for readable regions, supports multi-radix expression evaluation (hex, octal, decimal), and provides a persistent rustyline-based REPL with command history across sessions. (source: wiki/sources/descriptions/gamozolabs__mempeek.md)

## Links

- Repo: https://github.com/gamozolabs/mempeek

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[pince]] · [[procmap]] · [[mypower]] · [[libmem]]
