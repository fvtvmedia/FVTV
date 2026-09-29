# Execution Routing

Chat handles research, writing, analysis, connectors, Gmail, Calendar, Notion, source verification, and bounded connected-tool work.

Work handles authenticated browser execution, multi-app workflows, live forms, uploads, portals, and dashboard/browser actions Chat cannot operate.

Codex handles code, local files, media conversion, technical QA, website implementation, and computer-control work.

Owner/external is reserved for irreducible gates: signatures, device-bound 2FA, CAPTCHA, binding personal attestations, unapproved spending, physical actions, or facts unavailable elsewhere.

A browser limitation in Chat is not automatically an owner gate. Escalate to Work first.

Runtime states: NEW, READY, RUNNING, BLOCKED, WAITING, VERIFYING, REPAIR, DONE, CANCELLED.

Before side effects: re-read live state, confirm dependencies/authority, compute an input fingerprint where practical, check whether the intended side effect already exists, then claim the work.

DONE requires the definition of done, verification, durable completion evidence, artifact refs when applicable, and current verification for mutable state. Never repeat the same failed action more than twice without changing method or evidence.
