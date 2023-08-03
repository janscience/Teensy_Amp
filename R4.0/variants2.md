# Testing high-pass filter without low-pass

If not noted otherwise, all measurements at 48kHz sampling rate.


## Signal-filter

![filter](images/filtervariants2.png)

| Component | 1-CH* | 2-CH* |
| --------- | ----- | ----- |
| R1        | 1k    | 1k    |
| R2        | 0     | 0     |
| C2        | -     | -     |

### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- 0dB gain, 700mV rms sine wave:

  ![variants2-sig-gain1x1](images/variants2-sig1kHz700mV-gain1x1-spectra.png)

- 20dB gain, 70mV rms sine wave:

  ![variants2-sig-gain1x10](images/variants2-sig1kHz70mV-gain1x10-spectra.png)

- 40dB gain, 7mV rms sine wave:

  ![variants2-sig-gain1x100](images/variants2-sig1kHz7mV-gain1x100-spectra.png)


### High-pass filter

Measurement with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

![HP1k](images/variants2-filter-700mV-gain1x1-traces.png)


## Pre-amplifier

![preampinv](images/preampinvvariants2.png)

| Component | 1-CH* | 2-CH* |
| --------- | ----- | ----- |
| R1        | -     | -     |
| R2        | 4.7k  | 4.7k  |
| R3        | 47k   | 47k   |
| R4        | 0     | 0     |
| C3        | -     | -     |


### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- 0dB gain, 70mV rms sine wave:

  ![variants2-sig-gain10x1](images/variants2-sig1kHz70mV-gain10x1-spectra.png)

- 20dB gain, 7mV rms sine wave:

  ![variants2-sig-gain10x10](images/variants2-sig1kHz7mV-gain10x10-spectra.png)

- 40dB gain, 700uV rms sine wave:

  ![variants2-sig-gain10x100](images/variants2-sig1kHz700uV-gain10x100-spectra.png)


### High-pass filter

Measurement with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

![noHP](images/variants2-filter-70mV-gain10x1-traces.png)
