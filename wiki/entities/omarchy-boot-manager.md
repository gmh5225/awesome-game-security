---
title: Omarchy Boot Manager
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md
updated: 2026-09-26
confidence: medium
---

# Omarchy Boot Manager

Omarchy Linux plugin that simplifies Windows and Linux dual-booting while keeping UEFI Secure Boot enabled for both operating systems. Enrolls custom Secure Boot keys alongside Microsoft OEM certificates using sbctl, signs Limine bootloaders and kernel images, and configures Limine chainload entries for detected Windows EFI partitions. Provides a GTK4 GUI, Python CLI tools, and Omarchy menu integration for one-shot reboots into Windows or BIOS setup via efibootmgr, plus a Windows companion using bcdedit and a scheduled task for zero-UAC swaps back to Omarchy. Targets dual-boot gamers who need Secure Boot to satisfy anti-cheat systems such as Vanguard, EasyAntiCheat, and FACEIT without disabling firmware protections for Linux. (source: wiki/sources/descriptions/Azteriisk__omarchy-boot-manager.md)

## Links

- Repo: https://github.com/Azteriisk/omarchy-boot-manager

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[easy-anti-cheat]] · [[vanguard]] · [[hvci]]
