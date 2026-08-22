---
title: NoMoreBugCheck Reloaded
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__NoMoreBugCheckReloaded.md
updated: 2026-08-22
confidence: medium
---

# NoMoreBugCheck Reloaded

**UEFI-based no-BSOD** proof of concept that **patches the Windows kernel during boot** instead of loading a runtime driver. An **EFI-stage loader** alters crash-handling behavior early in startup—moving bugcheck interception from a conventional kernel driver into the firmware/boot chain. C/C++ components combine export lookup, pattern search, and low-level memory overwrite helpers across kernel and firmware code. (source: wiki/sources/descriptions/NSG650__NoMoreBugCheckReloaded.md)

Research lane: **firmware-to-kernel security**—early boot patching and **bugcheck interception** before normal OS driver-load telemetry. Successor/reloaded variant in the NSG650 bugcheck-research family (alongside runtime-driver approaches such as [[nomore-bugcheck]] and visual bugcheck hacks).

## Links

- Repo: https://github.com/NSG650/NoMoreBugCheckReloaded

## Related

[[nomore-bugcheck]] · [[bugcheck-suppressor]] · [[bootlicker]] · [[patchguard]] · [[ntdoom]] · [[overviews/windows-kernel]]
