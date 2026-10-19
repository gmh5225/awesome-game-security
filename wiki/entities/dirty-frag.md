---
title: DirtyFrag
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/mitschud__DirtyFrag.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# DirtyFrag

Android application and exploit chain that achieves **ephemeral root** on arm64 devices by abusing **CVE-2026-43284** — a kernel page-cache write primitive in IPsec ESP handling. Hardened fork of DFRoot: loads a custom kernel module without an unlocked bootloader or patched boot image, then hands off to a user-chosen KernelSU-style manager via staged `libksud`. Combines a Java manager UI with native C/JNI and a loadable kernel module (AES-CBC transforms, `crash_dump64` splice-based privilege escalation, in-place libc++ hooking). Includes vendor-specific bypasses for Samsung OneUI hardening (DEFEX, RKP, KDP). Root lasts only until reboot, with optional autorun, soft reboot, and module toggles. Mobile kernel exploitation and locked-bootloader compromise research. (source: wiki/sources/descriptions/mitschud__DirtyFrag.md)

Page-cache primitive lineage beside Dirty Pipe [[dirtypiperoot]] / [[dirtypipe-android]]; contemporary locked-bootloader root toolkit lane with [[ghostlock-oneplus]] / [[ghostlock-app]] (CVE-2026-43499).

## Chain components

| Layer | Role |
|-------|------|
| Java manager UI | Orchestrates exploit stages, module toggles, autorun, and soft reboot |
| Native C/JNI | AES-CBC transforms, `crash_dump64` splice privilege escalation, in-place libc++ hooking |
| Loadable kernel module | Delivers root primitive without unlocked bootloader or patched boot image |
| Staged `libksud` | Hands off to a user-chosen KernelSU-style root manager after elevation |

Samsung OneUI targets add DEFEX, RKP, and KDP bypass paths in the native/kernel stages. (source: wiki/sources/descriptions/mitschud__DirtyFrag.md)

## Links

- Repo: https://github.com/mitschud/DirtyFrag
- CVE: CVE-2026-43284

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[dirtypiperoot]] · [[dirtypipe-android]] · [[ghostlock-oneplus]] · [[ghostlock-app]] · [[mobile-anti-cheat]] · [[kernelsu]]
