---
title: HWID-Kernel-Spoofer
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__HWID-Kernel-Spoofer.md
updated: 2026-08-12
confidence: medium
---

# HWID-Kernel-Spoofer

**HWID-Kernel-Spoofer** is a **kernel-mode HWID spoofer** research repo that modifies hardware identifiers through **driver dispatch hook interception**. It spoofs disk serial numbers, MAC addresses, SMBIOS data, and GPU identifiers by hooking `IRP_MJ_DEVICE_CONTROL` handlers of storage and network drivers. (source: wiki/sources/descriptions/gmh5225__HWID-Kernel-Spoofer.md)

Sits in the `Cheat > HWID` lane beside sibling gmh5225 kernel-hook samples such as [[hwid-spoofer-eac-be]], [[hwid-spoofer]], [[precision-spoofer-cpp]], and [[hwid-permanent-hwid-spoofer]], general Windows spoofers such as [[hwidspoofer]], and Detection:HWID counterparts such as [[hwid-checker-mg]] and [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/gmh5225/HWID-Kernel-Spoofer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[hwid-spoofer-eac-be]] · [[hwid-spoofer]] · [[precision-spoofer-cpp]] · [[hwid-permanent-hwid-spoofer]] · [[hwidspoofer]] · [[hdd-serial-spoofer]] · [[hwid-checker-mg]]
