# TeensyAmp R5.0

Work in progress.

With digitaly adjustable gain and filter settings.

Based on
- 2 [TI TLV320ADC5140](tlv320adc5140.pdf) with 4-channel ADC and adjustable gain
- [TI OPA1622](../R4.0/opa1622.pdf) as inverting pre-amplifier.

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
|  6  | IN1P_GPI1   | SIG ?, uncouple with 1uF      |                 |
|  7  | IN1M_GPO1   | SIG ?       |                 |
|  8  | IN2P_GPI2   | SIG ?       |                 |
|  9  | IN2M_GPO2   | SIG ?       |                 |
| 10  | IN3P_GPI3   | SIG ?       |                 |
| 11  | IN3M_GPO3   | SIG ?       |                 |
| 12  | IN4P_GPI4   | SIG ?       |                 |
| 13  | IN4M_GPO4   | SIG ?       |                 |
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
| VSS | Thermal pad is device ground. Short the thermal pad directly to the board ground plane. |   |


### Layout and programming instructions

- For layout instructions of the PCB see page 116 and Fig. 179 of the [TI TLV320ADC5140 data sheet](tlv320adc5140.pdf).
- For programming instructions see page 109 of the [TI TLV320ADC5140 data sheet](tlv320adc5140.pdf).



## Improvements needed over R4.x

- Replace screw-terminals by some plugs for connecting the electrodes.
- Add a coin-battery holder connected to Vbat for the Teensy real-time clock!
- More GND inputs for the screw terminal:
  - power GND (as we have it)
  - shield of the electrode cable
  - an optional reference
- Add screw terminals for sensors:
  - 3.3V, GND, and IO for Dallas DS18x20 temperature sensor 
  - I2C (3.3V, GND, SDA, SCL) for light sensor, etc.
- Some means of detecting a device ID for setting a uniqe file name.
- Improve supported power supply to 3.5 to 14V, so that AA, LiPo and
  car batteries, solar panels can be used.