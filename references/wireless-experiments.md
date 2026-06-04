# Wireless Experiment Design

Use experiments to prove specific claims.

## Baselines

Select baselines by role:

- Direct competitor: same task and setting.
- Classical baseline: LS/LMMSE/MMSE, OMP/CS, WMMSE, ZF/MMSE detector, greedy scheduler, convex relaxation, or model-specific heuristic.
- Learning baseline: strong neural or unfolding method with comparable input information.
- Ablation baseline: remove or replace one claimed module.

## Metrics

Choose metrics that match claims:

- Estimation: NMSE, MSE, downstream BER/BLER, spectral efficiency.
- Beamforming/resource allocation: sum rate, SINR, outage, fairness, energy efficiency.
- Sensing/localization: error, detection probability, false alarm, CRB, tracking error.
- Classification: accuracy, F1, confusion matrix, cross-domain accuracy.
- Practicality: complexity, runtime, latency, memory, pilot overhead, feedback bits.

## Conditions

Report enough detail for reproduction:

- SNR/SINR range.
- Antenna, user, subcarrier, bandwidth, carrier, mobility, channel model.
- Dataset split and leakage controls.
- Training hyperparameters for learning methods.
- Random seeds or trial count when available.

## Figure Logic

Each figure should answer one question:

- Main gain: Does the method beat direct competitors?
- Ablation: Which module creates the gain?
- Sensitivity: Does it hold across channel/SNR/mobility?
- Cost: What overhead or complexity is paid?
- Boundary: Where does it fail?
