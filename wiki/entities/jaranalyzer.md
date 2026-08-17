---
title: JarAnalyzer
kind: entity
topics: [anti-cheat, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/winzysss__JarAnalyzer.md
updated: 2026-08-17
confidence: medium
---

# JarAnalyzer

Windows desktop tool for detecting Minecraft cheats during **screenshares**. Enumerates JAR files across all drives via fast NTFS Master File Table reads, inspects each class constant pool against a configurable cheat-term blacklist, and flags obfuscated, encrypted, or disguised archives as suspicious without requiring full decompilation. Also searches the recycle bin, probes running Java processes for loaded cheat paths, and unpacks nested JARs up to two levels deep. Built in Java with CFR (decompilation), ASM (bytecode analysis), and JNA (Windows APIs); ships GUI and CLI scanners that export evidence reports in text, JSON, and HTML. (source: wiki/sources/descriptions/winzysss__JarAnalyzer.md)

## Detection workflow

- **Disk sweep:** MFT-walk every NTFS volume for `.jar` files.
- **Static triage:** Constant-pool string matching against blacklist; heuristic flags for obfuscation/encryption/disguise.
- **Live & residual artifacts:** Recycle-bin search; Java process module/path inspection.
- **Nested archives:** Recursive unpack to depth two for embedded cheat JARs.
- **Reporting:** GUI or CLI export to text, JSON, or HTML for staff evidence review.

## Links

- Repo: https://github.com/winzysss/JarAnalyzer

## Related

[[local-anticheat-1-8-9]] · [[phantom-client]] · [[lenrete-mod]] · [[dakotaac]] · [[minecraft-anticheatai]] · [[bytecode-viewer]] · [[echoac-poc]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
