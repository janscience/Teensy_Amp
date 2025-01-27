# Power tests

Signal delivered via battery-driven signal-generator into water with
electrodes.

All measurements at x1000 gain (x10 fixed pregain, x100 gain on
PCM1865 chip).

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

