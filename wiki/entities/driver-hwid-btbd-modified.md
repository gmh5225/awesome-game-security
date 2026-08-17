---
title: Driver-HWID-btbd-modified
kind: entity
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-HWID-btbd-modified.md
updated: 2026-08-13
confidence: medium
---

# Driver-HWID-btbd-modified

**Driver-HWID-btbd-modified** is a **BTBD-derived kernel HWID spoofer** fork tuned for **manual mapping** on Windows 1909-era builds. It hooks disk and partition control paths, rewrites serial-related data returned by storage IOCTLs, clears GPT identifiers, updates disk properties, disables SMART failure prediction, and walks **storahci** RAID units to overwrite serial strings deeper in the storage stack — a coordinated storage-identity pipeline rather than a single serial patch. (source: wiki/sources/descriptions/gmh5225__Driver-HWID-btbd-modified.md)

Fork of BTBD storage-hook research; upstream WPP DeviceControl interception technique documented in [[wpp]]. Sits in the `Cheat > HWID` lane beside sibling gmh5225 storage-stack spoof samples such as [[easy-hwid-spoofer]] and [[hwid-kernel-spoofer]], manually mapped driver research such as [[driver-read-write]] and [[driver-session-mapper]], and Detection:HWID counterparts such as [[hwid-checker-mg]] and [[uncloaking-raid0-hwid-serials]].

## Links

- Repo: https://github.com/gmh5225/Driver-HWID-btbd-modified

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[wpp]] · [[easy-hwid-spoofer]] · [[hwid-kernel-spoofer]] · [[hdd-serial-spoofer]] · [[driver-read-write]] · [[driver-session-mapper]] · [[hwid-checker-mg]] · [[uncloaking-raid0-hwid-serials]]
