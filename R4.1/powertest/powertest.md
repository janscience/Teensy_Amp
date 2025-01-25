# Power tests

Signal delivered via battery-driven signal-generator into water with
electrodes.

All measurements at x1000 gain (x10 fixed pregain, x100 gain on
PCM1865 chip).

## Single R4.1 boards

LiIon battery is the gold-standard:
![liion1](liion-1-x100.png)

Power bank is almost as good:
![powerbank1](powerbank-1-x100.png)

12V battery via non-isolated DC/DC converter to 5V is really bad:
![12V1](12V-1-nonisol-x100.png)
This problem we should fix! This looks like we need to improve the
quality of the DC input.

__Try other DC/DC converters!__ They might differ in the quality of
their output.


## Two R4.1 boards powered directly by single battery

![liion2](liion-2-x100.png)
![powerbank2](powerbank-2-x100.png)
Signal is mostly ok, but is corrupted by frequent spikes.
How can we fix this?

![12V2](12V-2-nonisol-x100.png)
No signal anymore with the 12V battery. 
This is the problem we need to fix!


## Plain isolated DC/DC converter

### Single R4.1 board

![powerbank1isolated](powerbank-1-isolated-x100.png)

![12V1isolated](12V-1-isolated-x100.png)

No signal - just a flat zero line. This is simpy not working.


### Two R4.1 boards

![powerbank2isolated](powerbank-2-isolated-x100.png)

Quite many noise spikes, but again no signal.

![12V2isolated](12V-2-isolated-x100.png)

Again, no signal - just a flat zero line.

No surprise here, because already with a single board we got zero lines.


## Isolated DC/DC converter with input ground and isolated V- connected via 100Ohm resistance

### Single R4.1 board

![powerbank1isolated100Ohm](powerbank-1-isolated-100Ohm-x100.png)
Powerbank almost as good as connected directly.

![12V1isolated](12V-1-isolated-100Ohm-x100.png)
12V battery as bad as via non-isolated DC/DC converter.

1kOhm results again in zero lines.

__Measure 0Ohm!__


### Two R4.1 boards

![powerbank2isolated100Ohm](powerbank-2-isolated-100Ohm-x100.png)

Signal as bad as with single board. The isolator does not solve the problem!

![12V2isolated100Ohm](12V-2-isolated-100Ohm-x100.png)

Signal as bad as with single board. But better than two boards on
non-isolated DC/DC converter.


## Conclusion

- The main problem is the quality of the power supply!
  The output of the 12V DC/DC converters is not good enough,
  it introduces most of the noise.

- Try to avoid DC/DC converters!

- Easy and efficient solution:
  Run three R4.1 boards in series on 12V battery!

- Improve power supply by adding some low-pass filtering.
  $$f_c = (2 \pi \tau)^{-1} \Leftrightarrow \tau = (2 \pi f_c)^{-1} $$
  With $f_c = 10$Hz we get $\tau=16$ms. Let's aim for 5ms.

  $$\tau = RC \Leftrightarrow C = \tau/R$$
  The voltage drop over the resistance is $V=RI$.
  With $I=500$mA and $R=1$Ohm this is 500mV.
  And for the capacitance we then get 10mF.

- The secondary problem is that when two or more R4.1 boards are
  connected, then we still get noise spikes probably from SD card
  writes or other digital noise from the other board.

  This also requires to improve the power input.
  
  
  