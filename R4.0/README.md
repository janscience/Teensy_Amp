# TeensyAmp R4.0

Work in progress.

With digitaly adjustable gain and filter settings.

## Audio chips

- [TI PCM1865](https://www.ti.com/product/PCM1865): 8 input channels (but can only put out 4)
- [TLV320ADC5140](https://www.ti.com/product/TLV320ADC5140), 4 channels and ADCs, can be daisy-chained.

Use I2S or TDM protocol on [Teensy 4.1](https://www.pjrc.com/teensy/pinout.html#Teensy_4.1).

## TI PCM1865

- [web site](https://www.ti.com/product/PCM1865)
- [data sheet](https://www.ti.com/lit/gpn/pcm1865)
- [evalutation board](https://www.ti.com/lit/pdf/slau615)

### Pins

See page 11 and Fig 22 in the data sheet and Figure 15 of the
evaluation bard manual:

| pin | name        | connects to |
| --: | :---------- | :---------- |
|  1  | VINL2/VIN1M | SIG 3 / 7   |
|  2  | VINR2/VIN2M | SIG 2 / 6   |
|  3  | VINL1/VIN1P | SIG 1 / 5   |
|  4  | VINR1/VIN2P | SIG 0 / 4   |
|  5  | Mic Bias    | unconnected |
|  6  | VREF        | Connect 1-μF capacitor C5 to AGND |
|  7  | AGND        | Analog ground to common ground |
|  8  | AVDD        | 3.3V power supply, Fig 70/71. Connect 0.1-μF and 10-μF capacitors C8, C9, R1 from this pin to AGND. |
|  9  | XO          | not used, capacitor to ground |
| 10  | XI          | not used, capacitor to ground |
| 11  | LDO         | Connect 0.1-μF and 10-μF capacitors from this pin to DGND? |
| 12  | DGND        | Digital ground to common ground |
| 13  | DVDD        | 3.3V power supply, Fig 70/71. Connect 0.1-μF and 10-μF capacitors from this pin to DGND. |
| 14  | IOVDD       | 3.3V power supply, tied to DVDD, Fig 70/71. |
| 15  | SCKI        | 3.3-V CMOS MCLK input, not needed for ADC slave PLL mode! See table 5 and CLKDET_EN |
| 16  | LRCK        | Audio data world clock (left right clock) input/output. |
| 17  | BCK         | Audio data bit clock input/output. |
| 18  | DOUT        | Audio data digital output.         |
| 19  | GPIO3/INTC  | not needed  |
| 20  | GPIO2/INTB/DMCLK | not needed |
| 21  | GPIO1/INTA/DMIN  | not needed |
| 22  | MISO/GPIO0/DMIN2 | not needed |
| 23  | MOSI/SDA    | I2C bus SDA |
| 24  | MC/SCL      | I2C bus CLOCK |
| 25  | MS/AD       | I2C addres: one chip high, one chip low |
| 26  | MD0         | tied low for I2C communication |
| 27  | VINL4/VIN4M | SIGALT 3 / 6|
| 28  | VINR4/VIN3M | SIGALT 2 / 5|
| 29  | VINL3/VIN4P | SIGALT 1 / 4|
| 30  | VINR3/VIN3P | SIGALT 0 / 3|

### Power supply

- LDO to generate 3.3 V on AVDD
- Supply DVDD and IOVDD from Teensy 3.3V or also from LDO?
- What about AGND and DGND? DGND on Teensy, AGND on LDO?

- we use the onbard LDO to generate VREF.

### Signals and input channels

Signal pins VINL2, VINR2, VINL1, VINR1 connect via 100kOhm (R40-R47)
and capacitor (C1-C4, C15-C18: DEFAULT: SMD0805 10uF/16V/X7R ALT:
VSA-10uF/16V/ELECTROLYTIC, see evaluation board) to 4 input signals.

VINL4, VINR4, VINL3, VINR3 get a possibility for connecting to a
secondary PCB with some preamp.


### TDM audio data stream

- SCKI
- LRCK
- BCK
- DOUT


## TLV320ADC5140

[TLV320ADC5140 web site](https://www.ti.com/product/TLV320ADC5140)


### TDM

- 256bit frame
- 16 channels with each 16bit
- 2 independent TDM channels on Tensy 4.1 would allow 32 channel maximum!

### BCLK

- Teensy audio library generates LRCLK (44.1 kHz), BCLK (1.41 or 2.82
  MHz) and MCLK (11.29 MHz) for an 41kHz audio signal.
- bit clock ≥ (# channels/device) × (# devices) × (sample rate) × (word length)
- bit clock = 4 x 4 x 96kHz x 16 = 24.5MHz < 25MHz possible for the chip
- 25MHz is also the maximum for the Teensy 4.1
- bit clock = 4 x 1 x 44.1kHz x 16 = 2.82MHz default support by audio library
- higher frequencies seem to be possible

See https://www.ti.com/lit/an/sbaa383b/sbaa383b.pdf?ts=1680563663210
for configurations of multiple chips

## Power consumption

- Teensy 4.1: 100mA
- 25mA @ 3.3V for 4 channels at 96kHz for TLV320ADC5140
- 35mA @ 3.3V for 4 channels for TI PCM1865

### 8 channel
- 50mA/70mA for 4x2=8 channels
- 8 channel plus Teensy: 150mA/170mA
- 20Ah power bank / 0.15A = 133h/117h
- 8 x 8 = 64 channel plus control Teensy 200mA on 20Ah power bank: 1.4A/1.6Ah, lasts 14h/12.5h
- 1.4A/1.6A for 64 channels at 3.3V for 24h: 111/127VAh. On 12V car battery is just 9Ah/11Ah.

### 16 channel
- 100mA/140mA for 4x4=16 channels
- 16 channel plus Teensy: 200mA/240mA
- 20Ah power bank / 0.2A = 100h/83h
- 4 x 16 = 64 channel plus control Teensy 200mA on 20Ah power bank: 1A/1.2A, lasts 20h/16h
- 1A/1.2A for 64 channels at 3.3V for 24h: 80VAh/95VAh. On 12V car battery is just 7Ah/8Ah.

For power banks we need power supply switching every 24 hours on the fly (4 USB ports, 2 running, 2 new ones)!

Or just a single 20+ Ah car battery, lasting for two days!


## Storage

| channels | bits | sampling rate | per hour | per day |
| -------: | ---: | ------------: | -------: | ------: |
| 1        | 16   | 24kHz         | 173MB    | 4.2GB   |
| 4        | 16   | 24kHz         | 691MB    | 16.6GB  |
| 8        | 16   | 24kHz         | 1.4GB    | 33.2GB  |
| 16       | 16   | 24kHz         | 2.8GB    | 66.4GB  |


micro SD cards (prices from 2023):

| capacity | costs | 8 channels | 16 channels |
| -------: | ----: | ---------: | ----------: |
| 128GB    | 12 €  | 3.8 days   | 1.9 days    |
| 256GB    | 25 €  | 7.7 days   | 3.8 days    |
| 500GB    | 50 €  | 15.4 days  | 7.7 days    |

## Design

Use 8 channels (2 chips) and a 128GB, better 256GB microSD card and a
single 50Ah car battery. That lasts for 4 days minimum.
