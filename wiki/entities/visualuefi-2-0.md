---
title: VisualUEFI-2.0
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Shtan7__VisualUEFI-2.0.md
updated: 2026-08-21
confidence: medium
---

# VisualUEFI-2.0

**VisualUEFI-style UEFI development setup** configured for **Clang** and **DWARF** debugging information. Combines C and C++ UEFI sample code with **EDK2-related projects** and **Visual Studio** tooling to build firmware applications. The workflow targets **source-level debugging on Windows** through **VMware** and remote **GDB** frontends such as **CLion**. (source: wiki/sources/descriptions/Shtan7__VisualUEFI-2.0.md)

Useful for **firmware developers** and **security researchers** studying UEFI internals and boot-time behavior—complements streamlined Visual Studio scaffolds such as [[simpleuefi]] and minimal CMake builds such as [[eficmake]], and pairs with static UEFI RE plugins such as [[efixplorer]] and [[ida-efiutils]] when iterating from build to analysis.

## Links

- Repo: https://github.com/Shtan7/VisualUEFI-2.0

## Related

[[simpleuefi]] · [[eficmake]] · [[efixplorer]] · [[ida-efiutils]] · [[uefi-bootkit]] · [[uefi-bootloader]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
