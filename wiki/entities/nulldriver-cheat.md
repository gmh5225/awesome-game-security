---
title: NullDriverCheat
kind: entity
topics: [windows-kernel, game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__NullDriverCheat.md
updated: 2026-08-11
confidence: medium
---

# NullDriverCheat

Windows 11 adaptation of **Null's driver-cheat pattern**: hooks **`NtOpenCompositionSurfaceSectionInfo`** inside **dxgkrnl** to establish a covert user↔kernel communication channel instead of a monitored device IOCTL surface. The hook installer patches a small jump stub into the export; the handler accepts structured requests for **module-base lookup**, **process memory read/write**, and optional **GDI drawing helpers** sourced from win32k exports. The archived README frames it as a modified reimplementation with a different pool tag and syscall choice intended to reduce immediate detection versus simpler device-based approaches. (source: wiki/sources/descriptions/gmh5225__NullDriverCheat.md)

Mainly useful for reverse engineers studying **dxgkrnl export hooks**, structured user-kernel messaging, and GDI-assisted overlay or memory helpers in cheat drivers. Adjacent to [[dxgkrnl-hook]] (screen-buffer overlay research), composition-surface stealth I/O such as [[data-ptr-swap]] and [[double-callback]], and other non-IOCTL channels such as [[job-communication]] and [[r69-driver]].

## Links

- Repo: https://github.com/gmh5225/NullDriverCheat

## Related

[[dxgkrnl-hook]] · [[data-ptr-swap]] · [[double-callback]] · [[job-communication]] · [[r69-driver]] · [[krnl-gdi-render]] · [[present-hook]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
