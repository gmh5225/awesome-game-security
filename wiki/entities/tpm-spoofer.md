---
title: tpm-spoofer
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/SamuelTulach__tpm-spoofer.md
  - wiki/sources/descriptions/s0ngidong3__TPM-SPOOFER.md
updated: 2026-08-21
confidence: medium
---

# tpm-spoofer

Proof-of-concept **TPM identifier spoofing** research for anti-cheat hardware tracking. Implementations hook TPM request handling in kernel mode and ship user-mode utilities to read or verify TPM-derived signals (serial numbers, endorsement-key–related data). Built with C/C++ on Visual Studio and WDK; targets modern Windows TPM stack behavior. Primary use case: game-security research on how TPM and EK-based signals can be inspected, intercepted, and validated. (source: wiki/sources/descriptions/SamuelTulach__tpm-spoofer.md) (source: wiki/sources/descriptions/s0ngidong3__TPM-SPOOFER.md)

Detection counterparts: [[detect-tpm-spoofing]] (IOCTL vs `TPM.sys` cache mismatch) and [[tpm-mmio]] (MMIO-direct public EK read bypassing OS hooks). Broader HWID spoof research: [[hwidspoofer]], [[spoofer-amidewin]].

## Links

- Repo (SamuelTulach): https://github.com/SamuelTulach/tpm-spoofer
- Repo (s0ngidong3): https://github.com/s0ngidong3/TPM-SPOOFER

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[detect-tpm-spoofing]] · [[tpm-mmio]] · [[hwidspoofer]] · [[hvci]]
