---
title: CreateProcessAsPPL
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/2x7EQ13__CreateProcessAsPPL.md
updated: 2026-09-05
confidence: medium
---

# CreateProcessAsPPL

C++ command-line loader (2x7EQ13) that **launches Windows processes at specific Protected Process Light (PPL) levels**. Exposes modes for protection tiers such as **WinTCB**, **Windows**, **Antimalware**, and **LSA**, focusing on practical process-protection semantics and how executable launch behavior changes under each PPL mode. Useful for Windows internals and security researchers testing **protected-process boundaries**, tooling compatibility, and defensive assumptions. (source: wiki/sources/descriptions/2x7EQ13__CreateProcessAsPPL.md)

Complements offensive PPL **strip/downgrade** tooling such as [[pplkiller]] and handle-elevation research such as [[easy-handles]] (documented PPL limitations) by providing a **lab-side spawn path** for synthetic PPL targets—relevant when exercising [[etw-threat-intelligence]] cross-process memory telemetry or debugger/injector compatibility against protected processes.

## Links

- Repo: https://github.com/2x7EQ13/CreateProcessAsPPL

## Related

[[pplkiller]] · [[easy-handles]] · [[ghostdebug]] · [[remap]] · [[meme-rw]] · [[etw-threat-intelligence]] · [[kernel-callbacks]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
