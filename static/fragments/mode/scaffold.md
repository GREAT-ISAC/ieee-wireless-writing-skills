# Mode: Scaffold

Use the scaffold mode when the user wants a paper workspace, IEEEtran skeleton, or notes structure.

Preferred command:

```bash
python scripts/init_ieee_wireless_project.py ./my-wireless-paper \
  --title "Working Title" \
  --venue twc \
  --area csi \
  --sim-lang python
```

After scaffolding, immediately fill:

- `notes/claim_evidence_matrix.md`
- `notes/literature_matrix.md`
- `notes/experiment_plan.md`
- `notes/terminology_ledger.md`

Keep the project in IEEE format from the start. Do not draft in a generic article template and retrofit near submission.
