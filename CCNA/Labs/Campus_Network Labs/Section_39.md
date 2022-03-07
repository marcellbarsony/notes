# Section 39 - Campus Network Part 2

## Step 1 - Verify links using CDP

1. Verify CDP neighbors on **Core1**.

- CDP is enabled but no CDP neighbor is present.

```
Core1#show cdp
Global CDP information:
    Sending CDP packets every 60 seconds
    Sending a holdtime value of 180 seconds
    Sending CDPv2 advertisements is enabled
Core1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID    Local Intrfce   Holdtme    Capability   Platform    Port ID
```

2. Verify CDP and CDP neighbors on **Core2**.

- CDP is not enabled on **Core2**.
- CDP should be enabled on Cisco devices by default.

```
Core2#show cdp neighbors
% CDP is not enabled
```

3. Enable CDP on the Switches and the Router.

```
Core2(config)#cdp ?
  run  Enable CDP
Core2(config)#cdp run
```

4. Verify CDP configuration.

```
Global CDP information:
    Sending CDP packets every 60 seconds
    Sending a holdtime value of 180 seconds
    Sending CDPv2 advertisements is enabled
```

5. Verify CDP neighbors.

```
Core1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID    Local Intrfce   Holdtme    Capability   Platform    Port ID
Core2        Gig 1/0/23       164                    3650        Gig 1/0/23
Core2        Gig 1/0/24       164                    3650        Gig 1/0/24
Access1      Gig 1/0/1        150                    3650        Gig 1/0/23
Access2      Gig 1/0/2        125                    3650        Gig 1/0/23
Access3      Gig 1/0/3        138                    3650        Gig 1/0/23
```

## Step 2 - Verify links using LLDP

1. Enable LLDP on the switches.

- LLDP (Link Layer Discovery Protocol) is an industry standard protocol
- LLDP is not enabled by default on Cisco devices
- LDDP is useful in multi-vendor environments

```
Core1(config)#lldp run
```

2. Verify LLDP configuration.

```
Global LLDP Information:
    Status: ACTIVE
    LLDP advertisements are sent every 30 seconds
    LLDP hold time advertised is 120 seconds
    LLDP interface reinitialisation delay is 2 seconds
```

3. Verify LLDP neighbor configuration.

```
Core1#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
Device ID           Local Intf     Hold-time  Capability      Port ID
Access1             Gig1/0/1       120        R               Gig1/0/23
Access2             Gig1/0/2       120        R               Gig1/0/23
Access3             Gig1/0/3       120        R               Gig1/0/23
Core2               Gig1/0/23      120        R               Gig1/0/23
Core2               Gig1/0/24      120        R               Gig1/0/24
```

## Step 3 - Optimize Spanning Tree

1. Check Spanning Tree settings

```
Core1#show spanning-tree
```

> Note<br>
> Spanning Tree blocking ports transmit and receive management packets (network management protocols, e.g. CDP, LLDP, DTP).

2. Set SW Core1 as SPT primary on odd VLANs (VLAN 1, 10, 30)

```
Core1(config)#spanning-tree vlan 1 root primary
Core1(config)#spanning-tree vlan 10 root primary
Core1(config)#spanning-tree vlan 30 root primary
```

```
Core1(config)#spanning-tree vlan 1 priority 0
Core1(config)#spanning-tree vlan 10 priority 0
Core1(config)#spanning-tree vlan 30 priority 0
```

2. Set SW Core2 as SPT secondary (backup) on odd VLANS (VLAN 1, 10, 30)

```
Core2(config)#spanning-tree vlan 1 root secondary
Core2(config)#spanning-tree vlan 10 root secondary
Core2(config)#spanning-tree vlan 30 root secondary
```

```
Core2(config)#spanning-tree vlan 1 priority 4096
Core2(config)#spanning-tree vlan 10 priority 4096
Core2(config)#spanning-tree vlan 30 priority 4096
```

3. Set SW Core2 as SPT primary on even VLANs (VLAN 20, 100)

```
Core2(config)#spanning-tree vlan 20,100 priority 0
```

4. Set SW Core1 as SPT secondary (backup) on even VLANs (VLAN 20, 100)

```
Core1(config)#spanning-tree vlan 20,100 priority 4096
```

5. Verify VLAN Spanning Tree configuration

```
Core1#show spanning-tree
```

```
Core2#show spanning-tree
```

> Note<br>
> It is a good practice to have the core switches being root switches and backup routes for other VLANs.

The links between the two core switches are still blocking.<br>
The links need to be combined (or joined) in an ether channel to get better throughput.

## Step 4 - Optimize Spanning Tree - Ether Channel

Optimize Spanning Tree with Ether channel.<br>
Both links between the Core Switches need to be bonded into an Ether channel.

### Task Summary

Create the Ether channel (Port channel)

```
Switch(config)#int range g1/0/23 - 24
Swtich(config-if-range)# channel-group 1 mode active
```

Configure interfaces settings on the Port Channel.<br>
These settings are inherited by the interfaces.<br>

- When a **physical interface** is added to the **Port Channel**, the configuration need to be done on the **Port Channel** (`interface port-channel 1`) rather than on the **physical interfaces** (`int range g1/0/23 - 24`).
- The configuration applied on the logical **Port Channels** should filter down (be copied and applied) to the **physical interfaces** by the switch.
- The configuration applied needs to be verified on the **Port Channel** and the **physical interfaces** on both sides, on both **Logical Port channel**.
- To test the changes, the **physical interfaces** need to be `shut` and then `no shut`.

```
Switch(config)#interface port-channel 1
Switch(config-if)#switchport trunk encapsulation dot1q
Switch(config-ig)#switchport mode trunk
```

### Set up Ether Channel

1. `shut` the interfaces on Core SW1.

```
Core1(config)#interface range gigabitEthernet 1/0/23-24
Core1(config-if-range)#shut
```

2. Configure trunk mode on the switchports

- In this example, a Layer2 Ether channel is used
- 802.1q tagging is being run across the links
- It is acting as a traditional Layer 2 interfaces, rather than a routed interface

```
Core1(config-if-range)#switchport mode trunk
```

3. Create channel group

```
Core1(config-if-range)#channel-group 1 mode ?
  active     Enable LACP unconditionally
  auto       Enable PAgP only if a PAgP device is detected
  desirable  Enable PAgP unconditionally
  on         Enable Etherchannel only
  passive    Enable LACP only if a LACP device is detected

```

> Channel Group Protocols:<br>
> LACP (Link Aggregation Control Protocol) - Industry standard protocol<br>
> PAgP (Port Aggregation Protocol) - Cisco proprietary protocol<br>

> Channel Group Modes:<br>
> active - (LACP) The switch will use LACP messages to negotiate with the other side and actively try to form an Ether Channel with the switch on the other side of the link.<br>
> auto - (PAgP) The switch is only going to form an Ether Channel if
> desirable - (PAgP) The switch is going to desirably form an Ether channel.<br>
> on - The switch is not going to negotiate with the switch on the other side to set up an Ether Channel.<br>
> passive - (LACP) The switch waits for Ether Channel messages, then will form an Ether Channel with the other side.<br>

```
Core2(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1
```

4. `no shut` the interfaces.

```
Core1(config)#interface range gigabitEthernet 1/0/23-24
Core1(config-if-range)#no shut
```

5. Verify Ether Channel configuration

```
Core1#show etherchannel summary
Flags:  D - down        P - in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+--------------------------------

1      Po1(SU)           LACP   Gig1/0/23(P) Gig1/0/24(P)
```

## Step 5 - Optimize Spanning Tree - Ether Channel

In the real world, typically, once the interfaces are in the Port Channel, the configuration only needs to be done on the Ports channel.<br>
If the configuration is not applied on the physical interfaces, do the configuration on both the Port Channel and the physical interfaces.

1. Specify Spanning Tree link-type as `point-to-point`

- Configuration is being done on the physical interfaces
- Rapid Spanning Tree will converge quicker

```
Core1(config)#interface range gigabitEthernet 1/0/23 - 24
Core1(config-if-range)#spanning-tree link-type point-to-point
```

2. Verify Spanning Tree configuration

- The Port Channel is showing as Shared

```
Core1#show spanning-tree vlan 1
...
Interface        Role Sts Cost      Prio.Nbr Type
---------------- ---- --- --------- -------- --------------------------------
Gi1/0/1          Desg FWD 4         128.1    P2p
Gi1/0/2          Desg FWD 4         128.2    P2p
Gi1/0/3          Desg FWD 4         128.3    P2p
Po1              Desg FWD 3         128.29   Shr
```

3. Specify Spanning Tree link-type as `point-to-point`

- Configuration is being done on the Port Channel

```
Core2(config)#int port-channel 1
Core2(config-if)#spanning-tree link-type point-to-point
```

4. Verify Spanning Tree configuration

- The Port Channel is showing as ponint-to-point (P2p)

```
Core1#show spanning-tree vlan 1
...
Interface        Role Sts Cost      Prio.Nbr Type
---------------- ---- --- --------- -------- --------------------------------
Po1              Desg FWD 3         128.29   P2p
Gi1/0/1          Desg FWD 4         128.1    P2p
Gi1/0/2          Desg FWD 4         128.2    P2p
Gi1/0/3          Desg FWD 4         128.3    P2p
```

5. Verify VLAN propagation

- Vlan 10 is not propagated across the Port Channel

```
Core1#show spanning-tree vlan 10
...
Interface        Role Sts Cost      Prio.Nbr Type
---------------- ---- --- --------- -------- --------------------------------
Po1              Desg FWD 3         128.29   P2p
Gi1/0/1          Desg FWD 4         128.1    P2p
Gi1/0/2          Desg FWD 4         128.2    P2p
Gi1/0/3          Desg FWD 4         128.3    P2p
```

6. Configure trunking on the Port Channel

```
Core1(config)#interface port-channel 1
Core1(config-if)#switchport trunk encapsulation dot1q
Core1(config-if)#switchport mode trunk
```

## Step 6 - SVIs, IP addresses, routing

1. Configure IP routing

- IP routing is not enabled on the Layer 3 switch by default

```
Core1#show ip route
Default gateway is not set

Host               Gateway           Last Use    Total Uses  Interface
ICMP redirect cache is empty
```

- Enable IP routing

```
Core1(config)#ip routing
```

- Verify IP routing

```
Core1#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set
```

2. Configure IP addresses on Switches Virtual Interfaces (SVIs)

- The command `vlan 1` or `vlan 10` would create a VLAN in the VLAN database
- The command `interface vlan 1` or `interface vlan 10` would create a Switched Virtual Interfaces (or Layer 3 interface)

```
Core1(config)#interface vlan 1
Core1(config-if)#ip address 10.1.1.251 255.255.255.0
Core1(config-if)#no shut
```

3. Verify IP routing

```
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     10.0.0.0/24 is subnetted, 1 subnets
C       10.1.1.0 is directly connected, Vlan1
```
