## CAN bus

Several R4.1 devices can be synchronized via CAN-FD bus.  The CAN bus
needs to be isolated from the rest and will be powered externally.

![can-isolated](images/can-isolated.png)

Isolation on the level of the CAN RX, CAN TX and the I/O lines. The
CAN transceiver is already behind the isolation barrier and is
powered externally.  Therefore, we do not need the shutdown and
standby functionalities of the transceiver anymore.

- CAN-FD transceiver: [TI TCAN332 D](../R4.0/tcan334.pdf) without any standby, silent or shutdown modes.

![TCAN332](https://www.ti.com/ods/images/SLLSEQ7E/D_sop_pin_diagram_tcan332.svg)

- 4 channel digital isolator (2 forward, two reverse): [TI ISO6742 DW](https://www.ti.com/product/ISO6742).
  See Figure 10-2 in the data sheet for layout design.

![ISO6742](https://www.ti.com/ods/images/SLLSFJ6G/GUID-20210126-CA0I-SGMD-HJJB-7CFZ95JL2VND-low.gif)

- Two additional digital I/O lines for indexing the devices.

- 2x (5)6-pin Connectors for external VCC and GND, CANL, CANH, and one I/O line.

| Teensy 4.1 pin | Teensy_Amp R4.1b | Isolator intern | Isolator extern | Transceiver   | Connector Up | Connector Down |
| -------------: | :--------------- | :-------------- | :-------------- | :------------ | :----------- | :------------- |
| 3.3V           | VDD              | VCC1            |                 |               |              |                |
| GND            | GND              | GND1            |                 |               |              |                |
|                |                  |                 |                 |               | 1 (5 - 12V)  | 1 (5 - 12V)    |
|                |                  |                 | External VCC2   | External VCC  | 2            | 2              |
|                |                  |                 | External GND2   | External GND  | 3            | 3              |
| (36) remove    | (CAN SHDN)       |                 |                 |               |              |                |
| (37) remove    | (CAN STB)        |                 |                 |               |              |                |
| 30             | CAN RX           | OUTA            | INA             | RXD           | 4 CANL       | 4 CANL         |
| 31             | CAN TX           | INA             | OUTA            | TXD           | 5 CANH       | 5 CANH         |
| 28 (was 40)    | I/O UP           | INB             | OUTB            |               | 6 I/O        |                |
| 29 (was 41)    | I/O DOWN         | OUTB            | INB             |               |              | 6 I/O          |
|                |                  | EN1 to VCC1     | EN2 to VCC2     |               |              |                |

Two vertical connectors with 6 contacts (external GND, external 3.3V, CANL CANH, I/O, unused I/O) one for upstream, one for downstream.


See also:
- [power and signal isolation](https://www.digikey.com/en/articles/how-to-implement-power-and-signal-isolation-for-reliable-operation-of-can-buses)
- [TJA1052i](https://www.nxp.com/docs/en/data-sheet/TJA1052I.pdf)
- [TI isolators](https://www.ti.com/isolation/digital-isolators/overview.html)


## Grid configuration

See [power tests](powertest/powertest.md)

One power source driving several PCBs.

