---
title: GhostDebug
kind: entity
topics: [reverse-engineering, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/VollRagm__ghostdebug.md
updated: 2026-08-23
confidence: medium
---

# GhostDebug

Stealth **Windows x64 debugger** that attaches by injecting a core native DLL and controlling it from a **C# CLI** over a **named pipe**. Debugging runs through a **Vectored Exception Handler (VEH)** with software **INT3** breakpoints, single-stepping, register read/write, and breakpoint scripting—avoiding the **Win32 Debug API** that anti-cheat and anti-debug checks typically flag. (source: wiki/sources/descriptions/VollRagm__ghostdebug.md)

The CLI uses the **Iced** disassembler for live instruction views and **JSON** messaging to set breakpoints, resume, and step interactively. Bundled **TestTarget** exercises `IsDebuggerPresent`, PEB `BeingDebugged`, and `NtQueryInformationProcess` to validate session invisibility. Aimed at game-security researchers and reverse engineers debugging protected Windows processes.

## Architecture

| Component | Role |
|-----------|------|
| Injected DLL | VEH handler, INT3 breakpoints, single-step, register ops |
| C# CLI | Named-pipe control, Iced disassembly, JSON command protocol |
| TestTarget | Anti-debug probe harness for validation |

## Links

- Repo: https://github.com/VollRagm/ghostdebug

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[titanhide]] · [[anti-debugging]] · [[makin]]
