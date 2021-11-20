# TeensyAmp R1.0

by [Stefan Mucha](https://github.com/muchaste)

with support by [Avner Wallach](https://github.com/avner-wallach) and
[Jan Benda](https://github.com/janscience).


## Signals

VCC: 5V
VDD: 0V
GND1: 1.66V

VPP: 5V
VSS: 0V
GND2: 1.66V

## Pins

Input pins to the left, "TeensyAmp R1.0" bottom right.

### JP1
1: IN+ (bottom)
2: IN- (top)

### JP2
1: IN+ (bottom)
2: IN- (top)

### JP3

top row:
1 (left):  OUTB (JP2)
2 (right): OUTA (JP1)

bottom row (you might power the Teensy from these two pins):
3 (left):  VPP  5V
4 (right): VSS  0V -> this does not need to be connected to AGND or GND!

### JP4

1, 2 (top):    VCC
3, 4 (center): VDD
5, 6 (bottom): GND1

left column: connected to JP5

right column: VCC and VDD is used to create GND1 (1.6V)

### JP5
1 (top):     VPP = VCC
2 (center):  VSS = VDD
3 (bottom):  GND2 = GND1


## High-pass filter

| position                     | R1      | Ci    | taui   | fcutoff |
| :--------------------------- | ------: | ----: | -----: | ------: |
| p1 (upper jumper right)      | 100kOhm | 15uF  | 1.5s   | 0.1Hz   |
| p2 (upper jumper left)       | 100kOhm | 15nF  | 1.5ms  | 106Hz   |
| p3 (upper jumper cable left) | 100kOhm | 5.6nF | 0.56ms | 283Hz   |

WARNING: in AmplifierConfiguration2021-10-25.pdf 100Hz and 300Hz
high-pass filter are switched!


## Power consumption

| Configuration     | Voltage | Current | Power | Runtime |
| :---------------- | ------: | ------: | ----: | ------: |
| Teensy 3.5        | 5V      | 75mA    | 370mW | 133h    |
| Teensy 3.5        | 3.3V    | 68mA    | 225mW | 147h    |
| Teensy + SD       | 5V      | 103mA   | 515mW | 97h     |
| Teensy + SD       | 3.3V    | 96mA    | 315mW | 104h    |
| Amplifier         | 5V      | 11.4mA  | 57mW  | 877h    |
| Amplifier         | 3.3V    | 6.5mA   | 21mW  | 1588h   |
| Teensy + Amp      | 5V      | 87mA    | 433mW | 115h    |
| Teensy + Amp      | 3.3V    | 75mA    | 249mW | 133h    |
| Teensy + Amp + SD | 5V      | 115mA   | 575mW | 87h     |
| Teensy + Amp + SD | 3.3V    | 102mA   | 336mW | 98h     |

The last colum is the run time to be expected for a 10Ah battery (10Ah
divided by current).

So, the Teensy consumes about seven times more power than the amplifier.
If we want to cut power consumption, we need to cut it on the Teensy.
