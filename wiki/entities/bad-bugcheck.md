---
title: Bad-Bugcheck
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__Bad-Bugcheck.md
updated: 2026-08-22
confidence: medium
---

# Bad-Bugcheck

Updated **kernel BSOD visual hack** that renders **Bad Apple** animation frames through the **crash framebuffer path**. Maps and writes the **display framebuffer** directly instead of relying on legacy **BOOTVID VGA** output, and **hooks `KeBugCheckEx`** to intercept crash flow before drawing frames. C/C++ kernel code uses **stb_image** parsing and direct memory-copy routines for frame rendering. (source: wiki/sources/descriptions/NSG650__Bad-Bugcheck.md)

Research lane: **Windows internals** study of **bugcheck hooking**, **display ownership**, and **crash-screen rendering behavior**—for kernel researchers exploring the bugcheck environment, not a production stability tool. Part of the NSG650 bugcheck-research family alongside [[bugcheckhack]], [[bugcheck2linux]], and suppression PoCs such as [[nomore-bugcheck]].

## Links

- Repo: https://github.com/NSG650/Bad-BugCheck-Old

## Related

[[bugcheckhack]] · [[bugcheck2linux]] · [[nomore-bugcheck]] · [[nomore-bugcheck-reloaded]] · [[bugcheck-suppressor]] · [[patchguard]] · [[overviews/windows-kernel]]
