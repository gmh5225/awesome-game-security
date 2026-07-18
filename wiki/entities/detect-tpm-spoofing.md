---
title: DetectTpmSpoofing
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md
updated: 2026-07-18
confidence: medium
---

# DetectTpmSpoofing

Small KMDF Windows kernel driver (C/C++, CMake + WDK) that detects **TPM 2.0 response spoofing** on the device stack. It compares a `TPM2_ReadPublic` result from the normal IOCTL path against the same data from `TPM.sys` internal cached response buffers; mismatched FNV-1a hashes indicate a filter or `DeviceIoControl` hook forging public / endorsement keys used for hardware identity. Aimed at anti-cheat researchers spotting HWID spoofers that fake TPM attestation without touching the real TPM. (source: wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md)

Complements HWID fingerprint research such as [[nvidiaapi]] (GPU serial / board identity) under the same Detection:HWID lane.

## Links

- Repo: https://github.com/weak1337/DetectTpmSpoofing

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hvci]] · [[dma]] · [[nvidiaapi]]
