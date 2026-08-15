---
title: usbsn (ekknod)
kind: entity
topics: [game-hacking, mobile-security, windows-kernel]
sources:
  - wiki/sources/descriptions/ekknod__usbsn.md
updated: 2026-08-15
confidence: medium
---

# usbsn (ekknod)

**usbsn** is a **USB serial number changer** that rewrites peripheral serial identifiers at the host. It requires **root** privileges and is implemented in **C++** and **Java**. Anti-cheat and mobile-integrity stacks sometimes fingerprint USB device serials alongside disk, NIC, and SMBIOS surfaces; this tool targets that peripheral-identity lane on low-level Windows, Linux, and Android hosts. (source: wiki/sources/descriptions/ekknod__usbsn.md)

Curated under **Some Tricks / Android** and adjacent HWID-spoof research beside kernel disk/NIC spoofers such as [[easy-hwid-spoofer]] and [[hdd-serial-spoofer]].

## Links

- Repo: https://github.com/ekknod/usbsn

## Related

[[overviews/game-hacking]] · [[overviews/mobile-security]] · [[easy-hwid-spoofer]] · [[hdd-serial-spoofer]] · [[hwidspoofer]] · [[vm]]
