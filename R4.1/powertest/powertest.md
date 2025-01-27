# Power tests

630Hz signal delivered via battery-driven signal-generator into water
with electrodes.

All measurements at x1000 gain (x10 fixed pregain, x100 gain on
PCM1865 chip).

## Single R4.1 board powered directly by a battery

LiIon battery is the gold-standard:
![liion1](liion-1-x100.png)
This is as good as it gets in this setting.

Power bank is almost as good:
![powerbank1](powerbank-1-x100.png)

12V battery via non-isolated DC/DC converter to 5V is really bad:
![12V1](12V-1-nonisol-x100.png)
This problem we should fix! Looks like we need to improve the
quality of the DC input.


## Two R4.1 boards powered directly by single battery

![liion2](liion-2-x100.png)
![powerbank2](powerbank-2-x100.png)
Signal is mostly ok, but is corrupted by frequent spikes.
How can we fix this?

![12V2](12V-2-nonisol-x100.png)
No signal anymore with the 12V battery. 
This is the problem we need to fix!


## Conclusion

- The primary problem is the quality of the power supply!
  The output of the 12V DC/DC converters is not good enough,
  it introduces most of the noise.

- Improve power supply by adding some low-pass filtering.

  $$f_c = (2 \pi \tau)^{-1} \Leftrightarrow \tau = (2 \pi f_c)^{-1}$$
  
  With $f_c = 10\text{Hz}$ we get $\tau=16\text{ms}$ .
  Let's better aim for 5ms, i.e. 32Hz.

  $$\tau = RC \Leftrightarrow C = \tau/R$$
  
  The voltage drop over the resistance is $V=RI$.
  With $I=500\text{mA}$ and $R=1\Omega$ this is 500mV.
  For such a $1\Omega$ resistance we then get for the capacitance 5mF.
  For an $0.1\Omega$ resistance (50mV voltage drop) we then get for the capacitance 50mF.

- The secondary problem is that when two or more R4.1 boards are
  connected, then we still get noise spikes probably from SD card
  writes or other digital noise from the other board.

  This also requires to improve the power input.
  
  
  