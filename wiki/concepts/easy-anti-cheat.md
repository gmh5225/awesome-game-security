---
title: Easy Anti-Cheat
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md
  - wiki/sources/descriptions/thesecretclub__CVEAC-2020.md
  - wiki/sources/descriptions/lguilhermee__EAC-Extractor-Utility.md
  - wiki/sources/descriptions/ksoju__Eac-Bypass.md
  - wiki/sources/descriptions/kprprivate__EAC-CR3-BYPASS.md
  - wiki/sources/descriptions/inuNorii__Elden-Ring-CT-TGA.md
  - wiki/sources/descriptions/gmh5225__fortnite-triadz.md
updated: 2026-08-08
confidence: medium
---

# Easy Anti-Cheat

Epic’s Easy Anti-Cheat (EAC): multi-component architecture with service, kernel driver, and game-facing protections—process integrity, memory inspection, and runtime driver loading with strong client-side enforcement. Used by titles such as Fortnite, Apex Legends, and Rust. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Callback/handle surfaces ([[kernel-callbacks]]), memory/manual-map detection, driver trust and [[byovd]] blocklists, interaction with [[hvci]]/DSE, and DMA detection pipelines shared with other modern ACs.

Kernel-module integrity: historical PoC [[cveac-2020]] (WDK driver) targets an EAC kernel vulnerability with module enum, PE parse, hooks, and runtime code manipulation—Integrity Checks research lane. (source: wiki/sources/descriptions/thesecretclub__CVEAC-2020.md)

Overlay / screenshot monitoring is another research surface: PoCs such as [[eac-overlay]] explore alternate rendering surfaces or window manipulation to draw ESP without tripping EAC overlay detection. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md)

Static RE prep: utilities such as [[eac-extractor-utility]] locate EAC components in game directories and the Windows driver store, decrypt/extract the kernel driver, user-mode modules, and configuration for offline binary analysis. (source: wiki/sources/descriptions/lguilhermee__EAC-Extractor-Utility.md)

Offensive bypass lane: repos such as [[eac-bypass]] explore kernel driver and shader-based techniques to evade EAC runtime checks. (source: wiki/sources/descriptions/ksoju__Eac-Bypass.md)

CR3 / page-table root lane: minimal UM+KM teaching samples such as [[eac-cr3-bypass]] demonstrate bypassing EAC checks tied to CR3 via coordinated kernel driver + usermode code. (source: wiki/sources/descriptions/kprprivate__EAC-CR3-BYPASS.md)

Linux / Proton lane: Elden Ring CE tables such as [[elden-ring-ct-tga]] document protonhax launch + Wine-hosted Cheat Engine attach against Steam app `1245620`, with optional EAC launcher disable—useful for studying how EAC-protected titles behave under Proton-hosted cheat tooling. (source: wiki/sources/descriptions/inuNorii__Elden-Ring-CT-TGA.md)

Fortnite internal lane: samples such as [[fortnite-triadz]] (Triadz; UE4 engine hooking; ESP / aimbot / exploitation; in-process game-object + render access) illustrate internal cheat architecture and EAC detection surfaces on EAC-protected UE4 titles. (source: wiki/sources/descriptions/gmh5225__fortnite-triadz.md)

## Related

[[battleye]] · [[vanguard]] · [[cveac-2020]] · [[eac-overlay]] · [[eac-extractor-utility]] · [[eac-bypass]] · [[eac-cr3-bypass]] · [[elden-ring-ct-tga]] · [[fortnite-triadz]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
