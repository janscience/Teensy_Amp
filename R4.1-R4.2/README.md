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

#### Anker PowerCore PD 10000 Redux

[Anker PowerCore PD 10000 Redux](https://support.anker.com/s/product/a085g000004x2B1AAI/powercore-10000-pd-redux)

10Ah power bank with a small diameter.

![anker powercore 10000 redux](https://support.anker.com/sfc/servlet.shepherd/version/renditionDownload?rendition=ORIGINAL_Jpg&versionId=0685g000007gY4p&operationContext=CHATTER&contentId=05T5g00000MSYpG)


##### CPU speed

| capacity | voltage | duration | channels | sampling rate | CPU speed |
| -------: | ------: | -------- | -------: | ------------: | --------: |
|     10Ah |      5V | 16h45min |       16 |         48kHz |    600MHz |
|     10Ah |      5V | 18h25min |       16 |         48kHz |    150MHz |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |

Reducing CPU speed spares about 1.1mA/10MHz. A reduction of at maximum
66mA is possible from the 600MHz.


##### Channels

| capacity | voltage | duration | channels | sampling rate | CPU speed |
| -------: | ------: | -------- | -------: | ------------: | --------: |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |
|     10Ah |      5V | 22h30min |       12 |         48kHz |     24MHz |
|     10Ah |      5V | 21h50min |       12 |         48kHz |     24MHz |
|     10Ah |      5V | 22h25min |       12 |         48kHz |     24MHz |
|     10Ah |      5V | 27h35min |        8 |         48kHz |     24MHz |
|     10Ah |      5V | 28h05min |        8 |         48kHz |     24MHz |
|     10Ah |      5V | 28h05min |        8 |         48kHz |     24MHz |
|     10Ah |      5V | 32h50min |        4 |         48kHz |     24MHz |
|     10Ah |      5V | 32h45min |        4 |         48kHz |     24MHz |

Teensy microcontroller draws 169mA of current.
At a sampling rate of 48kHz, each pcm chip (including additional SD card activity) draws 54mA of current.
16 channels draw in total 385mA of current (1.27W)


##### USB interface power savings

| capacity | voltage | duration | channels | sampling rate | CPU speed | comment        |
| -------: | ------: | -------- | -------: | ------------: | --------: | :------------- |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |                |
|     10Ah |      5V | 19h35min |       16 |         48kHz |     24MHz |                |
|     10Ah |      5V | 19h20min |       16 |         48kHz |     24MHz | Serial.end()   |
|     10Ah |      5V | 19h40min |       16 |         48kHz |     24MHz | Serial.end(), setTeensySpeed(24)   |
|     10Ah |      5V | 19h55min |       16 |         48kHz |     24MHz | shutdown_usb() |
|     10Ah |      5V | 20h00min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h40min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h10min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h45min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h25min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |

Shutting down the USB serial interface spares about 3mA. Just ending the serial interface is not noticable.


##### Sampling rate

| capacity | voltage | duration | channels | sampling rate | CPU speed | comment        |
| -------: | ------: | -------- | -------: | ------------: | --------: | :------------- |
|     10Ah |      5V | 19h50min |       16 |         24kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h45min |       16 |         24kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 19h40min |       16 |         24kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|     10Ah |      5V | 17h25min |       16 |         96kHz |     48MHz | shutdown_usb(), setTeensySpeed(48) |
|     10Ah |      5V | 17h10min |       16 |         96kHz |     48MHz | shutdown_usb(), setTeensySpeed(48) |
|     10Ah |      5V | 17h10min |       16 |         96kHz |     48MHz | shutdown_usb(), setTeensySpeed(48) |
|     10Ah |      5V | 17h25min |       16 |         96kHz |     48MHz | shutdown_usb(), setTeensySpeed(48) |

A sampling rate of 96kHz requires a higher CPU speed and thus consumes 54mA more current.
Reducing the sampling rate to 24kHz seems not to spare any power.


##### Backup SD card on SPI bus

| capacity | voltage | duration | channels | sampling rate | CPU speed | comment        |
| -------: | ------: | -------- | -------: | ------------: | --------: | :------------- |
|     10Ah |      5V | 16h40min |       16 |         48kHz |    150MHz | plus backup SD |
|     10Ah |      5V | 16h30min |       16 |         48kHz |    150MHz | plus backup SD |
|     10Ah |      5V | 18h20min |       16 |         48kHz |    150MHz |   no backup SD |
|     10Ah |      5V | 18h55min |       16 |         48kHz |    150MHz |   no backup SD |

Additional backup SD card on SPI bus draws about 50mA of current.
And CPU speed cannot be 24MHz.


#### Realpower

10Ah power bank

| capacity | voltage | duration | channels | sampling rate | CPU speed |
| -------: | ------: | -------- | -------: | ------------: | --------: |
|     10Ah |      5V | 17h20min |       16 |         48kHz |    600MHz |
|     10Ah |      5V | 16h50min |       16 |         48kHz |    600MHz |
|     10Ah |      5V | 23h35min |       12 |         48kHz |     24MHz |


#### KeepPower Li-Ion battery

[Keeppower 26650 - 5500mAh, 3.6V Li-Ion protected battery](https://www.akkushop.de/de/keeppower-26650-li-ion-akku-5500mah-36v-bis-37v-masse-699x265mm-pcb-geschuetzt/?_gl=1*3tpsz6*_up*MQ..*_gs*MQ..&gclid=Cj0KCQiAo5u6BhDJARIsAAVoDWt3GoXz8Iy4VtOCWRfemFEa7uiMu-8cfNHHLCeWJMEUk6c8qhZRTr8aAmmdEALw_wcB)

![Keeppower 26650 - 5500mAh, 3,6V](https://cdn03.plentymarkets.com/i9a0e0hd8l6w/item/images/12060/full/Keeppower-26650-5500mAh-3-6V-3-7V-mit-BMS-P2655C-.jpg)

| capacity | voltage | duration | channels | sampling rate | CPU speed | comment        |
| -------: | ------: | -------- | -------: | ------------: | --------: | :------------- |
|  2x5.5Ah |    3.6V | 33h05min |       16 |         24kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|  2x5.5Ah |    3.6V | 33h05min |       16 |         48kHz |     24MHz |                |
|  2x5.5Ah |    3.6V | 33h00min |       16 |         48kHz |     24MHz |                |
|  2x5.5Ah |    3.6V | 32h35min |       16 |         48kHz |     24MHz | shutdown_usb(), setTeensySpeed(24) |
|  2x5.5Ah |    3.6V | 29h00min |       16 |         96kHz |     48MHz | shutdown_usb(), setTeensySpeed(48) |
|  2x5.5Ah |    3.6V | 31h25min |       16 |         48kHz |    150MHz |                |
|  2x5.5Ah |    3.6V | 45h15min |        8 |         48kHz |    150MHz |                |
|  2x5.5Ah |    3.6V | 49h00min |        8 |         48kHz |     24MHz |                |
|  2x5.5Ah |    3.6V | 49h15min |        8 |         24kHz |     24MHz |shutdown_usb(), setTeensySpeed(24) |


