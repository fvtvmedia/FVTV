# Email Operations Contract

Nia Hourly Email Ops handles new inbound business mail, one necessary reply to a new human message, transactional/fulfillment email, dedupe/cleanup, calendar reconciliation, and Notion state sync.

**Claude owns all email follow-ups.** Nia sends zero reminders, check-ins, nudges, second touches, reactivation emails, unanswered-outreach follow-ups, or alternate-subject follow-ups. Future touches are logged as `Follow-up owner: Claude` with context and due/checkpoint date.

Treat one company + one business purpose as one contact stream.

Before every outbound send:
1. search full Gmail Sent/Inbox history;
2. read the canonical Notion record;
3. compare recipient, company/domain, purpose, and recent language;
4. collapse duplicate or near-duplicate pending tasks;
5. send nothing from duplicate records.

Maximum one outbound email per recipient in a run. No identical or materially similar pitch to the same recipient, person, company, domain, or business purpose within 24 hours. Different subject lines, aliases, inboxes, campaigns, agents, or FVTV brands do not make duplicates distinct.

Sent is not replied. Replied is not booked. Booked is not paid.
