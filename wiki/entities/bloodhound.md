---
title: Bloodhound
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Skeletal-Group__Bloodhound.md
updated: 2026-08-21
confidence: medium
---

# Bloodhound

Experimental C++ user-mode library for detecting **EPT/NPT-based memory hooks** installed by hypervisors. Combines **vectored exception handling**, CPU intrinsics, and a **VPGATHER-based accessibility** technique to probe whether executable or readable pages are being manipulated through second-level address translation — focusing on stealthier checks for page-state transitions rather than obvious timing-only probes. Presented as a proof of concept for anti-cheat and virtualization security researchers studying hypervisor hook detection. (source: wiki/sources/descriptions/Skeletal-Group__Bloodhound.md)

Complements timing / write-and-compare EPT detectors such as [[ept-hook-detection]] and side-channel probes such as [[ermsb-meme]]; sits opposite stealth Type-2 stacks such as [[ophion]] and [[hypervisor]] that rely on EPT for kernel hooking without guest patches.

## Links

- Repo: https://github.com/Skeletal-Group/Bloodhound

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[ept-hook-detection]] · [[ermsb-meme]] · [[hypervisor-detection]] · [[checkhv-um]] · [[budget-ept]] · [[ophion]] · [[hypervisor]] · [[vpgather]]
