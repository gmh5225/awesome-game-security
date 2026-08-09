---
title: augur-riot
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__augur-riot.md
updated: 2026-08-09
confidence: medium
---

# augur-riot

**Riot Vanguard streamed-module to PE converter** (gmh5225). Converts Vanguard driver modules shipped in **RITO** format into valid PE/DLL images: resolves hashed imports, reconstructs sections, and writes analyzable binaries for static RE of Vanguard kernel protection and detection logic. (source: wiki/sources/descriptions/gmh5225__augur-riot.md)

The upstream description also frames broader Vanguard kernel-driver research (driver activity monitoring, callback enumeration, kernel-operation logging); the README entry centers on the RITO→PE reconstruction pipeline. (source: wiki/sources/descriptions/gmh5225__augur-riot.md)

Sits beside [[vgk-illegal-pf-logger]] and [[val-exception-handler]] in the Vanguard kernel RE lane, but as **offline module reconstruction** from streamed RITO payloads rather than runtime telemetry or exception PoCs. Complements [[lol-unpackman]] for Riot title client unpacking under [[vanguard]].

## Links

- Repo: https://github.com/gmh5225/augur-riot

## Related

[[vanguard]] · [[vgk-illegal-pf-logger]] · [[val-exception-handler]] · [[lol-unpackman]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
