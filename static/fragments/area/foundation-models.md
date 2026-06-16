# Area: Foundation Models for Wireless

Foundation-model papers need evidence that scale, pretraining, or transfer changes the wireless problem.

Require:

- Modality: CSI, IQ samples, channel matrices, spectrum waterfall, network logs, mobility traces, text/specification data, multimodal radio-sensing data, or protocol events.
- Pretraining objective: masked modeling, contrastive learning, autoregressive prediction, denoising, instruction tuning, reinforcement learning, or multimodal alignment.
- Transfer setting: cross-SNR, cross-channel, cross-band, cross-device, cross-cell, cross-environment, cross-task, or cross-dataset.
- Adaptation protocol: zero-shot, few-shot, linear probe, fine-tuning, prompt tuning, adapter, LoRA, or retrieval-augmented inference.
- Scale evidence: model size, data volume, compute, latency, memory, and scaling trend if the paper claims foundation-model behavior.

Avoid calling a model a foundation model when it is only a single-dataset supervised model with a larger backbone.
