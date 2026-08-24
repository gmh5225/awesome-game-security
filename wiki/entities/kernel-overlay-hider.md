---
title: Kernel Overlay Hider
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/J0xna__Kernel-Overlay-Hider.md
updated: 2026-08-24
confidence: medium
---

# Kernel Overlay Hider

**Proof-of-concept** (J0xna) that hides an overlay window handle from **window enumeration** by manipulating **kernel-side window structures**. A Windows kernel driver pairs with user-mode test programs to locate and modify **win32k**-related pointers and **TAGWND**-linked data using **DKOM-style** techniques. Includes examples for triggering the behavior from a **DirectX overlay** context. Intended for low-level Windows internals research around overlay visibility and anti-cheat evasion mechanics—not a maintained bypass product. (source: wiki/sources/descriptions/J0xna__Kernel-Overlay-Hider.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Kernel driver | Locates win32k window objects and patches TAGWND-linked fields |
| User-mode tests | Exercise enumeration bypass from a DirectX overlay HWND |
| DKOM-style edits | Direct kernel object manipulation rather than usermode API hooks |

Contrasts with user-mode overlay heuristics such as [[topmost-detection]] and external overlay strategies such as [[not-an-overlay]] and [[window-hijack-overlay]]. Complements win32k GUI-subsystem corpora such as [[win32k-file-collection]] and [[callmewin32kdriver]] for offline structure research.

## Links

- Repo: https://github.com/J0xna/Kernel-Overlay-Hider

## Related

[[topmost-detection]] · [[not-an-overlay]] · [[window-hijack-overlay]] · [[callmewin32kdriver]] · [[win32k-file-collection]] · [[capcom-dkom]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
