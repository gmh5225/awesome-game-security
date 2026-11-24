---
title: Kevar Integrity Checker
kind: entity
topics: [anti-cheat, windows-kernel, dma-attack]
sources:
  - wiki/sources/descriptions/windowsthumbsupsvg__kevar-integrity-checker.md
  - wiki/sources/README-categories.md
updated: 2026-11-24
confidence: medium
---

# Kevar Integrity Checker

Open-source Windows utility (windowsthumbsupsvg) for **tournament hosts**, competitive communities, and players to confirm key platform security features are enabled before play. All checks are **read-only**. (source: wiki/sources/descriptions/windowsthumbsupsvg__kevar-integrity-checker.md)

## Inspection scope

- **UEFI Secure Boot** (firmware variables)
- **Kernel DMA Protection**
- **HVCI** (Memory Integrity)
- **TPM 2.0**

Implementation uses firmware variables, `NtQuerySystemInformation`, and WMI queries. Ships in **C++** and **PowerShell**, with an optional **fileless PowerShell** workflow for quick on-machine runs without leaving artifacts.

## Audience and role

Targets game security and anti-cheat scenarios where titles lack strong kernel-level protection—helping block common cheat setups that depend on unsigned drivers, weak DMA firmware, or disabled memory integrity. Complements gamer-oriented launch diagnostics such as [[securebootcheck]] and runtime attestation samples such as [[windows-runtime-attestation-report]].

## Links

- Repo: https://github.com/windowsthumbsupsvg/kevar-integrity-checker

## Related

[[hvci]] · [[iommu-state-verification]] · [[securebootcheck]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[overviews/dma-attack]]