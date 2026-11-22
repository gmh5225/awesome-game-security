---
title: Bodycam EAC Driver Fixes
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Dezmonius__bodycam-eac-driver-fixes.md
  - wiki/sources/README-categories.md
updated: 2026-11-22
confidence: medium
---

# Bodycam EAC Driver Fixes

Documented **reversible Windows workarounds** (Dezmonius) when **Easy Anti-Cheat** blocks **Bodycam** launch over third-party kernel drivers still loaded on the host—commonly **`AsUpIO.sys`** (ASUS utilities), **`ssgdio64.sys`**, or **`RTCore64.sys`** (MSI Afterburner / similar). Catalogued as player troubleshooting and EAC kernel-inventory policy research, not EAC bypass or cheat tooling. (source: wiki/sources/descriptions/Dezmonius__bodycam-eac-driver-fixes.md)

## Mechanism

Each targeted fix ships as administrator **batch launchers** plus **PowerShell 5.1** scripts that:

| Step | Action |
|------|--------|
| Locate | Find registered kernel services by driver filename (`sc.exe`, WMI/CIM, registry service keys) |
| Back up | Snapshot startup settings to JSON under **ProgramData** |
| Disable | Turn off driver autoload |
| Stop | Attempt to stop the driver without deleting `.sys` files |

Companion **restore** scripts roll settings back from the JSON backups. A bundled technical report documents observed EAC dialog text, driver provenance (ASUS / MSI utility stacks), and verification limits. (source: wiki/sources/descriptions/Dezmonius__bodycam-eac-driver-fixes.md)

## Research relevance

Illustrates how commercial EAC enforces **loaded third-party kernel driver policy** on consumer PCs—orthogonal to [[byovd]] offensive lanes where the same ASUS **`AsUpIO.sys`** family appears as a signed primitive ([[imxyvimapper]], [[win-driver-exp]]). Contrasts with user-space utility coexistence such as [[discord-dpi-bridge]], which avoids loading conflicting kernel modules entirely.

## Links

- Repo: https://github.com/Dezmonius/bodycam-eac-driver-fixes

## Related

[[easy-anti-cheat]] · [[discord-dpi-bridge]] · [[imxyvimapper]] · [[win-driver-exp]] · [[byovd]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]