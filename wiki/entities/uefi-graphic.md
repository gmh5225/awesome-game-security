---
title: UEFI-Graphic
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/Oliver-1-1__UEFI-Graphic.md
updated: 2026-08-22
confidence: medium
---

# UEFI-Graphic

**UEFI-Graphic** (Oliver-1-1) is a **C++ UEFI graphics framework** that simplifies drawing in **pre-boot environments**. It wraps low-level UEFI protocols and **framebuffer** handling behind reusable classes for screens, colors, text, and basic shapes. The codebase includes support goals and implementations for **mouse input** and simple **file operations**, built with a **VisualUefi** workflow. Targets **firmware developers** and **low-level security researchers** who need custom graphical tools before the operating system loads. (source: wiki/sources/descriptions/Oliver-1-1__UEFI-Graphic.md)

Complements VisualUefi UEFI dev scaffolds such as [[simpleuefi]], [[easyuefi]], and [[visualuefi-2-0]], and pairs with integrated EFI cheat frameworks such as [[advanced-efi-driver-with-gdi-and-kernel-mouse-input]] when building pre-OS graphical tooling for security research.

## Links

- Repo: https://github.com/Oliver-1-1/UEFI-Graphic

## Related

[[simpleuefi]] · [[easyuefi]] · [[visualuefi-2-0]] · [[advanced-efi-driver-with-gdi-and-kernel-mouse-input]] · [[uefi-bootkit]] · [[eficmake]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
