---
title: BYOVD
kind: concept
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/xct__windows-kernel-exploits.md
  - wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md
  - wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md
  - wiki/sources/descriptions/wesmar__kvc.md
  - wiki/sources/descriptions/wesmar__WinDefCtl.md
  - wiki/sources/descriptions/wesmar__KernelResearchKit.md
  - wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md
  - wiki/sources/descriptions/vergamota__KslKatz.md
  - wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md
  - wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md
  - wiki/sources/descriptions/symeonp__Lenovo-CVE-2025-8061.md
  - wiki/sources/descriptions/shareef12__cpuz.md
  - wiki/sources/descriptions/sai2fast__DsArk64.md
updated: 2026-07-23
confidence: high
---

# BYOVD

Bring Your Own Vulnerable Driver: load a legitimately signed but vulnerable driver to obtain kernel read/write (or other primitives), then disable protections, map unsigned code, or blind anti-cheat. (source: wiki/sources/skills/windows-kernel.md)

## Typical chain

1. Load signed vulnerable driver (e.g. historically abused families like Capcom, RTCore, iqvw64e, dbutil, …)
2. Trigger vulnerable IOCTL / bug for arbitrary R/W
3. Tamper with DSE, callbacks, ETW, or load a hostile mapper

## Mitigations

Microsoft vulnerable-driver blocklist, [[hvci]], AC driver allowlists ([[vanguard]]-style), PiDDBCache/MmUnloadedDrivers forensics, EPT-protected callback lists. HVCI-oriented LOLdriver checks such as [[hvci-loldrivers-check]] help inventory known-abused signed drivers against Memory Integrity constraints. (source: wiki/sources/descriptions/trailofbits__HVCI-loldrivers-check.md) Broader LOLdriver scan clients such as [[loldrivers-client]] (Go/PowerShell) sit in the same cheat / vulnerable-driver research lane. (source: wiki/sources/descriptions/rtfmkiesel__loldrivers-client.md)

Educational kernel-exploit reference material such as [[windows-kernel-exploits]] sits in the same cheat / vulnerable-driver documentation lane. (source: wiki/sources/descriptions/xct__windows-kernel-exploits.md)

Concrete AV/EDR-evasion research such as [[ven0m-ransomware]] abuses `iMFForceDelete.sys` from IObit Malware Fighter (v12.1.0) rather than a classic ZwTerminateProcess-style killer driver. (source: wiki/sources/descriptions/xM0kht4r__VEN0m-Ransomware.md)

Process-terminate style killers such as [[av-edr-killer]] target `wsftprm.sys` via IOCTL `0x22201C` (1036-byte buffer; first DWORD = target PID). (source: wiki/sources/descriptions/xM0kht4r__AV-EDR-Killer.md)

DSE-disable controllers such as [[kvc]] use a signed Microsoft driver to patch CI.dll (`g_CiOptions`), plus `skci.dll` hijack / `SeCiCallbacks` redirection loaders and PP/PPL paths for LSASS dumps under HVCI/VBS. (source: wiki/sources/descriptions/wesmar__kvc.md)

Broader Win11 research kits such as [[kernel-research-kit]] combine boot-time `SeCiCallbacks` DSE bypass with multiple unsigned-load methods including BYOVD alongside manual map and IRP hijack (25H2; native subsystem; anti-loop dual-path). (source: wiki/sources/descriptions/wesmar__KernelResearchKit.md)

Defender neutralization CLIs such as [[windefctl]] escalate via a kernel driver to disable real-time protection and Tamper Protection (Win11 26H1; UAC/GUI bypass, stealth execution)—same AV/EDR-control research lane as process-kill BYOVD samples. (source: wiki/sources/descriptions/wesmar__WinDefCtl.md)

Full-stack EDR-blinding toolkits such as [[edrsandblast]] combine BYOVD with callback/ETW TI disable and ntdll unhook (offset automation + demo credential dump). (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md)

LSASS credential extractors such as [[kslkatz]] abuse Microsoft Defender’s `KslD.sys` for kernel-mode reads of WDigest plaintext and encrypted LSA secrets past PPL/AV. (source: wiki/sources/descriptions/vergamota__KslKatz.md)

OEM-driver LPE PoCs such as [[lenovo-cve-2025-8061]] target Lenovo `LnvMSRIO.sys` (CVE-2025-8061) via IOCTL abuse for kernel R/W and a SYSTEM shell. (source: wiki/sources/descriptions/symeonp__Lenovo-CVE-2025-8061.md)

Classic signed-utility driver abuse such as [[cpuz]] (CPU-Z; XP–Win10 1607) sits in the same cheat / vulnerable-driver research lane. (source: wiki/sources/descriptions/shareef12__cpuz.md)

Security-product handle-donor abuse such as [[dsark64]] targets Qihoo 360’s WHQL-signed `DsArk64.sys` (suspended installer + shellcode open `\\.\DsArk`, then `DuplicateHandle` → ring-0 process kill + kernel R/W). (source: wiki/sources/descriptions/sai2fast__DsArk64.md)

## Related

[[kernel-callbacks]] · [[hvci]] · [[hvci-loldrivers-check]] · [[loldrivers-client]] · [[patchguard]] · [[windows-kernel-exploits]] · [[ven0m-ransomware]] · [[av-edr-killer]] · [[dsark64]] · [[lenovo-cve-2025-8061]] · [[cpuz]] · [[kvc]] · [[kslkatz]] · [[kernel-research-kit]] · [[windefctl]] · [[edrsandblast]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]

