# Drive Content Governance

Google Drive is the live asset store. GitHub stores schemas and rules only.

Prefer semantic names: `ROLE_Subject_Content-or-Event_Date-or-Version.ext`. Useful prefixes include SOURCE, REFERENCE, MASTER, FINAL, ROUGH, PUBLISHED. Downloader names, UUIDs, vague labels, and provider-generated IDs should not survive past intake once content is known.

Source-provider names are not final classification. Takeout/Google Photos/import-mechanism folders are temporary provenance, not durable working lanes.

Reusable content should have an explicit state: active, reusable, published, exhausted, do-not-reuse, graveyard, intake, provenance-only, private, or restricted.

Published/exhausted one-time content must be clearly marked so production workers do not accidentally reuse it. Eligible overlooked content should remain discoverable through descriptive naming/classification.

Before move/rename/delete of path-sensitive assets, inventory dependencies, preserve Drive IDs where practical, hash-verify exact duplicates before deletion, preserve originals/checkpoints, and verify downstream paths. Never invent an identity.
