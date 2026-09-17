---
title: DbgPrint
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/zodiacon__DbgPrint.md
updated: 2026-09-17
confidence: medium
---

# DbgPrint

Windows desktop utility (C++/WTL) for viewing **OutputDebugString** and kernel **DbgPrint/DbgPrintEx** output in real time via ETW, without installing a custom driver or editing registry debug settings. (source: wiki/sources/descriptions/zodiacon__DbgPrint.md)

## Capabilities

- Captures user-mode `OutputDebugString`, including .NET `Debug.Write`/`Trace.Write`, and kernel `DbgPrint`/`DbgPrintEx` streams.
- Filtering, highlighting, log persistence, and on-demand enablement of all kernel debug components without registry edits or reboots.
- x86, x64, and ARM64 builds; monitors the current session or Session 0.

## Use cases

Aimed at Windows developers, security researchers, and reverse engineers who need to monitor application and driver debug traces during AC or driver analysis. Complements [[dbgviewex]] and schema-oriented ETW browsers such as [[etw-explorer]] by focusing on live debug-string capture from the same author family as [[object-explorer]].

## Links

- Repo: https://github.com/zodiacon/DbgPrint

## Related

[[dbgviewex]] · [[object-explorer]] · [[etw-explorer]] · [[openprocmon]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
