---
title: FiveM Backdoor Scanner
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/rpScripts__fivem-backdoor-scanner.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: high
---

# FiveM Backdoor Scanner

**FiveM Backdoor Scanner** (rpScripts) is an offline **static analysis** tool for vetting FiveM and RedM **server resources** before deployment—Lua/JS in folders or ZIP archives, with no execution or upload of target code. (source: wiki/sources/descriptions/rpScripts__fivem-backdoor-scanner.md)

## Mechanics

- **Node.js** ES modules; **luaparse** for Lua AST inspection; **fflate** for archive unpack.
- Versioned **rule catalog** flags hidden loaders, remote code via HTTP and `load()`, obfuscation, secret reads, leaked tokens, shell execution, and risky package contents in `.lua` and `.js`.
- **Folder and archive** scans; **JSON** reporting; **CI-friendly** exit codes; small **library API** for custom integrations.

## Role

Defensive **Game Tools** / supply-chain hygiene for FiveM server owners vetting third-party scripts and resource packs—complements runtime server AC such as [[dead-anticheat]] and client-side enforcement stacks such as [[phoenix-ac]], and pre-host static audit parallels such as [[roblox-exploit-auditor]].

## Links

- Repo: https://github.com/rpScripts/fivem-backdoor-scanner (MIT)

## Related

[[dead-anticheat]] · [[phoenix-ac]] · [[aeterna-rongroi]] · [[roblox-exploit-auditor]] · [[screenshare-signatures]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
