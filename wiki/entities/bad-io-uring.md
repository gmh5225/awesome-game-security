---
title: bad_io_uring
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Markakd__bad_io_uring.md
updated: 2026-08-23
confidence: medium
---

# bad_io_uring

**Android kernel exploitation proof of concept** (Markakd) focused on **io_uring-related privilege escalation**. Implemented mainly in **C** with **Android NDK** build scripts and **separate exploit variants** for different device and kernel targets. Includes helper tooling to **unpack boot images** and **extract kernel symbols** so the exploit can be adapted to matching firmware builds. Intended for **kernel security research**, **exploit reproduction**, and **root-cause study** in authorized mobile test environments—not a maintained universal root framework. (source: wiki/sources/descriptions/Markakd__bad_io_uring.md)

Complements structured Android kernel exploitation training such as [[android-kernel-exploitation]], CVE PoC collections such as [[android-kernel-cve-pocs]], and other Pixel 6 root research such as [[dirtypiperoot]]. Linux io_uring post-exploitation tooling such as [[ring-reaper]] shares the io_uring syscall surface but targets desktop post-exploit I/O rather than Android privesc chains.

## Links

- Repo: https://github.com/Markakd/bad_io_uring [Root for Pixel 6]

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[android-kernel-exploitation]] · [[android-kernel-cve-pocs]] · [[dirtypiperoot]] · [[ring-reaper]]
