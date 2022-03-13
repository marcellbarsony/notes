# DHCP Relay Agent

The **DHCP Relay Agent** is a TCP/IP host operates as the interface between DHCP Clients and the DHCP Server when they are on a different IP network.<br>

DHCP Clients will send a broadcast packet to discover DHCP Servers on the network, but broadcast packets are not forwarded by routers by default.

**DHCP Relay Agent**s receive DHCP DORA messages and then generate a new DHCP message to send out on another interface.
**DHCP Relay Agent** adds GIADDR (Gateway Address of the packet) field and also the **DHCP Relay Agent** information 82, if enabled.

## Configuration

### Router ports

The router's ports have been configured with the following IP addresses:

- `192.168.1.1` on `fa0/0`
- `192.168.2.1` on `fa0/1`

```
ROUTER(config)#int f0/0
ROUTER(config-if)#ip address 192.168.1.1 255.255.255.0
ROUTER(config-if)#no shutdown
ROUTER(config)#int f0/1
ROUTER(config-if)#ip address 192.168.2.1 255.255.255.0
ROUTER(config-if)#no shutdown
```

### DHCP Server

The DHCP Server's port has been configured with the following IP addresses:

- `192.168.2.2` on interface `fa0/0`.

```
DHCP_SERVER(config)#int f0/0
DHCP_SERVER(config-if)#ip address 192.168.2.2 255.255.255.0
DHCP_SERVER(config-if)#no shutdown
```

The DHCP pool is defined with name `POOL1` and network of `192.168.1.0` with subnet mask `255.255.255.0`.

```
DHCP_SERVER(config)#ip dhcp pool POOL1
DHCP_SERVER(dhcp-config)#network 192.168.1.0 255.255.255.0
DHCP_SERVER(dhcp-config)#default-router 192.168.1.1
DHCP_SERVER(dhcp-config)#exit
```

### Router - Relay configuration

Now, the `ip helper-address` command is used for configuring the router as a DHCP relay agent, giving `192.168.2.2` the address of DHCP Server.

This command will instruct the router to do the following:

- Watch for DHCP DORA messages on the interface `f0/0`.
- When a DHCP DORA packet arrives, set the packet's source IP address to the IP address of `f0/0`.
- Change the destination IP address of the packet from `255.255.255.255` to the IP address of the DHCP server (`192.168.2.2`) and send it to the DHCP Server.
- When the answer is received from the DHCP Server, change the packet's destination IP to `255.255.255.255` and send it out on its `f0/0` interface, so that the DHCP Client (which does not have an IP address yet) can receive the answer.

```
ROUTER(config)#int f0/0
ROUTER(config-if)#ip helper-address 192.168.2.2
ROUTER(config-if)#exit
```
