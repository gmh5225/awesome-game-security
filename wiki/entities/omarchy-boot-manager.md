---
title: Omarchy Boot Manager
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md
  - wiki/sources/README-categories.md
updated: 2026-09-26
confidence: medium
---

# Omarchy Boot Manager

**Omarchy Boot and Secure Boot Manager** (Azteriisk) is an Omarchy Linux plugin that simplifies Windows and Linux dual-booting while keeping UEFI Secure Boot enabled for both operating systems. Targets Linux gamers and dual-boot users who need Secure Boot to satisfy anti-cheat systems such as Vanguard, EasyAntiCheat, and FACEIT without disabling firmware protections for Linux. (source: wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md)

README category: Some Tricks / Linux.

## Secure Boot enrollment

Enrolls custom Secure Boot keys alongside Microsoft OEM certificates using **sbctl**, then signs Limine bootloaders and kernel images so Linux and Windows boot chains remain firmware-validated. (source: wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md)

## Boot chain and controls

Automatically configures Limine chainload entries for detected Windows EFI partitions. Ships a GTK4 GUI, Python CLI tools, and Omarchy menu integration for one-shot reboots into Windows or BIOS setup via **efibootmgr**. (source: wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md)

## Windows companion

Windows-side helper uses **bcdedit** and a scheduled task for zero-UAC swaps back to Omarchy after gaming sessions on the Windows partition. (source: wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md)

## Positioning

Complements Ring3 utility workarounds such as [[discord-dpi-bridge]] (avoids WinDivert drivers that EAC/Denuvo reject) by addressing the **Secure Boot posture** requirement that blocks many dual-boot Linux setups from running Vanguard/EAC/FACEIT titles on Windows without disabling firmware protections.

## Links

- Repo: https://github.com/Azteriisk/omarchy-boot-manager

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[discord-dpi-bridge]] · [[easy-anti-cheat]] · [[vanguard]] · [[hvci]]
