---
title: ApexSU
kind: entity
topics: [mobile-security, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md
updated: 2026-08-10
confidence: medium
---

# ApexSU

Hardened fork of [[kernelsu]] — a kernel-based Android root solution that grants superuser access through syscall hooks and a UID allowlist instead of patching the system partition. Userspace components (`ksud` daemon, JNI bridge) are rewritten in Rust; the loadable kernel module stays in C and handles SELinux policy injection, app profiles, and module management. Stealth hardening includes IOCTL communication over an anonymous inode disguised as `io_uring` with no `/proc`, `/sys`, or `/dev` entries, plus stricter module validation and built-in `ksud` diagnostics. The Kotlin and Jetpack Compose manager app provides superuser control, module installation, and boot image patching for GKI 2.0 devices on Android 12+. Aimed at Android security researchers and game anti-cheat analysts studying kernel-assisted root, root-detection evasion, and hardened root-framework design. (source: wiki/sources/descriptions/rathorekrishna401-NeuroVoid__ApexSU.md)

## Links

- Repo: https://github.com/rathorekrishna401-NeuroVoid/ApexSU

## Related

[[kernelsu]] · [[magisk]] · [[mobile-anti-cheat]] · [[magiskdetector]] · [[detection]] · [[android-native-root-detector]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]]
