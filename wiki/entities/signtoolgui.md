---
title: SignToolGUI
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/michaelmsonne__SignToolGUI.md
updated: 2026-07-30
confidence: medium
---

# SignToolGUI

Windows Forms GUI wrapper around Microsoft's `signtool.exe`. Supports three signing modes: Windows Certificate Store (thumbprint), PFX file, and Azure Trusted Signing (via Azure.CodeSigning SDK). Includes certificate monitoring, timestamp server management, signing validation, batch multi-file signing, and PowerShell script export for CI/CD integration. (source: wiki/sources/descriptions/michaelmsonne__SignToolGUI.md)

Complements cross-platform Authenticode tooling such as [[osslsigncode]] and low-level digest work such as [[pedigest]]: here the focus is a Windows-native GUI and automation surface over official `signtool`, not signature theft or leaked-cert abuse paths such as [[magic-signer]] or [[sigthief]].

## Links

- Repo: https://github.com/michaelmsonne/SignToolGUI

## Related

[[osslsigncode]] · [[pesign]] · [[pedigest]] · [[sdcm]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
