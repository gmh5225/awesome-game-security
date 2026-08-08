---
title: job_communication
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__job_communication.md
updated: 2026-08-08
confidence: medium
---

# job_communication

Small proof-of-concept for **undocumented Ring0↔Ring3 communication** via `NtQueryInformationJobObject` instead of monitored device IOCTL paths. (source: wiki/sources/descriptions/gmh5225__job_communication.md)

Kernel-side notes describe checking the current process **Job** field, resolving the job's server silo with `PsGetJobServerSilo`, and copying data from `ServerSiloGlobals` or `UserSharedData` into the output buffer returned to user mode. The user-mode sample calls `NtQueryInformationJobObject` with **`JobObjectReserved17Information`** and interprets returned **`SILO_USER_SHARED_DATA`** fields as the hidden communication result.

Mainly useful for Windows internals researchers studying obscure job-object and silo-based communication paths that bypass standard device IOCTL interfaces — adjacent to hook-based stealth I/O such as [[evcommunication]], [[kernel-payload-comms]], and [[read-write-driver]].

## Links

- Repo: https://github.com/gmh5225/job_communication

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[evcommunication]] · [[kernel-payload-comms]] · [[gina-public]]
