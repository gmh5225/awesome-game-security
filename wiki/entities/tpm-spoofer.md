---
title: TPM-SPOOFER
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/s0ngidong3__TPM-SPOOFER.md
updated: 2026-07-23
confidence: medium
---

# TPM-SPOOFER

Windows **kernel driver** that spoofs TPM (Trusted Platform Module) serial numbers by hooking TPM IOCTL communication. Includes a KM hook-based TPM response interceptor plus a user-mode serial checker to verify spoofed values. Aimed at game-security researchers studying HWID spoofing and anti-cheat ban-evasion surfaces under the Cheat `[TPM]` lane. (source: wiki/sources/descriptions/s0ngidong3__TPM-SPOOFER.md)

Detection counterparts: [[detect-tpm-spoofing]] (IOCTL vs `TPM.sys` cache mismatch) and [[tpm-mmio]] (MMIO-direct public EK read bypassing OS hooks). Broader HWID spoof research: [[hwidspoofer]], [[spoofer-amidewin]].

## Links

- Repo: https://github.com/s0ngidong3/TPM-SPOOFER

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[detect-tpm-spoofing]] · [[tpm-mmio]] · [[hwidspoofer]] · [[hvci]]
