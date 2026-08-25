---
title: flutter-re-demo
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/Guardsquare__flutter-re-demo.md
updated: 2026-08-25
confidence: medium
---

# flutter-re-demo

Research reproduction kit for reverse engineering **Flutter mobile applications**. Python tooling for IDA Pro parses reFlutter or DWARF debug output to rename Dart functions, import Flutter VM memory dumps, create Dart object structures, add cross-references, and improve decompilation via stack-pointer patching and microcode hooks. A Frida script captures runtime Flutter memory; sample obfuscated and non-obfuscated APKs from a Flutter game support hands-on testing of static and dynamic analysis against Dart decompilation and obfuscation limits. (source: wiki/sources/descriptions/Guardsquare__flutter-re-demo.md)

From Guardsquare alongside [[proguard]]; complements static AOT snapshot recovery via [[unflutter]] and mobile dynamic instrumentation via [[frida]].

## Links

- Repo: https://github.com/Guardsquare/flutter-re-demo

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[proguard]] · [[unflutter]] · [[frida]] · [[frida-ide]] · [[obfu-de-scate]] · [[jadx]] · [[apktool]]
