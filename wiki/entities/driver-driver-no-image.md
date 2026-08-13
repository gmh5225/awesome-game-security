---
title: Driver-DriverNoImage
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-DriverNoImage.md
updated: 2026-08-13
confidence: medium
---

# Driver-DriverNoImage

Kernel-driver proof of concept that executes custom shellcode through **other drivers** instead of exposing a normal standalone driver image path. Designed to inject shellcode into an existing driver to bypass signature-related constraints; the tree includes dedicated shellcode files, inline hook helpers, and patch modules rather than a conventional device interface only. (source: wiki/sources/descriptions/gmh5225__Driver-DriverNoImage.md)

Implementation patches existing dispatch routines such as **NTFS driver handlers**, temporarily disables write protection to install inline jumps, and preserves trampolines so the original path can still be called or restored on unload.

Mainly useful for Windows kernel researchers studying driver dispatch hijacking, shellcode-based execution inside existing drivers, and techniques for reducing the visibility of custom kernel payloads.

README tag: **Hijack Driver**.

## Links

- Repo: https://github.com/gmh5225/Driver-DriverNoImage

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[driver-read-write]] · [[boom]] · [[kernel-codecave-poc]] · [[windows-kernel-pagehook]] · [[driver-kdtour]] · [[cfb]] · [[research-rigor]]
