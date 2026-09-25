---
title: AxManagerD
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/bufanchen121101__AxManagerD.md
updated: 2026-09-25
confidence: medium
---

# AxManagerD

**AxManagerD** (bufanchen121101) is a **root-free modular extension framework** for Android that provides Magisk-style module loading without rooting, unlocking the bootloader, or modifying system partitions. Built primarily in Kotlin and Java with native C++ components. (source: wiki/sources/descriptions/bufanchen121101__AxManagerD.md)

## Capabilities

- Installable modules with Magisk-style lifecycle management on unmodified hosts
- Runtime daemons with sensor-based triggers
- **Property injection** and boot scripts for environment shaping
- **LSPatch-based Xposed hooking** for runtime app modification without a global root stack
- Script tracing and an integrated **AI assistant** for auditing and developing module behavior

## Device Owner (optional)

Activation through **Dhizuku** or **Shizuku** adds system-level app hiding, suspension, permission control, and related management features. (source: wiki/sources/descriptions/bufanchen121101__AxManagerD.md)

## Security research angle

Aimed at Android modders, developers, and security researchers who want deep customization and hooking while avoiding traditional root, bootloader-unlock, and system-partition signals used by banking and gaming applications.

Listed in the README under **Cheat → Magisk** beside Play Integrity orchestration modules such as [[jerrymanager]] and curated module catalogs such as [[zamr]].

## Links

- Repo: https://github.com/bufanchen121101/AxManagerD

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[mobile-anti-cheat]] · [[jerrymanager]] · [[zamr]] · [[webui-x-portable]] · [[lsposed-universal-template]] · [[frida]]
