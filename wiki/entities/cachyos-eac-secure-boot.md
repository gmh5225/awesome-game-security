---
title: CachyOS EAC Secure Boot
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/unicbda-droid__cachyos-eac-secure-boot.md
updated: 2026-11-11
confidence: high
---

# CachyOS EAC Secure Boot

Step-by-step **documentation guide** (unicbda-droid) for running **Easy Anti-Cheat Linux v2** on **CachyOS** while keeping **UEFI Secure Boot** enabled for everyday use. Shell snippets and configuration notes—not a standalone application. Focus is **boot-integrity compliance** with EAC v2 expectations (native Fortnite on supported Linux distros), not bypassing protections. (source: wiki/sources/descriptions/unicbda-droid__cachyos-eac-secure-boot.md)

## Dual boot-path design

- **Daily path:** GRUB and the normal kernel stay signed with personal **sbctl** keys for routine Secure Boot use.
- **EAC path:** A separate **firmware-only** entry boots the CachyOS-signed **`linux-cachyos-eac`** kernel via **systemd-boot** with `lockdown=integrity`, **module signature enforcement** (`module.sig_enforce`), and related kernel settings EAC v2 checks.

## Enrollment and maintenance

Covers sbctl key enrollment including the **CachyOS EAC CA**, rebuilding embedded-module GRUB, ESP layout, **pacman hooks** to keep the EAC kernel in sync after updates, verification with **`eac-status`**, and firmware troubleshooting.

## Positioning

Extends generic Arch/DIY Secure Boot enrollment in [[arch-linux-secure-boot-guide]] with a **CachyOS-specific** split-kernel workflow for **[[easy-anti-cheat]]** Linux v2. Complements Omarchy automation in [[omarchy-boot-manager]] and Windows-side diagnostics via [[securebootcheck]] when correlating launch failures with boot-chain posture.

## Links

- Repo: https://github.com/unicbda-droid/cachyos-eac-secure-boot

## Related

[[arch-linux-secure-boot-guide]] · [[omarchy-boot-manager]] · [[securebootcheck]] · [[easy-anti-cheat]] · [[eac-analysis]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
