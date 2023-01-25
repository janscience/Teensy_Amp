# TeensyAmp R4.0

Work in progress.

With digitaly adjustable gain and filter settings.

## TODO

- check annotation of the PCB - CH1 and CH2 on the top side might be wrong. It is right!
- check annotation of the PCB - RTP1/2, RGAIN1/2, CHP* on the bottom side might be wrong. 
- Only connect a single Teensy GND to ground plane (the one opposite of Vin).
- Remove wholes for VBAT, GND, VUSB
- Make connection REF_LDO permanent -> No, if stacked, we get loops.
- Move pads for channel routing closer together, such that they can be
  soldered without the 0Ohm resistance.


## AGND vs GND:

https://forum.pjrc.com/threads/45742-Proper-use-of-Teensy-3-x-AGND

https://forum.pjrc.com/attachment.php?attachmentid=11301&d=1503091846


## New stuff

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

