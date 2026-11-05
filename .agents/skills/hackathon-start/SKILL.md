---
name: hackathon-start
description: Inspect an assignment's instructions, starter code, submission requirements, and environment; form a minimal specification and prioritized work list before implementation.
---
# Hackathon Start

Apply the kit AGENTS.md and actual task rules first. The kit is reference material,
not the assignment root. No installers, external model calls, or browser automation.

Read the actual README, AGENTS.md, submission instructions, manifests, existing
tests, and relevant source. Inspect installed runtime versions with bounded commands.
Identify required artifacts, deadlines, dependencies, and available execution tools.
Do not assume Next.js, a database, an API, fixed ports, or capabilities from examples.
Record observed facts separately from technical choices and unresolved questions.

Before implementing a behavior, establish its input/source, the user's intended
observable result, and its required acceptance condition from task evidence or the
user. If a missing business fact prevents those, record a Type 1 / CTX question in
QUESTIONS and draft it for Jay to send to the problem-owner Bot. If the gap is a
builder choice, record Type 2 / BLD and ask Jay. Record only the affected task as
blocked; do not invent data access or product scope.
Continue independent permitted checks. Technical details inferable from code are not
questions for the user.

If the user supplies a draft to discuss, use idea-partner before proposing a solution.
For missing business context, prepare concise questions for the platform's business
agent; Jay uses the platform messenger. Record actual answers and sources in QUESTIONS,
separately from interpretation. Do not invoke external people or sessions.
Do not ask Jay technical questions that the environment can answer.

Propose a minimal scope and priorities against actual acceptance conditions. If the
user has already confirmed the direction and implementation, proceed without another
approval cycle. Otherwise wait for that decision before implementation.

Use the templates by reading them and creating only relevant documents in the
assignment workspace, normally docs/hackathon/. Merge rather than overwrite existing
documents. Actual task-required filenames override this default.
- PRD: problem, audience, success, confirmed scope and exclusions.
- TRD: observed environment, chosen design, necessary data flow/interfaces, testing.
- REQUIREMENTS: current scope, requirement IDs, behavior and acceptance checks.
- TASKS: small ordered tasks with one owner and current status.
- DECISIONS: meaningful choices and reasons, not every routine edit.
- VERIFICATION: baseline commands/results and pending checks.
- QUESTIONS: Type 1 / CTX context facts for the Bot and Type 2 / BLD implementation
  choices for Jay; read existing answers before asking and link affected tasks.
- TECHNICAL_BRIEF: a plain-Korean explanation of the implementation for Jay. Read
  templates/TECHNICAL_BRIEF.md from the kit; create it in the assignment workspace
  once technical decisions exist, not as invented specifications during ideation.

Link requirement IDs across documents and tests. A database or API section may be
not applicable; never create infrastructure to fill a template. Explain the important
choices in Korean so Jay can understand the delivered system.

For implementation use tdd-delivery; completion uses delivery-review. Read skill files
by their kit paths when the host does not discover them automatically.
