---
title: nvdrv
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__NVDrv.md
updated: 2026-08-11
confidence: medium
---

# nvdrv

C++ library that exploits NVIDIA's kernel driver stack (**`nvoclock`/`nvlddmkm`**) via crafted IOCTLs to obtain arbitrary **physical memory read/write** from user mode. Provides a [[byovd]] primitive for unsigned driver mapping, kernel patching, or anti-cheat bypass without loading a custom driver. Targets kernel security researchers studying NVIDIA driver vulnerabilities and BYOVD exploitation. (source: wiki/sources/descriptions/gmh5225__NVDrv.md)

README tags the cheat / vulnerable-driver lane as **`nvaudio.sys`** — the same NVIDIA signed-driver backend family abused by manual mapper [[ucmapper]].

## Links

- Repo: https://github.com/gmh5225/NVDrv

## Related

[[byovd]] · [[ucmapper]] · [[physmem-drivers]] · [[loldrivers]] · [[amd-ryzen-master-driver-v17-exploit]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
