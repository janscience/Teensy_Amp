# TeensyAmp R5.0

Work in progress.

With digitaly adjustable gain and filter settings.


## TI TLV320ADC5140

- 4 input channels
- 4 ADCs
- upto 4 chips can be daisy-chained

See
- [web site](https://www.ti.com/product/TLV320ADC5140)


## Improvements over R4.x

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