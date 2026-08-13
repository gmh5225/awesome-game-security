---
title: fortnite-efi-external
kind: entity
topics: [game-hacking, windows-kernel, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__Fortnite-EFI-External.md
updated: 2026-08-13
confidence: medium
---

# fortnite-efi-external

External Fortnite cheat sample (gmh5225; cheat / game:fortnite [External]). Uses **EFI (UEFI) runtime services** for stealthy out-of-process memory access: the usermode client talks to a UEFI driver through **`NtSetSystemEnvironmentValueEx`**, reading game memory **without loading a Windows kernel driver**—aimed at bypassing anti-cheat **driver enumeration and kernel-driver telemetry** on [[easy-anti-cheat]]-protected Fortnite clients. Useful for studying below-OS external cheat stacks, UEFI runtime ↔ OS usermode comm channels, and driverless RPM alternatives beside kernel-driver and [[dma]] externals. (source: wiki/sources/descriptions/gmh5225__Fortnite-EFI-External.md)

Contrasts with driver-backed Fortnite externals such as [[fortnite-external]], [[fortnite-ud-external]], and [[volto-external-spowar-ud-eac-be-fortnite-external-cheat]], and with pre-kernel bootkit PoCs such as [[bootlicker]] and runtime mappers such as [[uefi-bootloader]].

## Links

- Repo: https://github.com/gmh5225/Fortnite-EFI-External

## Related

[[easy-anti-cheat]] · [[bootlicker]] · [[uefi-bootloader]] · [[xigmapper]] · [[unreal-object-model]] · [[dma]] · [[fortnite-external]] · [[fortnite-ud-external]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
