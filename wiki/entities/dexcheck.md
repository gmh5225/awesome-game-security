---
title: dexcheck
kind: entity
topics: [anti-cheat, dma-attack, reverse-engineering]
sources:
  - wiki/sources/descriptions/ablanchard-dev__dexcheck.md
  - wiki/sources/README-categories.md
updated: 2026-09-23
confidence: medium
---

# dexcheck

**DexCheck** (ablanchard-dev) is a live, read-only forensic PC check for **Call of Duty** and **Warzone**, built to vet players during supervised screen-shares while a moderator watches the output. (source: wiki/sources/descriptions/ablanchard-dev__dexcheck.md)

## Probes and artifacts

Runs ~40 read-only probes on Windows via **PowerShell 5.1** (double-click launcher) plus a native **macOS** Bash companion. Scans cover USN journal and Prefetch artifacts, BAM/DAM, UserAssist, Shimcache, PCA, registry and startup persistence, live processes and outbound connections, kernel drivers, **PCIe device identity**, HWID spoof indicators, Code Integrity refusals, and anti-forensic wipe traces across signed-in user accounts.

## Verdict model

Rolls findings into **CLEAN**, **SUSPECT**, or critical verdicts without modifying the host or using the network. Ships a visual setup checklist for cases software cannot see (second-machine radar rigs, spoofed DMA hardware) plus a large PowerShell test suite exercised in CI.

## Audience

Tournament organizers, community anti-cheat moderators, and game-security researchers who need practical, consent-based player verification workflows. (source: wiki/sources/descriptions/ablanchard-dev__dexcheck.md)

## Links

- Repo: https://github.com/ablanchard-dev/dexcheck

## Related

[[error-pc-check]] · [[aeterna-rongroi]] · [[aetheris]] · [[luminary-dma]] · [[hoozi-cs2-dma]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
