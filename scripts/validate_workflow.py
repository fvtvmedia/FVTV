#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
"README.md","CONTRIBUTING.md","config/workflow-contract.json",
"docs/operations/source-of-truth.md","docs/operations/execution-routing.md","docs/operations/email-ops.md",
"docs/operations/video-production.md","docs/operations/drive-content-governance.md","docs/operations/interview-ops.md",
"docs/operations/accounting-controls.md","docs/operations/upwork-revenue.md",
"docs/editorial/README.md","docs/partners/README.md",
"ops/revenue/README.md","ops/partners/README.md","ops/editorial/README.md","ops/social/README.md","ops/video/README.md","ops/admin/README.md",
"schemas/task-record.schema.json","schemas/outreach-record.schema.json","schemas/video-manifest.schema.json",
"schemas/asset-record.schema.json","schemas/interview-record.schema.json","schemas/transaction-event.schema.json"
]
EXPECTED = ["NEW","READY","RUNNING","BLOCKED","WAITING","VERIFYING","REPAIR","DONE","CANCELLED"]
def fail(msg): raise SystemExit("workflow-contract: " + msg)
for rel in REQUIRED:
    if not (ROOT / rel).is_file(): fail("missing required file: " + rel)
c = json.loads((ROOT / "config/workflow-contract.json").read_text())
if c["source_of_truth"]["unfinished_work"] != "Notion: Nia Work Queue": fail("unfinished-work source drifted")
if c["runtime_states"] != EXPECTED: fail("runtime state contract drifted")
if c["github"]["business_task_queue"] is not False: fail("GitHub became business task queue")
if c["email"]["follow_up_owner"] != "Claude": fail("follow-up ownership drifted")
if c["email"]["duplicate_window_hours"] != 24: fail("duplicate window drifted")
if c["email"]["max_outbound_per_recipient_per_run"] != 1: fail("recipient run limit drifted")
expected_services = {"social_scheduler":"Metricool","interview_booking":"Calendly","interview_slot_minutes":60,"remote_interview_platform":"StreamYard","video_editor":"Filmora","voice_provider":"ElevenLabs","colab_active":False}
for k,v in expected_services.items():
    if c["services"].get(k) != v: fail("service contract drifted: " + k)
if not c["video"]["automatic_chatgpt_longform_hold"]: fail("automatic longform hold disabled")
if not c["video"]["automatic_elevenlabs_spend_hold"]: fail("automatic ElevenLabs spend hold disabled")
for path in (ROOT / "schemas").glob("*.json"):
    data = json.loads(path.read_text())
    if data.get("type") != "object" or "$schema" not in data: fail("invalid schema root: " + path.name)
print("workflow-contract: PASS")
