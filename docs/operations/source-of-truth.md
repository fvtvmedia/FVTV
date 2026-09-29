# Source-of-Truth Routing

GitHub is a technical implementation surface. It never outranks live operational state.

| Domain | Canonical source |
|---|---|
| Unfinished work | Notion — Nia Work Queue |
| Runtime/dependency model | Notion — Execution Graph Control Plane |
| Editorial/publishing rules | Notion — FVTV Posting Rules v3 |
| Video-production rules | Notion — FVTV Video Production Entry Point |
| Email/thread state | Gmail + canonical Notion record |
| File/asset state | Google Drive + canonical Notion record |
| Scheduling/publishing state | Metricool |
| Interview booking | Calendly |
| Remote interview recording | StreamYard |
| Transactions/bookkeeping/equipment | Notion — Accounting & Bookkeeping HQ |
| Pricing/offers | Notion — FVTV Services & Rates |
| Code/schemas/CI | GitHub |

Precedence: current owner direction, current canonical Notion rule, verified provider state, then repository cache.

Do not create a GitHub issue merely because a business task exists. GitHub issues are limited to repository implementation, code/schema/validator defects, CI failures, and technical debt belonging to this repository.
