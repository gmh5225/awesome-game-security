---
title: IDA-WPP-Remover
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/L4ys__IDA-WPP-Remover.md
updated: 2026-08-23
confidence: medium
---

# IDA-WPP-Remover

**IDA-WPP-Remover** (L4ys) is a Python **IDA Pro plugin** that cleans **Hex-Rays pseudocode** by stripping Windows Performance Profiling (**WPP**) trace-call noise. It applies a **microcode optimization pass** that replaces `WPP_SF*` invocations before decompiler output is emitted, automatically targeting Windows PE binaries and exposing a toggle directly from the decompiled view. Intended for reverse engineers who want clearer pseudocode during malware and game binary analysis. (source: wiki/sources/descriptions/L4ys__IDA-WPP-Remover.md)

Complements other Hex-Rays microcode-oriented plugins such as [[hex-rays-deob]] and [[genmc]], and pseudocode polish utilities such as [[happyida]]—focused specifically on WPP instrumentation clutter rather than obfuscation recovery or general decompiler UX.

Not to be confused with [[wpp]] (btbd), a kernel driver PoC that hijacks WPP trace infrastructure for IRP capture research.

## Links

- Repo: https://github.com/L4ys/IDA-WPP-Remover

## Related

[[hex-rays-deob]] · [[genmc]] · [[happyida]] · [[ntrays]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
