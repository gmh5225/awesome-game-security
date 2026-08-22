---
title: RuntimeViewer
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/MxIris-Reverse-Engineering__RuntimeViewer.md
updated: 2026-08-22
confidence: medium
---

# RuntimeViewer

**Objective-C Runtime Viewer for macOS and iOS** — Apple-platform runtime inspection application that explores Objective-C and Swift metadata from loaded binaries and frameworks. Built primarily in Swift with Objective-C components; includes communication layers for local or networked runtime access. Core features: interface browsing, syntax-highlighted views, export of discovered interfaces, framework loading, and work-in-progress code injection support. Targets reverse engineering, dynamic analysis, and runtime exploration on macOS and related Apple platforms. (source: wiki/sources/descriptions/MxIris-Reverse-Engineering__RuntimeViewer.md)

Complements static Apple ObjC/Swift RE tooling such as [[workflow-objc]], [[aimachdec]], and [[ida-ios-helper]], and dynamic instrumentation via [[frida]] / [[fridascript]] in the same macOS/iOS runtime lane. Same maintainer org as [[ida-mcp-server]].

## Links

- Repo: https://github.com/MxIris-Reverse-Engineering/RuntimeViewer

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[workflow-objc]] · [[aimachdec]] · [[ida-ios-helper]] · [[fridascript]] · [[xpc-tracer]] · [[ida-mcp-server]]
