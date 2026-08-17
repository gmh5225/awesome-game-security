---
title: Riru-MomoHider
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/canyie__Riru-MomoHider.md
updated: 2026-08-17
confidence: medium
---

# Riru-MomoHider

**Riru module** for hiding **Magisk root** from app-level detection. Hooks **system calls** and **Java APIs** used by root-detection libraries (e.g. [[magiskdetector]], RootBeer) to conceal Magisk presence: spoofing mount points, hiding Magisk files, and blocking property queries that reveal root status. C/Java module operates through **Riru's Zygote injection** mechanism. Aimed at Android users and security researchers studying root-detection bypass techniques. (source: wiki/sources/descriptions/canyie__Riru-MomoHider.md)

Sits in the Cheat / Magisk root-hide lane beside [[hideroot]], [[magiskhide]], and DenyList/Shamiko on [[magisk]]; distinct from Zygisk-era modules such as [[florida-zygisk]] but targets the same detector surface as [[detection]] and [[mobile-anti-cheat]] probes.

## Links

- Repo: https://github.com/canyie/Riru-MomoHider

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[magisk]] · [[magiskdetector]] · [[hideroot]] · [[magiskhide]] · [[mobile-anti-cheat]] · [[canyie-pine]]
