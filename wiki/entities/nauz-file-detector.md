---
title: Nauz File Detector
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/horsicq__Nauz-File-Detector.md
updated: 2026-08-05
confidence: medium
---

# Nauz File Detector

**Nauz File Detector (NFD)** is a standalone signature-based tool for identifying packers, compilers, protectors, linkers, and installers used to build executable files. Scans PE, ELF, Mach-O, and other binary formats to detect hundreds of known toolchains—MSVC, GCC, Clang, UPX, ASPack, Themida, VMProtect, and more. Ships as a C++/Qt application with both GUI and command-line interfaces for malware analysts and reverse engineers performing initial binary triage. (source: wiki/sources/descriptions/horsicq__Nauz-File-Detector.md)

Upstream to [[nfdx64dbg]], which embeds the same NFD engine as an [[x64dbg]] plugin tab. Complements emulation-based unpack lanes such as [[xvolkolak]] (same horsicq ecosystem) and static triage peers like Detect It Easy ([[die-engine-web]]).

## Links

- Repo: https://github.com/horsicq/Nauz-File-Detector

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[nfdx64dbg]] · [[x64dbg]] · [[xvolkolak]] · [[die-engine-web]]
