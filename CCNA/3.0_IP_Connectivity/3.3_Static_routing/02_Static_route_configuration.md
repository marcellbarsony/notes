## Static Route Configuration

Static IP Routes can be configured with the `ip route` command

```
IntRouter(config)#ip route ?
  A.B.C.D  Destination prefix
  profile  Enable IP routing table profile
  static   Allow static routes
  vrf      Configure static route for a VPN Routing/Forwarding instance
```

```
IntRouter(config)#ip route <destination_network_ip> <destination_network_subnet_mask> ?
IntRouter(config)#ip route 10.1.2.0 255.255.255.0 ?
  A.B.C.D          Forwarding router's address
  Dialer           Dialer interface
  Ethernet         IEEE 802.3
  FastEthernet     FastEthernet IEEE 802.3
  GigabitEthernet  GigabitEthernet IEEE 802.3z
  Loopback         Loopback interface
  Null             Null interface
  Serial           Serial
  Vlan             Catalyst Vlans
IntRouter(config)#ip route 10.1.2.0 255.255.255.0 10.1.1.0 255.255.255.0
```

```
IntRouter(config)#ip route 10.1.1.0 255.255.255.0 <forwarding_router_ip> <forwarding_router_subnet_mask>
IntRouter(config)#ip route 10.1.1.0 255.255.255.0 10.1.1.0 255.255.255.0
```
