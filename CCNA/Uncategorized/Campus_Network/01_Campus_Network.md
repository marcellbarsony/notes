# Campus Network

[[Lecture](https://deloittedevelopment.udemy.com/course/complete-networking-fundamentals-course-ccna-start/learn/lecture/8297162#overview)]

| No. | Switch 1 | Switch 2 | Command                                              | Description                                  |
| --- | :------: | :------: | ---------------------------------------------------- | -------------------------------------------- |
| 1.  |    X     |    X     | `Switch(config)>host <hostname>`                     | Configure hostname                           |
| 2.  |    X     |    X     | `SW1#show interfaces gigabitEthernet 0/1 switchport` | Show g0/1 switchport configuration           |
| 3.  |    X     |    X     | `SW1# show vlan brief`                               | Show VLAN configuration                      |
| 4.  |    X     |    X     | `SW1(config)#int vlan 1`                             | Create Switched Virtual Interface (SWI)      |
| 5.  |    X     |    X     | `SW1(config-if)#ip address 10.1.1.1 255.255.255.0`   | Configure IP address on the SWI              |
| 6.  |    X     |    X     | `SW1(config-if)#no shut`                             | Enable the port                              |
| 7.  |    X     |    -     | `SW1#show spanning-tree`                             | Show Spanning Tree configuration             |
| 8.  |    -     |    X     | `SW2(config-if)#no switchport`                       | Configure port as Routed Port (Layer 3 port) |

### 2. Command

- This physical interface is a Layer 2 interface.
- This interface supports protocols such as Spanning Tree
- Switchport is enabled (by default)
- Switchport is using dynamic auto DTP mode
- Switchport is in static access mode
- Negotiation of trunking is enabled - but it hasn't negotiated trunking with the other side
- The VLAN that interface belongs to is: VLAN 1

```
SW1#show interfaces gigabitEthernet 0/1 switchport
Name: Gig0/1
Switchport: Enabled
Administrative Mode: dynamic auto
Operational Mode: static access
Administrative Trunking Encapsulation: negotiated
Operational Trunking Encapsulation: native
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: none
Administrative private-vlan host-association: none
Administrative private-vlan mapping: none
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk private VLANs: none
Operational private-vlan: none
Trunking VLANs Enabled: All
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL
Protected: false
Unknown unicast blocked: disabled
Unknown multicast blocked: disabled
Appliance trust: none
```

### 3. Command

- Only VLAN 1 and the other default VLANs are configured on the switches

```
SW1# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                                Gig0/1, Gig0/2
1002 fddi-default                     active
1003 token-ring-default               active
1004 fddinet-default                  active
1005 trnet-default                    active
```

### 4. Command

- Create Switched Virtual Interface (SWI)
- The interface came down

```
SW1(config)#int vlan 1
*Mar 13 23:44:24.482: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to down
SW1(config-if)#
```

### 5-6. Command

- Configure IP address on the interface
- Enable interface
- Interfaces come up on SW1 and SW2: the switches are now able to ping each other.

```
SW1(config-if)#ip address 10.1.1.1 255.255.255.0
SW1(config-if)#no shut

SW1(config-if)#
%LINK-5-CHANGED: Interface Vlan1, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
```

### 7. Command

- Interface Gi0/1 is the designated port
- Interface Gi0/1 is forwarding

```
SW1#show spanning-tree
VLAN0001
  Spanning tree enabled protocol ieee
  Root ID    Priority    32769
             Address     0001.4334.7280
             This bridge is the root
             Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     0001.4334.7280
             Hello Time  2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  20

Interface        Role Sts Cost      Prio.Nbr Type
---------------- ---- --- --------- -------- --------------------------------
Gi0/1            Desg FWD 4         128.25   P2p
```

### 8. Command

- Make the port (Gig0/0) a Routed port (Layer 3)
- Routed ports are typically used between Switches and Routers
- SWIs and VLANs are typically used in a campus environment where you need to tag multiple VLANs across the interface
- Routed ports doesn't have the concept of VLANs

```
SW3(config-if)#no switchport
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down

%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up
```

- Show switchport configuration
- Switchport is disabled

```
SW3#show interfaces gig 0/1 switchport
Name: Gig0/1
Switchport: Disabled
```

- On the Routed interface, an IP address can be directly configured
- The Routed interface becomes a Layer 3 interface
- STP and DTP are not configured on the port anymore

```
SW3(config)#interface gig0/1
SW3(config-if)#ip address 10.1.2.1 255.255.255.0
```

```
SW3#show running-config
interface GigabitEthernet0/1
 no switchport
 ip address 10.1.2.1 255.255.255.0
 negotiation auto
```
