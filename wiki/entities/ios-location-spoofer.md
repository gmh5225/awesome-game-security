---
title: iOS Location Spoofer
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/mekos2772__ios-location-spoofer.md
updated: 2026-07-30
confidence: medium
---

# iOS Location Spoofer

JavaScript **network-level iOS location spoofer** that works **without jailbreak**. Intercepts and rewrites Apple map-lookup responses in transit (MITM), patching **WiFi BSSID** and **cell-tower coordinates** so Core Location receives forged network-derived fixes. Ships proxy modules for **Surge**, **Shadowrocket**, **Loon**, **Stash**, and **Quantumult X (QX)**, plus **motion-state spoofing** and a **location-picker web UI**. (source: wiki/sources/descriptions/mekos2772__ios-location-spoofer.md)

Contrasts with rooted Android GPS injectors such as [[locusmimic]]: this lane stays in the **iOS network / location** cheat surface and relies on a configured proxy rather than in-process hooks or mock-location APIs.

**Use cases:** authorized mobile security research, location-based anti-cheat evaluation, and reverse-engineering how games derive location from network signals on stock iOS.

## Links

- Repo: https://github.com/mekos2772/ios-location-spoofer

## Related

[[wloc]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[locusmimic]] · [[trustdevice-ios]] · [[move-certificate]]
