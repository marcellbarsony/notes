# OSPF Areas

A network is divided into **OSPF Areas** that are logical groupings of hosts and networks.
An area includes its connecting router having an interface for each connected network link.
Each router maintains a separate link-state database for the area whose information may be summarized towards the rest of the network by the connecting router.
The topology of an area is unknown outside the area - this reduces the routing traffic between parts of an autonomous system.

A router that has interfaces in more than one area is called **Area Border Router (ABR)**.<br>
A router that connects an **OSPF**network to other routing domain (e.g. EIGRP) is called **Autonomous System Border Router (ASBR)**.

OSPF defines several area types:

- Backbone
- Non-Backbone/regular
- Stub,
- Totally stubby
- Not-so-stubby
- Totally Not-so-stubby
- Transit

## Backbone Area

The **Backbone Area** (also known as **area 0** or **area 0.0.0.0**) forms the core of an **OSPF** network and other areas are connected to it (either directly or other routers).

## Regular Area

## Transit Area

## Stub Area

### Totally stubby area

## Not-so-stubby area

### Totally not-so-stubby area
