---
title: KPDB
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/rbmm__KPDB.md
  - wiki/sources/descriptions/GetRektBoy724__KPDB.md
updated: 2026-08-25
confidence: medium
---

# KPDB

Kernel-mode **PDB (Program Database) parsing** for resolving symbols directly from a Windows driver when usermode DIA/PDB tooling is unavailable. Two independent repos share the name:

- **GetRektBoy724/KPDB** — pure C parser extending lightweight logic to handle both **symbol and type streams**; resolves debug info at runtime to avoid brittle version-specific offsets and signature-scan patterns. Primary use: stable low-level tooling for kernel RE, security research, and anti-cheat development. (source: wiki/sources/descriptions/GetRektBoy724__KPDB.md)
- **rbmm/KPDB** — C++ project in the Some Tricks → Windows Ring0 lane for driver development and modding. (source: wiki/sources/descriptions/rbmm__KPDB.md)

Complements usermode PDB parse/merge tools such as [[pdb]] and syscall/PDB extractors such as [[ntsleuth]] when the research target is resolving symbols from ring 0 rather than from a debugger host.

## Links

- Repo: https://github.com/GetRektBoy724/KPDB
- Repo: https://github.com/rbmm/KPDB

## Related

[[pdb]] · [[ntsleuth]] · [[ida-kmdf]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
