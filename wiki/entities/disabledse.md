---
title: DisableDSE
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__DisableDSE.md
updated: 2026-08-14
confidence: medium
---

# DisableDSE

Windows Driver Signature Enforcement (DSE) bypass research tool that disables enforcement by patching the kernel image-validation chain. Targets the **`SeValidateImageHeader`** call path through **`MiValidateSectionCreate`** and **`MiValidateSectionSigningPolicy`** to allow loading unsigned kernel drivers. (source: wiki/sources/descriptions/gmh5225__DisableDSE.md)

Adjacent to CI.dll globals/hook PoCs such as [[dse-hook]] and [[dse-patcher-2]], `SeValidateImageData`/header patch mappers such as [[pdfwkrnl-mapper]], and `SeCiCallbacks`/`CiInitialize` loaders such as [[kdp-compatible-driver-loader]] — here the focus is patching section-create/signing-policy validation in the kernel path rather than `g_CiOptions` writes or CI.dll hooks.

## Links

- Repo: https://github.com/gmh5225/DisableDSE

## Related

[[dse-hook]] · [[dse-patcher-2]] · [[pdfwkrnl-mapper]] · [[kdp-compatible-driver-loader]] · [[kvc]] · [[upgdsed]] · [[pastdse]] · [[byovd]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
