---
title: simplify
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/CalebFenton__simplify.md
updated: 2026-08-29
confidence: medium
---

# simplify

**simplify** (CalebFenton) is a Java-based **Android deobfuscation framework** that simplifies **Dalvik bytecode** by virtually executing app logic. It includes a VM component, optimization passes, and demo materials for analysis workflows. The optimizer applies transformations such as **constant propagation**, **dead code removal**, and **reflection cleanup** to make recovered code easier to understand. It targets reverse engineers and mobile security researchers analyzing obfuscated Android applications. (source: wiki/sources/descriptions/CalebFenton__simplify.md)

Complements DEX→Java decompilers such as [[jadx]], smali-layer editors such as [[dalvikus]], and Python Dalvik emulators such as [[dalivm]] when obfuscated control flow or reflection must be reduced before static reading. Pairs with JVM bytecode deobfuscators such as [[deobfuscator]] and DEX search libraries such as [[dexkit-android]] in broader mobile RE pipelines.

## Links

- Repo: https://github.com/CalebFenton/simplify

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[jadx]] · [[dalvikus]] · [[dalivm]] · [[deobfuscator]] · [[dexkit-android]] · [[apktool]]
