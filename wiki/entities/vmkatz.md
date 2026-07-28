---
title: VMkatz
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/nikaiw__VMkatz.md
updated: 2026-07-28
confidence: medium
---

# VMkatz

Extracts Windows credentials in-place from VM memory snapshots and virtual disks (LSASS, SAM/LSA, cached creds, NTDS.dit), avoiding bulk disk-image exfil that is slow and SOC-visible. Aimed at anti-cheat engineers and defensive researchers in the Information System & Forensics lane. (source: wiki/sources/descriptions/nikaiw__VMkatz.md)

Adjacent to live/dump LSA recovery such as [[kvcforensic]] and offline RAM frameworks such as [[volatility3]]: here the input is VM snapshots / VHD-style disks rather than host `lsass.dmp` alone.

## Links

- Repo: https://github.com/nikaiw/VMkatz

## Related

[[kvcforensic]] · [[kslkatz]] · [[minidump]] · [[volatility3]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
