---
title: SecureBootCheck
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Krimziee__SecureBootCheck.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: high
---

# SecureBootCheck

Read-only Windows diagnostic (Krimziee) that reports whether a PC meets **Secure Boot** and **TPM 2.0** firmware settings many kernel-level anti-cheat systems require before titles launch. Implemented in PowerShell with an optional WPF (XAML) GUI and a batch launcher. (source: wiki/sources/descriptions/Krimziee__SecureBootCheck.md)

## Inspection scope

- UEFI vs legacy boot mode and GPT vs MBR disk layout
- Secure Boot state and key health
- TPM 2.0 readiness and BitLocker recovery-key status

Does **not** modify BIOS, disks, or the TPM. When checks fail, it explains likely causes and gives ordered, copyable fix steps tailored to detected PC or motherboard brand, including cases where hardware cannot support Secure Boot or TPM.

## Audience

Gamers and support staff troubleshooting Windows 10/11 launch blocks from anti-cheat Secure Boot and TPM requirements—not building or bypassing anti-cheat software.

## Positioning

Listed under **Anti Cheat** beside platform-trust tooling such as [[sewindows]] and dual-boot Secure Boot helpers such as [[omarchy-boot-manager]] and the Arch/DIY enrollment guide [[arch-linux-secure-boot-guide]].

## Links

- Repo: https://github.com/Krimziee/SecureBootCheck

## Related

[[hvci]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[omarchy-boot-manager]]
