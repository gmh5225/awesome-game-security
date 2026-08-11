---
title: dxgkrnl_hook
kind: entity
topics: [graphics-api, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/vmcall__dxgkrnl_hook.md
updated: 2026-07-19
confidence: medium
---

# dxgkrnl_hook

Research sample that **hooks the Windows graphics kernel subsystem (dxgkrnl)** to manipulate the screen buffer—used to draw overlays such as player boxes from Ring0 rather than via user-mode Present/swap-chain hooks alone. Aimed at game-security and reverse-engineering researchers in the cheat / render-draw lane. (source: wiki/sources/descriptions/vmcall__dxgkrnl_hook.md)

Adjacent to kernel DWM/composition samples such as [[double-callback]] and [[data-ptr-swap]], Win11 Null-pattern dxgkrnl export hooks such as [[nulldriver-cheat]] (`NtOpenCompositionSurfaceSectionInfo` covert comms + optional GDI helpers; gmh5225), and to user-mode [[present-hook]] / overlay detection surfaces under [[overviews/graphics-api]].

## Links

- Repo: https://github.com/vmcall/dxgkrnl_hook

## Related

[[present-hook]] · [[nulldriver-cheat]] · [[double-callback]] · [[data-ptr-swap]] · [[eac-overlay]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
