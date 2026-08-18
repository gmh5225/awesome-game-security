---
title: apk.sh
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/ax__apk.sh.md
updated: 2026-08-18
confidence: medium
---

# apk.sh

Bash workflow script that automates common Android APK reverse-engineering tasks: pull installed apps from a device, decode and rebuild with [[apktool]], patch smali/resources, inject a [[frida]] gadget for runtime instrumentation, merge app bundles and split APKs into one installable package, and re-sign with apksigner. Supports arm, arm64, x86, and x86_64 targets without requiring a rooted device. (source: wiki/sources/descriptions/ax__apk.sh.md)

Useful for mobile security researchers who want a single CLI pipeline from device pull through decode, gadget injection, and signed reinstall — complementary to agent MCP wrappers such as [[apktool-mcp-server]] and static analyzers such as [[glass]] and [[jadx]].

## Links

- Repo: https://github.com/ax/apk.sh

## Related

[[apktool]] · [[apksigner]] · [[frida]] · [[jadx]] · [[apktool-mcp-server]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
