---
title: valorant-esp-hack-with-driver
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__valorant-esp-hack-with-driver.md
updated: 2026-08-07
confidence: medium
---

# valorant-esp-hack-with-driver

Valorant **ESP** sample that exploits a vulnerability in the [[vanguard]] kernel driver to load a companion driver **before** Vanguard initializes — a boot-order / early-load race against Riot's boot-start AC. Build and inject with any kernel injector; the bundled driver component is aimed at experienced researchers rather than copy-paste users. Useful for game security researchers and reverse engineers studying offensive techniques in the cheat / game:valorant lane. (source: wiki/sources/descriptions/gmh5225__valorant-esp-hack-with-driver.md)

Sits beside EFI pre-OS map research such as [[xigmapper]] and other Vanguard early-load bypass samples, but scoped to a Vanguard-driver vulnerability plus kernel-injector workflow rather than dump/SDK or in-process internal bases alone.

## Links

- Repo: https://github.com/gmh5225/valorant-esp-hack-with-driver

## Related

[[vanguard]] · [[xigmapper]] · [[valorant-externals]] · [[valorant-internal]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
