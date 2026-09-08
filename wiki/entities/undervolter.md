---
title: UnderVolter
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/wesmar__UnderVolter.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# UnderVolter

**Native UEFI x64 application** (wesmar) that programs Intel CPU voltage offsets, power limits, turbo ratios, and related power-management settings from the **pre-boot environment** before any OS or hypervisor loads. Catalogued under **Cheat > EFI Driver**. (source: wiki/sources/descriptions/wesmar__UnderVolter.md)

## Mechanism

C with x64 assembly for direct MSR and MMIO access; EFI multiprocessor services apply settings across cores; INI profiles for Sandy Bridge through Arrow Lake. Capabilities include FIVR voltage-domain programming (MSR 0x150), NVRAM Setup variable patching (CFG/OC Lock), and Secure Boot certificate self-enrollment. Runs at firmware boot time, bypassing hypervisor MSR filtering from Hyper-V, VBS, and similar protections that block the same writes from user-mode or kernel tools.

## Research relevance

Pre-boot CPU control and **Plundervolt-class** voltage fault-injection surfaces; UEFI trust-chain manipulation beside tools such as [[efitool]] and [[perfectsmbios]].

## Links

- Repo: https://github.com/wesmar/undervolter

## Related

[[efitool]] · [[perfectsmbios]] · [[hvci]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
