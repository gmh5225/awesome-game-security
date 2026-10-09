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

**Flashwright** (contactjayclatty/flashwright) is a Windows 11 setup wizard that guides researchers from plug-in through update, root, and factory flash on **Google Pixel–class** Android phones. (source: wiki/sources/descriptions/contactjayclatty__flashwright.md)

README category: Cheat / **Android Root** — Windows 11 wizard to flash factory images, patch boot with Magisk, and OTA-update while keeping root (dry-run checks, backups, recovery).

## Capabilities

Opens factory and OTA packages, verifies **SHA-256** on each image, patches boot with **Magisk** for root, and can flash stock firmware while surfacing per-file checksums. Typed **adb** and **fastboot** invocation uses parsers, timeouts, and a human review step before any destructive write. **Dry-run** previews report planned vs blocked actions without writing. Safety gates check device/build match, security patch level, bootloader anti-rollback, A/B slot rules, and on-device boot images against factory sources. **Boot** and **vbmeta** partition backups, one-click restore, and Windows USB driver handling round out recovery. (source: wiki/sources/descriptions/contactjayclatty__flashwright.md)

## Architecture

**Rust** backend with **Tauri** desktop shell and **TypeScript/Vite** front end; a typed command layer wraps adb/fastboot instead of ad-hoc shell scripts. (source: wiki/sources/descriptions/contactjayclatty__flashwright.md)

## Positioning

Suited to practitioners who need a **controlled, auditable** device-modification workflow for integrity-related mobile security work — beside cross-platform [[pixel-flasher]], boot-image editors [[android-boot-image-editor]], [[magiskboot]], and payload tools [[payload-dumper]]. Contrasts with one-tap exploit root [[root-my-pixel]] by emphasizing verified stock images and explicit safety gates.

## Links

- Repo: https://github.com/contactjayclatty/flashwright

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[pixel-flasher]] · [[magisk]] · [[magiskboot]] · [[android-boot-image-editor]] · [[root-my-pixel]] · [[payload-dumper]] · [[mobile-trust-boundaries]]
