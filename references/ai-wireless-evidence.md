# AI+Wireless, Foundation Model, and Dataset Evidence

Use this reference when a manuscript claims AI-native wireless design, foundation-model capability, benchmark value, dataset contribution, or data-centric wireless research.

## Claim-Evidence Matrix

| Claim type | Required evidence | Common weak spot |
| --- | --- | --- |
| AI improves wireless performance | Direct wireless baselines, same input information, fair training/test protocol | Only compares against weak neural baselines |
| AI reduces overhead | Pilot/feedback/control-cost accounting | Ignores training or online adaptation cost |
| Model generalizes | Cross-domain split matching the claim | Random split leaks environment/session/user identity |
| Foundation model behavior | Pretraining scale, transfer across tasks/domains, adaptation protocol | Large supervised model is relabeled as foundation model |
| Dataset contribution | Collection setup, metadata, splits, labels, baseline tasks, license | Dataset is only described qualitatively |
| Benchmark value | Public tasks, metrics, baselines, versioning, leakage checks | No reproducible baseline scripts or split policy |

## Foundation-Model Checklist

- Name the radio modality and tokenization/representation.
- State whether pretraining is self-supervised, supervised, multimodal, contrastive, generative, or instruction-based.
- Define the transfer target and adaptation protocol.
- Report data volume, model size, compute, inference latency, and memory when practicality is claimed.
- Include classical and compact-model baselines when the task has established wireless methods.
- Separate pretraining benefit from architecture benefit through ablations.
- Avoid foundation-model wording unless the evidence shows reusable cross-task or cross-domain behavior.

## Dataset Checklist

- Provide a data card or dataset table with hardware, environment, frequency band, bandwidth, antennas, sampling rate, duration, labels, license, and privacy notes.
- Define official splits before reporting performance.
- Include leakage checks for user/session/location/time/environment.
- Provide benchmark tasks and metrics tied to wireless claims.
- Report data preprocessing and calibration steps.
- Use versioned releases when the dataset may evolve.

## Writing Patterns

Prefer:

`We pretrain [model] on [radio modality] from [data scope] using [objective], then evaluate transfer to [wireless tasks/domains] under [split].`

`The dataset supports [tasks] because it includes [diversity dimensions] and official [splits/metadata/baselines].`

Avoid:

- "AI-enabled" without a specific AI role.
- "Foundation model" without transfer evidence.
- "Large-scale dataset" without scale, diversity, and metadata.
- "Robust/generalizable" without cross-domain evaluation.
