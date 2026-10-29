---
name: tdd-delivery
description: Implement an authorized specification in small behavior-tested increments, investigate failures at their root cause, and retain reproducible evidence of verification.
---
# TDD Delivery

Apply the kit AGENTS.md and actual task rules first. Require confirmed direction and
explicit implementation authorization; an earlier clear authorization remains valid.
Read the current REQUIREMENTS, TASKS, decisions, baseline tests, and code before editing.
Read ponytail/SKILL.md from the sibling directory for minimum complete changes.
This workflow selectively adapts Superpowers TDD, debugging, and verification ideas;
it does not activate upstream plugins. See [NOTICE](../../../third-party/NOTICE.md).

## Small behavior slices
1. Choose the next required behavior and its acceptance criterion.
2. Write a focused test exercising real behavior, using installed tooling first.
3. Run it and observe failure for the intended missing behavior, not a syntax/setup error.
4. Implement the smallest complete change, including affected callers and error handling.
5. Run the test, then relevant existing tests. Refactor only while behavior stays green.
6. Update TASKS and VERIFICATION with the actual command, result, and remaining limits.

Bug fixes start with a reproduction and a regression test when feasible. Inspect the
error, recent changes, and data flow; test one root-cause hypothesis at a time. Repeated
failed repairs require reassessing the cause, not stacking speculative patches.
Preserve valid tests and existing working code. Do not delete a supplied implementation
because it was written before your tests; do not weaken assertions to claim success.
For prose, trivial styling/configuration, or an unavailable test harness, use an
appropriate bounded check and label the limit honestly; do not pretend it was TDD.

## Bounded coordination
Use one implementer; if supported and useful, one independent investigator/reviewer may
check a separate question. Keep all agents within provided Codex and allowed models.
No recursive spawning, external sessions, automatic worktrees, or concurrent writes
to the same file. Give context, relevant paths, acceptance criteria, and a finite scope.
The coordinator inspects results and reruns appropriate verification before integration.
No subagent tool means sequential implementation and a separate review pass.

Do not silently add scope or paid/external services. If a task is blocked, record
which acceptance criterion is blocked and continue independent permitted work.
Before finishing, use delivery-review; never auto-push, deploy, or submit in EXAM.
