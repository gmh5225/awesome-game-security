---
title: Kernel Anti-Cheat
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Kernel_Anti-Cheat.md
updated: 2026-08-12
confidence: medium
---

# Kernel Anti-Cheat

Experimental kernel anti-cheat driver from gmh5225 that combines several telemetry paths instead of relying on a single detector. Separate source modules cover NMI capture, thread scanning, pool analysis, hypervisor checks, and trace artifacts; the README tags the project under `[NMI]`. (source: wiki/sources/descriptions/gmh5225__Kernel_Anti-Cheat.md)

## Detection modules

| Module | Technique |
|--------|-----------|
| **NMI stack walk** | `HalSendNMI` + `RtlCaptureStackBackTrace` for cross-CPU stack forensics |
| **System threads** | Start-address scanning for threads whose entry points fall outside loaded driver images |
| **Big pool** | Large-pool inspection for manual-map footprints without matching modules |
| **Boot UUID** | Boot-time UUID collection for host identity telemetry |
| **Hypervisor** | Simple hypervisor presence checks |
| **Mapper residue** | `PiDDBCacheTable` enumeration for kdmapper / drvmap load timestamps |

The code is explicit about possible false positives and reads as a **research sandbox** for defensive engineers studying how kernel AC prototypes can fuse stack forensics, module-range validation, and mapper artifact checks in one driver — not a production AC product.

## Links

- Repo: https://github.com/gmh5225/Kernel_Anti-Cheat

## Related

[[kernel-pool-scanning]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[nmi-nmi-callback]] · [[known-driver-mappers]] · [[darken-anticheat]] · [[deep-learning-anti-cheat-csgo]] · [[ghostbusters]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
