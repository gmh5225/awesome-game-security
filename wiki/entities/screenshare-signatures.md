---
title: ScreenShare Signatures
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: medium
---

# ScreenShare Signatures

**ScreenShare Signatures** (Catusse2k) is a community-maintained JSON signature database and documentation for FiveM and Minecraft screenshare forensics on Windows. (source: wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md)

## Scope

Rules group DMA hardware and PCILeech-style tooling, kernel mappers and vulnerable-driver abuse, firmware/UEFI hints, game-specific cheat artifacts, input-emulation hardware, and anti-evasion traces (for example log wiping). Indicators cover processes, memory strings, registry keys, event logs, PnP IDs, paths, and procedural checks, with severity weights, confidence levels, and an allowlist for legitimate admin tools.

## Usage

Integrators load the database into their own scanner and correlate multiple hits before enforcement; the README illustrates simple Python string matching and notes planned YARA conversion. Pairs consensual workflows such as [[error-pc-check]], [[jaranalyzer]], and [[dexcheck]]. (source: wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md)

## Links

- Repo: https://github.com/Catusse2k/ScreenShare-Signatures

## Related

[[overviews/anti-cheat]] · [[error-pc-check]] · [[jaranalyzer]] · [[dexcheck]] · [[dma]]
