---
title: wloc
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Yu9191__wloc.md
updated: 2026-08-19
confidence: medium
---

# wloc

JavaScript **non-jailbreak iOS network location spoofer** targeting Apple's **gs-loc WLOC** (WiFi/cell network location) protobuf responses. Uses **MITM** through proxy apps to patch location payloads in transit—modules for **Surge**, **Quantumult X**, **Loon**, **Stash**, and **Shadowrocket**—plus an **online location picker** and **Shortcuts** integration. Converts **GCJ-02→WGS84** for China-region coordinate alignment. Scope is **indoor/WiFi positioning only** (network-derived fixes, not GPS hardware spoof). (source: wiki/sources/descriptions/Yu9191__wloc.md)

Sits beside [[ios-location-spoofer]] in the stock-iOS **network / location** cheat lane: both rely on configured proxy MITM rather than jailbreak hooks or mock-location APIs. Contrasts with rooted Android GPS injectors such as [[locusmimic]].

**Use cases:** authorized mobile security research, location-based anti-cheat evaluation, and reverse-engineering how games derive indoor/WiFi fixes from Apple network-location services on stock iOS.

## Links

- Repo: https://github.com/Yu9191/wloc

## Related

[[ios-location-spoofer]] · [[locusmimic]] · [[ptfaketouch]] · [[trustdevice-ios]] · [[move-certificate]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
