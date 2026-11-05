---
title: idafridascript
kind: entity
topics: [reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/ys1231__idafridascript.md
updated: 2026-11-05
confidence: medium
---

# idafridascript

**FridaTools** (ys1231/idafridascript) is an **IDA Pro 9.1** plugin that **generates Frida hook JavaScript** for the function under the cursor from the **disassembly window** (assembly-view shortcut **F**). Output uses IDA’s function analysis plus JavaScript templates for **generic function hooks** and **Flutter SSL pinning bypass** hooks. Implementation is mainly **Python** (IDA API) with hook templates; optional **HTTP MCP server** integration supports automated script-generation workflows. Targets reverse engineers and mobile security researchers who pair **static IDA analysis** with **dynamic Frida instrumentation**, including SSL pinning and Flutter app scenarios. (source: wiki/sources/descriptions/ys1231__idafridascript.md)

## Links

- Repo: https://github.com/ys1231/idafridascript (README: IDA Pro 9 plugin; one-click Frida hook scripts from disassembly; optional MCP)

## Related

[[frida]] · [[frinet]] · [[ghidra-frida-hook-gen]] · [[frida-forge]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]]
