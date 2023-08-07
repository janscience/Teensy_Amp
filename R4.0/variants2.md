# Testing high-pass filter without low-pass

If not noted otherwise, all measurements at 48kHz sampling rate.


## Signal-filter

![filter](images/filtervariants2.png)

| Component | 1-CH3R | 1-CH3L | 1-CH4R | 1-CH4L | 2-CH* |
| --------- | ------ | ------ | ------ | ------ | ----- |
| R1        | 1k     | 1k     | 1k     | 1k     | 1k    |
| R2        | 0      | 0      | 0      | 0      | 0     |
| C2=R3     | 330    | 1k     | 2.2k   | 10     | -     |
| fcutoff   |        |        |        |        | 5Hz   |

| Component | 1-CH3R | 1-CH3L | 1-CH4R | 1-CH4L |
| --------- | ------ | ------ | ------ | ------ |
| R1        | 100k   | 100k   | 100k   | 100k   |
| R2        | 0      | 0      | 0      | 0      |
| C2=R3     | 330    | 1k     | 2.2k   | 10     |
| fcutoff   | 80Hz   | 30Hz   | 15Hz   | 3Hz    |

### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- R1=1k, no C2, 0dB gain, 700mV rms sine wave:

  ![variants2-sig-gain1x1](images/variants2-sig1kHz700mV-gain1x1-spectra.png)

- R1=1k, no C2, 20dB gain, 70mV rms sine wave:

  ![variants2-sig-gain1x10](images/variants2-sig1kHz70mV-gain1x10-spectra.png)

- R1=1k, no C2, 40dB gain, 7mV rms sine wave:

  ![variants2-sig-gain1x100](images/variants2-sig1kHz7mV-gain1x100-spectra.png)


### High-pass filter

Measurement with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

- R1=1k, no C2, 0dB gain, 700mV rms sine wave:

![HP1k](images/variants2-filter-700mV-gain1x1-traces.png)

- R1=100k, R3=330, 0dB gain, 700mV rms sine wave:

![R3330HP1k](images/variants2b-filter-700mV-gain1x1-R1100k-R3330-traces.png)

- R1=100k, R3=1k, 0dB gain, 700mV rms sine wave:

![R31kHP1k](images/variants2b-filter-700mV-gain1x1-R1100k-R31k-traces.png)

- R1=100k, R3=2.2k, 0dB gain, 700mV rms sine wave:

![R32.2kHP1k](images/variants2b-filter-700mV-gain1x1-R1100k-R32200-traces.png)

- R1=100k, R3=10k, 0dB gain, 700mV rms sine wave:

![R310kHP1k](images/variants2b-filter-700mV-gain1x1-R1100k-R310k-traces.png)


## Pre-amplifier

![preampinv](images/preampinvvariants2.png)

| Component | 1-CH* | 2-CH* |
| --------- | ----- | ----- |
| R1        | 100k  | -     |
| R2        | 4.7k  | 4.7k  |
| R3        | 47k   | 47k   |
| R4        | 0     | 0     |
| C3        | -     | -     |


### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- R1=1k, 0dB gain, 70mV rms sine wave:

  ![variants2-sig-gain10x1](images/variants2-sig1kHz70mV-gain10x1-spectra.png)

- R1=1k, 20dB gain, 7mV rms sine wave:

  ![variants2-sig-gain10x10](images/variants2-sig1kHz7mV-gain10x10-spectra.png)

- R1=1k, 40dB gain, 700uV rms sine wave:

  ![variants2-sig-gain10x100](images/variants2-sig1kHz700uV-gain10x100-spectra.png)

- R1=100k, 0dB gain, 70mV rms sine wave:

  ![variants2a-sig-gain10x1](images/variants2a-sig1kHz70mV-gain10x1-spectra.png)


### High-pass filter

Measurement with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

- R1=1k, 0dB gain, 70mV rms sine wave:

![noHP](images/variants2-filter-70mV-gain10x1-traces.png)

- R1=100k, 0dB gain, 70mV rms sine wave:

![100k](images/variants2a-filter-70mV-gain10x1-traces.png)


### Conclusion

- R1=100k for grounding the signal
- R2=4.7k for a 5Hz high-pass filter
- R3=47k for a 10x gain
- no low-pass filter 

