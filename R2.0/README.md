# TeensyAmp R2.0

Based on the experiences with [TeensyAmp R1.0](../R1.0) we are
developing an improved version.


## Issues to be improved

- The signal is clipped at the bottom above Teensy 0V. Independent of
  gain.  Maybe we need to provide 3.3Volt to make it work -> no, this
  does not solve the issue.

  See [AD8224 data
  sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/AD8224.pdf),
  figures 25-28, in particular Fig 28. There is some asymmetry!

  ![AD8224-Fig28](images/AD8224-Fig28.png)

- Make it smaller!

- Power supply down to 3.3V!? not really, the AD8224 does not support
  this.

- The amplifier should generate 3.3V in addition to 1.6V,
  both for running the Amplifier and the Teensy.

- Use connectors that do not need that much room on the top?
  Make sure pins on the right (power and output) are on 2.54 raster.
  In a smart way! So that the amps can be easily soldered and connected
  to a base pcb, or directly on the Teensy! Like the Audio shield.
  Consider two use cases: (i) single amp directly soldered to Teensy,
  (ii) several amps.

- Screw terminals for inputs? Yes! Then one can easily combine the
  references or have them separated. And we do cut down on hight.

- High-pass filters: 10Hz, 100Hz, 300Hz What about OS203011MS1QP1
  (DP3T) as a switch to selectthe filter settings (same as for gain)?
  This one is not so wide!

- Low-pass filters: 7kHz, 15kHz, 33kHz for sampling rates of 20kHz,
  44kHz, 100kHz.

- Do we need USB connector?

- LED less bright!

