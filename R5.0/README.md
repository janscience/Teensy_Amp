# TeensyAmp R5.0

Work in progress.

Based on
- 2 [TI TLV320ADC5140](tlv320adc5140.pdf) with 4-channel ADC and adjustable gain
- 4 [TI OPA1662](opa1662.pdf) as pre-amplifier

## TLV320ADC5140

- [TI web site](https://www.ti.com/product/TLV320ADC5140)
- [data sheet](tlv320adc5140.pdf)
- [Multiple devices with shared TDM bus](sbaa383c.pdf)
- [Sampling rates](sbaa381b.pdf)
- [Power consumption](sbaa379.pdf)

### Pins

Pins of the TLV320ADC5140 - see page 4 in the data sheet:

| pin | name        | connects to | Teensy 4.1 pins |
| --: | :---------- | :---------- | --------------: |
|  1  | AVDD        | 3.3V power supply. Connect 0.1-μF and 1-μF capacitors to GND and 3.3V supply. See Fig. 172. |    |
|  2  | AREG        | Analog on-chip regulator output voltage for analog supply. Connect 0.1-μF and 10-μF capacitors to GND. |   |
|  3  | VREF        | Analog reference voltage filter output. Connect min. 1uF to AVSS |   |
|  4  | AVSS        | Analog ground. Short this pin directly to the board ground plane. All ground pins (AVSS and VSS) must be tied together. |   |
|  5  | MICBIAS     | unconnected |                 |
|  6  | IN1P_GPI1   | SIG 1P      |                 |
|  7  | IN1M_GPO1   | SIG COMMON  |                 |
|  8  | IN2P_GPI2   | SIG 2P      |                 |
|  9  | IN2M_GPO2   | SIG COMMON  |                 |
| 10  | IN3P_GPI3   | SIG 3P      |                 |
| 11  | IN3M_GPO3   | SIG COMMON  |                 |
| 12  | IN4P_GPI4   | SIG 4P      |                 |
| 13  | IN4M_GPO4   | SIG COMMON  |                 |
| 14  | SHDNZO      | Device hardware shutdown and reset (active low) | Some digital Pin  |
| 15  | ADDR1_MISO  | I2C slave address A1 pin. Connect to GND. |  |
| 16  | ADDR0_SCLK  | I2C slave address A0 pin. Connect to GND. |  |
| 17  | SCL_MOSI    | clock pin for I2C control bus | 19 |
| 18  | SDA_SSZ     | data pin for I2C control bus | 18 |
| 19  | IOVDD       | Digital I/O 3.3V power supply. See Fig. 172. | Teensy 3.3V |
| 20  | GPIO1       | General purpose digital input/output 1 (e.g. MCLK) |   |
| 21  | SDOUT       | Audio serial data bus output    |  8 |
| 22  | BCLK        | Audio serial data bus bit clock | 21 |
| 23  | FSYNC       | Audio serial data bus frame synchronization signal (LRCLK) | 20 |
| 24  | DREG        | Digital regulator output voltage for digital core supply. Connect 0.1-μF and 10-μF capacitors to GND. |   |
|     | VSS | Thermal pad is device ground. Short the thermal pad directly to the board ground plane. |   |

For layout instructions of the PCB see page 116 and Fig. 179 of the [TI TLV320ADC5140 data sheet](tlv320adc5140.pdf).


Teensy pins:

| Teensy 4.1 pin | Teensy_Amp R5.1 | Teensy_Amp R5.2 |
| -------------: | :----------- | :-------------- |
| Vin            | Vin +5V      | Vin +5V         |
| GND            | GND          | GND             |
| 3.3V           | VDD          | VDD             |
| 18             | I2C SDA      | -               |
| 19             | I2C SCL      | -               |
| 17             | -            | I2C SDA         |
| 16             | -            | I2C SCL         |
| 21             | BCK          | -               |
| 20             | FSYNC        | -               |
| 8              | DIN          | -               |
| 4              | -            | BCK             |
| 3              | -            | FSYNC           |
| 5              | -            | DIN             |
| 14             | -            | -               |
| 15             | GPIO3_1 chip1 | -              |
| 22             | GPIO3_2 chip2 | -              |
| 0              | -            | GPIO3 chip1     |
| 1              | -            | GPIO3 chip2     |
| 30             | -            | -               |
| 31             | -            | -               |
| 36             | -            | -               |
| 37             | -            | -               |
| 40             | -            | -               |
| 41             | -            | -               |
| 26             | LED extern   | -               |
| 27             | -            | LED extern      |


- Add data pin for Temperature sensor
- Add I2C pins for sensors


## Pre-amplifiers

![amplifiers](images/amplifiers.png)

### Power supply

- All opamps and the ADC are supplied by AVDD=3.3V relative to GND=0V.
- AVDD is provided by [onsemi NCP164CSN330T1G](ncp164c.pdf) 3.3V LDO with 300mA.

### Reference voltage sets virtual ground 

- All signals oscillate around a virtual ground VGND.
- VGND is created from half of MICBIAS of the TLV320ADC chip via a voltage divider.
- TODO: estimate currents!
- TODO: stabilize VGND via opamp?

- no longer needed: VGND is provided by voltage reference (e.g. 1.6V: [MAX6018AEUR16+T](max6018.pdf), 1.024V/1.2V/1.6V/1.8V TI REF35, 1.024V/1.25V/1.8V MicroChip MCP1502)

### Voltage divider

- R0 forms a voltage divider with R1 and R2 (R1=R2) attenuating strong signals with a gain of R1/(2R0+R1) (gain=0.1x, red).
- Alternatively, channels can be fed in directly (gain=1).
- Have two connectors, one for each option.

### Input impedance

- Is given by R1, R2, and R3 in parallel.
- TODO: make it as high as possible
- TODO: make test measurements in water to see what high means

### High-pass filter

- C1=10uF forms a high-pass filter with R2, R1, and R0.
- Time constant is tau=R2*C1*(R2+2*R0)/(R2+R0) , if R1=R2.
  tau=1s (R0=0), tau=2s (R0=500k)
- High-pass filter pulls signals to VGND by subtracting each signals DC offset.
- This is crucial to keep the signals within the operating range of the opamps.

### Pre-amplifier

- The [TI OPA1662](opa1662.pdf) non-inverting opamps (green) operate on
  virtual ground given by VGND.
  They return the amplified SIGx relative to VGND:
  gain*(SIGi-VGND)+VGND
  (in theory... with a gain of x11 the mean of the output is higher than VGND.
  This can be compensated for by a slightly lower VGND).
  The full-range output is then between GND and AVDD.
  Because of the common mode rejection (see below) non-inverting amplifiers
  are the only possibility.
- gain=1+R5/R4. For changing gain change R5.
  For R4=10k and R5=100k we get a x11 gain.
  For R4=10k and R5=10k we get a x2 gain.
  Although for R4=1k, ringing in response to step inputs is slightly smaller,
  R4=10k appears to be more stable and less noisy when having the R0/R1 voltage divider in front.
- In single-ended mode (S1 connected to MONO) we measure SIGi and thus
  get an approximated monopolar measurement.
- The INxM pins should be connected to VGND (or GND).
- This does not reject the common mode, mean(SIGi), which might be a problem
  with large external noise, or when coupling two or more loggers.
- TODO: test the possibility of an optional reference electrode at VGND.
- When having electrodes in a tank: connect VGND to ground of building. TOOD: Test it!

### Common mode rejection:

- Set S1 to DIFF.
- Via R3 we get the common mode signal AVRG=mean(SIGi) as an input to OP0,
  which is not contaminated by other sources.
- This is amplified in the same way against VGND as the signals.
- Only in this non-inverting configuration do we get an average signal
  independent of the number of input channels,
  because the current into the non-inverting input is zero and then
  the currents via R3 add up to zero!
- Measuring this in differential mode subtracts common mode from the signals:
  SIGi - mean(SIGi).
- This does not result in a monopolar measurement!
  The subtraction of the average introduces
  fake signals on channels without input, resembling the negative input
  on another channel. Also the average over all recorded signals is zero:
  mean(SIGi - mean(SIGi)) = mean(SIGi) - mean(SIGi) = 0.
  The larger the number of input channels, the more channels might
  have no signal, the closer mean(SIGi) to zero.

- Use [CUS-22TB](../R4.1/cus2604293.pdf) to switch between MONO and DIFF.
- Use a digital pin to check for the position of this pin.
- Based on this configure the ADC to differential or single-ended measurement.


### Input ranges:

#### ADC

[TI TLV320ADC5140](tlv320adc5140.pdf)

- single ended, AC coupled, with decoupling: saturates at +-1.375V  (p-p amplitude of 2.75V!)
- single ended, AC coupled, without decoupling: saturates at 0V - 2.75V, DC offset at 1.375V, not so tolerant against offsets.
- single ended, DC coupled, without decoupling: saturates at 0V - 2.75V, DC offset at 1.375V, it tolerates negative inputs but they are distorted. DC offset can be quite positive, but not negative.

#### OpAmps

[TI OPA1662](opa1662.pdf)

We have negative supply V- = GND and positive supply V+ = AVDD = 3.3V
for the non-inverting opamp.

The output of the OPA1662 is always clipped at GND and V+: GND < OUTx < V+
(the datasheet actually says V- + 0.6V < OUTx < V+ - 0.6V).
With VGND=AVDD/2=1.6V any signal centered around VGND is properly mapped onto
gain*(CHx-VGND)+VGND.
However, depending on the circuit, the optimal value of VGND can be considerably lower.

The opamp draws about 3.5mA for a full-scale sinewave on a single channel (two still need to be tested).

#### OpAmp with ADC

For best results (full range from GND to 2.75V measurements) we need

- positive supply of opamps at AVDD=3.3V (not 2.75V!)
- VGND = 1.6V (neither 2.75V nor 2.75V/2 or 1.8V!) produces best results with lowest THD for full scale signals.
- VGND draws less than 0.1mA of current for a single channel.
- differential, AC or DC coupled, with or without decoupling capacitances, with constant voltage at INxM: input on INxP is still limited to single-ended full range, although readings suggest twice the range.

Options:

- [onsemi NCP164CSN330T1G](ncp164c.pdf) 3.3V LDO with 300mA
  for supplying both the TLV320ADC and the opamps.
- 1.6V voltage reference for the opamps (e.g. [MAX6018AEUR16+T](max6018.pdf)).


## Improvements over R4.x

- 32 channel with 4PCBs!
- Properly clipping.
- Alternative 0.1x input (2x 4pin molex connectors for x1 plus 2x 4pin molex connectors for x0.1).
- Add GND/VGND pins for electrode cable shield
  (2-4 times, 1-2 at each side of the main PCB).
- Add VGND pin for external reference.
- Add voltage-divider with 2x 100kOhm for measuring supply power voltage.
- Add eeprom for storing PCB version and potential calibration values,
  and all the configuration. 
  e.g. microchip 24FC16T-E/OT36KVAO with 16kbit at I2C bus
