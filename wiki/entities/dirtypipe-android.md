---
title: DirtyPipe-Android
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/polygraphene__DirtyPipe-Android.md
updated: 2026-07-25
confidence: medium
---

# DirtyPipe-Android

Multi-stage Dirty Pipe (CVE-2022-0847) exploit for **permanent root** on Pixel 6: corrupts the kernel module loader via pipe page-cache overwrites, injects ARM64 shellcode to patch SELinux and credentials, then auto-installs Magisk v24.3 for root that survives reboot. (source: wiki/sources/descriptions/polygraphene__DirtyPipe-Android.md)

Contrasts with temporary-root packaging such as [[dirtypiperoot]] on the same CVE/device lane: this path chains into [[magisk]] persistence rather than a one-shot privilege window. Useful for mobile game-security research on Android Kernel CVE → systemless-root installers and how pipe page-cache bugs widen Magisk/root-hide detection surfaces.

## Links

- Repo: https://github.com/polygraphene/DirtyPipe-Android
- CVE: CVE-2022-0847

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[dirtypiperoot]] · [[magisk]] · [[kernelsu]] · [[cheese]] · [[android-vuln]]
