# Area: OFDM

OFDM work must expose:

- Subcarrier count, cyclic prefix, pilot pattern, modulation, coding if used, and synchronization assumptions.
- Impairments: CFO, SFO, phase noise, IQ imbalance, clipping, nonlinear PA, Doppler, or multipath selectivity.
- Whether the method operates per-subcarrier, across time-frequency grids, or in delay-Doppler/angle-delay domains.

Avoid hiding pilot overhead or synchronization cost when claiming spectral-efficiency gains.
