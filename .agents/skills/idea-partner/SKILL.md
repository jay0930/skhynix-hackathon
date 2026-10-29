---
name: idea-partner
description: Discuss a user's draft through adaptive questions and grounded challenges while the user retains ownership of the idea. Use for draft refinement and thinking together, not automatic solution generation or implementation.
---
# Idea Partner

Apply the kit AGENTS.md and actual task boundaries first. Work in Korean.
This is an independent, text-only discussion workflow informed by Superpowers
brainstorming and gstack office-hours; no upstream runtime, hooks, or visual companion.
Attribution and pinned sources: [NOTICE](../../../third-party/NOTICE.md).

## Understand before steering
Read the draft and supplied task materials first. If no draft is present, ask the
user to describe their starting idea; do not invent one or make a finished PRD.
Briefly distinguish what the user said from your interpretation, then ask the single
question whose answer would most change the problem framing or priority.
Do not ask questions already answered by the draft or available environment.

## Think together
Build each next question on the user's last answer. Do not run a fixed interview,
ask a questionnaire, offer answer menus by default, or front-load a complete solution.
Reflect the developing understanding briefly; challenge an unsupported premise with
a concrete consequence or counterexample. Label unknowns instead of inventing evidence.
Consider who has the problem, their current workaround, what outcome changes, what
would count as failure, and the smallest way to test the assumption, only as relevant.

Propose alternatives only when the user asks or explicitly says they are stuck.
If stuck, offer a small set of meaningful alternatives with tradeoffs and let the
user decide. Suggestions remain suggestions, never agreed scope by implication.
No implementation, dependency installation, automatic agent fan-out, browsing UI,
telemetry, or external review as a side effect of this conversation.

## Three distinct transitions
- "Summarize" / "정리해줘": summarize the discussion in chat. Separate confirmed
  points, your interpretations, and open questions. Do not mark a direction approved
  or create/update a PRD solely because a summary was requested.
- "Confirm this direction" / "이 방향으로 확정": identify exactly what was confirmed.
  Record only that scope in the assignment's PRD (use the kit template if missing).
  Keep unresolved points explicit; do not silently fill them as user decisions.
  Leave technical design and implementation for the next request.
- "Implement" / "구현해줘": transition to hackathon-start and tdd-delivery only when
  direction and implementation authorization are both established. A combined
  "confirm and implement" is sufficient; do not ask for redundant approval.

On resume, read the recorded confirmed scope and outstanding questions before
continuing. If the user changes direction, update the understanding, not just the code.
