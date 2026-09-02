---
title: COPG
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/AlirezaParsi__COPG.md
updated: 2026-09-02
confidence: medium
---

# COPG

**Zygisk module** for rooted Android devices that **spoofs per-app device profiles** — CPU, GPU, build properties, and other hardware or identity signals — so games and apps believe they run on flagship hardware. Built mainly in **C++** with a **JavaScript WebUI** and Magisk-style module scripts. (source: wiki/sources/descriptions/AlirezaParsi__COPG.md)

**Spoofing surface:** build props, serial numbers, IMEI, Widevine DRM level, SIM carrier, advertising IDs, and privacy hides such as VPN and mock-location masking. The on-device WebUI manages device libraries, per-app spoof lists, backups, and comfort tweaks without rebooting.

**Stealth modes:** many spoofing paths use **copy-on-write** or **unload-before-launch** techniques meant to leave no module footprint in process memory. Optional **resident hooks** for GPU, DRM, and similar features carry explicit anti-cheat risk warnings.

Aimed at mobile gamers and security researchers who want to bypass **hardware-gated FPS and graphics tiers**, or study how Android games fingerprint devices and distinguish stealth from detectable hooking.

## Links

- Repo: https://github.com/AlirezaParsi/COPG

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[mobile-anti-cheat]] · [[zygisk]] · [[magisk]] · [[android-faker]] · [[hidemyandroid]] · [[nexus]] · [[spoofing-collection]]
