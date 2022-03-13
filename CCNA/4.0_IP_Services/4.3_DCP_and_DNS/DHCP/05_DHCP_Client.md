# DHCP Client Configuration

Cisco routers can be configure as both **DHCP Servers** and **DHCP Clients**.
An interface on a router that connects to the Internet Service Provider (ISP) is often configured as a DHCP client - this way, the ISP can provide the IP information to the client device.

[[Study CCNA - Configure Cisco router as a DHCP client](https://study-ccna.com/configure-cisco-router-as-a-dhcp-client/)]

To configure an interface as a DHCP Client, the `ip address dhcp` command is used.

```
R1(config)#int Gi0/0
R1(config-if)#ip address dhcp
```

Verify that the Gi0/0 interface has indeed got its IP address from the DHCP Server.

```
R1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.0.1     YES DHCP   up                    up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
```

The DHCP keyword in the method column indicates that the IP information were obtained by the DHCP server.

> Note<br>
> To configure a Cisco switch as a DHCP client, the `ip address dhcp` command is used under the VLAN 1 configuration mode.
