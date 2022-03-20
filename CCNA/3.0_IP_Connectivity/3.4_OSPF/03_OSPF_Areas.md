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

The **Backbone Area** (also known as **area 0** or **area 0.0.0.0**) forms the core of an OSPF network and other areas are connected to it (either directly or other routers).<br>
Inter-area routing happens via routers connected to the **Backbone Area** and to their own associated areas.

All **OSPF Areas** must connect to the **Backbone Area**.
This connection, however, can be through a virtual link:<br>
Area `0.0.0.2` could connect to the **Backbone Area** through Area `0.0.0.1` if it doesn't have direct connection.

## Regular Area

A **Regular Area** is just a non-backbone (nonzero) area without specific feature, generating and receiving summary and external LSAs.
The Backbone Area is a special type of such area.

## Transit Area

A **Transit Area** is an area with two or more OSPF border routers and is used to pass network traffic from one adjacent area to another.
The **Transit Area** does not originate this traffic and is not the destination of such traffic.

## Stub Area

A **Stub Area** is an area that does not receive route advertisements external to the AS and routing from within the area is based entirely on a default route.

### Totally stubby area

## Not-so-stubby area

### Totally not-so-stubby area
