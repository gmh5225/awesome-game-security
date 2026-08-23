---
title: KernelSU Debug
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/MlgmXyysd__KernelSU_Debug.md
updated: 2026-08-23
confidence: medium
---

# KernelSU Debug

Modified **KernelSU** fork (MlgmXyysd) tuned for **debugging-oriented** Android root workflows rather than production stealth. Combines kernel-side **C** code with Android app and build assets for root access management, **profile control**, and customized policy handling. Changes include relaxed manager checks, permissive **SELinux**-oriented options, **init script** support, and broad root convenience features aimed at testing workflows. Primary audience is Android security research, system debugging, and experimentation in rooted environments. (source: wiki/sources/descriptions/MlgmXyysd__KernelSU_Debug.md)

Sits beside upstream [[kernelsu]] and hardened fork [[apex-su]] in the Cheat / Android root lane. Same author ecosystem as HyperOS bootloader bypass tooling [[xiaomi-hyperos-bootloader-bypass]]. Module stacks that target KernelSU roots—[[rezygisk]], [[ksu-rust-frida]], [[file-explorer]]—may pair with this fork when lab convenience outweighs hide hardening.

## Links

- Repo: https://github.com/MlgmXyysd/KernelSU_Debug (README: `[KernelSU modified for debugging]`)

## Related

[[overviews/mobile-security]] · [[kernelsu]] · [[apex-su]] · [[xiaomi-hyperos-bootloader-bypass]] · [[rezygisk]] · [[ksu-rust-frida]] · [[magisk]] · [[apatch]] · [[keyattestation]]
