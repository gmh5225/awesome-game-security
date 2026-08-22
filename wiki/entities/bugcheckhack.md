---
title: BugCheckHack
kind: entity
topics: [windows-kernel]
sources:
  - wiki/sources/descriptions/NSG650__BugCheckHack.md
updated: 2026-08-22
confidence: medium
---

# BugCheckHack

Windows **kernel driver** plus **user-mode utility** for modifying **BSOD appearance and behavior**. Loads the driver through a **service workflow**, resolves required **kernel offsets**, and **patches bugcheck-related routines**; C/C++ codebase with a desktop controller and supporting kernel components. (source: wiki/sources/descriptions/NSG650__BugCheckHack.md)

Research lane: **low-level Windows crash-mechanism** study and demonstration of **kernel patching** on the bugcheck path—not a production stability tool. Part of the NSG650 bugcheck-research family alongside suppression PoCs such as [[nomore-bugcheck]] and visual crash hacks such as [[bad-bugcheck]].

## Links

- Repo: https://github.com/NSG650/BugCheckHack

## Related

[[bad-bugcheck]] · [[bugcheck2linux]] · [[nomore-bugcheck]] · [[nomore-bugcheck-reloaded]] · [[bugcheck-suppressor]] · [[patchguard]] · [[overviews/windows-kernel]]
