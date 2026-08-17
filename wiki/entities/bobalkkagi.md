---
title: bobalkkagi
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bobalkkagi__bobalkkagi.md
updated: 2026-08-17
confidence: medium
---

# bobalkkagi

Python tool for unpacking and unwrapping Themida 3.1.3–protected Windows executables (Tiger red64), with planned devirtualization support. Emulates protected binaries with the Unicorn engine and hooks Windows APIs against a provided win10_v1903 DLL set so packer anti-debug and loader logic runs far enough to recover original code. Offers fast, hook_block, or hook_code emulation modes; optional original entry point (OEP) location; and a debugger-style hook_code workflow for extending hooks to other protectors or Themida versions. Built with Capstone/distorm3; Poetry/PyInstaller packaging. Aimed at reverse engineers and game-security researchers analyzing Themida-packed binaries. (source: wiki/sources/descriptions/bobalkkagi__bobalkkagi.md)

Companion surface to Cheat → Fix Themida work ([[unlicense]] Frida dynamic unpack, [[magicmida-rs]] Win32 Debug API unpack, [[themida-unmutate]] static mutation deobf): **Unicorn API-hook emulation** for Themida 3.1.3 Tiger red64 rather than live Frida/DBI or Debug API automation.

## Links

- Repo: https://github.com/bobalkkagi/bobalkkagi

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unlicense]] · [[magicmida-rs]] · [[themida-unmutate]] · [[themida-research]] · [[tde]]
