# Owned-Build Robustness and Diagnostic Triage

Use this reference to review source-level diagnostics and regression evidence
for owned game, engine, parser, plugin, or backend test builds. A crash, sanitizer
finding, game bug, and exploitable security defect are different conclusions.

## Start with the Correctness Contract

Record the input boundary, supported format/state, ownership/lifetime rules,
concurrency assumptions, resource budget, and expected failure behavior. Useful
contracts include bounded asset import, parser error handling, object lifetime,
single-owner state changes, and server-authorized transitions.

Choose diagnostics appropriate to that contract:

| Diagnostic | Useful evidence | Limitation to preserve |
|---|---|---|
| AddressSanitizer | Instrumented memory-error reports, including out-of-bounds and lifetime errors | Coverage depends on execution and instrumentation; absence of a report is not proof of safety |
| UndefinedBehaviorSanitizer | Selected language/runtime undefined-behavior checks | Check groups differ; unsigned overflow is not C/C++ undefined behavior and has a separate optional check |
| ThreadSanitizer | Instrumented data-race observations | Timing, instrumentation coverage and runtime overhead affect interpretation |
| Functional/state fixtures | Expected authorization, transaction, parser and resource behavior | Passing chosen cases does not establish all-state correctness |

[LLVM AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html),
[LLVM UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html),
[LLVM ThreadSanitizer](https://clang.llvm.org/docs/ThreadSanitizer.html)

TSan's runtime is not intended for production executables. Avoid a blanket rule
about every sanitizer runtime: LLVM also documents a minimal UBSan runtime
designed for production use. Decide deployment separately from test usefulness.

## Preserve and Interpret the Report

Keep source/build identifiers, compiler and runtime versions, instrumentation
configuration, fixture identity, symbolized diagnostics, logs, and expected
versus observed results. Start from the earliest reliable diagnostic and identify
the violated contract; later symptoms may be consequences of the same root cause.

Separate duplicate symptoms, tool limitations, compatibility problems, and
security impact. A stack trace alone does not establish attacker reachability,
required privilege, or real-world exploitability. Record those as unknown unless
supported independently. Use narrow, justified suppressions with reviewable scope.

After a fix, retain a focused regression case in the owned suite and check
relevant release-build behavior separately. Instrumentation changes execution,
layout and timing; do not mix its telemetry into enforcement datasets without
explicitly accounting for that difference.

## Connect Testing to Remediation

Associate findings with the affected component/version, remediation owner,
root-cause class, fix evidence, regression coverage, and release decision. Static
review, dynamic diagnostics and functional checks contribute different evidence.
Neither a green build nor a tool label certifies the whole product.
[NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)

Primary sources reviewed: 2026-09-09. The LLVM references describe diagnostic
contracts; the game-specific review workflow is a synthesis of those contracts.
