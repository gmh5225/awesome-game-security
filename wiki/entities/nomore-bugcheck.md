---
title: NoMoreBugCheck
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__NoMoreBugCheck.md
updated: 2026-08-22
confidence: medium
---

# NoMoreBugCheck

Windows **kernel driver** proof of concept that **suppresses standard BSOD handling** by **patching `KeBugCheckEx`**. The driver overwrites crash-entry behavior so fatal errors do not immediately enter the normal bugcheck path, with **direct code patching** and **restoration logic** implemented in C/C++ for kernel mode. (source: wiki/sources/descriptions/NSG650__NoMoreBugCheck.md)

Research lane: **Windows internals** and **kernel-hooking experiments** that demonstrate the risks of bypassing crash-safety mechanisms—not a production stability tool. Predecessor in the NSG650 bugcheck-research family; successor [[nomore-bugcheck-reloaded]] moves the same goal into a UEFI boot-stage loader.

## Links

- Repo: https://github.com/NSG650/NoMoreBugCheck

## Related

[[nomore-bugcheck-reloaded]] · [[bugcheck-suppressor]] · [[patchguard]] · [[overviews/windows-kernel]]
