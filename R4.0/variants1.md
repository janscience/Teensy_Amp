# Testing filter and gain variants

If not noted otherwise, all measurements at 48kHz sampling rate.


## Signal-filter

![filter](images/filtervariants1.png)

| Component | 1-CH3R | 1-CH3L | 1-CH4R | 1-CH4L | 2-CH3R | 2-CH3L | 2-CH4R | 2-CH4L | Comment |
| --------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------- |
| R1        | -     | 220   |    1k |  2.2k | -     | 220   |    1k |  2.2k | 20Hz, 5Hz, 2Hz highpass |
| R2        | 0     | 0     | 0     | 0     | 100   | 100   | 100   | 100   | TP       | 
| C2        | -     | -     | -     | -     | 10nF  | 10nF  | 10nF  | 10nF  | TP

### Noise

Inputs short circuited to ground.

- 0dB gain:

  ![variants1-zeros0dB](images/variants1-zeros-gain1x1-noise.png)

- 20dB gain:

  ![variants1-zeros20dB](images/variants1-zeros-gain1x10-noise.png)

- 40dB gain:

  ![variants1-zeros40dB](images/variants1-zeros-gain1x100-noise.png)

- Same offset and noise in all channels and variants.
- Noise increases according to gain.


### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- 0dB gain, 700mV rms sine wave:

  ![variants1-sig-gain1x1](images/variants1-sig1kHz700mV-gain1x1-spectra.png)

- 20dB gain, 70mV rms sine wave:

  ![variants1-sig-gain1x10](images/variants1-sig1kHz70mV-gain1x10-spectra.png)

- 40dB gain, 7mV rms sine wave:

  ![variants1-sig-gain1x100](images/variants1-sig1kHz7mV-gain1x100-spectra.png)

- In all conditions harmonics ar at least 90 to 100dB below the signal!
- With the low-pass filter (lower row) higher harmonics are stronger than
  without low-pass filter (upper row).
- The 2Hz and 5Hz high-pass filters (two rightmost columns) have the smalles harmonics.
- At higher gains the differences are marginally.
- Noise increases according to gain (every x10 by 20dB).


### Low-pass filter

A 8.8kHz signal without low-pass filter:

![8.8kHz no LP](images/sig8800Hz1V-gain1x1-spectra.png)

and with low-pass filter:

![8.8kHz LP](images/sig8800Hz1V-TP-gain1x1-spectra.png)

A 39.2kHz signal also appears at 8.8kHz.

Without low-pass filter:

![39.2kHz no LP](images/sig39200Hz1V-gain1x1-spectra.png)

With low-pass filter:

![39.2kHz LP](images/sig39200Hz1V-TP-gain1x1-spectra.png)

- Low-pass filter is not really needed.


### High-pass filter

All measurements with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

Without highpass filter:

![noHP](images/filter-700mV-gain1x1-noHP-traces.png)

With R1=220 we get a 30Hz high-pass filter with strange behavior at
lower freqencies:

![HP220](images/filter-700mV-gain1x1-HP220-traces.png)

With R1=1k we get a 5Hz high-pass filter:

![HP1000](images/filter-700mV-gain1x1-HP1000-traces.png)

With R1=2.2k we get a 2Hz high-pass filter:

![HP2200](images/filter-700mV-gain1x1-HP2200-traces.png)

- Let's use R1=1k for a 5Hz high-pass filter.


## Pre-amplifier

![preampinv](images/preampinvvariants1.png)

| Component | 1-CH1R | 1-CH1L | 1-CH2R | 1-CH2L | 2-CH1R | 2-CH1L | 2-CH2R | 2-CH2L | Comment |
| --------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------- |
| R1        | -     | -     | -     | -     | 1k    | 1k    | 1k    | 1k    | 5Hz highpass |
| R2        | 1k    | 1k    |  4.7k |  4.7k | 1k    | 1k    |  4.7k |  4.7k | 20x gain |
| R3        | 22k   | 22k   | 100k  | 100k  | 22k   | 22k   | 100k  | 100k  | 20x gain |
| R4        | 100   | 0     | 100   | 0     | 100   | 0     | 100   | 0     | TP       |
| C3        | 10nF  | -     | 10nF  | -     | 10nF  | -     | 10nF  | -     | TP


### Noise

Inputs short circuited to ground.

- 0dB gain:

  ![variants1-zeros0dB](images/variants1-zeros-gain20x1-noise.png)

- 20dB gain:

  ![variants1-zeros20dB](images/variants1-zeros-gain20x10-noise.png)

- 40dB gain:

  ![variants1-zeros40dB](images/variants1-zeros-gain20x100-noise.png)

- Twice as much noise with the 100k gain.
- At 20dB gain, amounting to x200 overall gain, the noise standard
  deviation is three times smaller than 40dB gain (x100) without preamp.


### Linearity

1 kHz sine wave (Minirator) applied to each channel individually:

- 0dB gain, 30mV rms sine wave:

  ![variants1-sig-gain1x1](images/variants1-sig1kHz30mV-gain20x1-spectra.png)

- 20dB gain, 3mV rms sine wave:

  ![variants1-sig-gain1x10](images/variants1-sig1kHz3mV-gain20x10-spectra.png)

- 40dB gain, 300uV rms sine wave:

  ![variants1-sig-gain1x100](images/variants1-sig1kHz300uV-gain20x100-spectra.png)

- Low-pass filter introduces stronger 2nd harmonics at 0dB gain.
- Effect of high-pass filter is small.
- Effect of 22k versus 100k gain is small. 
- Noise floor is similar in all variants (in contrast to the noise measurement).
- At comparable gains, preamp introduces slightly more harmonics.
- Let's take variant 2-CH1L (R1=1k, R2=1k, R3=22k, R4=0, C3=-).


### Low-pass filter

An 1kHz signal without low-pass filter:

![1kHz no LP](images/sig1kHz30mV-gain20x1-spectra.png)

and with low-pass filter:

![1kHz LP](images/sig1kHz30mV-TP-gain20x1-spectra.png)

With a sampling rate of 48kHz a 47kHz signal will appear also at 1kHz.

Without low-pass filter:

![47kHz no LP](images/sig47kHz30mV-gain20x1-spectra.png)

With low-pass filter:

![47kHz LP](images/sig47kHz30mV-TP-gain20x1-spectra.png)

The same for a 8.8kHz signal - a bit closer to the Nyquist frequency:

![8.8kHz no LP](images/sig8800Hz30mV-gain20x1-spectra.png)

A 39.2kHz signal also appears at 8.8kHz.

Without low-pass filter:

![39.2kHz no LP](images/sig39200Hz30mV-gain20x1-spectra.png)

With low-pass filter:

![39.2kHz LP](images/sig39200Hz30mV-TP-gain20x1-spectra.png)

- Low-pass filter is not really needed!


### High-pass filter

All measurements with frequencies 10Hz to 20kHz in 1/3 octaves, each for 500ms.

With R1=1k we get a 30Hz high-pass filter (R2=1kHz and R3=22kHz):

![HP1k](images/filter-HP1k-30mV-gain20x1-traces.png)

Without R1 we still have a 25Hz high-pass filter (R2=1kHz and R3=22kHz):

![noHP](images/filter-noHP-30mV-gain20x1-traces.png)

Without R1 and R2=4.7kHz and R3=100kHz,  we still have a 5Hz high-pass filter:

![noHPR3100k](images/filter-noHP-30mV-R3100k-gain20x1-traces.png)

