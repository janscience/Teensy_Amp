# TeensyAmp R1.0

by [Stefan Mucha](https://github.com/muchaste)

with support by [Avner Wallach](https://github.com/avner-wallach) and
[Jan Benda](https://github.com/janscience).

- [EAGLE circuit board](teensy_amp_loads_of_switches.brd)
- [EAGLE design rule](teensy_amp_loads_of_switches.dru)
- [EAGLE schematics file](teensy_amp_loads_of_switches.sch)
- [EAGLE autorouter statistics](teensy_amp_loads_of_switches.pro)

The input signals are processed in the following way:

- simple RC high-pass filtering, cutoff frequencies selectable via
  S1/S2 switches (0.1Hz, 100Hz, 300Hz)

- amplification ([Analog devices
  AD8224HACPZ-WP](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8224.pdf)),
  gain selectable via S3/S4 switches (x5, x30, x180)

- low-pass filtering ([Analog devices
  OP2177ARZ](https://www.analog.com/media/en/technical-documentation/data-sheets/op1177_2177_4177.pdf)),
  cutoff frequencies selectable via S5/S6 switches (10kHz, 33kHz)

- a voltage-divider generates the 1.66V reference/ground potential ([Analog devices OP1177R](https://www.analog.com/media/en/technical-documentation/data-sheets/op1177_2177_4177.pdf))


## Circuit

![circuit](images/teensy_amp_switches_circuit.png)

- VCC: 5V
- VDD: 0V
- GND1: 1.66V

- VPP: 5V
- VSS: 0V
- GND2: 1.66V

## Pins

Input pins to the left, "TeensyAmp R1.0" bottom right.

![pins](images/teensy_amp_switches_PCB.png)

### JP1: differential input signal 1

- 1 IN+ (bottom)
- 2 IN- (top)

### JP2: differential input signal 2

- 1 IN+ (bottom)
- 2 IN- (top)

### JP3: output signals and power fowarding

top row:
- 1 (left):  OUTB (JP2)
- 2 (right): OUTA (JP1)

bottom row (you might power the Teensy from these two pins):
- 3 (left):  VPP  5V
- 4 (right): VSS  0V -> this does not need to be connected to AGND or GND!

### JP4: power and reference input and forwarding

- 1, 2 (top):    VCC
- 3, 4 (center): VDD
- 5, 6 (bottom): GND1

left column: connected to JP5

right column: VCC and VDD is used to create GND1 (1.6V)

### JP5: power for voltage divider

- 1 (top):     VPP = VCC
- 2 (center):  VSS = VDD
- 3 (bottom):  GND2 = GND1


## Filter

In files [`tests/filter-*.wav`](tests) the frequency of a 23mV signal
was increased as follows: 10Hz, 12.5Hz, 16Hz, 20Hz, 25Hz, 31.5Hz,
40Hz, 50Hz, 63Hz, 80Hz, 100Hz, 125Hz, 160Hz, 200Hz, 250Hz, 315Hz,
400Hz, 500Hz, 630Hz, 800Hz, 1000Hz, 1250Hz, 1600Hz, 2000Hz, 2500Hz,
3150Hz, 4000Hz, 5000Hz, 6300Hz, 8000Hz, 10000Hz.

100Hz high-pass, 7kHz low-pass:
![filter 100Hz-7kHz](images/filter-100Hz-7kHz-gain30-23mV-traces.png)

100Hz high-pass, 33kHz low-pass:
![filter 100Hz-33kHz](images/filter-100Hz-33kHz-gain30-23mV-traces.png)


### High-pass filter

| S1/S2 switch/jumper position | R1      | Ci    | tau    | fcutoff |
| :--------------------------- | ------: | ----: | -----: | ------: |
| p1 (upper jumper right)      | 100kOhm | 15uF  | 1.5s   | 0.1Hz   |
| p2 (upper jumper left)       | 100kOhm | 15nF  | 1.5ms  | 106Hz   |
| p3 (upper jumper cable left) | 100kOhm | 5.6nF | 0.56ms | 283Hz   |

WARNING: in AmplifierConfiguration2021-10-25.pdf 100Hz and 300Hz
high-pass filter are switched!


### Low-pass filter

| S5/S6 switch position | fcutoff |
| :-------------------- | ------: |
| p1 (left)             |  7kHz   |
| p2 (right)            | 33kHz   |


## Power consumption

### Powered by 5V (power bank)

| Configuration     | Voltage | Current | Power | Runtime |
| :---------------- | ------: | ------: | ----: | ------: |
| Amplifier         | 5V      | 11.4mA  | 57mW  | 877h    |
| Teensy 3.5        | 5V      | 75mA    | 370mW | 133h    |
| Teensy + SD       | 5V      | 103mA   | 515mW | 97h     |
| Teensy + Amp      | 5V      | 87mA    | 433mW | 115h    |
| Teensy + Amp + SD | 5V      | 115mA   | 575mW | 87h     |

The amplifier takes just 11.5mA (57mW).

The Teensy consumes about seven to ten (with SD card writes) times
more power than the amplifier.

If we want to cut power consumption, we need to cut it on the Teensy!


### Powered by 3.3V

| Configuration     | Voltage | Current | Power | Runtime |
| :---------------- | ------: | ------: | ----: | ------: |
| Amplifier         | 3.3V    | 6.5mA   | 21mW  | 1588h   |
| Teensy 3.5        | 3.3V    | 68mA    | 225mW | 147h    |
| Teensy + SD       | 3.3V    | 96mA    | 315mW | 104h    |
| Teensy + Amp      | 3.3V    | 75mA    | 249mW | 133h    |
| Teensy + Amp + SD | 3.3V    | 102mA   | 336mW | 98h     |

The last colum is the run time to be expected for a 10Ah battery (10Ah
divided by current).
