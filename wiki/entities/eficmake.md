---
title: EfiCMake
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/mrexodia__EfiCMake.md
updated: 2026-07-29
confidence: medium
---

# EfiCMake

Minimal **CMake template** for building UEFI applications with EDK2 SDK headers **without** the full EDK2 build system. Produces standalone `.efi` binaries via MSVC (`/GS-`, `/EHs-`) linked with `/SUBSYSTEM:EFI_APPLICATION`, exposing bare-metal entry and direct access to `EFI_SYSTEM_TABLE` and boot services. (source: wiki/sources/descriptions/mrexodia__EfiCMake.md)

Useful as a lightweight scaffold when prototyping pre-OS / EFI research payloads that complement mapper demos such as [[uefi-bootloader]] and [[xigmapper]], or when iterating on UEFI apps later annotated in IDA via [[ida-efiutils]].

## Links

- Repo: https://github.com/mrexodia/EfiCMake

## Related

[[uefi-bootloader]] · [[efitool]] · [[xigmapper]] · [[ida-efiutils]] · [[minivisorpkg]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
