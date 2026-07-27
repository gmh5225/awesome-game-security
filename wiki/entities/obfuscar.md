---
title: Obfuscar
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/obfuscar__obfuscar.md
updated: 2026-07-27
confidence: medium
---

# Obfuscar

Open-source, minimalistic .NET assembly obfuscator (C#) that protects code and secrets from casual reverse engineering. Renames methods, properties, events, fields, types, and namespaces with massive overloading so identifiers collapse to a small set distinguished mainly by signature. Also supports string hiding, selective skip/filter rules, BAML handling for WPF resources, and shipping as a NuGet tool or .NET global tool. Built on low-level metadata and PE APIs for .NET and Mono developers shipping protected binaries. (source: wiki/sources/descriptions/obfuscar__obfuscar.md)

Useful as a managed/CLR Obfuscation Engine reference alongside native protectors such as [[wprotect]], [[alcatraz]], and dual-mode [[vxlang-page]]—not a commercial virtualizer or unpacker.

## Links

- Repo: https://github.com/obfuscar/obfuscar

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[wprotect]] · [[alcatraz]] · [[vxlang-page]] · [[obfcoder]] · [[obfusk8]]
