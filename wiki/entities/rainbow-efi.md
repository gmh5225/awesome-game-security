---
title: rainbow-efi
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__-Rainbow---EFI.md
updated: 2026-08-15
confidence: medium
---

# rainbow-efi

UEFI boot-stage HWID spoof research project (gmh5225; cheat / HWID). Combines a Visual Studio and MSBuild-friendly **EDK II** environment with a separate **`rainbow`** UEFI driver project and debugger assets (OVMF images, UEFI shell ISO, ROM files for local testing). The **`rainbow.efi`** payload hooks **`ExitBootServices`**, walks early Windows boot structures such as **`OslLoaderBlock`**, then hooks **`IopLoadDriver`** to apply spoofing logic before removing its own hook. Project layout includes both boot-stage driver code and the supporting UEFI library layer for building and debugging the EFI component—not just a standalone binary drop. Aimed at firmware and Windows boot researchers studying how UEFI drivers are built, loaded from an EFI shell, and used to alter behavior during the transition into the Windows kernel. (source: wiki/sources/descriptions/gmh5225__-Rainbow---EFI.md)

Contrasts with OS-runtime UEFI cheat comm such as [[fortnite-efi-external]], staged EFI→kernel implants such as [[driver-efi-bootkit]], and kernel-mode HWID spoofers such as [[hwid-kernel-spoofer]] and [[easy-hwid-spoofer]].

## Links

- Repo: https://github.com/gmh5225/-Rainbow---EFI

## Related

[[bootlicker]] · [[driver-efi-bootkit]] · [[uefi-bootloader]] · [[eficmake]] · [[efixplorer]] · [[hwid-kernel-spoofer]] · [[easy-hwid-spoofer]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
