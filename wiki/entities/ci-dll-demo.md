---
title: CiDllDemo
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ido-Moshe-Github__CiDllDemo.md
updated: 2026-08-24
confidence: medium
---

# CiDllDemo

Kernel driver demonstration of calling **ci.dll** APIs to validate executable **Authenticode** signatures from kernel mode. Hooks process-creation notifications, invokes `CiValidateFileObject` and `CiCheckSignedFile`, and inspects returned policy information to extract certificate details. C/C++ Windows driver development with x86 and x64 build support — aimed at security researchers exploring Windows Code Integrity behavior alongside DSE/[[hvci]] enforcement paths. (source: wiki/sources/descriptions/Ido-Moshe-Github__CiDllDemo.md)

Defensive/research-oriented counterpart to CI.dll bypass PoCs such as [[dse-hook]] and [[dse-patcher-2]]: here the focus is invoking and observing CI validation APIs rather than patching `g_CiEnabled` / `g_CiOptions`.

## Links

- Repo: https://github.com/Ido-Moshe-Github/CiDllDemo

## Related

[[dse-hook]] · [[dse-patcher-2]] · [[bootbypass]] · [[wdactools]] · [[mssymbolscollection]] · [[kernel-callbacks]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
