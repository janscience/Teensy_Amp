# TeensyAmp R4.0

Work in progress.

With digitaly adjustable gain and filter settings.

## TODO

- check annotation of the PCB - CH1 and CH2 on the top side might be wrong.
- Move pads for channel routing closer together, such that they can be
  soldered without the 0Ohm resistance.

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
