# FVTV Workflow OS

This repository is the public-safe technical control layer for FVTV Media. It stores workflow contracts, schemas, validation code, technical runbooks, and implementation history.

It is **not** the live business task queue.

## Source of truth

Live operating state stays in the connected private systems:

- **Notion — Nia Work Queue:** only canonical unfinished-work queue.
- **Notion — Execution Graph Control Plane:** runtime states, dependencies, authority gates, verification, idempotency, and WIP rules.
- **Notion — FVTV Posting Rules v3:** live editorial, publishing, scheduler, voice, media, and production rules.
- **Notion — FVTV Video Production Entry Point:** live video-production handoff and release contract.
- **Notion — Accounting & Bookkeeping HQ:** actual transactions, allocations, recurring costs, bills, receivables, and equipment.
- **Notion — FVTV Services & Rates:** current commercial offers and pricing.
- **Notion — FVTV Remote Artist Interview Workflow:** booking, payment, platform, preflight, recording, and post-production rules.
- **Gmail:** actual email/thread state.
- **Google Drive:** actual file/asset state.
- **Metricool:** actual scheduling and publishing state.
- **GitHub:** code, schemas, technical QA, and implementation artifacts only.

When a cached rule here conflicts with live Notion, the live Notion rule wins.

## Current business architecture

FVTV Media is the single current business umbrella. Current service lines are FVTV Production, FVTV Creative, FVTV Studios, FVTV Media / Partnerships / Editorial, and Culture Intelligence. Gold Vision Films / GVF and KR3ATIVE are legacy provenance only. Keylo Nsane and SFTS remain separate public brands.

## Repository map

| Path | Purpose |
|---|---|
| `config/workflow-contract.json` | Machine-readable cross-system contract |
| `schemas/` | Public-safe schemas for tasks, outreach, media, interviews, assets, and bookkeeping events |
| `scripts/validate_workflow.py` | Structural and contract validation |
| `docs/operations/` | Technical runbooks derived from live Notion rules |
| `docs/editorial/` | Editorial implementation boundary and source-of-truth notes |
| `docs/partners/` | Partner implementation boundary and privacy rules |
| `ops/revenue/` | Revenue-system implementation notes, never live leads |
| `ops/partners/` | Partner-system implementation notes, never private correspondence |
| `ops/editorial/` | Editorial technical controls, never the live content queue |
| `ops/social/` | Scheduler and publishing technical controls |
| `ops/video/` | Video manifests, gates, and production implementation |
| `ops/admin/` | Drive/accounting/admin technical controls |
| `.github/ISSUE_TEMPLATE/` | Repository-change and workflow-bug intake only |
| `.github/workflows/` | Repository and workflow-contract validation |

## Runtime states

Technical workflow code uses the canonical Notion execution states:
`NEW, READY, RUNNING, BLOCKED, WAITING, VERIFYING, REPAIR, DONE, CANCELLED`.

A generated artifact is not DONE until the definition of done is satisfied and completion evidence is verified. Writes must be idempotent: do not duplicate emails, posts, calendar events, files, tasks, or outreach.

## GitHub working method

GitHub issues are for **repository changes and workflow bugs**, not business leads, content assignments, partner follow-ups, interview scheduling, or revenue opportunities. Those belong in the Nia Work Queue and their canonical private systems.

See `docs/operations/repo-gap-audit.md` for the implementation audit.
