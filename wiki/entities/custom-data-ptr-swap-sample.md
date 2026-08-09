---
title: custom_data_ptr_swap_sample
kind: entity
topics: [windows-kernel, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__custom_data_ptr_swap_sample.md
updated: 2026-08-09
confidence: medium
---

# custom_data_ptr_swap_sample

C/C++ kernel research sample centered on **`NtQueryLicenseValue`** as a stealth Ring0↔usermode communication path for driver development and modding research. (source: wiki/sources/descriptions/gmh5225__custom_data_ptr_swap_sample.md)

Mainly useful for game-security and reverse-engineering researchers mapping offensive KM↔UM channels that avoid obvious IOCTL or named-device surfaces — adjacent to data-ptr hook samples such as [[data-ptr-swap]], [[dataptrhookwin11]], and hook-based stealth I/O such as [[job-communication]] and [[evcommunication]].

## Links

- Repo: https://github.com/gmh5225/custom_data_ptr_swap_sample

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[data-ptr-swap]] · [[dataptrhookwin11]] · [[job-communication]] · [[evcommunication]]
