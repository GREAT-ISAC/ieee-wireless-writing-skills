# Mode: Experiment Gap Audit

Audit experiment evidence as a reviewer-facing sufficiency check, not as a full experiment-design task.

Return a gap matrix with:

- Claim or result statement.
- Available evidence: figure, table, log, theorem, dataset card, or note.
- Missing experiment or detail.
- Review risk if it remains missing.
- Minimal manuscript-facing fix: add evidence, narrow the claim, cite a boundary, or mark `AUTHOR_INPUT_NEEDED`.

Prioritize missing baselines, unfair comparisons, absent ablations, narrow channel/SNR/mobility coverage, missing complexity or latency evidence, dataset leakage risk, and unreproducible settings. Do not propose implementation steps, training scripts, or simulation code changes unless the user explicitly asks.
