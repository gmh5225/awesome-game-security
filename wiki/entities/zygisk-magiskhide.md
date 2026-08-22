---
title: Zygisk-MagiskHide
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/PShocker__Zygisk-MagiskHide.md
updated: 2026-08-22
confidence: medium
---

# Zygisk-MagiskHide

**Zygisk-based Magisk module** that recreates **MagiskHide-style** root concealment after upstream Magisk removed built-in MagiskHide. Native code **conceals Magisk-related mounts** and **patches sensitive Android system properties** that root-detection checks commonly inspect. Build scripts package **multi-ABI** binaries into installable module archives for rooted devices. Targets mobile security research and anti-detection testing where apps enforce root checks. (source: wiki/sources/descriptions/PShocker__Zygisk-MagiskHide.md)

Contrasts with ptrace-based [[magiskhide]] (no Zygisk required) and Riru-era [[riru-momo-hider]]; sits in the Cheat / Magisk root-hide lane opposite detectors such as [[magiskdetector]], [[magisk-killer]], and [[detection]]. Requires [[magisk]] with **Zygisk** enabled and the [[zygisk]] specialization hook path.

## Links

- Repo: https://github.com/PShocker/Zygisk-MagiskHide

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[magisk]] · [[zygisk]] · [[magiskhide]] · [[hideroot]] · [[riru-momo-hider]] · [[magiskdetector]] · [[mobile-anti-cheat]]
