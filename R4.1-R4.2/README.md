# TeensyAmp R4.1 + R4.2

The [TeensyAmp R4.1](../R4.1) can be stacked on top of the [TeensyAmp
R4.2](../R4.2):

![R4.1b + R4.2b](images/Teensy_Amp-R41b-R42b.jpg)

![R4.1b + R4.2b side](images/Teensy_Amp-R41b-R42b-side.jpg)

For the first version of PCB boards, see [R4.1 + R4.2](r4142.md).


## Connectors

molex [Micro-Lock Plus](https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/micro-lock-plus-connectors) with [1.25mm pitch](https://www.molex.com/content/dam/molex/molex-dot-com/en_us/pdf/datasheets/987652-6322.pdf). See [application specification](https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/applicationspecificationspdf/505/505565/5055650000-AS-000.pdf) for an overview and part numbers.

Here we use right-angle SMT male connectors, 4 pins, part number 5055670471, [datasheet](../R4.1/molex5055670471_sd.pdf) for
the 8 input channels.

Use the precrimped cables from the cable assembly 45111 series for connecting your electrodes (30cm female/female 26 AWG cable, 7mm wide, part number 451110403).


### 16 channels

The two boards together provide 16 input channels.


### Power consumption

See the [first version](r4142.md#power-consumption) for power consumption measurements.


## Software

Use
[ControlPCM186x.h](https://github.com/janscience/TeeRec/blob/main/src/ControlPCM186x.h) of the [TeeRec library](https://github.com/janscience/TeeRec) for setting up the [TI PCM1865](../R4.0/pcm1865.md) chips. The TDM data stream can then be read in via [InputTDM.h](https://github.com/janscience/TeeRec/blob/main/src/InputTDM.h).

Use [ESensors](https://github.com/janscience/ESensors) library for communication with sensors connected to the OneWire and I2C bus.


## Applications

- [R4-sensors-logger](https://github.com/janscience/TeeGrid/tree/main/examples/R4-sensors-logger) 
- [R4-logger](https://github.com/janscience/TeeGrid/tree/main/examples/R4-logger) 
