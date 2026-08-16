---
title: NMI Callback Handler
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/donnaskiez__nmi-callback-handler.md
updated: 2026-08-16
confidence: medium
---

# NMI Callback Handler

Windows kernel driver demonstrating **NMI-based thread stack walking** for cheat detection research. It registers an NMI callback via `KeRegisterNmiCallback`, locates the **MACHINE_FRAME** structure from the `iretq` ISR return path to recover the interrupted instruction pointer, and captures interrupted **RIP** values across all processors — enabling detection of code executing from suspicious memory regions such as manually mapped drivers. Aimed at anti-cheat developers and kernel security researchers studying NMI callback stack forensics. (source: wiki/sources/descriptions/donnaskiez__nmi-callback-handler.md)

Complements defensive NMI callback study such as [[nmi-callback]] and [[nmi-nmi-callback]], offensive NMI disable PoCs such as [[nmi-callback-blocker2]], [[disable-nmi-callbacks]], and [[nmi]], and multi-telemetry AC prototypes such as [[kernel-anti-cheat]] within the [[kernel-callbacks]] lane.

## Links

- Repo: https://github.com/donnaskiez/nmi-callback-handler [Mapped Driver by NMI Callback]

## Related

[[nmi-callback]] · [[nmi-nmi-callback]] · [[nmi-enum-nmi-callback]] · [[kernel-anti-cheat]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
