---
title: PolyEngine
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/LongWayHomie__PolyEngine.md
updated: 2026-08-23
confidence: medium
---

# PolyEngine

**LongWayHomie** polymorphic **PE packer/crypter engine** with per-build mutation: junk code insertion, instruction substitution, **XTEA** encryption, **RunPE** process hollowing, stack spoofing, module stomping, and **Hell's Gate** syscall invocation. Targets CTF and Windows low-level security education—layered obfuscation with in-memory execution rather than shipping as a commercial AC product. Listed under Anti Cheat → Binary Packer. (source: wiki/sources/descriptions/LongWayHomie__PolyEngine.md)

Useful as an evasive PE packer/crypter reference alongside [[atom-pe-packer]], [[hm-pe-packer]], and [[windows-process-injection]]—not a full unpacker or turnkey protector.

## Links

- Repo: https://github.com/LongWayHomie/PolyEngine

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[atom-pe-packer]] · [[hm-pe-packer]] · [[pe-packer]] · [[exe-packer]] · [[windows-process-injection]] · [[rs-ldr]] · [[polymorphic-engine]]
