## Spanning Tree Priority: Root Primary and Root Secondary

**STP** is a Layer 2 loop prevention mechanism that will block one port on the network switch if it detects a loop of broadcast messages within its architecture.
By default, Spanning Trees are enabled on most interconnected Cisco switches.

Switches send out BDPU on all active interfaces.
BPDU contains STP information needed to elect a root switch and detect loops.

# STP Root Switch Election

The SPA process begins with the **Root Switch Election**.<br>

The election is based on the **Bridge ID**s (**BID**s) sent in the BPDUs.<br>
Each switch that participates in STP will have a 8-byte **Bridge ID** that comprises of the following data:

- **2-byte Bridge Priority field** — All switches have the priority of 32768 by default.<br>
  This value can be changed using configuration commands.

- **6-byte System ID** — A value based on the MAC address of each switch.

A switch with the **lowest BID** will become a Root Switch - as lower number means higher priority.

### PVST+ Extended Bridge ID

The **PVST+ Extended Bridge ID** is still 8-bytes in length and comprises of the following data:

- **4-bit Bridge Priority field** — All switches have the priority of 32768 by default.<br>
  This value can be changed using configuration commands.

- **12-bit Extended System ID** — Populated with the VLAN number.

- **6-byte System ID** — A value based on the MAC address of each switch.

If all the spanning tree bridge priority has the same priority value on all the switches, then the MAC address will be the tiebreaker.
The **lowest MAC address** will be elected as the **Root Bridge**.<br>
Most of the older switches have a lower value of MAC address - have lower bandwidth, and limited CPU/memory as compared to newer switches.
Electing an older switch as the **Root Bridge** could cause a suboptimal operation on a network.

## ST Priority Root Bridge Optimization

### BID priority

To influence the election process, the BID priority can be changed to a lower value on a switch.

```
SW1(config)#spanning-tree vlan <vlan_id> priority <value>
```

The priority must be in increments of 4096:

```
SW1(config)#spanning-tree vlan 1 priority 224
  % Bridge Priority must be in increments of 4096.
  % Allowed values are:
  0 4096 8192 12288 16384 20480 24576 28672
  32768 36864 40960 45056 49152 53248 57344 61440
```

### Root primary

To prevent having a suboptimal network, a Root Bridge could be chosen manually.<br>
To do that, the value of the Root Bridge could be manually configured using the `root primary` command.

```
SW1(config)#spanning-tree vlan <vlan_id> root primary
```

### Root secondary

To optimize further, we need to a **Secondary Root Bridge** to be set in case the **Primary Root Bridge** is not operational.
To do that, we enter the `root secondary` command.
This command will set the bridge priority to 28672, which is lower than the default priority but higher than the root primary.

```
SW2(config)#spanning-tree vlan <vlan_id> root secondary
```

### Verify changes

The changes can be verified with the `show spanning-tree vlan <vlan_id>` command

```
SW1#show spanning-tree vlan 1
  VLAN0001
  Spanning tree enabled protocol ieee
  Root ID Priority 24577
  Address 0001.9725.3338
  Cost 19
  Port 1 (FastEthernet0/1)
  Hello Time 2 sec Max Age 20 sec Forward Delay 15 sec
  Bridge ID Priority 28673 (priority 28672 sys-id-ext 1)
  Address 0040.0B2C.E63A
  Hello Time 2 sec Max Age 20 sec Forward Delay 15 sec
  Aging Time 20
```
