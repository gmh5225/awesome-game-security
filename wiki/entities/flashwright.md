---
title: Flashwright
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/contactjayclatty__flashwright.md
  - wiki/sources/README-categories.md
updated: 2026-10-09
confidence: medium
---

# Flashwright

Windows 11 **Tauri** desktop wizard (Rust core + TypeScript/Vite UI) for **Pixel-class** factory flash, **Magisk** boot patching, and **OTA updates while keeping root**. Typed **adb/fastboot** command layer with parsers, timeouts, and a review gate before destructive writes. Opens factory/OTA packages, verifies **SHA-256** per image, and supports dry-run previews that report blocked vs planned actions without writing. Safety checks cover device/build match, security patch level, bootloader anti-rollback, A/B slot rules, and on-device boot vs factory comparisons; **boot/vbmeta backups**, one-click restore, and Windows USB driver handling. Listed under Cheat / **Android Root** beside boot-image tooling. (source: wiki/sources/descriptions/contactjayclatty__flashwright.md)

## Links

- Repo: https://github.com/contactjayclatty/flashwright

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[pixel-flasher]] · [[magisk]] · [[magiskboot]] · [[android-boot-image-editor]] · [[root-my-pixel]] · [[payload-dumper]]
