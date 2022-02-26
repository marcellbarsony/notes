## STP - Electing Root Switch

The STP process begins with the **root switch election**.<br>
The election is based on the **bridge IDs (BIDs)** sent in the BPDUs.
Each switch that participates in STP will have a 8-byte switch ID that comprises of the following fields:

- **2-byte priority field** — All switches have the priority of 32768 by default.<br>
  This value can be changed using configuration commands.

- **6-byte system ID** — A value based on the MAC address of each switch.

A switch with the lowest BID will become a root switch. (Lower number means higher priority)

## Root switch configuration

To influence the election process, the BID priority can be changed to a lower value on a switch.

```
SW1(config)#spanning-tree vlan <ID> priority <value>
```

The priority must be in increments of 4096:

```
SW1(config)#spanning-tree vlan 1 priority 224
  % Bridge Priority must be in increments of 4096.
  % Allowed values are:
  0 4096 8192 12288 16384 20480 24576 28672
  32768 36864 40960 45056 49152 53248 57344 61440
```
