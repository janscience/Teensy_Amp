# TeensyAmp R4.1 + R4.2

The [TeensyAmp R4.1](../R4.1) can be stacked on top of the [TeensyAmp
R4.2](../R4.2):

![R4.1 + R4.2](images/Teensy_Amp-R41-R42.png)

![R4.1 + R4.2 side](images/Teensy_Amp-R41-R42-side.png)

![R4.1 + R4.2 front](images/Teensy_Amp-R41-R42-front.png)


### 16 channels

The two PCBs provide 16 input channels.

In the following plot a 1kHz signal was supplied to each input channel in turn:

![16-channels](images/16channels-traces.png)

The 16 channels are all in sync (same 1kHz signal on all channels):

![16-channels-sync](images/16channels-sync-traces.png)


### Power consumption

| brand                       | capacity | voltage | duration | channels | sampling rate | CPU speed |
| :-------------------------- | -------: | ------: | -------- | -------: | ------------: | --------: |
| Realpower                   |     10Ah |      5V | 17h20min |       16 |         48kHz |    600MHz |
| Realpower                   |     10Ah |      5V | 16h50min |       16 |         48kHz |    600MHz |
| Realpower                   |     10Ah |      5V | 23h35min |       12 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 16h45min |       16 |         48kHz |    600MHz | 
| Anker PowerCore 10000 redux |     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 22h30min |       12 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 21h50min |       12 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 22h25min |       12 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 27h35min |        8 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 28h05min |        8 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 28h05min |        8 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 32h50min |        4 |         48kHz |     24MHz |
| Anker PowerCore 10000 redux |     10Ah |      5V | 32h45min |        4 |         48kHz |     24MHz |
| 2x KeepPower 26650 5500mAh  |  2x5.5Ah |    3.6V | 33h05min |       16 |         48kHz |     24MHz |
| 2x KeepPower 26650 5500mAh  |  2x5.5Ah |    3.6V | 33h00min |       16 |         48kHz |     24MHz |
| 2x KeepPower 26650 5500mAh  |  2x5.5Ah |    3.6V | 49h00min |        8 |         48kHz |     24MHz |


