---
title: bagbak
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/ChiChou__bagbak.md
updated: 2026-08-27
confidence: medium
---

# bagbak

Node.js and TypeScript CLI that uses Frida to decrypt and dump iOS applications into IPA files from jailbroken devices. A Frida agent handles runtime decryption; the tool supports app extensions and embedded frameworks, with USB and remote device connections. (source: wiki/sources/descriptions/ChiChou__bagbak.md)

Aimed at iOS security researchers performing app decryption, binary analysis, and reverse engineering on jailbroken hardware. README notes `bagbak@5` requires Frida 17; the project is marked deprecated in the curated list.

Complements sibling ChiChou tooling [[grapefruit]] and [[vscode-frida]] as a focused IPA acquisition lane before static analysis.

## Links

- Repo: https://github.com/ChiChou/bagbak

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[frida]] · [[grapefruit]] · [[vscode-frida]] · [[frida-ide]]
