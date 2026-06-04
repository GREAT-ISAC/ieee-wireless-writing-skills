# Literature and Direction Workflow

Use this when reading papers, building related work, or selecting a new IEEE wireless direction.

## Paper Reading Matrix

| Paper | Venue/year | Setting | Assumptions | Method | Evidence | Baselines | Limitation | Replication target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Extract from full papers whenever possible. Abstract-only reading is acceptable only for triage and must be labeled as such.

## Gap Types Worth Pursuing

- Assumption relaxation: imperfect CSI, pilot overhead, mobility, hardware impairments, quantization, blockage, non-stationarity.
- Evidence expansion: untested SNR range, cross-domain split, latency, scalability, or stress condition.
- Method delta: model-driven architecture, complexity reduction, robust optimization, overhead-aware design, or physically meaningful representation.
- System integration: joint communication-sensing, edge inference, feedback compression, scheduling, or deployment constraint.

Weak direction patterns:

- Replace one neural backbone with another without a wireless reason.
- Add "6G", "IoT", "vehicular", or "RIS" only in motivation.
- Use a new dataset but keep the same claim and method.
- Tune parameters without a new assumption, metric, or constraint.

## Direction Ranking

Score each direction from 1 to 5:

- Novelty against direct IEEE competitors.
- Execution risk.
- Evidence cost.
- Reproducibility.
- Fit for target venue.

Prefer the easiest credible direction, not the most ambitious one.
