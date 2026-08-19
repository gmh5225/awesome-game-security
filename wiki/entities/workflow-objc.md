---
title: workflow-objc
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/Vector35__workflow_objc.md
updated: 2026-08-19
confidence: medium
---

# workflow-objc

Objective-C analysis workflow plugin for Binary Ninja (Vector35). Implemented in C++, it extends BN analysis by cleaning up Objective-C call patterns around dynamic dispatch — notably rewriting many `objc_msgSend`-style calls into clearer direct-call representations when message targets can be inferred. Intended for reverse engineers analyzing macOS and iOS binaries that rely heavily on Objective-C runtime behavior. The standalone plugin repo has been migrated into the main Binary Ninja API repository. (source: wiki/sources/descriptions/Vector35__workflow_objc.md)

Complements IDA-side Mach-O / ObjC tooling such as [[aimachdec]], [[ida-ios-helper]], and [[swift-ida]], and Binary Ninja macOS loaders such as [[binja-kc]] in the same Apple static-RE lane.

## Links

- Repo: https://github.com/Vector35/workflow_objc

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[binja-kc]] · [[aimachdec]] · [[binary-ninja-mcp]] · [[binaryninja-pcode]]
