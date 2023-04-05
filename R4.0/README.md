# TeensyAmp R4.0

Work in progress.

With digitaly adjustable gain and filter settings.

## Audio chips

- [TI PCM1865](https://www.ti.com/product/PCM1865): 8 input channels, but can only put out 4)
- [TLV320ADC5140](https://www.ti.com/product/TLV320ADC5140), 4 channels and ADCs, can be daisy-chained.

### [TLV320ADC5140](https://www.ti.com/product/TLV320ADC5140)

#### TDM

- 256bit frame
- 16 channels with each 16bit
- 2 independent TDM channels on Tensy 4.1 would allow 32 channel maximum!

#### BCLK

- Teensy audio library generates LRCLK (44.1 kHz), BCLK (1.41 or 2.82
  MHz) and MCLK (11.29 MHz) for an 41kHz audio signal.
- bit clock ≥ (# channels/device) × (# devices) × (sample rate) × (word length)
- bit clock = 4 x 4 x 96kHz x 16 = 24.5MHz < 25MHz possible for the chip
- 25MHz is also the maximum for the Teensy 4.1
- bit clock = 4 x 1 x 44.1kHz x 16 = 2.82MHz default support by audio library
- higher frequencies seem to be possible

See https://www.ti.com/lit/an/sbaa383b/sbaa383b.pdf?ts=1680563663210
for configurations of multiple chips

#### Power consumption

- Teensy 4.1: 100mA
- 25mA @ 3.3V for 4 channels at 96kHz

#### 8 channel
- 50mA for 4x2=8 channels
- 8 channel plus Teensy: 150mA
- 20Ah battery / 0.15A = 133h
- 8 x 8 channel plus control Teensy 200mA: 1.4A, lasts 14h

#### 16 channel
- 100mA for 4x4=16 channels
- 16 channel plus Teensy: 200mA
- 20Ah battery / 0.2A = 100h
- 4 x 16 channel plus control Teensy 200mA: 1A, lasts 20h

We need power supply switching on the fly (4 USB ports, 2 running, 2 new ones)!


#### Storage

- 1channel at 16bit and 24kHz needs 173MB per hour, 4.2GB per day
- 4channel at 16bit and 24kHz needs 691MB per hour, 16.6GB per day
- 8channel at 16bit and 24kHz needs 1.4GB per hour, 33.2GB per day
- 16channel at 16bit and 24kHz needs 2.8GB per hour, 66.4GB per day

- 256 GB cost about 25 Euros (2023): 3.8 days for 16 channels, 7.7 days for 8 channels 
- 500 GB cost about 50 Euros (2023): 7.7 days for 16 channels, 15.4 days for 8 channels


## TODO for improving R3.0

- annotation of the PCB - RTP1/2, RGAIN1/2, CHP* on the bottom side is switched. 
- Only connect a single Teensy GND to ground plane (the one opposite of Vin).
- Remove wholes for VBAT, GND, VUSB
- Make connection REF_LDO permanent -> No, if stacked, we get loops.
- Move pads for channel routing closer together, such that they can be
  soldered without the 0Ohm resistance.


### AGND vs GND:

https://forum.pjrc.com/threads/45742-Proper-use-of-Teensy-3-x-AGND

https://forum.pjrc.com/attachment.php?attachmentid=11301&d=1503091846


### New stuff

- put an ADC on the amplifier. The Teensy one is always corruped by
  noise no matter how it is used.
- (Make connection REF_LDO permanent) with ADC not needed.

- Gains:               x8, x16, x32, x64, x128, x256, x512, x1024
  Resistances (kOhm): 100,  47,  12,  10,  5.6,  2.2,    1,   0.5

- Required highpass filter settings and capacitors? 2 or 3?

  | high-pass frequency | capacity |
  | ------------------: | -------: |
  |  10Hz               |          |
  | 100Hz               |          |
  | 300Hz               |          |

- Required low-pass cutoff freuqencies:

  | Sampling rate | low-pass frequency | R         |
  | ------------: | -----------------: | --------: |
  |  22.05kHz     |    8kHz            |           |
  |  44.1kHz      |   16KHz            |           |
  |  96kHz        |   32kHz            |           |
  | 192kHz        |   64kHz            |           |


## 16 channels

Test it!:

  A0     1    0   S0  B2
  A1     1    0   S0  B1
  A2     X    1   S0  B4
  A3     X    1   S0  B3
  A4     1    0   S1  B8
  A5     1    0   S1  B7
  A6     1    0   S1  B6
  A7     1    0   S1  B5
  A8     1    0   S1  B4
  A9     1    0   S1  B3
  A10    X    1   S1  B2
  A11    0    1   S1  B1
  A18    0    1   S0  B8
  A19    0    1   S0  B7
  A20    0    1   S0  B6
  A22    0    1   S0  B5

Alternative: A25/A26 cool on Teensy 3.5 - not on Teensy 3.6
  A2     X    1   S0  B8
  A3     X    1   S0  B7
  A4     1    0   S1  B8
  A5     1    0   S1  B7
  A6     1    0   S1  B6
  A7     1    0   S1  B5
  A8     1    0   S1  B4
  A9     1    0   S1  B3
  A10    X    1   S1  B2
  A11    0    1   S1  B1
  A19    0    1   S0  B6
  A20    0    1   S0  B5
  A21    1    0   S0  B2
  A22    0    1   S0  B4
  A25    1    0   S0  B1
  A26    0    1   S0  B3

