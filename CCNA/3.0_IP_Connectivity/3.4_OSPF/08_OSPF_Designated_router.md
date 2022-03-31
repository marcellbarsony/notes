# OSPF Designated & Backup Designated Router

Based on the network type, **OSPF Routers** can elect a **Designated Router (DR)** and a **Backup Designated Router (BDR)**.
**DR** and **BDR** server as the central point for exchanging **OSPF information**.
**DR** will distribute topology information to every other router in the network segment, that reduces OSPF traffic.

To send routing information to a **DR** or **BDR**, the multicast address of `224.0.0.6` is used.
**DR** sends routing updates to the multicast address of `224.0.0.4`.

Every router on the network segment will establish a full neighbor relationship with the **DR** and **BDR**.
**Non-DR** and **Non-BDR** routers will establish a two way neighbor relationship between themselves.

## Designated Router

The Designated Routers is selected based on the following criteria

1. Highest OSPF priority of the interface

   - Range 0 to 255
   - Default value: 1
   - 0 excludes the router

2. Highest Router ID

Only the Designated Router listening for and receiving multicasting packets.
The multicast destination IP address of the packet is: `244.0.0.6`
