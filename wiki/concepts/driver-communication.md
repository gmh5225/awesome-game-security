---
title: Driver Communication
kind: concept
topics: [game-hacking, windows-kernel, anti-cheat]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/zoand__BOOM.md
  - wiki/sources/descriptions/gmh5225__Driver-read_write.md
  - wiki/sources/descriptions/gmh5225__DataPtrSwap-driver.md
  - wiki/sources/descriptions/Sinclairq__data-communication.md
updated: 2026-09-09
confidence: medium
---

# Driver Communication

Kernel–user **data channels** used by cheat drivers, research tools, and some anti-cheat components. The README catalog lists 40+ methods; classify by transport mechanism and observation surface rather than treating all as equivalent stealth. (source: wiki/sources/skills/game-hacking.md)

## Taxonomy

| Class | Mechanism | Notes |
|-------|-----------|-------|
| IOCTL | `DeviceIoControl` with custom codes; buffered/direct/`METHOD_NEITHER` | Most common; driver object and code ranges are observable |
| Data pointer swap | Abuse legitimate syscalls (`NtUser*`, `NtGdi*`, `NtDxgk*`, etc.) to pass kernel pointers | Win32k and composition syscall research lane |
| Shared memory | `ZwCreateSection` + `ZwMapViewOfSection`; physical mapping; event signaling | Named sections may appear in object enumeration |
| Callbacks | Registry (`CmRegisterCallbackEx`), minifilter ports, object callbacks with embedded payloads | Correlates with [[kernel-callbacks]] forensics |
| Unconventional | Named pipes from kernel, window messages, ETW providers, WSK sockets, filter callbacks, `DbgPrint` interception | Higher novelty; still has provenance and load-path artifacts |

## Illustrative corpus

- [[boom]] — hijacks `Beep.sys` for covert KM↔UM I/O (zoand; cheat / driver communication)
- [[driver-read-write]] — swaps `IRP_MJ_DEVICE_CONTROL` on a hijacked driver for process R/W + module base; PiDDBCache/MmUnloadedDrivers cleanup (gmh5225)
- [[dataptrswap-driver]] — win32kbase data-pointer swap on `NtSetCompositionSurfaceAnalogExclusive` with explorer attach (gmh5225)
- [[data-communication]] — kernel `.data` pointer swap for high-speed messaging and R/W via `NtCompareSigningLevels` research (Sinclairq)
- [[driver-communication-list]] — curated README index of communication methods

Catalog samples are **versioned threat-model examples**—verify IOCTL layouts, syscall availability, and patch level on the target build before analysis or detection rules. (source: wiki/sources/skills/game-hacking.md)

## Detection surface

- Driver image hash, service name, and load order
- Device object and symlink creation
- Unexpected IOCTL traffic to non-game drivers
- Win32k/DXGK syscall hook or pointer anomalies
- Shared section names and cross-process kernel mappings

Missing one collector's artifact does not prove a channel is invisible—scope conclusions to the observer and lifecycle covered.

## Related

[[kernel-callbacks]] · [[byovd]] · [[stack-spoofing]] · [[km-um-communication]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
