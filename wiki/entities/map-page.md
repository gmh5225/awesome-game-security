---
title: MapPage
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/EBalloon__MapPage.md
updated: 2026-08-25
confidence: medium
---

# MapPage

**MapPage** (EBalloon/MapPage) is a Windows **kernel proof of concept** in C++ that reduces **mapped-driver memory traces** after [[kdmapper]]-based loading. It documents freeing mapped pages with routines such as **`MmFreePagesFromMdl`** and **pool cleanup**, then demonstrates a **data-pointer communication** channel via **`NtUserGetObjectInformation`** with notes on possible alternatives. Primary use case: low-level **anti-cheat bypass** research and **driver-mapping stealth** experiments. README category: cheat / `[NtUserGetObjectInformation]`. (source: wiki/sources/descriptions/EBalloon__MapPage.md)

Sits in the **post-map trace reduction** lane beside [[revert-mapper]], [[nullmap]], and [[clear-driver-traces]], but targets **kdmapper-mapped page footprints** specifically rather than generic PiDDBCache/MmUnloadedDrivers scrubbing alone.

## Links

- Repo: https://github.com/EBalloon/MapPage

## Related

[[kdmapper]] · [[revert-mapper]] · [[nullmap]] · [[known-driver-mappers]] · [[kernel-pool-scanning]] · [[remap]] · [[mm-copy-memory]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
