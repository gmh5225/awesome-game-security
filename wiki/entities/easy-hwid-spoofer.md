---
title: EASY-HWID-SPOOFER
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__EASY-HWID-SPOOFER.md
updated: 2026-08-13
confidence: medium
---

# EASY-HWID-SPOOFER

**EASY-HWID-SPOOFER** is a **kernel-mode HWID spoofer** research repo that modifies disk, NIC, GPU, and SMBIOS serial identifiers. It hooks driver dispatch functions and directly patches physical memory to alter hardware fingerprints reported to anti-cheat systems; tested on Windows 10. (source: wiki/sources/descriptions/gmh5225__EASY-HWID-SPOOFER.md)

Sits in the `Cheat > HWID` lane beside sibling gmh5225 kernel-hook samples such as [[hwid-kernel-spoofer]], [[hwid-spoofer-eac-be]], [[hwid-spoofer]], and [[precision-spoofer-cpp]], general Windows spoofers such as [[hwidspoofer]], and Detection:HWID counterparts such as [[hwid-checker-mg]] and [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/gmh5225/EASY-HWID-SPOOFER

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hwid-kernel-spoofer]] · [[hwid-spoofer-eac-be]] · [[hwid-spoofer]] · [[precision-spoofer-cpp]] · [[hwidspoofer]] · [[hdd-serial-spoofer]] · [[hwid-checker-mg]]
