---
title: Driver-HideKernelThread-IoCancelIrp
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Driver-HideKernelThread-IoCancelIrp.md
updated: 2026-08-13
confidence: medium
---

# Driver-HideKernelThread-IoCancelIrp

Small proof-of-concept kernel driver that **disguises a custom system thread** by making its visible start routine look like **`IoCancelIrp`**. (source: wiki/sources/descriptions/gmh5225__Driver-HideKernelThread-IoCancelIrp.md)

The technique: allocate an IRP, register a custom cancel routine, then start the system thread at `IoCancelIrp` so the real payload runs later through the **IRP cancellation path** instead of appearing as the thread's nominal entry point. The single source file walks the full flow — IRP allocation, cancel-routine wiring, context handoff through `UserBuffer` and `MdlAddress` — and documents defensive heuristics such as flagging **`IoCancelIrp` thread starts** or walking system-thread stacks with APCs.

Mainly useful for Windows kernel researchers studying concealed thread startup and the detection strategies that can still expose it.

README tag: **Hide Kernel Thread**.

## Links

- Repo: https://github.com/gmh5225/Driver-HideKernelThread-IoCancelIrp

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[zero-thread-kernel]] · [[system-thread-finder]] · [[stealth-sytem-thread-finder-be]] · [[hidden-thread-finder]] · [[kernel-anti-cheat]] · [[driver-systemthread-from-pspcidtable-src]] · [[research-rigor]]
