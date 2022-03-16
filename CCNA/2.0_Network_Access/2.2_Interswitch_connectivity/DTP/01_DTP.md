# Dynamic Trunking Protocol (DTP)

**Dynamic Trunking Protocol (DTP)** is a Cisco proprietary trunking protocol that is used to automatically negotiate trunking on a link between two VLAN-aware switches, and to negotiate the type of trunking encapsulation to be used.
It works on Layer 2 of the OSI model.
Trunk negotiations are managed by **DTP** only if the prt is directly connected to each other.

[[Wikipedia - Dynamic Trunking Protocol](https://en.wikipedia.org/wiki/Dynamic_Trunking_Protocol)]

[[Study CCNA - Cisco Dynamic Trunking Protocol (DTP) Explained](https://study-ccna.com/dynamic-trunking-protocol-dtp-cisco/)]

### DTP vs VTP

**DTP** and **VTP** serve different purposes:

- **DTP** aids with trunk port establishment.
- **VTP** communicates VLAN existence information between switches.

Neither protocol transmits the data frames that trunks carry.

### DTP packets

**DTP packets** are sent via **VLAN1** when **ISL** is used.<br>
**DTP packets** are sent via **Native VLAN** when **802.1Q** is used.
