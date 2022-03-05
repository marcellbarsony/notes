# Cisco Discovery Protocol (CDP)

**CDP (Cisco Discovery Protocol)** is a Cisco proprietary Data Link Layer (Layer 2) protocol.<br>
**CDP** is used to discovers information about directly connected Cisco equipment.
**CDP** can also be used for [On-Demand Routing](https://en.wikipedia.org/wiki/On_Demand_Routing), which is a method of including routing information in CDP announcements that dynamic routing protocols do not need to be used in simple networks.

To discover information, Cisco devices send **CDP** messages out each of their interfaces.
**CDP** messages contain information, such as hostname, network and data link addresses, device model, IOS version, etc.

## Operation

- Cisco devices send **CDP announcements** to the destination MAC address 01:00:0c:cc:cc:cc on each connected network interface.
  This multicast destination is also used in other Cisco protocols such as VLAN VTP.
- By default, **CDP announcements** sent every 60 seconds on interfaces that support [Subnetwork Access Protocol (SNAP)](https://en.wikipedia.org/wiki/Subnetwork_Access_Protocol) headers, including Ethernet, [Frame Relay](https://en.wikipedia.org/wiki/Frame_Relay) and [Asynchronous Transfer Mode](ATM)(https://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode).
- Each Cisco device (that supports CDP) stores the information received from other devices in a **CDP table** that can be viewed using the `show cdp neighbors` command, and via [SNMP](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol).
- The **CDP Table** information is refreshed each time an announcement is received, and the holdtime for that entry is reinitialized.

[[Wikipedia - CDP](https://en.wikipedia.org/wiki/Cisco_Discovery_Protocol)]

## Commands

To display information about directly connected devices, use the `show cdp neighbor` or the `show cdp neighbor details` command.

<details>
<summary>EXAMPLE - show cdp neighbors</summary>
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
- **Holdtime** – the amount of time (lifetime - 180 seconds) the local device will hold the information before discarding it if no more CDP packets are received.
- **Capability** – the capability of the directly connected device. The letter **S** indicates that the directly connected device is a switch.
  The letter **R** would indicate a router.
- **Platform** – the model and OS level running on the neighbor, **2960 series switch** in this case.
- **Port ID** – the neighbor device’s interface on which the CDP packets were sent, in this case **Fa0/1**.

To get even more information about the neighbors, use the `show cdp neighbors detail` command.

<details>
<summary>EXAMPLE - show cdp neighbors details</summary>
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
