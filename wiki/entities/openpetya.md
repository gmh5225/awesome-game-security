---
title: OpenPetya
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/iss4cf0ng__OpenPetya.md
updated: 2026-08-04
confidence: medium
---

# OpenPetya

Open-source educational reimplementation of the Petya ransomware bootloader: replaces the MBR, transitions Real→Protected Mode via a custom stage-2 bootloader with keyboard input, derives encryption keys, and encrypts NTFS Master File Table records with Salsa20. Assembly/C/C++ PoC MBR bootkit for studying pre-OS persistence and disk-level crypto forensics—not a live weaponized variant. (source: wiki/sources/descriptions/iss4cf0ng__OpenPetya.md)

## Links

- Repo: https://github.com/iss4cf0ng/OpenPetya

## Related

[[ntfstool]] · [[bootbypass]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
