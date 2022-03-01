# Cisco Discovery Protocol (CDP)

**CDP (Cisco Discovery Protocol)** is a proprietary protocol developed by Cisco used to discovers information about the locally attached Cisco equipment.
With CDP, the administrator can gather hardware and protocol information about neighboring devices, which can be helpful when troubleshooting or documenting the network.

To discover information, Cisco devices send CDP messages out each of their interfaces.
These messages contain information about them, such as their hostname, network and data link addresses, the device model, IOS version, etc.

To display information about directly connected devices, we use the show `cdp neighbor` command.

<details>
<summary>Example - show cdp neighbors</summary>
<br>

```
Floor1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID Local Intrfce Holdtme Capability Platform Port ID
Switch Gig 0/0 166 S 2960 Fas 0/1
```

</details>

As per the example above, there is one directly connected device.
Here is a description of each field:

- **Device ID** – the hostname of the directly connected device. In this case the hostname is **Switch**.
- **Local Interface** – the local interface on which the CDP messages were received (**Gi0/0** in this case).
- **Holdtime** – the amount of time the local device will hold the information before discarding it if no more CDP packets are received.
- **Capability** – the capability of the directly connected device. The letter **S** indicates that the directly connected device is a switch.
  The letter **R** would indicate a router.
- **Platform** – the model and OS level running on the neighbor, **2960 series switch** in this case.
- **Port ID** – the neighbor device’s interface on which the CDP packets were sent, in this case **Fa0/1**.

To get even more information about the neighbors, use the `show cdp neighbors detail` command.

<details>
<summary>Example - show cdp neighbors details</summary>
<br>

```
Floor1#show cdp neighbors detail

Device ID: Switch
Entry address(es):
Platform: cisco 2960, Capabilities: Switch
Interface: GigabitEthernet0/0, Port ID (outgoing port): FastEthernet0/1
Holdtime: 126

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASE-M), Version 12.2(25)FX, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2005 by Cisco Systems, Inc.
Compiled Wed 12-Oct-05 22:05 by pt_team

advertisement version: 2
Duplex: full
```

</details>

> **Note**<br>
> IEEE has released a vendor-neutral link layer protocol called **Link Layer Discovery Protocol (LLDP)** as an alternative to CDP.
