import unittest

from decision_engine import Decision, EmailState, decide, stream_key


class TestDecisionEngine(unittest.TestCase):
    def test_fresh_inbound_replies(self):
        self.assertEqual(decide(EmailState(latest_human_inbound=True)), Decision.REPLY_NEW_INBOUND)

    def test_already_replied_blocks_second_reply(self):
        state = EmailState(latest_human_inbound=True, fvtv_replied_after_latest_inbound=True)
        self.assertEqual(decide(state), Decision.NO_ACTION)

    def test_followup_always_goes_to_claude(self):
        state = EmailState(follow_up=True, transactional_necessity=True)
        self.assertEqual(decide(state), Decision.HANDOFF_TO_CLAUDE)

    def test_duplicate_blocks(self):
        state = EmailState(latest_human_inbound=True, similar_outbound_within_24h=True)
        self.assertEqual(decide(state), Decision.BLOCK_DUPLICATE)

    def test_per_run_recipient_limit_blocks(self):
        state = EmailState(transactional_necessity=True, outbound_to_recipient_already_this_run=True)
        self.assertEqual(decide(state), Decision.BLOCK_DUPLICATE)

    def test_transactional_send(self):
        self.assertEqual(decide(EmailState(transactional_necessity=True)), Decision.SEND_TRANSACTIONAL)

    def test_owner_review_precedes_send(self):
        state = EmailState(latest_human_inbound=True, owner_approval_required=True)
        self.assertEqual(decide(state), Decision.OWNER_REVIEW)

    def test_suppression_precedes_everything(self):
        state = EmailState(latest_human_inbound=True, do_not_contact=True)
        self.assertEqual(decide(state), Decision.NO_ACTION)

    def test_stream_key_normalizes(self):
        self.assertEqual(stream_key("Acme, Inc.", "Interview Booking"), "acme-inc::interview-booking")


if __name__ == "__main__":
    unittest.main()
