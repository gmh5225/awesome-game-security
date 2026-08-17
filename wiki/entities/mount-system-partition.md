---
title: Mount System Partition (brew02)
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/brew02__MountSystemPartition.md
updated: 2026-08-17
confidence: medium
---

# Mount System Partition (brew02)

**MountSystemPartition** (brew02/MountSystemPartition) demonstrates how to **programmatically mount the hidden EFI system partition (ESP)** on Windows using only the **Windows API**. The C++ sample covers **partition enumeration and mounting** without external tools or elevated command-line utilities, serving as a user-mode reference for accessing the system partition from running Windows. Aimed at **UEFI security researchers** and system-level developers who need programmatic ESP access for firmware/bootkit analysis, boot-loader inspection, or offline ESP file workflows. (source: wiki/sources/descriptions/brew02__MountSystemPartition.md)

Complements pre-OS NTFS/ESP access tools such as [[ntfs-efi]] and UEFI runtime research samples such as [[uefi-bootloader]] and [[efidump]].

## Links

- Repo: https://github.com/brew02/MountSystemPartition

## Related

[[ntfs-efi]] · [[uefi-bootloader]] · [[efidump]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
