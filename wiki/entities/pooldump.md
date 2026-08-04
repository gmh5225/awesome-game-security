---
title: pooldump
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ioncodes__pooldump.md
updated: 2026-08-04
confidence: medium
---

# pooldump

Windows **kernel pool memory dumper** that scans kernel pool pages to enumerate allocated blocks — pool tags, sizes, and owning drivers — and can dump the contents of specific pool allocations. Targets kernel forensics researchers and anti-cheat analysts hunting kernel-mode artifacts from drivers and rootkits in pool memory, including evidence of manually mapped drivers. (source: wiki/sources/descriptions/ioncodes__pooldump.md)

README positions it for **extracting the DLL that Easy Anti-Cheat manual-maps into the game process** — a concrete manual-map footprint recovery workflow alongside Segment Heap–era [[kernel-pool-scanning]] heuristics and Big Pool diff tooling such as [[kn-diff-pool]].

## Links

- Repo: https://github.com/ioncodes/pooldump (README tag: Extract the DLL that EACs manualmaps into the game process)

## Related

[[kernel-pool-scanning]] · [[kn-diff-pool]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[easy-anti-cheat]] · [[research-rigor]]
