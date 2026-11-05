---
title: sapdragon/vac
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/sapdragon__vac.md
updated: 2026-11-05
confidence: high
---

# sapdragon/vac

**Classic VAC scan-module reconstruction** (sapdragon): C++20 byte-for-byte rebuild of fifteen legacy 32-bit Valve Anti-Cheat scan modules plus the `steamservice.dll` host that loads and runs them. Shared module SDK preserves the original `_runfunc` export path, VLV RSA signing checks, manual mapping, and report sealing via ICE and raw RSA-512. Scanner workers fingerprint boot config, drivers, PCI/USB devices, in-memory and on-disk PE images, process memory maps, shared sections, system handles, and WoW64 Heaven's Gate syscalls. Each rebuilt scanner is validated for exact **4232-byte output parity** against Valve's signed originals, deliberately preserving quirks, bugs, and stack artifacts from the legacy binaries. Writeups document IPC, module management, and scanner mechanics for anti-cheat architecture and Steam client integrity telemetry research. (source: wiki/sources/descriptions/sapdragon__vac.md)

Complements annotated decompile corpora ([[vac]], danielkrupinski) and forensic CS2 architecture notes ([[como-funciona-vac]]) with a **rebuild-and-parity-test** reference implementation. Dump/emulation lanes include [[dumpvac]], [[vac-dumper]], [[vac-emulator]], and [[vacation3-emu]]; same author's syscall and anti-analysis tooling includes [[syscalls-cpp]] and [[hint-break]].

## Links

- Repo: https://github.com/sapdragon/vac

## Related

[[vac]] · [[como-funciona-vac]] · [[dumpvac]] · [[vac-dumper]] · [[vac-emulator]] · [[vacation3-emu]] · [[vac-hooks]] · [[syscalls-cpp]] · [[hint-break]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
