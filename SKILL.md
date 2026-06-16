---
name: ieee-wireless-writing
description: Draft, restructure, polish, audit, or scaffold IEEE-style wireless communications manuscripts, magazine articles, and reviewer responses. Use for IEEE TWC, TVT, WCL, JSAC, TCOM, IoTJ, IEEE Wireless Communications, ICC, GLOBECOM, and work involving CSI, OFDM, MIMO, channel estimation, beamforming, RIS, ISAC, mmWave, THz, WiFi sensing, radio ML, AI+wireless, foundation models, wireless datasets, network optimization, IEEEtran LaTeX, literature-gap mapping, claim-evidence audits, experiments, rebuttals, or Chinese-to-English wireless paper writing.
---

# IEEE Wireless Writing

## Router

Use this skill to move a wireless communications paper from evidence to an IEEE-ready manuscript. The design combines a literature-to-manuscript workflow with a short router and on-demand fragments.

Always run this routing protocol:

1. Read [manifest.yaml](manifest.yaml).
2. Read every file listed under `always_load`.
3. Detect these axes from the user request: `mode`, `venue`, `area`, `section`, and `language`.
4. State the detected axes in one short line so the user can correct routing cheaply.
5. Load only the fragments mapped by the selected axis values. Do not load every file under `static/`.
6. Reach for `references/` only when a workflow step needs deeper rules.

## Workflow

Follow the core workflow unless the user asks only for a small local edit:

1. Gather artifacts: PDF papers, TeX files, figures, tables, code, logs, reviewer comments, or Chinese notes.
2. Build or update the claim-evidence map before strengthening any claim.
3. Separate evidence types: proven analysis, simulation/measurement observation, dataset fact, implementation detail, and hypothesis.
4. For literature or direction tasks, read [references/literature-direction.md](references/literature-direction.md).
5. For drafting or restructuring, load the relevant section fragment and write around problem, gap, method, evidence, and boundary.
6. For experiment planning or result sections, read [references/wireless-experiments.md](references/wireless-experiments.md).
7. For venue-sensitive work, apply the venue fragment after section logic and before sentence polish.
8. For LaTeX project setup, run `scripts/init_ieee_wireless_project.py` and then use [references/ieee-latex.md](references/ieee-latex.md).
9. For reviewer responses, load `static/fragments/mode/reviewer-response.md` and [references/reviewer-response.md](references/reviewer-response.md).

## Operating Rules

- Do not invent citations, datasets, equations, baselines, channel models, line numbers, figure panels, SNR ranges, mobility settings, or reviewer-requested changes.
- Treat unsupported factual, novelty, or superiority statements as blockers. Either add evidence, cite a primary source, weaken the claim, or mark `AUTHOR_INPUT_NEEDED`.
- Prefer IEEE-style precision over broad-impact language: define the wireless setting, assumptions, variables, channel model, metrics, baselines, and reproducibility boundary.
- Keep related work analytical: group by technical limitation and direct competitor, not by a chronological list of citations.
- Keep contribution bullets concrete: each bullet must name the method/theory/system delta and its supporting evidence.
- Preserve mathematical notation and acronym definitions consistently across abstract, body, figures, and tables.

## Resources

- [manifest.yaml](manifest.yaml): Axis definitions and fragment map.
- `static/core/`: Default stance, workflow, and output package.
- `static/fragments/`: Mode, venue, area, section, and language rules loaded on demand.
- [references/claim-evidence.md](references/claim-evidence.md): Claim audit and evidence matrix.
- [references/literature-direction.md](references/literature-direction.md): Paper reading, gap extraction, and direction ranking.
- [references/wireless-experiments.md](references/wireless-experiments.md): Baseline, metric, ablation, and channel-condition rules.
- [references/ai-wireless-evidence.md](references/ai-wireless-evidence.md): AI+wireless, foundation-model, and dataset evidence rules.
- [references/ieee-latex.md](references/ieee-latex.md): IEEEtran project and build guidance.
- [references/reviewer-response.md](references/reviewer-response.md): Point-by-point response workflow.
- [references/terminology.md](references/terminology.md): Wireless terminology and notation guardrails.
- `scripts/init_ieee_wireless_project.py`: Create an IEEEtran manuscript workspace with notes and experiment folders.
- `scripts/build_ieee_pdf.sh`: Compile an IEEEtran manuscript with `latexmk`.
