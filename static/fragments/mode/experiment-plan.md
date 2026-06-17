# Mode: Experiment Plan

Use this mode only when the user explicitly asks for experiment design or planning. Otherwise use `experiment-gap-audit`.

Keep planning at the manuscript-evidence level unless implementation is explicitly requested.

Minimum experiment package:

- Direct communication baselines for the same task.
- A simple non-learning or classical baseline when relevant.
- Ablations for each claimed module.
- Sensitivity tests over channel, SNR, mobility, antenna count, pilot overhead, blockage, or traffic load as relevant.
- Complexity or latency evidence when claiming practical deployment.
- Failure cases or boundary tests for robustness claims.

Every planned figure must answer one review question. Do not modify project code, launch simulations, or write training scripts unless the user explicitly asks.
