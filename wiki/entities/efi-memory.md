---
title: efi-memory
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/SamuelTulach__efi-memory.md
updated: 2026-08-21
confidence: medium
---

# efi-memory

**efi-memory** (SamuelTulach) is a proof-of-concept **EFI runtime driver** for **reading and writing virtual memory** from a **firmware context**. Communication uses a **SetVariable hook** pattern inspired by **EfiGuard**, with separate **firmware-side** and **user-mode companion** components. The repository also ships a **mapper client** derived from a **kdmapper-style** workflow for manual-mapping scenarios on Windows. Primary use cases are **firmware security research**, **low-level memory access experiments**, and **game security studies** involving pre-OS or runtime driver interactions. README category: cheat / [EFI RPM]. (source: wiki/sources/descriptions/SamuelTulach__efi-memory.md)

Sits in the **EFI RPM** lane beside SetVariable-backed samples such as [[sub-get-variable]], boot-loaded runtime access such as [[efi-driver-access]], and minimal post-boot dump PoCs such as [[efidump]]. Same author as protected-process R/W framework [[meme-rw]] and UEFI bootkit [[rainbow]].

## Links

- Repo: https://github.com/SamuelTulach/efi-memory

## Related

[[sub-get-variable]] · [[efi-driver-access]] · [[efidump]] · [[efi-monitor]] · [[kdmapper]] · [[meme-rw]] · [[uefi-bootloader]] · [[sumap]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
