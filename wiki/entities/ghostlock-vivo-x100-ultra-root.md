---
title: GhostLock Vivo X100 Ultra Root
kind: entity
topics: [mobile-security, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/Romk-a__CVE-2026-43499-ghostlock-vivo-x100-ultra-root.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# GhostLock Vivo X100 Ultra Root

Device-focused Android kernel root exploit for **Vivo X100 Ultra (PD2366)** weaponizing **CVE-2026-43499** (PI-futex race) to obtain controlled kernel writes, SELinux relaxation, credential overwrite to uid 0, and KernelSU bootstrap. Combines a Kotlin/Jetpack Compose app (HOCON kernel profiles, Shizuku UserService, logging) with a standalone C++23 native runtime and a Rust boot-image extractor that builds per-release GLK1 profiles from boot images, OTA packages, or URLs. Exploitation middleware includes multicast waiter, TCP zerocopy, and select-stack race routes, plus KernelSnitch timing leaks and documented research on bypassing Vivo **vr.ko** anti-root (tracepoint probe neutralization, per-task tag clearing). Intended for authorized mobile kernel security research and vendor anti-tamper study on PGO/BOLT-hardened Qualcomm Android 14/16 kernels. (source: wiki/sources/descriptions/Romk-a__CVE-2026-43499-ghostlock-vivo-x100-ultra-root.md)

Extends the GhostLock CVE-2026-43499 family beside [[ghostlock-oneplus]] and [[ghostlock-app]] with a Vivo-specific vr.ko bypass research track.

## Links

- Repo: https://github.com/Romk-a/CVE-2026-43499-ghostlock-vivo-x100-ultra-root
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[ghostlock-oneplus]] · [[ghostlock-app]] · [[kernelsu]] · [[mobile-anti-cheat]] · [[cve-2026-43499-popsicle]]
