---
title: Bad-BugCheck Old
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__Bad-BugCheck-Old.md
updated: 2026-08-22
confidence: medium
---

# Bad-BugCheck Old

Early **Windows kernel driver** proof of concept that plays **animated frames** on a **forced crash (BSOD) screen**. Uses **Bootvid** routines such as **`VidBitBlt`** for **VGA-style rendering**, loads frames from kernel mode, then **triggers a bugcheck after playback**. C code implements low-level frame loading and display handling. (source: wiki/sources/descriptions/NSG650__Bad-BugCheck-Old.md)

Research lane: **Windows kernel graphics experimentation** around **BSOD behavior** and legacy **BOOTVID** crash-screen output—precursor to the updated [[bad-bugcheck]] framebuffer approach. Part of the NSG650 bugcheck-research family alongside [[bugcheckhack]], [[bugcheck2linux]], and suppression PoCs such as [[nomore-bugcheck]].

## Links

- Repo: https://github.com/NSG650/Bad-BugCheck-Old

## Related

[[bad-bugcheck]] · [[kmdfmandelcheck]] · [[bugcheckhack]] · [[bugcheck2linux]] · [[nomore-bugcheck]] · [[nomore-bugcheck-reloaded]] · [[bugcheck-suppressor]] · [[overviews/windows-kernel]]
