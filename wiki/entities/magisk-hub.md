---
title: Magisk Hub
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Yass5002__magisk-hub.md
  - wiki/sources/README-categories.md
updated: 2026-10-04
confidence: medium
---

# Magisk Hub

**Community-maintained static directory** that indexes and documents Android root modules for **Magisk**, **KernelSU**, and **APatch**. Built with Astro and automated Python sync scripts; pulls normalized module metadata and release assets from upstream GitHub repositories on a six-hour schedule with JSON schema validation and freshness checks. (source: wiki/sources/descriptions/Yass5002__magisk-hub.md)

The catalog organizes modules into categories such as root management, performance tuning, networking proxies, and development instrumentation—covering Frida, root hiding, and Play Integrity bypass modules used in mobile security work. Tiered Markdown and JSON records provide prerequisites, configuration notes, and direct download links for hundreds of third-party modules.

Targets rooted Android users, reverse engineers, and mobile security researchers who need a curated source for integrity bypass, root concealment, and instrumentation modules when testing app and game protection on rooted devices. (source: wiki/sources/descriptions/Yass5002__magisk-hub.md)

Listed in the README under **Cheat → Magisk** as an active-source directory and static site for Magisk/KernelSU/APatch modules with schema validation and automated release sync.

Complements curated MMRL catalogs such as [[zamr]], module managers such as [[fox-magisk-module-manager]], and WebUI hosts such as [[webui-x-portable]]; sits in the same root/integrity lane as [[jerrymanager]] and [[pif-config-generator]].

## Links

- Repo: https://github.com/Yass5002/magisk-hub

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[magisk]] · [[kernelsu]] · [[zamr]] · [[fox-magisk-module-manager]] · [[webui-x-portable]] · [[mobile-anti-cheat]]
