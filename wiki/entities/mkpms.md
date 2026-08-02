---
title: mkpms
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/kkkbbb__mkpms.md
updated: 2026-08-02
confidence: medium
---

# mkpms

**wxshadow** — a **KernelPatch Module (KPM)** for Android that implements **stealth breakpoint/hook** via **R^X page split** (separate read-only and execute views of the same code page), designed to **bypass self-read integrity checks** that compare mapped memory against expected bytes. (source: wiki/sources/descriptions/kkkbbb__mkpms.md)

Companion kernel module for [[rust-frida]]'s **WXSHADOW** stealth tier: userspace shadow-page patching pairs with kernel-scope page splitting so hooks are less visible to `/proc` memory scans and inline integrity probes.

## What it covers

- KPM load path via KernelPatch / [[apatch-kpm]] on rooted GKI Android
- Stealth native hook/breakpoint without classic RWX patches
- R^X page-split shadow pages — execute view holds hooked code; read view preserves original bytes for self-checks

Audience: game-security researchers and reverse engineers studying offensive Android kernel explorer techniques in the cheat / kernel driver lane.

## Links

- Repo: https://github.com/kkkbbb/mkpms

## Related

[[rust-frida]] · [[apatch-kpm]] · [[kpm-memreader]] · [[frida]] · [[kernel-hack]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
