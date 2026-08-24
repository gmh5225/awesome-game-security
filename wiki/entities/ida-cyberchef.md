---
title: ida-cyberchef
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/HexRaysSA__ida-cyberchef.md
updated: 2026-08-24
confidence: medium
---

# ida-cyberchef

Official Hex-Rays IDA Pro plugin that embeds a CyberChef-style data transformation interface inside the disassembler. Implemented mainly in Python with a Qt-based UI and standard IDA plugin metadata, it supports decode/encode pipelines and chained transformations without leaving the RE session—aimed at malware analysis and binary triage when analysts need rapid in-IDA data manipulation. (source: wiki/sources/descriptions/HexRaysSA__ida-cyberchef.md)

Complements other in-IDA encoding and string helpers such as [[big5-decode-ida]] (locale-specific decode), [[hrtng]] (string/data decrypt in Hex-Rays microcode), [[ida-jm-xorstr-decrypt-plugin]], and [[ida-gameguard-str-dec]].

## Links

- Repo: https://github.com/HexRaysSA/ida-cyberchef

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[big5-decode-ida]] · [[hrtng]] · [[yara4ida]] · [[idaplugins]] · [[ida-plugins]]
