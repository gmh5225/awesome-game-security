---
title: Raccine
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/Neo23x0__Raccine.md
updated: 2026-08-22
confidence: medium
---

# Raccine

Lightweight **Windows anti-ransomware** tool that blocks destructive shadow-copy deletion commands before they succeed. Registers as a debugger for utilities such as `vssadmin` and `wmic`, evaluates command-line behavior with **YARA rules**, and when malicious patterns match terminates the parent process chain and logs events—without requiring a resident agent service. (source: wiki/sources/descriptions/Neo23x0__Raccine.md)

The codebase combines C, C++, and C# components and targets defensive security operations and incident prevention. README category: `[EDR]`.

## Mechanism

| Layer | Approach |
|-------|----------|
| **Debugger registration** | Image File Execution Options–style attachment to `vssadmin`, `wmic`, and similar shadow-copy tools |
| **Command-line inspection** | YARA rule matching on invoked arguments |
| **Response** | Parent process-chain termination + event logging |
| **Deployment** | No persistent background service required |

## Positioning

Defensive counterpart to ransomware tradecraft that deletes Volume Shadow Copies before encryption. Complements SOC endpoint stacks such as [[wazuh]], detection-lab generators such as [[bamboozledr]], and YARA-oriented AC samples such as [[peregrine-anticheat]] on the EDR / incident-prevention side of game-security research.

## Links

- Repo: https://github.com/Neo23x0/Raccine

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[bamboozledr]] · [[the-hive]] · [[wazuh]] · [[peregrine-anticheat]] · [[pi-defender]]
