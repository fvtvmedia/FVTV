from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re


class Decision(str, Enum):
    REPLY_NEW_INBOUND = "REPLY_NEW_INBOUND"
    SEND_TRANSACTIONAL = "SEND_TRANSACTIONAL"
    HANDOFF_TO_CLAUDE = "HANDOFF_TO_CLAUDE"
    BLOCK_DUPLICATE = "BLOCK_DUPLICATE"
    OWNER_REVIEW = "OWNER_REVIEW"
    NO_ACTION = "NO_ACTION"


@dataclass(frozen=True)
class EmailState:
    latest_human_inbound: bool = False
    fvtv_replied_after_latest_inbound: bool = False
    transactional_necessity: bool = False
    follow_up: bool = False
    similar_outbound_within_24h: bool = False
    duplicate_stream_pending: bool = False
    outbound_to_recipient_already_this_run: bool = False
    do_not_contact: bool = False
    declined: bool = False
    closed: bool = False
    superseded: bool = False
    other_agent_owns_next_step: bool = False
    owner_approval_required: bool = False
    sender_identity_valid: bool = True


def normalize_key(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def stream_key(company_or_person: str, business_purpose: str) -> str:
    return f"{normalize_key(company_or_person)}::{normalize_key(business_purpose)}"


def decide(state: EmailState) -> Decision:
    # Suppression / closure beats every send path.
    if state.do_not_contact or state.declined or state.closed or state.superseded:
        return Decision.NO_ACTION

    # Identity or binding-authority problems cannot be automated.
    if state.owner_approval_required or not state.sender_identity_valid:
        return Decision.OWNER_REVIEW

    # Follow-up ownership is absolute.
    if state.follow_up:
        return Decision.HANDOFF_TO_CLAUDE

    # Duplicate protection is fail-closed.
    if (
        state.similar_outbound_within_24h
        or state.duplicate_stream_pending
        or state.outbound_to_recipient_already_this_run
    ):
        return Decision.BLOCK_DUPLICATE

    # Another worker already owns the next touch.
    if state.other_agent_owns_next_step:
        return Decision.NO_ACTION

    # Fresh inbound can receive one reply only if not already answered.
    if state.latest_human_inbound and not state.fvtv_replied_after_latest_inbound:
        return Decision.REPLY_NEW_INBOUND

    # Transactional mail is allowed when needed and non-duplicative.
    if state.transactional_necessity:
        return Decision.SEND_TRANSACTIONAL

    return Decision.NO_ACTION
