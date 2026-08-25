---
title: BD-UN-JB
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Gezine__BD-UN-JB.md
updated: 2026-08-25
confidence: medium
---

# BD-UN-JB

**Blu-ray Disc Java (BD-J)** jailbreak exploit chain for **PlayStation** consoles: BD-J xlet payloads combined with `jdk.internal.misc.Unsafe` to achieve code execution, plus a C-based **`bdj_unpatch`** tool for **BDMV** manipulation and a Python log client for debugging. (source: wiki/sources/descriptions/Gezine__BD-UN-JB.md)

README positions it as **BD-JB RemoteJarLoader** for already-jailbroken **PS5 (≤12.00)**: unpatch BD-J restrictions, build/manipulate ISO images, and load JAR payloads over the network with logging support. Primary audience: console security researchers studying PlayStation exploit chains and **BD-J sandbox escape** techniques.

## Links

- Repo: https://github.com/Gezine/BD-UN-JB

## Related

[[cssfontface-exploit]] · [[ps5-linux-loader]] · [[nines]] · [[a53-code-exec]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
