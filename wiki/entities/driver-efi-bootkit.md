---
title: driver-efi-bootkit
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-efi-bootkit.md
updated: 2026-08-13
confidence: medium
---

# driver-efi-bootkit

**UEFI boot-stage implant framework** that chains execution from an infected EFI application into the Windows kernel before normal driver-load telemetry exists. C code hooks **`ExitBootServices`** and **`SetVirtualAddressMap`**, tracks the image runtime virtual address, then patches **`OslArchTransferToKernel`** so a target driver can be modified before the OS fully starts. The kernel stage locates a chosen driver image, repurposes its **`.rsrc`** section as executable space, maps an additional payload with **`MmMapIoSpace`**, updates the driver entry point, and restores the original entry path to reduce boot instability. Python tooling extracts the flat shellcode blob, calculates hashed identifiers, injects the **BOOTDOOR** payload into an EFI binary, and can optionally patch **`bootmgfw`** integrity checks. (source: wiki/sources/descriptions/gmh5225__Driver-efi-bootkit.md)

Aimed at low-level Windows boot, firmware, and kernel researchers studying **EFI hooks**, **loader interception**, and **pre-OS driver patching**—adjacent to generic bootkit PoCs such as [[bootlicker]] and runtime mappers such as [[uefi-bootloader]], but focused on a staged EFI→kernel implant with driver-image hijack rather than post-boot runtime services or Boot Manager patching alone.

## Links

- Repo: https://github.com/gmh5225/Driver-efi-bootkit

## Related

[[bootlicker]] · [[uefi-bootloader]] · [[xigmapper]] · [[efixplorer]] · [[efidump]] · [[patchguard]] · [[dse-hook]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
