---
title: driver-dll-finder
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/armvirus__DriverDllFInder.md
updated: 2026-08-18
confidence: medium
---

# driver-dll-finder

Windows user-mode **PE section scanner** that locates candidate driver or DLL modules with oversized sections large enough to host another image. It enumerates files under `System32` or `System32\drivers`, parses PE headers, and compares a chosen section size against the target image size. For driver targets it skips currently loaded drivers by querying active services, narrowing results to on-disk files that remain replaceable. Intended for low-level Windows and anti-cheat research workflows where **section-based mapping** hosts must be identified quickly — a recon step before mappers such as [[sinmapper]] overlay a payload into signed-driver image bounds. (source: wiki/sources/descriptions/armvirus__DriverDllFInder.md)

README tags the project under **Find Driver Useless Memory** (armvirus).

## Links

- Repo: https://github.com/armvirus/DriverDllFInder

## Related

[[sinmapper]] · [[kdmapper]] · [[known-driver-mappers]] · [[kernel-codecave-poc]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
