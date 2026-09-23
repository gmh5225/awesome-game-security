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

## Detection targets

Probes aim to surface cheat software, **DMA cards**, **capture hardware**, **Cronus/XIM-style input devices**, anti-forensic wipe traces, and persistence across **every signed-in user account**—without modifying the host or using the network. (source: wiki/sources/descriptions/ablanchard-dev__dexcheck.md)

## Probes and artifacts

Runs ~40 read-only probes on Windows via **PowerShell 5.1** (double-click launcher) plus a native **macOS** Bash companion. Scans cover USN journal and Prefetch artifacts, BAM/DAM, UserAssist, Shimcache, PCA, registry and startup persistence, live processes and outbound connections, kernel drivers, **PCIe device identity**, HWID spoof indicators, Code Integrity refusals, **system security posture**, and anti-forensic wipe traces.

## Verdict model

Rolls findings into **CLEAN**, **SUSPECT**, or **critical** verdict tiers. Ships a visual setup checklist for cases software cannot see (second-machine radar rigs, spoofed DMA hardware). A large PowerShell test suite is exercised in CI.

## Design constraints

Read-only collectors only—no host writes, no outbound network use. Intended for consent-based, moderator-supervised workflows rather than silent background enforcement.

## Audience

Tournament organizers, community anti-cheat moderators, and game-security researchers who need practical, consent-based player verification workflows. (source: wiki/sources/descriptions/ablanchard-dev__dexcheck.md)

## Links

- Repo: https://github.com/ablanchard-dev/dexcheck

## Related

[[error-pc-check]] · [[aeterna-rongroi]] · [[alibi]] · [[aetheris]] · [[luminary-dma]] · [[hoozi-cs2-dma]] · [[hardware-input-injection]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]] · [[overviews/reverse-engineering]]
