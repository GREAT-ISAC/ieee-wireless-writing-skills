# IEEE LaTeX Guidance

Use IEEEtran from the start when preparing an IEEE journal or conference manuscript.

Recommended structure:

```text
paper/
  main.tex
  references.bib
  sections/
    01_introduction.tex
    02_related_work.tex
    03_system_model.tex
    04_method.tex
    05_experiments.tex
    06_conclusion.tex
  figures/
  tables/
notes/
  claim_evidence_matrix.md
  literature_matrix.md
  experiment_plan.md
  terminology_ledger.md
experiments/
  python/ or matlab/
```

Build:

```bash
scripts/build_ieee_pdf.sh ./paper
```

Rules:

- Keep figures readable in one-column or two-column IEEE width.
- Use vector PDF/EPS for line plots when possible.
- Use `\IEEEPARstart` only if the venue/template expects it.
- Avoid manual vertical spacing until the final layout pass.
- Keep equations numbered only when referenced.
- Put unsupported citation placeholders in notes instead of fake `.bib` entries.
