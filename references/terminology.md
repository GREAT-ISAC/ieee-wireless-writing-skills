# Wireless Terminology and Notation

Keep terminology consistent across the manuscript.

## Acronyms

Define acronyms at first use:

- CSI: channel state information.
- OFDM: orthogonal frequency-division multiplexing.
- MIMO: multiple-input multiple-output.
- RIS: reconfigurable intelligent surface.
- ISAC: integrated sensing and communications.
- SNR: signal-to-noise ratio.
- SINR: signal-to-interference-plus-noise ratio.
- NMSE: normalized mean square error.
- BER/BLER: bit/block error rate.
- FM: foundation model, but avoid the acronym unless the manuscript defines it clearly.
- AI-native wireless: use only when AI changes architecture, operation, or control logic, not when a standard model is merely applied offline.

## Notation Checks

- Use bold lowercase for vectors and bold uppercase for matrices if the manuscript follows that convention.
- Do not reuse the same symbol for channel, loss, and number of antennas.
- State dimensions for key matrices.
- Define whether complex Gaussian noise is circularly symmetric and what variance convention is used.
- Keep logarithm base and rate units clear.

## Claim Words

Use with evidence:

- `robust`: stress tests or uncertainty model.
- `real-time`: latency measurement and hardware/software context.
- `scalable`: complexity or large-system evidence.
- `generalizable`: cross-domain or theoretical support.
- `low-overhead`: pilot/feedback/control cost comparison.
- `foundation model`: pretraining scale, reusable representations, and transfer/adaptation evidence.
- `large-scale dataset`: sample count, diversity dimensions, metadata, and benchmark scope.
