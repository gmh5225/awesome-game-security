---
title: windows-software-policy
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/KiFilterFiberContext__windows-software-policy.md
updated: 2026-08-23
confidence: medium
---

# windows-software-policy

**windows-software-policy** documents and analyzes the Windows kernel **licensing path** exposed through the **`SystemPolicyInformation`** query class of **`NtQuerySystemInformation`**. It explains how user-mode licensing components communicate with the kernel policy driver and where policy data is handled. The repository includes **C** source and headers for low-level experimentation plus a **Python** helper script for related binary processing. (source: wiki/sources/descriptions/KiFilterFiberContext__windows-software-policy.md)

Useful for **Windows internals**, reverse engineering, and **software protection** research — complementary to user-mode anti-tamper frameworks such as [[anti-crack-system]] and kernel introspection tooling in [[overviews/windows-kernel]].

## Links

- Repo: https://github.com/KiFilterFiberContext/windows-software-policy

## Related

[[anti-crack-system]] · [[ntoskrnlwalker]] · [[winnt5-src-20201004]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
