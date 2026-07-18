---
title: EfiTool
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/wesmar__EfiTool.md
updated: 2026-07-18
confidence: medium
---

# EfiTool

UEFI EFI application that patches the Windows `SYSTEM` registry hive in RAM at `ExitBootServices`, before the NT kernel takes over. The demo sets `SetupType` and `CmdLine` so `cmd.exe` launches as `NT AUTHORITY\SYSTEM` on the next boot—no disk writes and no kernel driver. (source: wiki/sources/descriptions/wesmar__EfiTool.md)

Documents `gBS->ExitBootServices` hooking, regf hive cell patching, anti-analysis string obfuscation, and BitLocker / PCR boundary notes for Windows 11 research (production builds claim no PCR violations so BitLocker does not prompt). Aimed at game-security / RE study of cheat ↔ EFI driver techniques rather than a production bootkit. (source: wiki/sources/descriptions/wesmar__EfiTool.md)

Adjacent to EFI manual-map research such as [[xigmapper]], but focuses on in-RAM hive privilege setup instead of unsigned driver mapping.

## Links

- Repo: https://github.com/wesmar/EfiTool

## Related

[[xigmapper]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
