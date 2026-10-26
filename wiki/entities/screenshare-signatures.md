---
title: ScreenShare Signatures
kind: entity
topics: [anti-cheat, dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: high
---

# ScreenShare Signatures

**ScreenShare Signatures** (Catusse2k; *ScreenShare Forensic Scanner*) is a community-maintained JSON signature database and documentation for FiveM and Minecraft Windows screenshare forensics during moderated, consent-based sessions. (source: wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md)

## Artifact model

Threat categories group rules for DMA hardware and [[pcileech]]-style tooling, kernel mappers and [[byovd]]-class vulnerable-driver abuse, firmware/UEFI hints, game-specific cheat artifacts, input-emulation hardware, and anti-evasion traces (for example log wiping). Each rule can target processes, memory strings, registry keys, event logs, PnP IDs, filesystem paths, and procedural checks, carrying severity weights and confidence labels plus an allowlist for legitimate admin tools.

## Integration

Integrators load the JSON into their own scanner, correlate **multiple hits** before enforcement, and tune false positives with the bundled allowlist; the README shows simple Python string matching and documents planned YARA conversion and deeper forensic automation. (source: wiki/sources/descriptions/Catusse2k__ScreenShare-Signatures.md)

## Audience

Server moderators and security-minded staff who need community-sourced, updatable indicators for kernel cheats, DMA setups, and bypass attempts—complements full workflows such as [[error-pc-check]], [[aeterna-rongroi]], [[jaranalyzer]], and [[dexcheck]] rather than shipping a standalone agent.

## Links

- Repo: https://github.com/Catusse2k/ScreenShare-Signatures

## Related

[[overviews/anti-cheat]] · [[dma]] · [[byovd]] · [[error-pc-check]] · [[aeterna-rongroi]] · [[jaranalyzer]] · [[dexcheck]]
