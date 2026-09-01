---
title: windows-runtime-attestation-report
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/CodeMaxx__windows-runtime-attestation-report.md
  - wiki/sources/README-categories.md
updated: 2026-09-01
confidence: medium
---

# windows-runtime-attestation-report

C++ console sample (Visual Studio 2022; Windows SDK 10.0.29648; x64/ARM64) that calls **GetRuntimeAttestationReport** to retrieve, parse, and print signed **Runtime Report Packages** from Windows. Decodes **driver reports** (loaded kernel drivers with image hashes, publisher certificate thumbprints, flags) and **hotpatch reports** (kernel-mode images with Microsoft-signed hotpatches: base address, image size, patch sequence numbers). Requires **VBS** and **[[hvci]]** on supported Windows 11 builds; intended for security researchers, anti-cheat developers, and kernel integrity analysts inspecting runtime attestation data locally (no remote attestation or RSA-PSS verification). (source: wiki/sources/descriptions/CodeMaxx__windows-runtime-attestation-report.md)

Listed under README **Windows Security Features**. Complements TPM PCR tooling such as [[sewindows]] by exposing OS-signed runtime driver/hotpatch integrity reports.

## Links

- Repo: https://github.com/CodeMaxx/windows-runtime-attestation-report

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]] · [[hvci]] · [[sewindows]]
