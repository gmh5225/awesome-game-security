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
  - wiki/sources/descriptions/gmh5225__fortnite-internal-updated-ritz.md
  - wiki/sources/descriptions/gmh5225__ZeroGui-Fortnite-Internal.md
  - wiki/sources/descriptions/gmh5225__fortnite-exploits.md
  - wiki/sources/descriptions/gmh5225__VOLTO-EXTERNAL-SPOWAR-UD-EAC-BE-FORTNITE-EXTERNAL-CHEAT.md
  - wiki/sources/descriptions/gmh5225__Serenity.gg-FN-and-Loader.md
  - wiki/sources/descriptions/gmh5225__eac-bypass-1.md
  - wiki/sources/descriptions/gmh5225__ce-EasyAntiCheat-Bypass.md
updated: 2026-08-10
confidence: medium
---

# Easy Anti-Cheat

Epic’s Easy Anti-Cheat (EAC): multi-component architecture with service, kernel driver, and game-facing protections—process integrity, memory inspection, and runtime driver loading with strong client-side enforcement. Used by titles such as Fortnite, Apex Legends, and Rust. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Callback/handle surfaces ([[kernel-callbacks]]), memory/manual-map detection, driver trust and [[byovd]] blocklists, interaction with [[hvci]]/DSE, and DMA detection pipelines shared with other modern ACs.

Kernel-module integrity: historical PoC [[cveac-2020]] (WDK driver) targets an EAC kernel vulnerability with module enum, PE parse, hooks, and runtime code manipulation—Integrity Checks research lane. (source: wiki/sources/descriptions/thesecretclub__CVEAC-2020.md)

Overlay / screenshot monitoring is another research surface: PoCs such as [[eac-overlay]] explore alternate rendering surfaces or window manipulation to draw ESP without tripping EAC overlay detection. (source: wiki/sources/descriptions/xBrunoMedeiros__eac-overlay.md)

Static RE prep: utilities such as [[eac-extractor-utility]] locate EAC components in game directories and the Windows driver store, decrypt/extract the kernel driver, user-mode modules, and configuration for offline binary analysis. (source: wiki/sources/descriptions/lguilhermee__EAC-Extractor-Utility.md)

Offensive bypass lane: repos such as [[eac-bypass]] explore kernel driver and shader-based techniques to evade EAC runtime checks. (source: wiki/sources/descriptions/ksoju__Eac-Bypass.md) Win32k syscall channels such as [[eac-bypass-1]] (`NtMapVisualRelativePoints`; C++ driver development; cheat / driver communication) study stealth KM↔UM I/O alongside EAC evasion. (source: wiki/sources/descriptions/gmh5225__eac-bypass-1.md) Cheat Engine tool-detection bypass samples such as [[ce-easyanticheat-bypass]] patch or hide CE process, window class, driver, and memory-access signatures so scan/edit workflows run on EAC-protected games—useful for studying how EAC fingerprints common debugging tools. (source: wiki/sources/descriptions/gmh5225__ce-EasyAntiCheat-Bypass.md)

CR3 / page-table root lane: minimal UM+KM teaching samples such as [[eac-cr3-bypass]] demonstrate bypassing EAC checks tied to CR3 via coordinated kernel driver + usermode code. (source: wiki/sources/descriptions/kprprivate__EAC-CR3-BYPASS.md)

Linux / Proton lane: Elden Ring CE tables such as [[elden-ring-ct-tga]] document protonhax launch + Wine-hosted Cheat Engine attach against Steam app `1245620`, with optional EAC launcher disable—useful for studying how EAC-protected titles behave under Proton-hosted cheat tooling. (source: wiki/sources/descriptions/inuNorii__Elden-Ring-CT-TGA.md)

Fortnite internal lane: samples such as [[fortnite-triadz]] (Triadz; UE4 engine hooking; ESP / aimbot / exploitation; in-process game-object + render access) and updated Ritz forks such as [[fortnite-internal-updated-ritz]] (refreshed offsets + EAC bypass for newer builds) illustrate internal cheat architecture and EAC detection surfaces on EAC-protected UE4 titles. ZeroGui-overlay samples such as [[zerogui-fortnite-internal]] (visuals-only ESP enabled; aimbot / exploits disabled) narrow that lane to in-process render/visual study on Fortnite without full combat modules. Exploit-chain documentation such as [[fortnite-exploits]] (client vulns; UE4 features; EAC bypass for injection / memory access) complements those runnable samples for researchers mapping Fortnite-specific bypass paths. External Fortnite samples such as [[volto-external-spowar-ud-eac-be-fortnite-external-cheat]] (gmh5225; C/C++; kernel driver + overlay; HWID-spoof / EAC-evasion naming; out-of-process RPM) and [[serenity-gg-fn-and-loader]] (gmh5225; C/C++; kernel driver + shader work + module loader) illustrate the complementary external lane on the same EAC-protected title. (source: wiki/sources/descriptions/gmh5225__fortnite-triadz.md) (source: wiki/sources/descriptions/gmh5225__fortnite-internal-updated-ritz.md) (source: wiki/sources/descriptions/gmh5225__ZeroGui-Fortnite-Internal.md) (source: wiki/sources/descriptions/gmh5225__fortnite-exploits.md) (source: wiki/sources/descriptions/gmh5225__VOLTO-EXTERNAL-SPOWAR-UD-EAC-BE-FORTNITE-EXTERNAL-CHEAT.md) (source: wiki/sources/descriptions/gmh5225__Serenity.gg-FN-and-Loader.md)

## Related

[[battleye]] · [[vanguard]] · [[cveac-2020]] · [[eac-overlay]] · [[eac-extractor-utility]] · [[eac-bypass]] · [[eac-bypass-1]] · [[ce-easyanticheat-bypass]] · [[eac-cr3-bypass]] · [[elden-ring-ct-tga]] · [[fortnite-triadz]] · [[fortnite-internal-updated-ritz]] · [[zerogui-fortnite-internal]] · [[fortnite-exploits]] · [[volto-external-spowar-ud-eac-be-fortnite-external-cheat]] · [[serenity-gg-fn-and-loader]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
