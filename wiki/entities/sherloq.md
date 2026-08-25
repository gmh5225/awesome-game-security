---
title: Sherloq
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/GuidoBartoli__sherloq.md
updated: 2026-08-25
confidence: medium
---

# Sherloq

Open-source **digital image forensics** toolset for detecting image manipulation and tampering. Python-based GUI with analysis modules for **error level analysis (ELA)**, **EXIF metadata** inspection, **frequency domain** analysis, gradient maps, histogram analysis, **cloning detection**, and integration with the **TruFor** neural network detector. Mainly useful for digital forensics researchers and **anti-cheat analysts** investigating image authenticity and **screenshot manipulation**. (source: wiki/sources/descriptions/GuidoBartoli__sherloq.md)

Pairs with AC screenshot capture paths documented in [[anti-screenshot-capture]] and evasion PoCs such as [[screenshot-detection-bypass]] when reviewers need to assess whether submitted or captured frames were edited, spliced, or recompressed after capture.

## Links

- Repo: https://github.com/GuidoBartoli/sherloq

## Related

[[anti-screenshot-capture]] · [[screenshot]] · [[screenshot-detection-bypass]] · [[deadlock-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
