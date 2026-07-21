---
title: tpm-mmio
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/synctop__tpm-mmio.md
updated: 2026-07-21
confidence: medium
---

# tpm-mmio

PoC that uses **MMIO (Memory-Mapped I/O)** to read a TPM 2.0 public Endorsement Key (EK) and related TPM state directly from the chip, bypassing OS TPM stack hooks. Aimed at anti-cheat / Detection:HWID engineers who need a ground-truth EK path that is not mediated by `DeviceIoControl` or `TPM.sys` filters. (source: wiki/sources/descriptions/synctop__tpm-mmio.md)

Complements stack-integrity detectors such as [[detect-tpm-spoofing]] (IOCTL vs `TPM.sys` cache mismatch) and sits alongside other HWID fingerprint research such as [[nvidiaapi]].

## Links

- Repo: https://github.com/synctop/tpm-mmio

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[detect-tpm-spoofing]] · [[hvci]] · [[nvidiaapi]]
