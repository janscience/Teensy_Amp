# TeensyAmp R4.1

If not noted otherwise, all measurements at 48kHz sampling rate.

## Pre-amplifier

![preampinv](images/preampinv.png)

- R1=100k for grounding the signal
- C1=10uF and R2=4.7k for a 5Hz high-pass filter
- R2=4.7k and R3=47k for a 10x gain (gain=R3/R2)
- no low-pass filter 


### Reference voltage

![vref](images/vref.png)

- the voltage reference needs to be really stable!


### Pins

Pins of the PCM1865 - see page 11 and Fig 22 in the data sheet and
Figure 15 of the evaluation board manual:

| pin | name        | connects to | Teensy 4.1 pins | Teensy 3.5 pins |
| --: | :---------- | :---------- | --------------: | --------------: |
|  1  | VINL2/VIN1M | SIG 3       |                 |                 |
|  2  | VINR2/VIN2M | SIG 2       |                 |                 |
|  3  | VINL1/VIN1P | SIG 1       |                 |                 |
|  4  | VINR1/VIN2P | SIG 0       |                 |                 |
|  5  | Mic Bias    | unconnected |                 |                 |
|  6  | VREF        | Connect 1-μF capacitor C5 to AGND |   |   |
|  7  | AGND        | Analog ground to common ground |   |   |
|  8  | AVDD        | 3.3V power supply, Fig 70/71. Connect 0.1-μF and 10-μF capacitors C8, C9, R1 from this pin to AGND. |    |   |
|  9  | XO          | not used, open |   |   |
| 10  | XI          | not used, open |   |   |
| 11  | LDO         | Connect 0.1-μF and 10-μF capacitors from this pin to AGND? |    |   |
| 12  | DGND        | Digital ground connect to common ground |   |   |
| 13  | DVDD        | 3.3V power supply, Fig 70/71. Connect 0.1-μF and 10-μF capacitors from this pin to DGND. |    |   |
| 14  | IOVDD       | 3.3V power supply, tied to DVDD, Fig 70/71.  | From Teensy 3.3V? |   |
| 15  | SCKI        | not used, open |  |   |
| 16  | LRCK        | Audio data world clock (left right clock) input/output. | 20 | 23 |
| 17  | BCK         | Audio data bit clock input/output. | 21 |  9 |
| 18  | DOUT        | Audio data digital output.         |  8 | 13 |
| 19  | GPIO3/INTC  | not needed  |  |  |
| 20  | GPIO2/INTB/DMCLK | not needed | chip1: 28 / chip2: 35 | chip1: 28 / chip2: 35 |
| 21  | GPIO1/INTA/DMIN  | not needed | chip2: 29 / chip2: 36 | chip2: 29 / chip2: 36 |
| 22  | MISO/GPIO0/DMIN2 | not needed | chip1: 6, chip2: 32 | 38 |
| 23  | MOSI/SDA    | I2C bus SDA   | 18 | 18 |
| 24  | MC/SCL      | I2C bus CLOCK | 19 | 19 |
| 25  | MS/AD       | I2C addres: first chip low, second chip high |  |   |
| 26  | MD0         | tied low for I2C communication |  |   |
| 27  | VINL4/VIN4M | SIGALT 3     |    |   |
| 28  | VINR4/VIN3M | SIGALT 2     |    |   |
| 29  | VINL3/VIN4P | SIGALT 1     |    |   |
| 30  | VINR3/VIN3P | SIGALT 0     |    |   |

Pins of the Teensy:

| Teensy 4.1 pin | Teensy 3.5 pin |              |
| -------------: | -------------: | :----------- |
| Vin            | Vin            | Vin          |
| GND            | GND            | GND          |
| 3.3V           | 3.3V           | IOVDD        |
| 18             | 18             | I2C SDA      |
| 19             | 19             | I2C SCL      |
| 21             | 9              | BCK          |
| 20             | 23             | LRCK         |
| 8              | 13             | DOUT         |
| 28             | 28             | GPIO2 chip1  |
| 35             | 35             | GPIO2 chip2  |
| 29             | 29             | GPIO1 chip1  |
| 36             | 36             | GPIO1 chip2  |
| 6              | ?              | GPIO0 chip1  |
| 32             | ?              | GPIO0 chip2  |
| 0              | 4              | CAN RX       |
| 1              | 3              | CAN TX       |
| 24             | 24             | I/O          |
| 31             | 31             | LED inverted |


### 16 channels

In the following plot a 1kHz signal was supplied to each input channel in turn, on two R4.0 boards onnected to a single Teensy 4.1:

![16-channels](images/16channels-traces.png)

