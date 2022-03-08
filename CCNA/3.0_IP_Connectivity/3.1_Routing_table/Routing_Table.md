# Routing Table

A **Routing Table** (or Routing Information Base - RIB) is a data table stored in a router or a network host that lists the routes to particular network destinations.<br>
The **Routing Table** contains information about the topology of the network immediately around it, and in some cases, metrics (distances) associated with the routes.

Each **Routing Table** consists of the following entries:

- **Network destination and Subnet mask** – specifies a range of IP addresses.
- **Remote router** – IP address of the router used to reach that network.
- **Outgoing interface** – outgoing interface the packet should go out to reach the destination network.

There are three different methods for populating a routing table:

- Using **Directly connected subnets**
- Using **Static routing**
- Using **Dynamic routing**

### Example

Example Routing Table in a Unix-like operating system

The host has several interfaces:

- _eth0_ is the interface name of the network interface card representing an Ethernet port
- _ppp0_ is a PPPoE interface, which is configured as the default route in this example

The default route is recognized by the destination 0.0.0.0 and the flag **G**.<br>
The network router is identified by the network mask 255.255.255.255 and the flag **H**

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         71.46.14.1      0.0.0.0         UG    0      0        0 ppp0
10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth0
71.46.14.1      0.0.0.0         255.255.255.255 UH    0      0        0 ppp0
169.254.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
172.16.0.0      0.0.0.0         255.240.0.0     U     0      0        0 eth0
192.168.0.0     0.0.0.0         255.255.0.0     U     0      0        0 eth0
192.168.1.0     192.168.96.1    255.255.255.0   UG    0      0        0 eth0
192.168.96.0    0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

- **Network Destination** and **Netmask** together describe the **Network identifier**
- **Network identifier** — The destination subnet and netmask
- **Gateway** — Contains the same information as **Next hop**.
- **Next hop** — The next hop, or gateway, is the address of the next station to which the packet is to be sent.
- **Metric** indicates the associated cost of using the indicated route.
  This is useful for determining the efficiency of a certain route from two points in a network.

| Flag | Description                           |
| ---- | ------------------------------------- |
| G    | Use Gateway (gateway filled in)       |
| H    | Target is a Host (bitmask of 32 bits) |
| U    | Route is Up                           |
