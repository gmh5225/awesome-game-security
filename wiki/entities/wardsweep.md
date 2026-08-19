---
title: WardSweep
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/poli0981__wardsweep.md
updated: 2026-08-19
confidence: medium
---

# WardSweep

Windows tool for uninstalling games that ship kernel-mode anti-cheat and cleaning up orphaned drivers, services, registry entries, and filesystem residue those titles leave behind. Combines a Rust elevated broker and CLI with a C# WPF user interface, using a signed TOML catalog to detect products such as [[vanguard]], [[easy-anti-cheat]], [[battleye]], and ACE. Core workflows include read-only auditing, game removal through official uninstallers, and orphan sweeps for anti-cheat residue after games are gone—with quarantine, rollback manifests, path deny-lists, and split-privilege IPC to limit destructive actions. Aimed at legitimate system cleanup rather than bypassing or disabling anti-cheat while games remain playable; explicitly rejects ban evasion, runtime tampering, and hardware identifier modification. (source: wiki/sources/descriptions/poli0981__wardsweep.md)

Complements forensic inspection tools such as [[openark]] on the same driver/service/registry surfaces from a post-uninstall maintenance angle—not an AC bypass lane.

## Links

- Repo: https://github.com/poli0981/wardsweep

## Related

[[easy-anti-cheat]] · [[battleye]] · [[vanguard]] · [[openark]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
