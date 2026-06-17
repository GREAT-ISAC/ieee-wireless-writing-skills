# Output Format

For drafting:

- `Detected routing:` one line with mode, venue, area, section, and language.
- `Assumptions or missing inputs:` only when needed.
- Drafted prose in the requested language/style.
- `Evidence hooks:` list the figure, table, equation, theorem, or citation each major claim depends on.

For audits:

- Findings first, ordered by severity.
- Use `Issue`, `Why it matters for IEEE review`, and `Concrete fix`.
- Include claim-evidence, notation, citation, and experiment gaps when present.

For literature or direction tasks:

- Provide a paper-reading matrix or direction-ranking table.
- Score directions by novelty, execution risk, required evidence, reproducibility, and venue fit.
- For innovation ideation, include high-level missing evidence without designing experiment protocols.

For experiment-gap audits:

- Return a gap matrix with claim, current evidence, missing experiment/detail, review risk, and minimal manuscript-facing fix.
- Avoid implementation steps unless explicitly requested.

For reviewer responses:

- Preserve reviewer wording.
- Draft point-by-point responses with manuscript-location placeholders when exact line numbers are unknown.
- Mark unverifiable actions as `AUTHOR_INPUT_NEEDED`.
