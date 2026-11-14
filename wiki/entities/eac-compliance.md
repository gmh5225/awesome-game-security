---
title: EAC Compliance
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/MarceloAlm__EAC-compliance.md
updated: 2026-11-14
confidence: high
---

# EAC Compliance

Production-oriented **Arch Linux guide and tooling** (MarceloAlm) for meeting **Easy Anti-Cheat Linux v2** host-trust requirements—not bypass material. Documentation plus `check-eac-compliance.sh`, a Bash auditor that reads kernel security interfaces via **sysfs** and **procfs** instead of high-level distro utilities. (source: wiki/sources/descriptions/MarceloAlm__EAC-compliance.md)

## Trust-chain checklist

Walks through **UEFI Secure Boot**, **TPM 2.0** measured boot, signed kernels and **DKMS** modules, **kernel lockdown** in integrity mode, disabled **kexec**, **IOMMU** isolation, and **LSM BPF**. Uses a **Shim** and **MOK** dual-keyring pattern so **NVIDIA** and other out-of-tree drivers remain usable alongside compliance.

## Companion material

Includes CIS-style Debian VM lockdown notes and an Ansible security blueprint for defensive server posture—adjacent hardening, not game-client bypass.

## Positioning

Complements generic Secure Boot enrollment in [[arch-linux-secure-boot-guide]] and CachyOS split-kernel workflow in [[cachyos-eac-secure-boot]] with an Arch-focused compliance path and direct kernel-interface verification for [[easy-anti-cheat]] Linux v2.

## Links

- Repo: https://github.com/MarceloAlm/EAC-compliance

## Related

[[arch-linux-secure-boot-guide]] · [[cachyos-eac-secure-boot]] · [[omarchy-boot-manager]] · [[securebootcheck]] · [[easy-anti-cheat]] · [[iommu]] · [[hvci]] · [[overviews/anti-cheat]]