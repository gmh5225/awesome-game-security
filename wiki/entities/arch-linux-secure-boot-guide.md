---
title: Arch Linux Secure Boot Guide
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/OTAKUWeBer__arch-linux-secure-boot-guide.md
updated: 2026-10-14
confidence: high
---

# Arch Linux Secure Boot Guide

Beginner-oriented **Markdown documentation** (OTAKUWeBer) for enabling and maintaining UEFI **Secure Boot** on Arch Linux and similar rolling or DIY distributions that do not ship Microsoft-signed boot shims. Content is procedural Bash and firmware notes—not application source code. (source: wiki/sources/descriptions/OTAKUWeBer__arch-linux-secure-boot-guide.md)

## Enrollment and signing

Walks through generating and enrolling custom keys with **sbctl**, signing kernels and bootloaders for **GRUB**, **systemd-boot**, **rEFInd**, and unified kernel images (UKI), and keeping signatures valid across package updates via automatic hooks. Covers retaining Microsoft OEM keys where dual-boot Windows must stay firmware-validated.

## Dual-boot and anti-cheat

Emphasizes Windows 10/11 dual-boot so competitive titles that require Secure Boot—**Valorant** with [[vanguard]], **FACEIT**, and similar kernel anti-cheats—can run without toggling firmware Secure Boot each OS switch. Includes UEFI prerequisites, **BitLocker** recovery precautions, and troubleshooting common boot failures.

## Linux-only posture

Also frames Secure Boot as defense against bootkits and unauthorized pre-kernel code on Linux-only machines.

## Positioning

Complements Omarchy-specific automation in [[omarchy-boot-manager]] with a distro-agnostic Arch/DIY guide. Pairs with Windows-side read-only checks in [[securebootcheck]] when diagnosing launch blocks versus enrolling Linux boot chains.

## Links

- Repo: https://github.com/OTAKUWeBer/arch-linux-secure-boot-guide

## Related

[[omarchy-boot-manager]] · [[securebootcheck]] · [[vanguard]] · [[easy-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hvci]]
