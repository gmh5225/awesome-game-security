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

**odzhan-hwid** (odzhan/hwid) is a read-only native C++20 console utility for Windows 10/11 x64 that inventories hardware identifiers exposed by the operating system and device drivers. Targets security researchers, anti-cheat analysts, and reverse engineers studying how Windows hardware identity is queried and which identifiers are reliable or spoofable. (source: wiki/sources/descriptions/odzhan__hwid.md)

## Query surfaces

| API / subsystem | Example identifiers |
|-----------------|---------------------|
| WMI | System UUID, motherboard and BIOS serials |
| SetupAPI | Storage devices, USB device IDs |
| IP Helper | Network interface identifiers |
| TBS/CNG | TPM public key hashes |
| DXGI / NVML (optional) | GPU data |
| CPUID | Processor details |

Each field records **provenance**, **confidence level**, **mutability notes**, **availability status**, and diagnostic context — deliberately **no single composite fingerprint**.

## Output

Human-readable tables or structured JSON; optional verbose diagnostics and a **redaction mode** to suppress sensitive values.

## Positioning

Defensive **Detection:HWID** inventory lane — complements spoofers such as [[hwid]] (btbd) and checkers such as [[hwid-checker-mg]] by documenting per-field query paths and mutability without modifying system state. Contrasts with WMI-only CLIs such as [[windows-hardware-info]] by multi-API coverage and per-field reliability metadata.

## Links

- Repo: https://github.com/odzhan/hwid (README tag: Anti Cheat / Detection:HWID)

## Related

[[hwid]] · [[hwid-spoofing]] · [[hwid-checker-mg]] · [[filtertap]] · [[windows-hardware-info]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
