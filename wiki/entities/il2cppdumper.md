---
title: IL2CPPDumper
kind: entity
topics: [game-engine, mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/kp7742__IL2CPPDumper.md
updated: 2026-08-01
confidence: medium
---

# IL2CPPDumper

C/C++ [[il2cpp]] static dump tool for **Android**: extracts type/method metadata from Unity mobile titles by pairing `libil2cpp.so` with `global-metadata.dat` (or equivalent) to produce analyst-friendly output (`dump.cs`, headers, `script.json`) for IDA/Ghidra import. README lane `[Il2Cpp Dump for Android Platform]`; also tagged for driver development, networking, and modding research. (source: wiki/sources/descriptions/kp7742__IL2CPPDumper.md)

From the same author as [[ue4dumper]] and [[memdumper]]; complements APK diff tooling such as [[il2cpp-spy]] and live Frida dumps via [[frida-il2cpp-bridge]] on the mobile Unity explorer lane.

## Links

- Repo: https://github.com/kp7742/IL2CPPDumper

## Related

[[il2cpp]] · [[ue4dumper]] · [[memdumper]] · [[il2cpp-spy]] · [[frida-il2cpp-bridge]] · [[android-il2cpp-modspeed]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
