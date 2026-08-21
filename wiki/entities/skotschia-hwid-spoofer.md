---
title: hwid_spoofer (Skotschia)
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Skotschia__hwid_spoofer.md
updated: 2026-08-20
confidence: medium
---

# hwid_spoofer (Skotschia)

**hwid_spoofer** (Skotschia) is a Windows **C++ HWID spoofer** proof of concept targeting **disk serial numbers**, **SMART disk identifiers**, and **SMBIOS-related values**. It ships low-level helper modules and Visual Studio project files for building and testing hardware fingerprint spoofing techniques. The author describes it as an older PoC with significant room for improvement and detection hardening. Primary use case is **educational research** into hardware fingerprint spoofing in anti-cheat evasion contexts. (source: wiki/sources/descriptions/Skotschia__hwid_spoofer.md)

Distinct from the gmh5225 [[hwid-spoofer]] EAC/BattlEye kernel research sample and from kernel-driver samples such as [[hwid--spoofer]] and [[easy-hwid-spoofer]]; this repo focuses on usermode C++ modules for disk/SMART/SMBIOS identifier surfaces rather than a full kernel IOCTL-hook stack.

Sits in the `Cheat > HWID` lane beside disk-serial research such as [[hdd-serial-spoofer]], broader HWID spoofers such as [[hwidspoofer]] and [[hwid]], and Detection:HWID counterparts such as [[hwid-checker-mg]] and [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/Skotschia/hwid_spoofer

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[hdd-serial-spoofer]] · [[hwidspoofer]] · [[hwid]] · [[hwid-spoofer]] · [[easy-hwid-spoofer]] · [[hwid-checker-mg]] · [[uncloaking-raid0-hwid-serials]]
