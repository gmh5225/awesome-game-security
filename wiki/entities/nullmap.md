---
title: nullmap
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__nullmap.md
updated: 2026-08-08
confidence: medium
---

# nullmap

Windows driver mapper that manually maps an unsigned kernel driver, runs its entry point, then **erases mapping traces**: zeroes PE headers, removes pool allocations, and unlinks references so manual-map forensics find minimal leftover evidence. (source: wiki/sources/descriptions/gmh5225__nullmap.md)

README tags the project under the `Afd.sys` lane (gmh5225). Useful for studying anti-forensic driver-mapping cleanup and how post-execution artifact removal interacts with pool walks, PiDDBCache/MmUnloadedDrivers checks, and AC memory scanners—not a production evasion tool.

## Links

- Repo: https://github.com/gmh5225/nullmap

## Related

[[revert-mapper]] · [[saturn-mapper]] · [[kdmapper-rs]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[afd-irp-call-dispatch]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
