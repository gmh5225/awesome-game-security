---
title: odzhan-hwid
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/odzhan__hwid.md
  - wiki/sources/README-categories.md
updated: 2026-10-04
confidence: medium
---

# odzhan-hwid

**odzhan-hwid** (odzhan/hwid) is a read-only native C++20 console utility for Windows 10/11 x64 that inventories hardware identifiers exposed by the operating system and device drivers. It collects system UUID, motherboard and BIOS serials, storage and network identifiers, USB device IDs, TPM public key hashes, DXGI GPU data, CPUID processor details, and related metadata through WMI, SetupAPI, IP Helper, TBS/CNG, and optional NVML. Each field includes provenance, confidence level, mutability notes, availability status, and diagnostic context rather than producing a single composite fingerprint. Output is available as human-readable tables or structured JSON, with optional verbose diagnostics and a redaction mode to suppress sensitive values. Targets security researchers, anti-cheat analysts, and reverse engineers studying how Windows hardware identity is queried and which identifiers are reliable or spoofable. (source: wiki/sources/descriptions/odzhan__hwid.md)

Defensive **Detection:HWID** inventory lane — complements spoofers such as [[hwid]] (btbd) and checkers such as [[hwid-checker-mg]] by documenting per-field query paths and mutability without modifying system state.

## Links

- Repo: https://github.com/odzhan/hwid (README tag: Anti Cheat / Detection:HWID)

## Related

[[hwid]] · [[hwid-spoofing]] · [[hwid-checker-mg]] · [[filtertap]] · [[windows-hardware-info]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
