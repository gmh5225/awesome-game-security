---
title: GhostLock Vivo X100 Ultra Root
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Romk-a__CVE-2026-43499-ghostlock-vivo-x100-ultra-root.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# GhostLock Vivo X100 Ultra Root

Device-focused Android kernel root exploit for **Vivo X100 Ultra (PD2366)** weaponizing **CVE-2026-43499** — a PI-futex race that yields controlled kernel writes, SELinux relaxation, credential overwrite to uid 0, and handoff to a root child for **KernelSU** bootstrap. Intended for authorized mobile kernel security research, reverse engineering of vendor anti-tamper modules, and studying exploitation on PGO- and BOLT-hardened Qualcomm Android 14/16 kernels rather than casual end-user rooting. (source: wiki/sources/descriptions/Romk-a__CVE-2026-43499-ghostlock-vivo-x100-ultra-root.md)

Extends the GhostLock CVE-2026-43499 family beside [[ghostlock-oneplus]] and [[ghostlock-app]] with a Vivo-specific **vr.ko** anti-root bypass research track (tracepoint probe neutralization, per-task tag clearing, and related paths documented in-repo).

## Stack

| Layer | Role |
|-------|------|
| Kotlin / Jetpack Compose app | HOCON kernel profiles, Shizuku UserService, logging |
| C++23 native runtime | Standalone exploit middleware and execution |
| Rust boot-image extractor | Builds per-release **GLK1** profiles from boot images, OTA packages, or URLs |

Exploitation middleware includes multicast waiter, TCP zerocopy, and select-stack race routes, plus **KernelSnitch** timing leaks for kernel layout discovery on hardened builds.

## Links

- Repo: https://github.com/Romk-a/CVE-2026-43499-ghostlock-vivo-x100-ultra-root
- CVE: CVE-2026-43499

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[ghostlock-oneplus]] · [[ghostlock-app]] · [[kernelsu]] · [[mobile-anti-cheat]] · [[cve-2026-43499-popsicle]]
