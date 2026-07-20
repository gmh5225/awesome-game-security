---
title: MiniVisorPkg
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/tandasat__MiniVisorPkg.md
updated: 2026-07-20
confidence: medium
---

# MiniVisorPkg

tandasat educational research hypervisor for Intel processors, packaged as both a UEFI driver and a Windows driver. As UEFI, it can inspect system activity before the OS boots; as a Windows driver, it is intended to be debugged with familiar tools such as WinDbg. Aimed at game-security researchers and reverse engineers studying hypervisor / EFI-driver techniques in the cheat / EFI driver lane—not a production anti-cheat component. (source: wiki/sources/descriptions/tandasat__MiniVisorPkg.md)

Pairs with minimal VT-x learning stacks such as [[hv]], stealth Type-2 research such as [[ophion]], and hacked-hypervisor stress tooling such as [[vt-debuuger]] under `Detection: Hacked Hypervisor`. Same author as [[sushi]] (PatchGuard monitoring).

## Links

- Repo: https://github.com/tandasat/MiniVisorPkg

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[hv]] · [[ophion]] · [[vt-debuuger]] · [[baresvm]] · [[checkhv-um]] · [[hypervisor-detection]] · [[sushi]] · [[hvci]] · [[overviews/game-hacking]]
