---
title: NTFS-EFI
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/wesmar__NTFS_EFI.md
updated: 2026-08-04
confidence: medium
---

# NTFS-EFI (EfiNtfs)

Native UEFI x64 NTFS read-and-write filesystem driver (**EfiNtfs**) that exposes NTFS volumes through `EFI_SIMPLE_FILE_SYSTEM_PROTOCOL`, enabling pre-boot file operations without booting a full OS. Written in pure C11 against prebuilt EDK2 static libraries and built with plain MSVC project files — no EDK2 BaseTools required. (source: wiki/sources/descriptions/wesmar__NTFS_EFI.md)

Implements a full NTFS engine: B+tree indexing, MFT and `$MFTMirr` handling, LZNT1 decompression, cluster allocation, and chkdsk-clean unmount semantics. Ships three EFI binaries: `ntfs.efi` (driver), `EC.efi` (EFI Commander — dual-panel pre-boot file manager with unified FAT32/NTFS VFS), and `ntfs_probe.efi` (functional test and benchmark harness). (source: wiki/sources/descriptions/wesmar__NTFS_EFI.md)

Aimed at low-level firmware research, offline recovery, forensic extraction, and pre-OS tasks such as bootloader patching, driver staging, and registry or disk manipulation before Windows loads. Complements same-author UEFI tooling such as [[efitool]] and user-mode NTFS forensics such as [[ntfstool]] / [[file-recovery-tool]].

## Links

- Repo: https://github.com/wesmar/NTFS_EFI

## Related

[[efitool]] · [[ntfstool]] · [[file-recovery-tool]] · [[uefi-bootloader]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
