---
title: Disabling Hyper-V
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__Disabling-Hyper-V.md
updated: 2026-08-14
confidence: medium
---

# Disabling Hyper-V

Guide for **completely disabling Hyper-V on Windows 10**, including Device Guard and Credential Guard. Documents using Microsoft's **Device Guard and Credential Guard hardware readiness tool** to turn off [[hvci]] and other virtualization-based security features that otherwise block full Hyper-V removal. README category `[Disable Hyper-V]`. (source: wiki/sources/descriptions/gmh5225__Disabling-Hyper-V.md)

Useful for kernel research labs that need a non-hypervisor host—contrasts with HVCI bypass PoCs such as [[zero-hvci]] and Hyper-V offensive frameworks such as [[voyager]] that assume the hypervisor stack remains active.

## Links

- Repo: https://github.com/gmh5225/Disabling-Hyper-V

## Related

[[hvci]] · [[zero-hvci]] · [[bootbypass]] · [[voyager]] · [[go-detection-hyper-v]] · [[overviews/windows-kernel]]
