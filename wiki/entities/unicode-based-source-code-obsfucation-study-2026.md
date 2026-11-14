---
title: Unicode-based source code obfuscation study 2026
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/cxlines__unicode_based_source_code_obsfucation_study_2026.md
updated: 2026-11-14
confidence: medium
---

# Unicode-based source code obfuscation study 2026

**Reproducible ICRAS 2026 empirical benchmark** (cxlines) comparing **read-only static detectors** for **Unicode-based obfuscation in Python source**. Escalating analyzer tiers run from per-code-point scans through lexical token checks to **AST and symbol-table–aware rules**, including an extended **D3+** variant with mixed-script and contextual text handling; results are benchmarked against a fixed **Ruff** linter configuration on **CPython 3.14.7** with **Unicode 16.0.0** tables. Handcrafted inert fixtures cover bidirectional controls, confusable identifiers, default-ignorable characters, and NFKC-related spellings; sampled upstream release archives supply a second corpus. The package records localization and alert metrics with bootstrap intervals and ships scripts to fetch locked inputs, rebuild corpora, run tests, and regenerate figures **without executing** analyzed third-party sources—aimed at security researchers, static-analysis engineers, and reviewers quantifying tradeoffs between homoglyph/formatting attacks and false alerts on legitimate multilingual or test data in supply-chain and code-review workflows. (source: wiki/sources/descriptions/cxlines__unicode_based_source_code_obsfucation_study_2026.md)

README category: **Anti Cheat → Detection:Obfuscation**. Complements Python analyst tooling such as [[de4py]] and supply-chain static scanners such as [[fivem-backdoor-scanner]]; homoglyph-style identifier heuristics overlap [[leaf-mod-analyzer]] JAR triage.

## Links

- Repo: https://github.com/cxlines/unicode_based_source_code_obsfucation_study_2026

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[de4py]] · [[fivem-backdoor-scanner]] · [[leaf-mod-analyzer]] · [[binary-evidence]]