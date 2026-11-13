---
title: INF Studio
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/zodiacon__InfStudio.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: high
---

# INF Studio

**INF Studio** (zodiacon/InfStudio) is a native Windows desktop application for viewing and editing driver **installation INF** files used when packaging and installing kernel-mode and user-mode drivers. (source: wiki/sources/descriptions/zodiacon__InfStudio.md)

## Capabilities

- **Scintilla** text editor (Lexilla) with a custom INF syntax lexer; find/replace, dark mode, and ANSI / UTF-8 / UTF-16 encoding handling.
- Navigable **section tree** for `Version`, `Manufacturer` / `Models`, `AddReg`, `CopyFiles`, and related INF sections.
- Parsing through Windows **SetupAPI** via the shared **InfCore** library (C++20, **WTL**).
- Integrated **WDK infverif** runs for Windows Driver and WHQL validation.
- Starter templates for common **KMDF**, **UMDF**, USB, and virtual-device scenarios.
- **DumpInf** console utility lists version metadata and section names.

## Use cases

Driver developers, reverse engineers, and security researchers use INF Studio to inspect or author Windows driver packages—clarifying which binaries are copied, how services register, and whether installation manifests pass formal verification before lab deployment. It sits in the same zodiacon **Windows Kernel Explorer** tooling family as [[dbgprint]], [[poolmonxv3]], and [[object-explorer]].

## Links

- Repo: https://github.com/zodiacon/InfStudio (README: GUI editor and section tree viewer for Windows driver installation INF files, with Scintilla editing, templates, and infverif integration)

## Related

[[driver-trust-boundaries]] · [[driver-base]] · [[dbgprint]] · [[poolmonxv3]] · [[object-explorer]] · [[overviews/windows-kernel]] · [[research-rigor]]
