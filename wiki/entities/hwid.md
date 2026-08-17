---
title: hwid
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/btbd__hwid.md
updated: 2026-08-17
confidence: medium
---

# hwid

**hwid** (btbd/hwid) is an upstream **Windows kernel HWID spoofer** that modifies disk, volume, NIC, ARP, SMBIOS, boot, and GPU identifiers. A kernel driver intercepts and rewrites **IOCTL responses** to return spoofed hardware serial numbers and identifiers; a user-mode component handles **registry keys** and common **tracking files**. Tested on Windows 10 builds **1507 through 1903** on **x64**; **NVME-specific IOCTLs are not handled**. Aimed at game-security researchers studying hardware fingerprinting and HWID-based ban evasion. (source: wiki/sources/descriptions/btbd__hwid.md)

Upstream baseline for BTBD-derived forks such as [[driver-hwid-btbd-modified]] and storage-hook research such as [[wpp]]. Sits in the `Cheat > HWID` lane beside [[easy-hwid-spoofer]], [[hwid-kernel-spoofer]], and [[hdd-serial-spoofer]], with Detection:HWID counterparts such as [[hwid-checker-mg]] and [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/btbd/hwid

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[driver-hwid-btbd-modified]] · [[wpp]] · [[easy-hwid-spoofer]] · [[hwid-kernel-spoofer]] · [[hdd-serial-spoofer]] · [[hwid-checker-mg]] · [[uncloaking-raid0-hwid-serials]]
