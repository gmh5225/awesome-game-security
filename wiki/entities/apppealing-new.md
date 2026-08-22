---
title: AppPealing-new
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/NPC2000__AppPealing-new.md
updated: 2026-08-22
confidence: medium
---

# AppPealing-new

**Android Xposed module** that disables protections from **Inka AppSealing** — a commercial anti-cheat and anti-root packer common on mobile games. Targets root and cheat-detection bypasses and can **dump decrypted DEX** for inspection and debugging. Combines **Java** Xposed/LSPosed integration with **C++ native hooking** via [[dobby]] in a **Magisk + LSPosed** workflow. Aimed at mobile app and game security testing, reverse engineering, and anti-tamper analysis. (source: wiki/sources/descriptions/NPC2000__AppPealing-new.md)

Sits in the offensive lane against commercial packers documented under [[mobile-anti-cheat]] (AppSealing alongside DexGuard and pairipcore). Complements DEX recovery tooling such as [[zygisk-dump-dex]] and static decode via [[jadx]] after protections are stripped.

## Links

- Repo: https://github.com/NPC2000/AppPealing-new

## Related

[[mobile-anti-cheat]] · [[xposed-module-kit]] · [[magisk]] · [[dobby]] · [[zygisk-dump-dex]] · [[jadx]] · [[frida]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
