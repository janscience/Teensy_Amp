# TeensyAmp R3.0

by [jlm Innovation](https://www.jlm-innovation.de/) and [Jan
Benda](https://github.com/janscience), based on the R2.0 circuit by
[Stefan Mucha](https://github.com/muchaste).

![top](images/Teensy_Amp-R3b-top.png)

![bottom](images/Teensy_Amp-R3b-bottom.png)

The input signals are processed in the following way:

- simple RC high-pass filtering, cutoff frequencies selectable via
  plug-in capacitors.

- amplification ([Texas Instruments
  INA2321-EA](https://www.ti.com/product/INA2321)),
  gain selectable via plug-in resistances.

- low-pass filtering ([Analog devices
  OP2177ARZ](https://www.analog.com/media/en/technical-documentation/data-sheets/op1177_2177_4177.pdf)),
  cutoff frequencies selectable via plug-in resistances.

- An [Onsemi
  NCP164ASN330](https://www.onsemi.jp/products/power-management/linear-regulators-ldo/ncp164?pdf=Y)
  generates the 3.3V for power and analog reference.

- An LDO, [Analog Devices
  ADR3412](https://www.analog.com/en/products/adr3412.html),
  generatesd the 1.6V reference.
  

## Circuit

- [EAGLE schematics file](teensy_amp_R3b.sch)
- [EAGLE circuit board](teensy_amp_R3b.brd)

![circuit](images/teensy_amp_R3b_circuit.png)

## Pins

![pcb](images/teensy_amp_R3b_pcb.png)

### Input

The signal to be measured is connected via the screw-terminal block on
the right.

- Channel 1: top two pins.
- Channel 2: bottom two pins.

- The two inner pins are the positive V+ inputs.
- The two outer pins are the negative V- inputs.

### Output

Each of the amplified signals can be assinged to one of four analog
input pins of the Teensy. The following tables also indicate from
which of the two ADCs those pins can be accessed on a Teensy 3.5 or
3.6

Signal 1 (Channel1):

| Pad    | Teensy | ADC0 | ADC1 | Board |
| ------ | ------ | ---- | ---- | ----- |
| S1_A10 | A10    | 1    | 1    | A X   | 
| S1_A11 | A11    | 0    | 1    | B Y   | 
| S1_A7  | A7     | 1    | 0    | C     | 
| S1_A6  | A6     | 1    | 0    | D     | 

Signal 2 (Channel2):

| Pad    | Teensy | ADC0 | ADC1 | Board |
| ------ | ------ | ---- | ---- | ----- |
| S2_A5  | A5     | 1    | 0    | A     |  
| S2_A4  | A4     | 1    | 0    | B     |  
| S2_A3  | A3     | 1    | 1    | C Y   |  
| S2_A2  | A2     | 1    | 1    | D X   |  


### Power

- Vin: 3.3V - 5V on bottom left pin (Teensy Vin).
- GND: on top left pin (Teensy GND).


## Gain

Gain of the INA is given by

![gain](images/gain.svg)

where *R1 = RGAIN1* and *R2* = *R9* = 100kOhm.

The total gain of the amplifier is the INA gain times 1.7.


| RGAIN1  | INA gain  | Total gain |
| ------: | --------: | ---------: |
|   1MOhm |       5.5 |            |
| 100kOhm |        10 |            |
|  47kOhm |        15 |            |
|  27kOhm |        24 |         40 |
|  12kOhm |        47 |         80 |
|  10kOhm |        55 |            |
| 5.6kOhm |        94 |        160 |
| 4.7kOhm |       111 |            |
| 2.2kOhm |       232 |        400 |
| 1.5kOhm |       338 |            |
|   1kOhm |       505 |        870 |
|  500Ohm |      1005 |            |
|  200Ohm |      2505 |            |
|  100Ohm |      5005 |            |
|   50Ohm |     10005 |            |


## Filter

![cutofffreq](images/cutofffreq.svg)

### High-pass filter

![Ccutoff](images/Ccutoff.svg)

| R1-R4   | CHP1A-CHP2B | tau    | fcutoff | real fcutoff |
| ------: | ----------: | -----: | ------: | -----------: |
| 100kOhm | 220nF       | 22ms   |   7.2Hz |        <10Hz |
| 100kOhm | 150nF       | 15ms   |  10.6Hz |              |
| 100kOhm |  22nF       | 2.2ms  |  72Hz   |         70Hz |
| 100kOhm |  15nF       | 1.5ms  | 106Hz   |              |
| 100kOhm | 5.6nF       | 0.56ms | 283Hz   |              |
| 100kOhm | 4.7nF       | 0.47ms | 338Hz   |              |

### Low-pass filter

![Rcutoff](images/Rcutoff.svg)

*C* = 820pF
*R* = RTP1 + 4.5kOhm

| RTP1, RTP2 | fcutoff | sampling rate | real fcutoff |
| ---------: | ------: | ------------: | -----------: |
|  27kOhm    |  7kHz   |  20kHz        |         8kHz |
|  12kOhm    | 15kHz   |  44kHz        |        15kHz |
| 5.6kOhm    | 20kHz   |  60kHz        |              |
| 2.2kOhm    | 29kHz   |  87kHz        |       >20kHz |
| 1.5kOhm    | 33kHz   | 100kHz        |              |
|   1kOhm    | 35kHz   | 106kHz        |              |


## Gain and linearity tests

### Control

Sine wave recorded with Measurement Computing USB_1608_GX_2AO:

![control](images/gaincontrol-20mV-traces.png)
![controlspectrum](images/gaincontrol-20mV-spectra.png)

The sine wave generator (NTI Minirator) produces a third harmonic
ca. 70dB below fundamental. Very clean sine wave!

### Gain tests

In files [`tests/gain-*.wav`](tests) sine wave signals were recorded
with various gains (70Hz high-pass, 7kHz low-pass).

x40: RGAIN1=27kOhm with 20mV rms amplitude (56mV p-p):

![gain](images/gain27kOhm-20mV-traces.png)
![gainspectrum](images/gain27kOhm-20mV-spectra.png)

x80: RGAIN1=12kOhm with 10mV rms amplitude (28mV p-p):

![gain](images/gain12kOhm-10mV-traces.png)
![gainspectrum](images/gain12kOhm-10mV-spectra.png)

x160: RGAIN1=5.6kOhm with 5mV rms amplitude (14mV p-p):

![gain](images/gain5600Ohm-5mV-traces.png)
![gainspectrum](images/gain5600Ohm-5mV-spectra.png)

x400: RGAIN1=2.2kOhm with 2mV rms amplitude (5.6mV p-p):

![gain](images/gain2200Ohm-2mV-traces.png)
![gainspectrum](images/gain2200Ohm-2mV-spectra.png)

x800: RGAIN1=1kOhm with 1mV rms amplitude (2.8mV p-p):

![gain](images/gain1kOhm-1mV-traces.png)
![gainspectrum](images/gain1kOhm-1mV-spectra.png)


### Conclusion

- Amplifier and/or Teensy produce many harmonics. And they are only
  about 25dB below the fundamental.
- Noisy at gains larger x100.


## Transfer function and filter tests

In files [`tests/filter-*.wav`](tests) a 20mV rms signal was sampled with
44kHz and its frequency was increased as follows: 10Hz, 12.5Hz, 16Hz,
20Hz, 25Hz, 31.5Hz, 40Hz, 50Hz, 63Hz, 80Hz, 100Hz, 125Hz, 160Hz,
200Hz, 250Hz, 315Hz, 400Hz, 500Hz, 630Hz, 800Hz, 1000Hz, 1250Hz,
1600Hz, 2000Hz, 2500Hz, 3150Hz, 4000Hz, 5000Hz, 6300Hz, 8000Hz,
10kHz, 12.5kHz, 16kHz, 20kHz.

7Hz high-pass, 7kHz low-pass:

![filter 7Hz-7kHz](images/filter-7Hz-7kHz-gain24-20mV-traces.png)

70Hz high-pass, 7kHz low-pass:

![filter 70Hz-7kHz](images/filter-70Hz-7kHz-gain24-20mV-traces.png)

70Hz high-pass, 15kHz low-pass:

![filter 70Hz-15kHz](images/filter-70Hz-15kHz-gain24-20mV-traces.png)

70Hz high-pass, 29kHz low-pass:

![filter 70Hz-29kHz](images/filter-70Hz-29kHz-gain24-20mV-traces.png)

### Conclusion

- High- and low-pass filter are working as expected.
- Pass-band should be flatter.


## Signal range and clipping

![clipping](images/clipping-gain024-20mV-step1mV-traces.png)

### Conclusion

- The full output voltage range is used.


## Noise and SD write artifacts

### AREF configuration

Gain 27kOhm, HF 22nF, LW 27kOhm:

- Plain amplifier output recorded with Measurement Computing
  USB_1608_GX_2AO (range 1V):

  <img src="images/sdwrites-gain024-external-traces.png" width=36%>
  <img src="images/sdwrites-gain024-external-noise.png" width=24%>
  <img src="images/sdwrites-gain024-external-spectra.png" width=36%>
  
- Teensy internal 3.3V REF:

  <img src="images/sdwrites-gain024-teensy3v3-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain024-teensy3v3-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain024-teensy3v3-all0ohm-spectra.png" width=36%>
  
- Amplifier LDO 3.3V connected to AREF:

  <img src="images/sdwrites-gain024-ldo-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain024-ldo-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain024-ldo-all0ohm-spectra.png" width=36%>
  
- Amplifier LDO 3.3V connected to AREF, AGND connected to GND:

  <img src="images/sdwrites-gain024-ldo-all0ohm-agnd-traces.png" width=36%>
  <img src="images/sdwrites-gain024-ldo-all0ohm-agnd-noise.png" width=24%>
  <img src="images/sdwrites-gain024-ldo-all0ohm-agnd-spectra.png" width=36%>

### Gain dependence

Amplifier LDO 3.3V connected to AREF, HF 220nF, LW 27kOhm.
  
- Gain 12kOhm:

  <img src="images/sdwrites-gain080-ldo-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain080-ldo-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain080-ldo-all0ohm-spectra.png" width=36%>

- Gain 5.6kOhm:

  <img src="images/sdwrites-gain160-ldo-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain160-ldo-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain160-ldo-all0ohm-spectra.png" width=36%>

- Gain 2.2kOhm:

  <img src="images/sdwrites-gain400-ldo-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain400-ldo-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain400-ldo-all0ohm-spectra.png" width=36%>

- Gain 1kOhm:

  <img src="images/sdwrites-gain870-ldo-all0ohm-traces.png" width=36%>
  <img src="images/sdwrites-gain870-ldo-all0ohm-noise.png" width=24%>
  <img src="images/sdwrites-gain870-ldo-all0ohm-spectra.png" width=36%>
  
- Gain 1kOhm, AGND connected to GND:

  <img src="images/sdwrites-gain870-ldo-all0ohm-agnd-traces.png" width=36%>
  <img src="images/sdwrites-gain870-ldo-all0ohm-agnd-noise.png" width=24%>
  <img src="images/sdwrites-gain870-ldo-all0ohm-agnd-spectra.png" width=36%>


### Conclusion

- The LDO of the amplifier seems to be able to produce a stable voltage from
  the supply voltage of the Teensy:
  Amplified short circuited signals are stable and do not show SD
  write artifacts.
- Using the Teensy's ADC however shows the SD write artifacts.
- SD write artifact gets smaller when AREF is driven by LDO voltage.
- Removing Teensy's R3 resistance does not make a difference
  (see `../images/sdwrites-*noR3*`).
- Connecting AGND to GND does not make a difference.
- The larger the gain, the larger the baseline noise.


## ADC settings

For a gain of 40x (27kOhm), highpass filter of 70Hz (22nF), lowpass
filter of 7kHz (27kOhm) and a sampling rate of 20kHz, the [averaging
sketch](https://github.com/janscience/TeeRec/tree/main/examples/averaging)
reports (sampling rate of 100kHz gives similar results):

| convers  | sampling | avrg |   A2 |  A10 |
| :------- | :------- | ---: | ---: | ---: |
| veryhigh | veryhigh |    1 |  1.4 |  1.3 |
| veryhigh | veryhigh |    4 |  0.9 |  0.9 |
| veryhigh | veryhigh |    8 |  0.9 |  0.9 |
| veryhigh | veryhigh |   16 |  0.9 |  0.8 |
| veryhigh | veryhigh |   32 |  0.7 |  0.8 |
| veryhigh | high     |    1 |  1.2 |  1.1 |
| veryhigh | high     |    4 |  0.9 |  0.9 |
| veryhigh | high     |    8 |  0.8 |  0.9 |
| veryhigh | high     |   16 |  0.8 |  0.7 |
| veryhigh | high     |   32 |  0.9 |  0.9 |
| veryhigh | med      |    1 |  1.1 |  1.1 |
| veryhigh | med      |    4 |  0.9 |  0.8 |
| veryhigh | med      |    8 |  0.8 |  0.8 |
| veryhigh | med      |   16 |  0.8 |  0.8 |
| veryhigh | med      |   32 |  0.9 |  1.0 |
| veryhigh | low      |    1 |  1.2 |  1.2 |
| veryhigh | low      |    4 |  0.9 |  0.9 |
| veryhigh | low      |    8 |  0.7 |  0.8 |
| veryhigh | low      |   16 |  0.8 |  0.8 |
| veryhigh | low      |   32 |  0.8 |  0.7 |
| veryhigh | verylow  |    1 |  1.3 |  1.2 |
| veryhigh | verylow  |    4 |  0.8 |  0.9 |
| veryhigh | verylow  |    8 |  0.8 |  0.9 |
| veryhigh | verylow  |   16 |  0.8 |  0.8 |
| veryhigh | verylow  |   32 |  0.8 |  0.7 |
| high     | veryhigh |    1 |  1.1 |  1.4 |
| high     | veryhigh |    4 |  0.8 |  0.9 |
| high     | veryhigh |    8 |  0.8 |  1.0 |
| high     | veryhigh |   16 |  0.8 |  0.9 |
| high     | veryhigh |   32 |  0.7 |  0.7 |
| high     | high     |    1 |  1.1 |  1.2 |
| high     | high     |    4 |  0.9 |  1.0 |
| high     | high     |    8 |  0.9 |  0.9 |
| high     | high     |   16 |  0.8 |  0.7 |
| high     | med      |    1 |  1.1 |  1.1 |
| high     | med      |    4 |  0.9 |  0.8 |
| high     | med      |    8 |  0.8 |  0.8 |
| high     | med      |   16 |  0.8 |  0.8 |
| high     | low      |    1 |  1.1 |  1.0 |
| high     | low      |    4 |  0.9 |  0.8 |
| high     | low      |    8 |  0.8 |  0.8 |
| high     | low      |   16 |  0.8 |  0.7 |
| high     | verylow  |    1 |  1.1 |  1.0 |
| high     | verylow  |    4 |  0.8 |  0.8 |
| high     | verylow  |    8 |  0.8 |  0.8 |
| high     | verylow  |   16 |  0.7 |  0.7 |
| med      | veryhigh |    1 |  1.1 |  1.3 |
| med      | veryhigh |    4 |  0.9 |  0.8 |
| med      | veryhigh |    8 |  0.8 |  0.8 |
| med      | veryhigh |   16 |  0.7 |  0.8 |
| med      | high     |    1 |  1.1 |  1.0 |
| med      | high     |    4 |  0.8 |  0.8 |
| med      | high     |    8 |  0.8 |  0.8 |
| med      | high     |   16 |  0.7 |  0.7 |
| med      | med      |    1 |  1.2 |  1.1 |
| med      | med      |    4 |  0.8 |  0.8 |
| med      | med      |    8 |  0.9 |  0.8 |
| med      | low      |    1 |  1.2 |  1.0 |
| med      | low      |    4 |  0.8 |  0.8 |
| med      | low      |    8 |  0.8 |  0.7 |
| med      | verylow  |    1 |  1.2 |  1.3 |
| med      | verylow  |    4 |  0.9 |  0.9 |
| med      | verylow  |    8 |  0.7 |  0.7 |

A good setting:

![high-high-8 noise](images/averaging-gain024-020kHz-12bit-convhigh-samplhigh-avrg08-noise.png)
![high-high-8 traces](images/averaging-gain024-020kHz-12bit-convhigh-samplhigh-avrg08-traces.png)


With the same settings but with 16bit the results look like this:

| convers  | sampling | avrg |   A2 |  A10 |
| :------- | :------- | ---: | ---: | ---: |
| veryhigh | veryhigh |    1 | 17.4 | 15.7 |
| veryhigh | veryhigh |    4 | 15.1 | 12.7 |
| veryhigh | veryhigh |    8 | 12.5 | 11.4 |
| veryhigh | veryhigh |   16 | 12.3 | 11.7 |
| veryhigh | veryhigh |   32 | 14.9 | 11.0 |
| veryhigh | high     |    1 | 16.5 | 18.3 |
| veryhigh | high     |    4 | 12.8 | 10.8 |
| veryhigh | high     |    8 | 13.4 | 13.0 |
| veryhigh | high     |   16 | 11.8 | 11.4 |
| veryhigh | high     |   32 | 13.4 | 11.8 |
| veryhigh | med      |    1 | 15.7 | 15.3 |
| veryhigh | med      |    4 | 12.5 | 12.7 |
| veryhigh | med      |    8 | 12.3 | 12.2 |
| veryhigh | med      |   16 | 10.8 | 10.7 |
| veryhigh | med      |   32 | 10.5 | 11.5 |
| veryhigh | low      |    1 | 19.7 | 15.1 |
| veryhigh | low      |    4 | 11.7 |  9.1 |
| veryhigh | low      |    8 | 11.7 | 11.8 |
| veryhigh | low      |   16 | 11.8 | 11.5 |
| veryhigh | low      |   32 | 10.2 | 10.2 |
| veryhigh | verylow  |    1 | 17.5 | 15.5 |
| veryhigh | verylow  |    4 | 11.9 | 11.4 |
| veryhigh | verylow  |    8 | 11.4 | 11.2 |
| veryhigh | verylow  |   16 | 11.0 | 11.0 |
| high     | veryhigh |    1 | 16.6 | 14.2 |
| high     | veryhigh |    4 | 11.8 | 11.9 |
| high     | veryhigh |    8 | 11.2 | 11.3 |
| high     | veryhigh |   16 | 10.7 | 11.0 |
| high     | high     |    1 | 15.3 | 14.5 |
| high     | high     |    4 | 12.0 | 11.9 |
| high     | high     |    8 | 11.2 | 11.0 |
| high     | high     |   16 | 11.1 | 11.4 |
| high     | med      |    1 | 15.5 | 15.4 |
| high     | med      |    4 | 12.2 | 11.8 |
| high     | med      |    8 | 11.7 | 12.2 |
| high     | med      |   16 | 10.7 | 11.1 |
| high     | low      |    1 | 16.1 | 14.9 |
| high     | low      |    4 | 12.5 | 12.2 |
| high     | low      |    8 | 11.7 | 10.9 |
| high     | low      |   16 | 11.3 | 10.5 |
| high     | verylow  |    1 | 16.0 | 15.5 |
| high     | verylow  |    4 | 11.5 | 11.6 |
| high     | verylow  |    8 | 11.4 | 10.8 |
| med      | veryhigh |    1 | 17.6 | 14.3 |
| med      | veryhigh |    4 | 12.9 | 11.8 |
| med      | veryhigh |    8 | 11.0 | 10.5 |
| med      | high     |    1 | 15.6 | 15.5 |
| med      | high     |    4 | 11.8 | 11.5 |
| med      | high     |    8 | 11.1 | 11.0 |
| med      | med      |    1 | 17.1 | 15.1 |
| med      | med      |    4 | 13.0 | 11.7 |
| med      | med      |    8 | 11.9 | 11.1 |
| med      | low      |    1 | 16.3 | 13.7 |
| med      | low      |    4 | 12.5 | 12.2 |
| med      | low      |    8 | 11.4 | 12.1 |
| med      | verylow  |    1 | 16.8 | 15.2 |
| med      | verylow  |    4 | 12.4 | 11.4 |
| med      | verylow  |    8 | 10.3 | 10.6 |

A good setting:

![high-high-8 noise](images/averaging-gain024-020kHz-16bit-convhigh-samplhigh-avrg08-noise.png)
![high-high-8 traces](images/averaging-gain024-020kHz-16bit-convhigh-samplhigh-avrg08-traces.png)
