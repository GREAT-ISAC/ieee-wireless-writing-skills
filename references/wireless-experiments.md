# Wireless Experiment Evidence Audit

Audit whether the available experiments prove the manuscript's specific claims. Prefer missing-evidence analysis over experiment design unless the user explicitly asks for a protocol.

## Baselines

Check whether baselines cover these roles:

- Direct competitor: same task and setting.
- Classical baseline: LS/LMMSE/MMSE, OMP/CS, WMMSE, ZF/MMSE detector, greedy scheduler, convex relaxation, or model-specific heuristic.
- Learning baseline: strong neural or unfolding method with comparable input information.
- Ablation baseline: remove or replace one claimed module.
- Foundation-model baseline: pretrained, fine-tuned, linear-probe, few-shot, zero-shot, adapter, or compact supervised variants when foundation-model claims are made.

## Metrics

Check whether metrics match claims:

- Estimation: NMSE, MSE, downstream BER/BLER, spectral efficiency.
- Beamforming/resource allocation: sum rate, SINR, outage, fairness, energy efficiency.
- Sensing/localization: error, detection probability, false alarm, CRB, tracking error.
- Classification: accuracy, F1, confusion matrix, cross-domain accuracy.
- Foundation models: transfer accuracy, sample efficiency, adaptation cost, zero/few-shot performance, cross-domain robustness.
- Datasets: coverage, diversity, split leakage, label quality, benchmark reproducibility.
- Practicality: complexity, runtime, latency, memory, pilot overhead, feedback bits.

## Conditions

Check whether the manuscript reports enough detail for reproduction:

- SNR/SINR range.
- Antenna, user, subcarrier, bandwidth, carrier, mobility, channel model.
- Dataset split and leakage controls.
- Training hyperparameters for learning methods.
- Pretraining data scope, adaptation protocol, and dataset split policy for AI+wireless or foundation-model claims.
- Dataset hardware, environment, metadata, license, and leakage-control details for dataset papers.
- Random seeds or trial count when available.

## Figure Logic

Each existing or missing figure should answer one question:

- Main gain: Does the method beat direct competitors?
- Ablation: Which module creates the gain?
- Sensitivity: Does it hold across channel/SNR/mobility?
- Cost: What overhead or complexity is paid?
- Boundary: Where does it fail?
- Transfer: Does pretraining help outside the source domain?
- Leakage: Does performance remain after user/session/location/time leakage controls?

## Gap Output

For experiment-section audits, return a compact matrix:

- Claim.
- Current evidence.
- Missing evidence or setting.
- Review risk.
- Minimal fix: add evidence, narrow the claim, cite a boundary, or mark `AUTHOR_INPUT_NEEDED`.

Do not prescribe code edits, hyperparameter sweeps, training commands, or simulation scripts unless the user explicitly asks for implementation.
