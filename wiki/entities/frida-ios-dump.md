---
title: frida-ios-dump
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md
  - wiki/sources/README-categories.md
updated: 2026-10-14
confidence: medium
---

# frida-ios-dump

Python host driver that pulls decrypted IPA packages from apps on jailbroken iPhones and iPads. Frida attaches and injects a JavaScript agent using the Objective-C bridge to dump in-memory Mach-O binaries and embedded frameworks while FairPlay encryption is stripped, then repackages the bundle with parallel SFTP transfers over USB or SSH. (source: wiki/sources/descriptions/AloneMonkey__frida-ios-dump.md)

Supports listing installed apps by display name or bundle identifier, Frida 17 with bundled frida-objc-bridge compilation, and flexible SSH authentication (config aliases and keys). Aimed at mobile security researchers and reverse engineers who need analyzable iOS binaries for static inspection, patching workflows, or studying protected games and apps on device.

Listed under Cheat → IOS App Packaging in the README category map. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/AloneMonkey/frida-ios-dump

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[bagbak]] · [[il2cpp-re]]
