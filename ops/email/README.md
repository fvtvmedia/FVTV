# Nia Email Ops Engine

This module is the executable policy layer behind the hourly Nia email worker.

The live worker runs in ChatGPT Automations and uses connected Gmail + Notion. This code makes the decision rules deterministic and testable so future implementations do not reinterpret them.

## Allowed outcomes

- REPLY_NEW_INBOUND
- SEND_TRANSACTIONAL
- HANDOFF_TO_CLAUDE
- BLOCK_DUPLICATE
- OWNER_REVIEW
- NO_ACTION

## Hard rules

1. Nia replies only to a fresh human inbound when no FVTV reply already answers it.
2. Nia may send transactional/fulfillment mail for an active transaction, confirmed appointment, paid fulfillment, explicit reschedule, or direct recipient request.
3. Nia sends zero follow-ups. Claude owns every reminder/check-in/reactivation/second touch.
4. One company + one business purpose = one contact stream.
5. Max one outbound to the same recipient per run.
6. No materially similar outbound within 24 hours to the same recipient/person/company/domain/business purpose.
7. Existing relevant threads are reused.
8. Decline, opt-out, do-not-contact, closed state, superseding context, or another agent owning the next step prevents a Nia send.
9. Binding terms, unapproved pricing, spend, legal commitments, rights/exclusivity, refunds outside policy, or unclear authority route to OWNER_REVIEW.
10. Sender identity is Nia Brooks / FVTV Media.

## Runtime

The active scheduled worker is `Nia Hourly Email Ops`. Notion remains source of truth. Gmail is source of truth for actual message/thread state.
