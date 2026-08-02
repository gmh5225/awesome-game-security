---
title: Herpaderping
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/jxy-s__herpaderping.md
updated: 2026-08-02
confidence: medium
---

# Herpaderping

Process/file obfuscation PoC and tool for studying how on-disk attribution diverges from mapped executable content. The workflow writes a target PE, maps it as an image section (`NtCreateSection` / `SEC_IMAGE`), creates the process object, overwrites the backing file with decoy bytes while the handle stays open, then creates the initial thread—so process-creation callbacks and on-write scanners that inspect at `IRP_MJ_CLEANUP` see the modified file rather than the image that was mapped. This produces curious behavior in security products and the OS itself. (source: wiki/sources/descriptions/jxy-s__herpaderping.md)

README category: Hide Process/File. Offensive hide/evasion lane adjacent to kernel process-hide samples such as [[blanket]] and file-hide drivers such as [[hide-file]]; defensive counterparts include runtime injection scanners such as [[xmalhunter]] and offline memory forensics such as [[volatility]] / [[volatility3]] (rebuild mapped sections vs on-disk bytes).

## Links

- Repo: https://github.com/jxy-s/herpaderping
- Deep dive: https://jxy-s.github.io/herpaderping/

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]] · [[blanket]] · [[hide-file]] · [[xmalhunter]] · [[volatility]]
