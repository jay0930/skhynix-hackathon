---
name: delivery-review
description: Check a deliverable against confirmed requirements, inspect implementation and test evidence, and prepare an honest handoff before the participant manually submits.
---
# Delivery Review

Apply the kit AGENTS.md and actual submission rules first. During EXAM, no automated
browser/UI actions, external review, pushing, deployment, or submission. In PREPARATION,
an explicitly authorized generic-kit publication is a separate maintainer action,
not part of this assignment review workflow. This independent local
review draws on gstack review and Superpowers verification; see [NOTICE](../../../third-party/NOTICE.md).

Read the confirmed PRD, REQUIREMENTS, TASKS, DECISIONS, and actual changes. Check that
the solution addresses the user's problem, not just a convenient technical substitute.
Map every required behavior to code and a test or clearly named manual check.
Review error handling, input boundaries, state consistency, avoidable complexity,
and the effects of changed shared code on callers. Do not invent new feature scope.

Run appropriate installed tests, lint, and build commands against the final code.
Use the full project test suite when feasible. If time or environment prevents it,
report exactly which checks ran and which did not; never extrapolate a partial pass.
Inspect exit status and actual output. A prior success or another agent's claim is
not fresh evidence. Report pre-existing failures separately without hiding them.

Terminal HTTP checks are allowed where permitted; automated browser tests are not.
For a web preview, keep the server bound to 0.0.0.0 at its actual port, then give Jay
short manual steps for the platform Browser. Do not create a tunnel or alter protection.
Only record a manual check as passed after Jay reports its result. Otherwise pending.

Update VERIFICATION with command/results/coverage limits, TASKS with actual status,
and DECISIONS with meaningful changes. Explain the problem solved, key design choices,
what was tested, and known limits in plain Korean before the essay stage.

Check actual required filenames, paths, saved state, and unintended files; do not
assume hidden files or /tmp are excluded from submission. The participant handles the
platform preview, final confirmation, and completion-screen verification manually.
Once follow-up essays start, stop assistance entirely. No essay questions or answers.
