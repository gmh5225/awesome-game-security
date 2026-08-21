---
title: Windows-Spoofer
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Scrut1ny__Windows-Spoofer.md
updated: 2026-08-21
confidence: medium
---

# Windows-Spoofer

**Windows-Spoofer** (Scrut1ny) is an open-source **Windows 10 and 11** spoofing and cleanup toolkit. It combines **Batch** and **PowerShell** modules to change selected system identifiers, adjust network-related values, and clear common trace artifacts. The workflow integrates external utilities for tasks such as **volume ID** and **SMBIOS-related** modification, with extensive notes on platform support and operational limits. Primary use case is **game security and anti-cheat research** where analysts study hardware and software fingerprinting behavior in controlled test environments. (source: wiki/sources/descriptions/Scrut1ny__Windows-Spoofer.md)

Distinct from kernel-driver HWID spoofers such as [[easy-hwid-spoofer]], [[hwid-kernel-spoofer]], and [[eac-spoofer-meme]]; this repo is a **usermode orchestration toolkit** (Batch/PowerShell + bundled external helpers) rather than a custom KMDF/IOCTL-hook stack. Complements AMIDEWIN-oriented research such as [[spoofer-amidewin]], disk-serial PoCs such as [[hdd-serial-spoofer]] and [[skotschia-hwid-spoofer]], and defensive inventory tools such as [[windows-hardware-info]] and [[hwid-checker-mg]]. Screenshare attestation kits such as [[alibi]] scan for HWID-spoofer artifacts on accused-player machines.

Sits in the `Cheat > HWID` lane for studying identifier surfaces, trace cleanup, and operational limits of non-kernel spoof workflows.

## Links

- Repo: https://github.com/Scrut1ny/Windows-Spoofer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[spoofer-amidewin]] · [[hdd-serial-spoofer]] · [[skotschia-hwid-spoofer]] · [[hwid-checker-mg]] · [[windows-hardware-info]] · [[alibi]] · [[ow-anti-flag]]
