# Contributing to FVTV Workflow OS

This repository accepts technical implementation work: schemas, validation, workflow code, runbooks, CI, configuration, and repository documentation.

Do not use GitHub issues as a second business task queue. Live business work belongs in the canonical Notion Nia Work Queue.

Before changing a workflow, read the current canonical Notion page for the lane and confirm live provider state where applicable. Repository rules are a cache; live Notion wins on conflict.

Pull requests must state which canonical rule or bug they implement, preserve idempotency for writes and retries, include validation when behavior is machine-enforceable, and avoid private operational data.

A repository change is done only when the intended code exists, `python scripts/validate_workflow.py` passes, repository hygiene passes, and the intended branch/merge state is verified.
