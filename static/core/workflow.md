# Core Workflow

1. Intake: identify target venue, section, subarea, evidence artifacts, and missing inputs.
2. Problem framing: state the wireless problem in one sentence with entities, channel/traffic setting, and optimization/learning target.
3. Gap mapping: identify what prior work assumes, ignores, or cannot handle.
4. Contribution ledger: draft each contribution as `delta + evidence + boundary`.
5. Literature alignment: map each major claim to direct competitors and foundational references.
6. Method logic: connect system model, algorithm architecture, training/inference process, and complexity.
7. Experiment evidence audit: identify missing baselines, metrics, channel settings, ablations, stress tests, and reproducibility details before writing result prose; avoid full protocol design unless explicitly requested.
8. IEEE prose pass: tighten transitions, define acronyms, unify notation, remove hype, and keep paragraphs single-purpose.
9. QA pass: check claim-evidence alignment, citation role, notation consistency, figure/table readability, and venue fit.

Ask for missing artifacts only when the task cannot be completed without them. Otherwise proceed with explicit assumptions and mark unresolved items as `AUTHOR_INPUT_NEEDED`.
