---
title: Packpeek
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/cognis-digital__packpeek.md
updated: 2026-08-16
confidence: medium
---

# Packpeek

Dependency-free static binary fingerprinter in C that detects packing and identifies common runtime packers/protectors (UPX, ASPack, Themida, VMProtect, MPRESS, and others) via documented byte markers plus Shannon entropy scoring for high-randomness compressed or obfuscated regions. Format-agnostic across PE, ELF, Mach-O, and raw firmware blobs; emits structured JSON and pairs with a Python companion for deployable YARA rules and SARIF output for CI and code-scanning workflows. Reads files locally without execution or network calls—defensive triage for malware analysts, reverse engineers, and game security researchers assessing protected or suspicious binaries. (source: wiki/sources/descriptions/cognis-digital__packpeek.md)

Complements browser/desktop packer ID ([[die-engine-web]]), Android APK fingerprinting ([[apkid]]), and YARA plugin lanes ([[hyara]], [[findyara-ida]])—not an unpacker or debugger.

## Links

- Repo: https://github.com/cognis-digital/packpeek

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[die-engine-web]] · [[apkid]] · [[awesome-executable-packing]] · [[vmpunpacker]] · [[hyara]] · [[findyara-ida]]
