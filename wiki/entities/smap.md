---
title: smap
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/btbd__smap.md
updated: 2026-08-17
confidence: medium
---

# smap

**smap** (btbd/smap; Scatter Manual Map) is a **Windows kernel-mode shellcode mapper** in C that loads position-independent shellcode into kernel memory using a **vulnerable signed driver**. Unlike full driver mappers such as [[umap]] or [[kdmapper]], it operates on **raw shellcode** rather than PE images — copying payload bytes to kernel pool memory and executing them via the vulnerable driver's arbitrary execution primitive. That design avoids PE section/import/reloc handling and can reduce PE-signature-based detection of mapped kernel code. Aimed at kernel security researchers studying shellcode-based kernel payloads and detection evasion. (source: wiki/sources/descriptions/btbd__smap.md)

Sits in the BTBD manual-map research lane beside [[umap]], [[known-driver-mappers]], and [[wpp]].

## Links

- Repo: https://github.com/btbd/smap

## Related

[[umap]] · [[kdmapper]] · [[known-driver-mappers]] · [[byovd]] · [[wpp]] · [[kernel-pool-scanning]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
