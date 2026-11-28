---
title: AntiCheatExpert
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/mioolio__AntiCheatExpert.md
updated: 2026-11-21
confidence: medium
---

# AntiCheatExpert

**Security research repository** documenting and reverse-engineering the commercial **Tencent AntiCheatExpert (ACE)** suite across **kernel drivers**, **user-mode services**, **plugins**, **SGuard**, and related **PE/UEFI** components—**18** documented binaries in the README category map. The workflow centers on **Python** utilities for PE parsing, Capstone disassembly, diff reporting, **IOCTL** table extraction, and log-crypto analysis, paired with **Microsoft MASM (ml64)** and a custom **COFF linker** to converge rebuilt images that match originals including **Authenticode** layout. (source: wiki/sources/descriptions/mioolio__AntiCheatExpert.md)

Ships structured assembly sources, pack metadata, per-component reports, and Chinese-language deep dives into capabilities, protocols, component interaction, and bypass-oriented analysis matrices. Aimed at researchers and educators studying game anti-cheat internals, driver behavior, and integrity protection; distributes **text artifacts only**—no signed executables or samples.

Listed in the README as reverse-engineering and byte-faithful rebuild documentation for Tencent AntiCheatExpert (drivers, SGuard, plugins, UEFI).

Complements mobile-focused Tencent ACE RE such as [[ff-ace-anticheat-analysis]] and [[anticheat-anogs-tencent]], authorized ACE **console/CDN/backend** assessment [[ace-security-research]], host cleanup tooling such as [[deltaforce-cleaner]], and other full-stack commercial AC dossiers such as [[all-about-eac]] and [[fortnite-ac-reversal]].

## Links

- Repo: https://github.com/mioolio/AntiCheatExpert

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ff-ace-anticheat-analysis]] · [[anticheat-anogs-tencent]] · [[deltaforce-cleaner]] · [[anticheattoggle]] · [[sguard-limit]] · [[anticheat-scanner]] · [[research-rigor]]