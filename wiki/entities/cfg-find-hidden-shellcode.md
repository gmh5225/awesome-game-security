---
title: CFG-FindHiddenShellcode
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/jdu2600__CFG-FindHiddenShellcode.md
updated: 2026-08-03
confidence: medium
---

# CFG-FindHiddenShellcode

Windows tool that detects **hidden shellcode execution** by analyzing **Control Flow Guard (CFG) bitmap inconsistencies**. It scans process memory for executable regions that are valid CFG call targets but not part of any known module's legitimate code — indicating injected shellcode that has been marked CFG-valid. The C implementation demonstrates using CFG metadata as a detection signal. (source: wiki/sources/descriptions/jdu2600__CFG-FindHiddenShellcode.md)

Aimed at anti-cheat engineers and EDR developers studying CFG-based code injection detection under `Detection:ShellCode`. Complements working-set page-fault monitors such as [[faultline]] and in-memory evasion PoCs such as [[shellcode-fluctuation]] on the offensive side; pairs with other jdu2600 defensive telemetry tools such as [[etw-syscall-monitor]] and [[etwti-fluctuation-monitor]].

## Links

- Repo: https://github.com/jdu2600/CFG-FindHiddenShellcode

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[faultline]] · [[shellcode-fluctuation]] · [[x64dbg-xfg-marker]] · [[cet-research]] · [[etw-syscall-monitor]] · [[etwti-fluctuation-monitor]]
