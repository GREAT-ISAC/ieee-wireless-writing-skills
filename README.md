# IEEE Wireless Writing Skill

`ieee-wireless-writing` is a Codex skill for drafting, polishing, auditing, and scaffolding IEEE-style wireless communications manuscripts. It is designed for papers targeting venues such as IEEE TWC, TVT, WCL, JSAC, TCOM, IoTJ, ICC, and GLOBECOM, with domain support for CSI, OFDM, MIMO, channel estimation, beamforming, RIS, ISAC, mmWave/THz, WiFi sensing, radio ML, and wireless networking.

The skill emphasizes evidence-bound writing: it helps convert ideas, notes, experiments, reviewer comments, and partial LaTeX drafts into IEEE-style technical prose while avoiding unsupported claims, fake citations, hidden assumptions, and over-broad novelty statements.

## Design Lineage

This skill is inspired by several community skills:

- [`Eroticoo/sci-writing`](https://github.com/Eroticoo/sci-writing): literature-to-paper workflow, direction selection, IEEE-style manuscript scaffolding, and experiment iteration.
- [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills): router-style skill design, manifest-driven fragments, and dynamic loading of journal/section/language rules.

This repository adapts those ideas specifically to IEEE wireless communications writing.

## What This Skill Does

Use this skill when you need help with:

- Drafting IEEE-style abstracts, introductions, related work, system models, methods, experiment sections, conclusions, and reviewer responses.
- Polishing Chinese-influenced English into concise IEEE technical English.
- Auditing contribution bullets, novelty claims, baselines, notation, and experiment evidence.
- Designing wireless communication experiments with fair baselines, metrics, ablations, and channel conditions.
- Creating an IEEEtran manuscript workspace with paper, notes, references, and experiment scaffolding.
- Preparing point-by-point reviewer responses without fabricating line numbers, experiments, or citations.

## Core Principles

The skill follows these rules:

- Do not invent citations, datasets, equations, baselines, channel models, line numbers, figure panels, numerical gains, or reviewer-requested changes.
- Treat every strong claim as a contract between manuscript text and evidence.
- Separate proven analysis, simulation/measurement observation, dataset facts, implementation details, and hypotheses.
- Prefer bounded IEEE-style technical claims over broad impact language.
- Make assumptions visible: CSI availability, channel model, SNR range, mobility, antenna configuration, pilots, bandwidth, carrier frequency, hardware constraints, dataset split, and traffic model.
- Compare against direct wireless baselines, not only generic machine learning or generic optimization baselines.

## Installation

Clone the repository and install it into your Codex skills directory.

Recommended installation name:

```bash
git clone https://github.com/Peter-jj/ieee-wireless-writing-skills.git ieee-wireless-writing
mkdir -p ~/.codex/skills
cp -R ieee-wireless-writing ~/.codex/skills/
```

Then restart Codex so the new skill is discovered.

The repository name may be `ieee-wireless-writing-skills`, but the skill name inside `SKILL.md` is:

```text
ieee-wireless-writing
```

Use this name when invoking the skill.

## Quick Start

Example prompts:

```text
Use $ieee-wireless-writing to polish this Chinese-English abstract for IEEE TWC. The paper is about CSI masked autoencoders for WiFi sensing.
```

```text
Use $ieee-wireless-writing to audit my introduction for a WCL submission. Focus on novelty, contribution bullets, and unsupported claims.
```

```text
Use $ieee-wireless-writing to draft the system model section for an OFDM channel-estimation paper with imperfect CSI and pilot overhead.
```

```text
Use $ieee-wireless-writing to create a reviewer-response plan from these IEEE TWC reviewer comments.
```

```text
Use $ieee-wireless-writing to scaffold a new IEEEtran paper workspace for a RIS-assisted ISAC manuscript.
```

## Routing Model

The skill uses a manifest-driven router:

```text
SKILL.md -> manifest.yaml -> static/core/* -> static/fragments/* -> references/*
```

`SKILL.md` is the entry point. It tells Codex to read `manifest.yaml`, load the core files, detect task axes, and then load only the fragments needed for the current request.

The routing axes are:

| Axis | Purpose | Examples |
| --- | --- | --- |
| `mode` | The user task type | `draft`, `polish`, `audit`, `scaffold`, `literature-direction`, `experiment-plan`, `reviewer-response` |
| `venue` | Target IEEE venue | `twc`, `tvt`, `wcl`, `jsac`, `tcom`, `iotj`, `conference`, `generic` |
| `area` | Wireless subarea | `csi`, `ofdm`, `channel-estimation`, `mimo-beamforming`, `ris`, `isac`, `mmwave-thz`, `wifi-sensing`, `radio-ml`, `networks` |
| `section` | Manuscript section | `title`, `abstract`, `introduction`, `related-work`, `system-model`, `method`, `experiments`, `discussion`, `conclusion` |
| `language` | Language/writing pattern | `en`, `zh-to-en` |

This keeps the main skill concise while allowing domain-specific behavior.

## Repository Structure

```text
.
├── SKILL.md
├── manifest.yaml
├── agents/
│   └── openai.yaml
├── static/
│   ├── core/
│   │   ├── output-format.md
│   │   ├── stance.md
│   │   └── workflow.md
│   └── fragments/
│       ├── area/
│       ├── language/
│       ├── mode/
│       ├── section/
│       └── venue/
├── references/
│   ├── claim-evidence.md
│   ├── ieee-latex.md
│   ├── literature-direction.md
│   ├── reviewer-response.md
│   ├── terminology.md
│   └── wireless-experiments.md
└── scripts/
    ├── build_ieee_pdf.sh
    └── init_ieee_wireless_project.py
```

## Script: Create an IEEE Wireless Paper Workspace

The skill includes a helper script for creating an IEEEtran-style paper workspace:

```bash
python scripts/init_ieee_wireless_project.py ./my-wireless-paper \
  --title "CSI Masked Autoencoder for Wireless Sensing" \
  --venue twc \
  --area csi \
  --author "Your Name" \
  --sim-lang python
```

Generated structure:

```text
my-wireless-paper/
├── paper/
│   ├── main.tex
│   ├── references.bib
│   ├── sections/
│   ├── figures/
│   └── tables/
├── notes/
│   ├── claim_evidence_matrix.md
│   ├── experiment_plan.md
│   ├── literature_matrix.md
│   ├── reviewer_response_tracker.md
│   └── terminology_ledger.md
└── experiments/
    └── main_experiment.py
```

For MATLAB-based work:

```bash
python scripts/init_ieee_wireless_project.py ./my-wireless-paper \
  --venue tvt \
  --area isac \
  --sim-lang matlab
```

## Script: Build the IEEE PDF

If `latexmk` and a LaTeX distribution are installed:

```bash
scripts/build_ieee_pdf.sh ./my-wireless-paper/paper
```

The output PDF is written to:

```text
./my-wireless-paper/paper/build/main.pdf
```

## Typical Workflows

### 1. Polish an Abstract

Use the skill with:

```text
Use $ieee-wireless-writing to polish this abstract for IEEE TWC. Area: CSI and WiFi sensing. Preserve the technical meaning and flag unsupported claims.
```

Expected behavior:

- Detect `mode=polish`, `venue=twc`, `area=csi,wifi-sensing`, `section=abstract`, `language=zh-to-en` or `en`.
- Rewrite the abstract with IEEE-style concision.
- Flag missing evidence such as unsupported robustness, generalization, or SOTA claims.

### 2. Audit an Introduction

Use:

```text
Use $ieee-wireless-writing to audit this introduction for WCL. Focus on whether the gap, contributions, and evidence are strong enough.
```

Expected behavior:

- Identify unsupported novelty claims.
- Check whether contribution bullets contain a technical delta and evidence hook.
- Recommend section-level fixes before sentence-level polish.

### 3. Build Related Work

Use:

```text
Use $ieee-wireless-writing to synthesize related work from these papers for a RIS-assisted ISAC manuscript.
```

Expected behavior:

- Build a paper-reading matrix.
- Group papers by technical limitation or method family.
- Avoid chronological citation lists.
- Convert the literature matrix into gap-driven related-work paragraphs.

### 4. Plan Experiments

Use:

```text
Use $ieee-wireless-writing to design experiments for a channel-estimation paper. Claims: low pilot overhead, better NMSE, and robust performance under mobility.
```

Expected behavior:

- Map each claim to a metric and figure.
- Propose direct wireless baselines such as LS, LMMSE/MMSE, OMP/CS, model-driven unfolding, or recent neural estimators when appropriate.
- Require SNR range, antenna count, pilot length, channel model, and mobility settings.

### 5. Prepare Reviewer Responses

Use:

```text
Use $ieee-wireless-writing to draft point-by-point responses to these IEEE TWC reviewer comments.
```

Expected behavior:

- Preserve reviewer comments.
- Assign IDs such as `R1.1`, `R1.2`, and `R2.1`.
- Draft respectful, technical responses.
- Mark missing line numbers, unfinished experiments, or unverifiable changes as `AUTHOR_INPUT_NEEDED`.

## Supported Venues

| Venue | Focus |
| --- | --- |
| Generic IEEE | Default IEEE journal/conference style |
| TWC | Wireless modeling depth, direct baselines, reproducible experiments |
| TVT | Mobility, vehicular channels, deployment constraints |
| WCL | Compact contribution, short evidence path |
| JSAC | Special-issue fit, system-level significance |
| TCOM | Communication-theoretic rigor, signal model, derivation |
| IoTJ | IoT constraints, scalability, energy, edge/device limitations |
| Conference | Crisp problem, compact evidence, direct contribution |

## Supported Wireless Areas

| Area | Typical checks |
| --- | --- |
| CSI | Acquisition, preprocessing, domain split, calibration, robustness |
| Channel estimation | Pilot overhead, channel model, NMSE, fair estimators |
| MIMO/beamforming | CSI assumptions, antenna/RF architecture, constraints |
| OFDM | Subcarrier/pilot design, synchronization, impairments |
| RIS | Cascaded CSI, phase quantization, training/control overhead |
| ISAC | Communication and sensing metrics, tradeoff curves |
| mmWave/THz | Blockage, beam training, near-field, hardware impairments |
| WiFi sensing | Device/session/user/location splits, leakage control |
| Radio ML | Input representation, baselines, latency, domain shift |
| Networks | Traffic, topology, scheduling, scalability, fairness |

## Extending the Skill

To add a new venue:

1. Create a file under `static/fragments/venue/`, for example `static/fragments/venue/tnse.md`.
2. Add it to `manifest.yaml` under `axes.venue.values`.
3. Keep the venue fragment short and focused on review expectations.

To add a new wireless area:

1. Create a file under `static/fragments/area/`.
2. Add it to `manifest.yaml` under `axes.area.values`.
3. Include assumptions, metrics, baselines, and claim boundaries for that area.

To add a new task mode:

1. Create a file under `static/fragments/mode/`.
2. Add it to `manifest.yaml` under `axes.mode.values`.
3. Add output expectations to `static/core/output-format.md` if needed.

## Validation

If you have Codex's `skill-creator` validation script available, run:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

You can also sanity-check the manifest paths:

```bash
python -c "from pathlib import Path; import yaml; root=Path('.'); data=yaml.safe_load((root/'manifest.yaml').read_text()); paths=list(data['always_load']); [paths.extend(v['values'].values()) for v in data['axes'].values()]; paths.extend(item['path'] for item in data['references']['on_demand']); missing=[p for p in paths if not (root/p).exists()]; print('all manifest paths exist' if not missing else missing)"
```

## Notes for Chinese Authors

This skill is especially useful for Chinese-to-English IEEE writing. It does not simply translate Chinese sentence order. It rewrites the argument into IEEE-style technical English:

- Replace broad openings such as "with the development of 6G" with the exact wireless bottleneck.
- Convert "has important significance" into a concrete system or performance reason.
- Turn long Chinese sentences into shorter IEEE-style technical sentences.
- Flag missing evidence instead of smoothing over weak claims.

## Limitations

- This is not an official IEEE tool.
- It does not replace target-journal author guidelines.
- It cannot verify citations, numerical results, or reviewer line numbers unless the user provides the source artifacts.
- It should not be used to fabricate experiments, citations, or claims.

## License

No license file is included yet. Add a license before broad public redistribution if you want others to reuse, modify, or redistribute the skill under clear terms.
