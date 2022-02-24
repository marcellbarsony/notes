## Native VLAN

A **Native VLAN** is a special VLAN whose traffic traverses on the 802.1Q trunk without any VLAN tag.

A **Native VLAN** is per trunk per switch configuration.
The 802.1Q trunk port assigns untagged traffic on a native VLAN.

### Management traffic

Management traffic will always use the **Native VLAN**:

- **STP BPDU** (Spanning Tree Protocol - Bridge Protocol Data Unit)
- **DTP** (Dynamic Trunking Protocol)

Management traffic will always use VLAN1 but tagged if native VLAN is not VLAN1:

- **CDP** (Cisco Discovery Protocol)
- **VTP** (VLAN Trunk Protocol)
- **PAgP** (Port Aggregation Protocol)
- **UDLD** (Unidirectional Link Detection)
