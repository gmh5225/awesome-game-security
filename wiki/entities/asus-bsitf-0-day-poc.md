---
title: asus-bsitf-0-day-poc
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__asus-bsitf-0-day-poc.md
updated: 2026-08-09
confidence: medium
---

# asus-bsitf-0-day-poc

Rust proof-of-concept for **CVE-2026-13585** in ASUS **`bsitf.sys`** / **`AsusBSItf.sys`**. The PoC opens `\\.\bsitf` and uses IOCTL **`0x222808`** to allocate attacker-sized physically contiguous NonPagedPool memory, map it into the calling process with full usermode read/write access, and return both virtual and physical addresses; IOCTL **`0x22280C`** frees the mapping. A test pattern write verifies the usermode-visible mapping. (source: wiki/sources/descriptions/gmh5225__asus-bsitf-0-day-poc.md)

The primitive is an admin-to-kernel escalation useful in [[byovd]] chains: NonPagedPool exhaustion, physical-address disclosure, and on older builds staging executable kernel memory from usermode-mapped pool. Intended for authorized researchers studying vulnerable signed OEM drivers, kernel IOCTL abuse, and Windows privilege escalation. (source: wiki/sources/descriptions/gmh5225__asus-bsitf-0-day-poc.md)

## Links

- Repo: https://github.com/gmh5225/asus-bsitf-0-day-poc

## Related

[[byovd]] · [[kdu]] · [[imxyvimapper]] · [[pdfwkrnl-exploit]] · [[dbk64-vulnerability-driver]] · [[loldrivers]] · [[overviews/windows-kernel]]
