---
title: unlicense
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ergrelet__unlicense.md
updated: 2026-08-15
confidence: medium
---

# unlicense

Python 3 dynamic unpacker and import fixer for Windows executables protected with Themida and WinLicense 2.x and 3.x. Runs the target under instrumentation (notably [[frida]]), dumps the unpacked PE after recovering the original entry point, and reconstructs the often obfuscated import table. Supports 32-bit and 64-bit native PE executables and DLLs as well as .NET assembly EXEs; relies on PE parsing and analysis libraries such as LIEF and Capstone. Aimed at reverse engineers and security researchers analyzing Themida/WinLicense-protected binaries in a controlled environment. (source: wiki/sources/descriptions/ergrelet__unlicense.md)

Companion surface to Cheat → Fix Themida work ([[magicmida-rs]] debugger-driven unpack, [[tde]] IDA devirtualization, [[themida-research]] VM internals): Frida/DBI-driven dynamic unpack + OEP/IAT rebuild rather than Win32 Debug API automation or plugin recovery.

## Links

- Repo: https://github.com/ergrelet/unlicense

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[themida-unmutate]] · [[themida-research]] · [[tde]] · [[magicmida-rs]] · [[frida]] · [[dynamic-binary-instrumentation]]
