---
title: Android ClassyShark
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/google__android-classyshark.md
updated: 2026-08-07
confidence: medium
---

# Android ClassyShark

Google **ClassyShark** is a standalone Java GUI for inspecting Android and Java bytecode without full decompilation. It opens APK, DEX, AAR, and `.class` inputs and surfaces class hierarchies, method counts, field layouts, dependency graphs, and multidex structure in an interactive viewer—useful for rapid triage of app complexity, third-party SDK footprint, and native-library dependencies before deeper RE. (source: wiki/sources/descriptions/google__android-classyshark.md)

Complements decode/decompile lanes ([[apktool]], [[jadx]], [[dex2jar]]), packer ID ([[apkid]]), and unified assessment CLIs such as [[nightowl]]; peers multi-format decompilers like [[garlic]] for quick structural overview rather than recovered source.

## Links

- Repo: https://github.com/google/android-classyshark

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool]] · [[jadx]] · [[apkid]] · [[nightowl]] · [[garlic]] · [[dex2jar]]
