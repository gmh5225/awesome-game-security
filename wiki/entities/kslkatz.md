---
title: KslKatz
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/vergamota__KslKatz.md
updated: 2026-07-19
confidence: medium
---

# KslKatz

Kernel-mode credential dumper that reads LSASS process memory through a vulnerable Microsoft Defender driver (`KslD.sys`) to extract WDigest plaintext passwords and encrypted LSA credentials, bypassing PPL and antivirus protections. (source: wiki/sources/descriptions/vergamota__KslKatz.md)

Illustrates the [[byovd]] credential-extraction lane: a signed OS-component driver is abused for cross-process kernel read of a protected process, adjacent to DSE/PPL research such as [[kvc]] and post-dump LSA recovery such as [[kvcforensic]].

## Links

- Repo: https://github.com/vergamota/KslKatz

## Related

[[byovd]] · [[kvc]] · [[kvcforensic]] · [[lsass-extend-mapper]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
