# Repository Gap Audit — 2026-09-28

The repository described a broad operating system but contained mainly policy docs, three business issue forms, one hygiene workflow, and two operations docs. The README referenced multiple directories that did not exist, while the live Notion workflow had canonical lanes for execution routing, email, video, Drive, interviews, accounting, revenue/Upwork, and scheduler operations.

GitHub issues were also being used as a parallel business task queue even though the current canonical Notion architecture declares the Nia Work Queue the only unfinished-work queue.

Implemented:
- source-of-truth and execution-routing runbooks;
- email dedupe/follow-up contract;
- video production/release-gate contract;
- Drive asset classification/reuse contract;
- interview booking/platform contract;
- accounting/bookkeeping boundary;
- Upwork/revenue boundary;
- missing docs/ops directory map;
- machine-readable workflow contract;
- schemas for tasks, outreach, video manifests, assets, interviews, and bookkeeping events;
- workflow validator and CI;
- repository-only issue intake;
- historical reclassification of the old deliverable index.

Architectural decision: keep one technical monorepo/control layer by default. FVTV's current business architecture explicitly consolidates shared infrastructure and reduces duplicate systems. Split a component into its own repository only when an independent deployment, security boundary, release cadence, or ownership model justifies it.
