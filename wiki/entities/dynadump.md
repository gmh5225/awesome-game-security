---
title: dynadump
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/DerekSelander__dynadump.md
updated: 2026-08-26
confidence: medium
---

# dynadump

**dynadump** is an **Objective-C command-line class-dump tool** for **Apple binaries** and **shared cache** images. It can list loaded dylibs, enumerate Objective-C classes, dump class interfaces, print demangled signatures, and attempt in-place signing operations. The tool relies on **dlopen** with exception-handling strategies to avoid constructor side effects during analysis. It targets **macOS** and **iOS** reverse engineering workflows where analysts need fast runtime-assisted Objective-C introspection. (source: wiki/sources/descriptions/DerekSelander__dynadump.md)

Complements static Apple ObjC/Swift RE tooling such as [[workflow-objc]], [[malimite]], and [[aimachdec]], and dynamic runtime browsers such as [[runtime-viewer]].

## Links

- Repo: https://github.com/DerekSelander/dynadump (README: A runtime ObjC class-dump)

## Related

[[workflow-objc]] · [[malimite]] · [[aimachdec]] · [[runtime-viewer]] · [[ida-ios-helper]] · [[ipapatch]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
