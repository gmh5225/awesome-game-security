---
title: PowerHook
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/Archie-osu__PowerHook.md
updated: 2026-09-02
confidence: medium
---

# PowerHook

Windows **kernel-mode proof of concept** that hooks a **processor power-management callback** to intercept execution in kernel context (Archie-osu). Implemented in **C++** as a **KMDF driver**; rewires the **PRCB `IdlePreselect`** routine while preserving the original handler for cleanup. The hook routine demonstrates **thread and process object lookups** from kernel space and logs **execution-context details**. Primarily useful for **Windows internals learning** and **low-level game security research**—not a production cheat or evasion stack. (source: wiki/sources/descriptions/Archie-osu__PowerHook.md)

Complements per-process **PTE hooks** such as [[windows-kernel-pagehook]] and paging-structure redirection in [[page-table-hook]], and KPRCB-oriented thread research such as [[detect-hiddenthread-via-kprcb]] when studying processor control-block internals.

## Links

- Repo: https://github.com/Archie-osu/PowerHook (README tag: Hooking KPRCB IdlePreselect)

## Related

[[windows-kernel-pagehook]] · [[page-table-hook]] · [[detect-hiddenthread-via-kprcb]] · [[fast-pf-hook]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
