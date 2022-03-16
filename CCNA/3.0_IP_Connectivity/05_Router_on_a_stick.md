# Router on a stick

**Router on a stick** (also know as **one-armed router**), is a router that ha a single physical or logical connection to a network.<br>
It is a method of inter-VLAN routing where on e router is connected to a switch via a single cable.
The router has physical connections ot the broadcast domains where one or more VLANs require the need for routing between them.

[[Wikipedia - Router on a stick](https://en.wikipedia.org/wiki/Router_on_a_stick)]<br>
[[GeeksforGeeks - Configuration of Router on a stick](https://www.geeksforgeeks.org/configuration-of-router-on-a-stick/)]

## Configure sub-interface

Configure sub-interface on interface `f0/0`

```
R1(config)#interface fastEthernet 0/0
R1(config-if)#no shut
R1(config-if)#interface fastEthernet f0/0.1
R1(config-subif)#encapsulation dot1Q 1 native
R1(config-subif)#ip address 10.1.1.254 255.255.255.0
```
