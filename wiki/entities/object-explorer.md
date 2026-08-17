---
title: Object Explorer
kind: entity
topics: [windows-kernel, reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/zodiacon__ObjectExplorer.md
updated: 2026-08-17
confidence: medium
---

# Object Explorer

Windows GUI (C++/WTL) for browsing and inspecting the kernel **Object Manager** namespace, object types, handles, and per-process object ownership. A bundled kernel driver reads object-manager data; in-memory kernel structures are decoded with PDB debug symbols through a DIA (Debug Interface Access) helper library. Views cover object properties, security descriptors, access-mask decoding, handle enumeration, and zombie-process detection. Aimed at Windows internals researchers, reverse engineers, and security analysts who need deep visibility into kernel objects for debugging, forensics, and anti-cheat research. (source: wiki/sources/descriptions/zodiacon__ObjectExplorer.md)

Complements Object Manager GUIs such as [[winobjex64]] (callback enumeration + namespace edit) and defensive inspection tools such as [[openark]] on the same kernel-object surfaces.

## Links

- Repo: https://github.com/zodiacon/ObjectExplorer

## Related

[[winobjex64]] · [[openark]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]] · [[overviews/anti-cheat]]
